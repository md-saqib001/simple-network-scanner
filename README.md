# Simple Network Scanner (ICMP)

A lightweight Python utility designed to discover active hosts on a network subnet using ICMP Echo Requests (Ping). This tool was built to demonstrate raw socket interaction, subnet iteration, and process handling in a Unix/Linux environment.

## 🚀 Features

- **Range Sweeping:** Scans user-defined IP ranges (LAN or WAN) efficiently.
- **OS Integration:** Leverages the native `ping` utility via Python's `subprocess` module.
- **Clean Output:** Filters standard system noise to report only "Live" hosts.
- **Linux/WSL Optimized:** Specifically tuned for Ubuntu and WSL environments using the `-c` flag.


### Prerequisites
- Python 3.x
- Linux environment (Ubuntu, Debian, or WSL)

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/simple-network-scanner.git](https://github.com/YOUR_USERNAME/simple-network-scanner.git)

```

2. Navigate to the directory:
```bash
cd simple-network-scanner

```



### Running the Scanner

Run the script directly from the terminal:

```bash
python3 scanner.py

```

## 📊 Sample Output

Below is an example of the scanner identifying active hosts on a public ISP subnet (`36.255.14.x`):

```text
Starting scan on 36.255.14.230 - 36.255.14.250...
----------------------------------------
[+] Host 36.255.14.241 is ONLINE
[+] Host 36.255.14.242 is ONLINE
[+] Host 36.255.14.244 is ONLINE
----------------------------------------
Scan Complete.

```

## 🔍 How It Works

The script iterates through the specified IP range and spawns a child process for each target. It interprets the **Exit Code** of the system's `ping` command to determine status:

* **Exit Code 0:** Host is Reachable (UP).
* **Exit Code 1/2:** Host is Unreachable/Offline (DOWN).


## 📖 Glossary

Here are the key networking concepts utilized in this script:

- **ICMP (Internet Control Message Protocol):** A network layer protocol used by network devices to diagnose communication issues. This tool uses ICMP "Echo Request" packets to check if a host is reachable.
- **Ping:** A standard utility that uses ICMP to measure the time it takes for messages to travel from the source to a destination and back.
- **Subnet (Subnetwork):** A logical subdivision of an IP network. Scanning a specific range (e.g., `192.168.1.1` to `192.168.1.255`) allows network administrators to manage traffic and security efficiently.
- **Exit Code:** A number returned by a child process to its parent process. In Linux/Unix:
  - `0`: Success (The host replied).
  - `1` or `2`: Failure (The host did not reply or is unreachable).
- **WSL (Windows Subsystem for Linux):** A compatibility layer for running Linux binary executables directly on Windows. This script is optimized for the specific way WSL handles network interfaces.
- **WAN vs. LAN:**
  - **LAN (Local Area Network):** Your private home/office network (e.g., `192.168.x.x`). Scanning this reveals physical devices like phones and printers.
  - **WAN (Wide Area Network):** The public internet (e.g., `36.255.x.x`). Scanning this reveals public-facing routers and gateways, often hiding internal devices behind NAT.


### Code Logic

The core scanning logic utilizes the `subprocess` module to silence standard output (`stdout`) and standard error (`stderr`), providing a clean console interface:

```python
response = subprocess.call(
    ['ping', '-c', '1', '-W', '1', target_ip],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

```

## 📝 Configuration

To scan a different network (such as your local Wi-Fi), modify the `scan_network` call at the bottom of `scanner.py`:

```python
if __name__ == "__main__":
    # Example 1: Scan a Public Range (WAN)
    scan_network("36.255.14", 230, 250)

    # Example 2: Scan Local Network (LAN)
    # scan_network("192.168.1", 1, 20)

```

## ⚠️ Disclaimer

This tool is provided for educational purposes and authorized network testing only. Scanning public IP ranges or networks you do not own may violate ISP terms of service or local regulations.

