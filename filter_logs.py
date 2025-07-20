logs = [
    "IP 10.0.0.3 failed login",
    "IP 192.168.1.5 success",
    "IP 172.16.0.1 failed login",
    "IP 10.0.0.2 success",
    "IP 192.168.1.1 failed login",
    "IP 10.0.0.5 failed login",
    "IP 192.168.0.12 success",
    "IP 127.0.0.1 failed login"
]

failed_logs = [log for log in logs if log.find("failed") != -1]
failed_ips = [log.split(" ")[1] for log in failed_logs]
print(failed_ips)