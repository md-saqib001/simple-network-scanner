#!/usr/bin/env python3
"""
Network Sweeper
----------------
A simple Python utility to scan a local subnet for active hosts using ICMP (Ping).
Built to run on Linux/WSL environments.
"""

import subprocess

def scan_network(network_base, start_range, end_range):
    print(f"Starting scan on {network_base}.{start_range} - {network_base}.{end_range}...")
    print("-" * 40)

    for i in range(start_range, end_range + 1):
        target_ip = f"{network_base}.{i}"
        
        # Ping command: -c 1 (count), -W 1 (wait/timeout in seconds)
        # We redirect stdout/stderr to hide the raw ping output
        response = subprocess.call(
            ['ping', '-c', '1', '-W', '1', target_ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if response == 0:
            print(f"[+] Host {target_ip} is ONLINE")
        else:
            # Optional: Print offline hosts
            pass

    print("-" * 40)
    print("Scan Complete.")

if __name__ == "__main__":
    # Example: Scanning the 36.255.14.x subnet
    scan_network("36.255.14", 230, 250)