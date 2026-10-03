from analyzer import analyze_logs

successful_logins, failed_logins, failed_ips, port_activity = analyze_logs("sample_logs.txt")

print("Network Security Log Analyzer")

print("\nLogin Summary")
print("Successful Logins:", successful_logins)
print("Failed Logins:", failed_logins)

print("\nFailed Attempts by IP:")

for ip, count in failed_ips.items():
    print(ip, "->", count)

print("\nSecurity Alerts:")

for ip, count in failed_ips.items():
    if count >= 3:
        print("ALERT: Suspicious IP detected:", ip)
        print("Failed attempts:", count)

print("\nPort Activity:")

for port, count in port_activity.items():
    print("Port", port, "->", count, "scan(s)")