import re

failed_logs = []
ip_attempt = {}
ips = set()

failed_pattern = r"(Failed|Unauthorized|Error)"
ip_pattern = r"(\d+\.\d+\.\d+\.\d+)"

with open("access.log", "r") as file:
    for line in file:
        if re.search(failed_pattern,line):
            failed_logs.append(line.strip())
            match = re.search(ip_pattern, line)
            if match:
                ip = match.group(1)
                ips.add(ip)
                ip_attempt[ip] = ip_attempt.get(ip, 0) + 1

print("All failed log:")
for log in failed_logs:
    print(f" - {log}")

print(f"Unique IPs: {", ".join(ips)}")

print("Failed attempt:")
for ip, attempt in ip_attempt.items():
    print(f" - {ip}: {attempt} attempt(s)")
