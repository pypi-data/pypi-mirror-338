#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
import subprocess
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

import paramiko
from blessed import Terminal

# Default color and conditional formatting functions (using blessed.Terminal)
def format_temp(temp_str: str, term: Terminal):
    try:
        t = int(temp_str)
    except ValueError:
        return temp_str, False
    if t < 70:
        return f"{term.yellow}{temp_str}{term.normal}", False
    else:
        return f"{term.red}{temp_str}{term.normal}", True

def format_util(util_str: str, term: Terminal):
    try:
        u = int(util_str)
    except ValueError:
        return util_str, False
    if u < 90:
        return f"{term.green}{util_str}{term.normal}", False
    else:
        return f"{term.bold_green}{util_str}{term.normal}", True

def format_memory(used_str: str, total_str: str, term: Terminal):
    try:
        used = int(used_str)
        total = int(total_str)
        ratio = used / total if total > 0 else 0
    except ValueError:
        return f"{used_str}/{total_str} MB", False

    if ratio < 0.9:
        return f"{term.green}{used_str}/{total_str} MB{term.normal}", False
    else:
        return f"{term.bold_yellow}{used_str}/{total_str} MB{term.normal}", True

def format_users(user_mem: dict, term: Terminal):
    """
    user_mem: dict { username: memory_usage (int) }
    """
    if not user_mem:
        return "-"
    # Display username and memory usage (unit: MiB)
    parts = []
    for user, mem in sorted(user_mem.items()):
        parts.append(f"{term.bold_magenta}{user}{term.normal} ({mem}MiB)")
    return ", ".join(parts)

def shorten_gpu_name(name: str) -> str:
    # For example: "6000 Ada Generation" -> "6000A"
    return name.replace("6000 Ada Generation", "6000A")

# Function to query remote server's GPU information
def get_remote_nvidia_info(server: dict, term: Terminal, usage_filter: str = None):
    """
    Connects to a remote server via SSH and queries GPU information and driver version using nvidia-smi.
    If GPUs matching the condition exist, returns the header and a list of GPU lines.
    """
    host = server.get("host")
    port = server.get("port", 22)
    username = server.get("username")
    password = server.get("password")
    key_filename = server.get("key_filename")
    header = ""
    gpu_lines = []

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password, key_filename=key_filename, timeout=10)

        # Query driver version (based on the first GPU)
        ver_cmd = "nvidia-smi --query-gpu=driver_version --format=csv,noheader,nounits"
        stdin, stdout, stderr = ssh.exec_command(ver_cmd)
        driver_version_output = stdout.read().decode('utf-8').strip()
        driver_version = driver_version_output.splitlines()[0] if driver_version_output else "N/A"

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        header = f"{term.bold_white}{host}{term.normal}  {now}  {term.bold_black}{driver_version}{term.normal}"

        # Query GPU information
        gpu_cmd = (
            "nvidia-smi --query-gpu=index,uuid,name,temperature.gpu,utilization.gpu,"
            "memory.used,memory.total --format=csv,noheader,nounits"
        )
        stdin, stdout, stderr = ssh.exec_command(gpu_cmd)
        gpu_output = stdout.read().decode('utf-8').strip()
        gpu_lines_raw = gpu_output.splitlines()

        gpu_info = {}
        for line in gpu_lines_raw:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 7:
                continue
            index, uuid, name, temp, util, mem_used, mem_total = parts
            gpu_info[uuid] = {
                "index": index,
                "name": shorten_gpu_name(name),
                "temp": temp,
                "util": util,
                "mem_used": mem_used,
                "mem_total": mem_total,
                "processes": []  # Changed: storing process information instead of just pids
            }

        # Query GPU process information (pid, used_memory, gpu_uuid)
        proc_cmd = "nvidia-smi --query-compute-apps=pid,used_memory,gpu_uuid --format=csv,noheader,nounits"
        stdin, stdout, stderr = ssh.exec_command(proc_cmd)
        proc_output = stdout.read().decode('utf-8').strip()
        pids = []
        for line in proc_output.splitlines():
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 3:
                continue
            pid, used_mem, gpu_uuid = parts
            if gpu_uuid in gpu_info:
                gpu_info[gpu_uuid]["processes"].append({"pid": pid, "used_mem": used_mem})
            pids.append(pid)

        # Query the user for each PID
        pid_to_user = {}
        if pids:
            pids_str = ",".join(pids)
            ps_cmd = f"ps -o pid=,user= -p {pids_str}"
            stdin, stdout, stderr = ssh.exec_command(ps_cmd)
            ps_output = stdout.read().decode('utf-8').strip()
            for line in ps_output.splitlines():
                parts = line.strip().split()
                if len(parts) >= 2:
                    pid_val, user_val = parts[0], parts[1]
                    pid_to_user[pid_val] = user_val

        # Generate a line for each GPU (apply filter)
        for uuid, info in gpu_info.items():
            # Filter: if --used-only then processes must exist; if --unused-only then processes must not exist
            if usage_filter == "used" and not info["processes"]:
                continue
            if usage_filter == "unused" and info["processes"]:
                continue

            idx = info["index"]
            name_str = info["name"]
            temp_str = info["temp"]
            util_str = info["util"]
            mem_used_str = info["mem_used"]
            mem_total_str = info["mem_total"]

            # Aggregate GPU memory usage per user
            user_mem = {}
            for proc in info["processes"]:
                pid = proc["pid"]
                try:
                    mem = int(proc["used_mem"])
                except ValueError:
                    mem = 0
                if pid in pid_to_user:
                    user = pid_to_user[pid]
                    user_mem[user] = user_mem.get(user, 0) + mem

            colored_temp, temp_high = format_temp(temp_str, term)
            colored_util, util_high = format_util(util_str, term)
            colored_mem, mem_high = format_memory(mem_used_str, mem_total_str, term)
            colored_name = f"{term.blue}{name_str}{term.normal}"
            colored_users = format_users(user_mem, term)
            if temp_high or util_high or mem_high:
                colored_index = f"{term.bold_red}{idx}{term.normal}"
            else:
                colored_index = f"{term.bold_cyan}{idx}{term.normal}"

            line_fmt = (
                f"[{colored_index}] {colored_name:<16} | "
                f"{colored_temp}°C, {colored_util}% | "
                f"{colored_mem} | "
                f"{colored_users}"
            )
            gpu_lines.append(line_fmt)

        ssh.close()
    except Exception as e:
        # If an error occurs, do not output the corresponding server
        return None, None, []

    if not gpu_lines:
        return None, None, []
    return host, header, gpu_lines

