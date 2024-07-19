import subprocess

def run_command(command):
    """
    Run a shell command and return the output.
    """
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        return result.stdout, result.stderr
    except Exception as e:
        return "", str(e)

def check_ping(ip):
    """
    Check network connectivity using ping.
    """
    print(f"--- Pinging {ip} ---")
    stdout, stderr = run_command(f"ping -c 4 {ip}")
    print(stdout if stdout else stderr)

def check_telnet(ip, port):
    """
    Check network connectivity using telnet.
    """
    print(f"--- Telnet to {ip}:{port} ---")
    stdout, stderr = run_command(f"echo quit | telnet {ip} {port}")
    print(stdout if stdout else stderr)

def check_nc(ip, port):
    """
    Check network connectivity using nc (netcat).
    """
    print(f"--- Netcat to {ip}:{port} ---")
    stdout, stderr = run_command(f"nc -zv {ip} {port}")
    print(stdout if stdout else stderr)

def check_ip_route():
    """
    Show the routing table using ip route.
    """
    print("--- IP Route ---")
    stdout, stderr = run_command("ip route show")
    print(stdout if stdout else stderr)

def check_nslookup(hostname):
    """
    Perform a DNS lookup using nslookup.
    """
    print(f"--- NSLookup for {hostname} ---")
    stdout, stderr = run_command(f"nslookup {hostname}")
    print(stdout if stdout else stderr)

def check_curl(url):
    """
    Check network connectivity using curl.
    """
    print(f"--- Curl to {url} ---")
    stdout, stderr = run_command(f"curl -I {url}")
    print(stdout if stdout else stderr)

def check_selinux():
    """
    Check SELinux status.
    """
    print("--- SELinux Status ---")
    stdout, stderr = run_command("sestatus")
    print(stdout if stdout else stderr)

def main():
    # Example usage
    ip_address = "8.8.8.8"
    hostname = "www.google.com"
    port = 80
    url = "http://www.google.com"

    check_ping(ip_address)
    check_telnet(ip_address, port)
    check_nc(ip_address, port)
    check_ip_route()
    check_nslookup(hostname)
    check_curl(url)
    check_selinux()

if __name__ == "__main__":
    main()
