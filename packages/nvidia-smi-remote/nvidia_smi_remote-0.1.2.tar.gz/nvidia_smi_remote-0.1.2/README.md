nvidia-smi-remote
=================

[![pypi](https://img.shields.io/pypi/v/nvidia-smi-remote.svg?maxAge=86400)](https://pypi.org/project/nvidia-smi-remote/)
[![license](https://img.shields.io/github/license/ive2go/nvidia-smi-remote.svg?maxAge=86400)](LICENSE)

A CLI tool to display remote GPU status via SSH with colorful terminal output – showing GPU temperature, utilization, memory usage, and per-user process memory details. It’s like a remote version of `nvidia-smi` with enhanced readability!

This project is inspired by [gpustat](https://github.com/wookayin/gpustat).

Quick Installation
------------------

Install from [PyPI](https://pypi.org/project/nvidia-smi-remote/):

```bash
pip install nvidia-smi-remote
```

If you don’t have root privileges, try installing it in your user namespace:

```bash
pip install --user nvidia-smi-remote
```

To install the latest version from the master branch:

```bash
pip install git+https://github.com/ive2go/nvidia-smi-remote.git@master
```

### NVIDIA Driver, `nvidia-smi`, and Python Requirements

- **NVIDIA Requirement:** This tool requires NVIDIA GPUs and the `nvidia-smi` utility to be installed on the target systems.
- **Python Version:** Python 3.8 or higher is recommended.
- **Dependencies:**
  - [`paramiko`](https://pypi.org/project/paramiko/) – For SSH connectivity.
  - [`blessed`](https://pypi.org/project/blessed/) – For terminal styling.
  - The `nvidia-smi` command (bundled with the NVIDIA driver installation).

Usage
-----

`nvidia-smi-remote` is designed to query GPU information from remote servers via SSH. You can supply the remote server configuration either via a JSON configuration file or by setting the environment variable `NVIDIA_SMI_REMOTE_CONFIG`.

**Basic Usage with Configuration File:**

```bash
nvidia-smi-remote -r config.json
```

**Basic Usage with Environment Variable:**

```bash
export NVIDIA_SMI_REMOTE_CONFIG=/path/to/config.json
nvidia-smi-remote
```

**Command-line Options:**

* `-r, --remote-config`  : Path to the remote GPU server configuration JSON file (expects a list of server definitions).  
* `-i, --interval`       : Update interval in seconds (watch mode). Set to `0` for a single output.  
* `--no-header`          : Do not display the header (host, driver version, and time).  
* `--no-color`           : Disable colored terminal output.  
* `--used-only`          : Display only GPUs that have running processes.  
* `--unused-only`        : Display only GPUs without any running processes.

**Remote Configuration JSON Example:**

```json
[
  {
    "host": "remote.server.com",
    "port": 22,
    "username": "user",
    "password": "password"
  },
  {
    "host": "another.server.com",
    "username": "user",
    "key_filename": "/path/to/private/key"
  }
]
```

**Default Display Example:**

```
remote.server.com  2025-04-03 12:34:56  450.80.02
[0] GeForce RTX 3080   | 65°C,  50 % | 4000/10000 MB | user (1500MiB)
--------------------------------------------------------------------------------
```

- **Header:** Displays the hostname, current timestamp, and driver version.
- **GPU Line:** Shows GPU index, name, temperature, utilization, memory usage, and the aggregated memory usage per user.

Changelog
---------

See [CHANGELOG.md](CHANGELOG.md) for a complete list of changes.

License
-------

[MIT License](LICENSE)

Contact
-------

For questions or suggestions, please contact the author at [ive2go@naver.com](mailto:ive2go@naver.com).