# Function to query local system's GPU information (using subprocess)
def get_local_nvidia_info(term: Terminal, usage_filter: str = None):
    header = ""
    gpu_lines = []
    try:
        # Query driver version (based on the first GPU)
        ver_cmd = ["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader,nounits"]
        driver_version_output = subprocess.check_output(ver_cmd, encoding="utf-8").strip()
        driver_version = driver_version_output.splitlines()[0] if driver_version_output else "N/A"

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hostname = os.uname().nodename if hasattr(os, "uname") else "localhost"
        header = f"{term.bold_white}{hostname}{term.normal}  {now}  {term.bold_black}{driver_version}{term.normal}"

        # Query GPU information
        gpu_cmd = [
            "nvidia-smi",
            "--query-gpu=index,uuid,name,temperature.gpu,utilization.gpu,"
            "memory.used,memory.total",
            "--format=csv,noheader,nounits"
        ]
        gpu_output = subprocess.check_output(gpu_cmd, encoding="utf-8").strip()
        gpu_lines_raw = gpu_output.splitlines()

        gpu_info = {}
        for line in gpu_lines_raw:
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 7:
                continue
            index, uuid, name, temp, util, mem_used, mem_total = parts
            gpu_info[uuid] = {
                "index": index,
                "name": shorten_gpu_name(name),
                "temp": temp,
                "util": util,
                "mem_used": mem_used,
                "mem_total": mem_total,
                "processes": []
            }

        # Query GPU process information (pid, used_memory, gpu_uuid)
        proc_cmd = [
            "nvidia-smi",
            "--query-compute-apps=pid,used_memory,gpu_uuid",
            "--format=csv,noheader,nounits"
        ]
        try:
            proc_output = subprocess.check_output(proc_cmd, encoding="utf-8").strip()
        except subprocess.CalledProcessError:
            proc_output = ""
        pids = []
        for line in proc_output.splitlines():
            parts = [p.strip() for p in line.split(',')]
            if len(parts) < 3:
                continue
            pid, used_mem, gpu_uuid = parts
            if gpu_uuid in gpu_info:
                gpu_info[gpu_uuid]["processes"].append({"pid": pid, "used_mem": used_mem})
            pids.append(pid)

        # Query the user for each PID
        pid_to_user = {}
        if pids:
            ps_cmd = f"ps -o pid=,user= -p {','.join(pids)}"
            ps_output = subprocess.check_output(ps_cmd, shell=True, encoding="utf-8").strip()
            for line in ps_output.splitlines():
                parts = line.strip().split()
                if len(parts) >= 2:
                    pid_val, user_val = parts[0], parts[1]
                    pid_to_user[pid_val] = user_val

        # Generate a line for each GPU (apply filter)
        for uuid, info in gpu_info.items():
            if usage_filter == "used" and not info["processes"]:
                continue
            if usage_filter == "unused" and info["processes"]:
                continue

            idx = info["index"]
            name_str = info["name"]
            temp_str = info["temp"]
            util_str = info["util"]
            mem_used_str = info["mem_used"]
            mem_total_str = info["mem_total"]

            user_mem = {}
            for proc in info["processes"]:
                pid = proc["pid"]
                try:
                    mem = int(proc["used_mem"])
                except ValueError:
                    mem = 0
                if pid in pid_to_user:
                    user = pid_to_user[pid]
                    user_mem[user] = user_mem.get(user, 0) + mem

            colored_temp, temp_high = format_temp(temp_str, term)
            colored_util, util_high = format_util(util_str, term)
            colored_mem, mem_high = format_memory(mem_used_str, mem_total_str, term)
            colored_name = f"{term.blue}{name_str}{term.normal}"
            colored_users = format_users(user_mem, term)
            if temp_high or util_high or mem_high:
                colored_index = f"{term.bold_red}{idx}{term.normal}"
            else:
                colored_index = f"{term.bold_cyan}{idx}{term.normal}"

            line_fmt = (
                f"[{colored_index}] {colored_name:<16} | "
                f"{colored_temp}°C, {colored_util}% | "
                f"{colored_mem} | "
                f"{colored_users}"
            )
            gpu_lines.append(line_fmt)
    except Exception as e:
        return None, None, []
    if not gpu_lines:
        return None, None, []
    return "local", header, gpu_lines

