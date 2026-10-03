def analyze_logs(filename):
    failed_logins = 0
    successful_logins = 0
    failed_ips = {}
    port_activity = {}

    with open(filename, "r") as file:
        for line in file:

            if "LOGIN_FAILED" in line:
                failed_logins += 1

                ip = line.split("ip=")[1].strip()

                if ip in failed_ips:
                    failed_ips[ip] += 1
                else:
                    failed_ips[ip] = 1

            elif "LOGIN_SUCCESS" in line:
                successful_logins += 1

            elif "PORT_SCAN" in line:
                port = line.split("port=")[1].strip()

                if port in port_activity:
                    port_activity[port] += 1
                else:
                    port_activity[port] = 1

    return successful_logins, failed_logins, failed_ips, port_activity