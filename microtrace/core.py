import platform
import subprocess
import re


def trace(host, max_hops=30):
    system = platform.system().lower()

    if system == "windows":
        cmd = ["tracert", "-h", str(max_hops), host]
    else:
        cmd = ["traceroute", "-m", str(max_hops), host]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=90
        )
    except FileNotFoundError:
        print("MicroTrace Error:")
        print("Traceroute command not found.")
        print()
        print("Install it with:")
        print("  pkg install traceroute")
        print("or:")
        print("  sudo apt install traceroute")
        return

    output = result.stdout or result.stderr
    print(output)

    hops = []
    for line in output.splitlines():
        line = line.strip()
        if re.match(r"^\d+", line):
            hops.append(line)

    print()
    print("MicroTrace Summary")
    print("==================")
    print(f"Target: {host}")
    print(f"Hops Found: {len(hops)}")

    if hops:
        print(f"Last Hop: {hops[-1]}")