def parse_remote_config(path: str):
    with open(path, "r") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(
        description="GPU status CLI-like output (local/remote) - Displays GPUs in use or not and each user's GPU memory usage"
    )
    parser.add_argument("-r", "--remote-config", type=str, default=None,
                        help="Remote GPU server configuration JSON file (list format). If not specified, displays local nvidia-smi output")
    parser.add_argument("-i", "--interval", type=float, default=0,
                        help="Watch mode: update interval (seconds). 0 means output once")
    parser.add_argument("--no-header", action="store_true", default=False,
                        help="Do not output header (host/driver version/time)")
    parser.add_argument("--no-color", action="store_true", default=False,
                        help="Output without colors")
    parser.add_argument("--used-only", action="store_true", default=False,
                        help="Only display GPUs in use (with GPU processes)")
    parser.add_argument("--unused-only", action="store_true", default=False,
                        help="Only display GPUs not in use (without GPU processes)")
    args = parser.parse_args()

    if args.used_only and args.unused_only:
        sys.stderr.write("Error: --used-only and --unused-only options cannot be used simultaneously.\n")
        sys.exit(1)

    term = Terminal(force_styling=not args.no_color)

    usage_filter = None
    if args.used_only:
        usage_filter = "used"
    elif args.unused_only:
        usage_filter = "unused"

    def update_display():
        output_lines = []
        # If no command-line argument is provided, read the value from environment variable.
        remote_config_path = args.remote_config or os.environ.get("NVIDIA_SMI_REMOTE_CONFIG")
        if remote_config_path:
            try:
                servers = parse_remote_config(remote_config_path)
            except Exception as e:
                sys.stderr.write(f"Failed to load remote configuration file: {e}\n")
                sys.exit(1)
            with ThreadPoolExecutor(max_workers=len(servers)) as executor:
                futures = [executor.submit(get_remote_nvidia_info, srv, term, usage_filter) for srv in servers]
                for future in futures:
                    host, header, gpu_lines = future.result()
                    if gpu_lines:
                        if not args.no_header:
                            output_lines.append(header)
                        output_lines.extend(gpu_lines)
                        output_lines.append("-" * 80)
        else:
            sys.stderr.write("No remote configuration information provided.\n")
            sys.exit(1)
        return "\n".join(output_lines)

    if args.interval > 0:
        with term.fullscreen(), term.hidden_cursor():
            try:
                while True:
                    print(term.home + term.clear, end='')
                    print(update_display())
                    time.sleep(args.interval)
            except KeyboardInterrupt:
                pass
    else:
        print(update_display())

if __name__ == "__main__":
    main()
