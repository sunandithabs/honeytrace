#!/usr/bin/env python3
import socket
import datetime
import os
import json
import urllib.request

log_file = "logs/honeytrace.log"

def log_event(data):
    os.makedirs("logs", exist_ok=True)
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{ts}] {data}\n")
    print(f"[+] logged -> {data}")

def geo_lookup(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        r = urllib.request.urlopen(url, timeout=3)
        j = json.load(r)
        return {
            "ip": ip,
            "city": j.get("city", "unknown"),
            "region": j.get("region", "unknown"),
            "country": j.get("country", "unknown"),
            "org": j.get("org", "unknown")
        }
    except:
        return {"ip": ip, "city": "unknown", "region": "unknown", "country": "unknown", "org": "unknown"}

def fake_shell(conn, ip, port):
    banner = "ssh-2.0-openssh_7.9\n"
    conn.sendall(banner.encode())

    conn.sendall(b"username: ")
    user = conn.recv(1024).decode(errors="ignore").strip()

    conn.sendall(b"password: ")
    pwd = conn.recv(1024).decode(errors="ignore").strip()

    log_event(f"credentials from {ip}:{port} user={user} pass={pwd}")

    conn.sendall(b"\naccess granted\n\n")
    conn.sendall(b"> ")

    while True:
        cmd = conn.recv(1024).decode(errors="ignore").strip()
        if not cmd:
            break
        if cmd.lower() in ["exit", "quit"]:
            conn.sendall(b"logout\n")
            break
        log_event(f"cmd from {ip}:{port} -> {cmd}")
        conn.sendall(b"permission denied\n> ")

def start_honeytrace(port=2222):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", port))
    s.listen(5)
    print(f"[+] honeytrace running on port {port}")
    print("[+] waiting for connections")

    while True:
        conn, addr = s.accept()
        ip = addr[0]

        geo = geo_lookup(ip)
        log_event(f"connection from {geo}")

        try:
            fake_shell(conn, ip, port)
        except:
            log_event(f"error handling connection from {ip}")
        finally:
            conn.close()

if __name__ == "__main__":
    try:
        start_honeytrace()
    except KeyboardInterrupt:
        print("\n[!] honeytrace shut down.")
