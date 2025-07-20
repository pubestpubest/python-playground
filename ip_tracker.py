logins = [
    {"user": "root", "ip": "10.0.0.1"},
    {"user": "root", "ip": "10.0.0.2"},
    {"user": "admin", "ip": "10.0.0.1"},
    {"user": "guest", "ip": "8.8.8.8"},
    {"user": "guest", "ip": "8.8.8.8"},
]

ip_attempt = {}
ips = set()

for login in logins:
    ip = login["ip"]
    ip_attempt[ip] = ip_attempt.get(ip, 0) + 1
    ips.add(ip)

more_than_one = [ip for ip, attempt in ip_attempt.items() if attempt > 1]


print(ip_attempt)
print(ips)
print(more_than_one)