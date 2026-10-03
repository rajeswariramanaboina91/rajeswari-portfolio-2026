from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


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


@app.route("/", methods=["GET", "POST"])
def dashboard():

    log_file = "sample_logs.txt"
    uploaded_filename = "sample_logs.txt"

    if request.method == "POST":
        file = request.files["logfile"]

        if file.filename:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            log_file = filepath
            uploaded_filename = file.filename

    successful_logins, failed_logins, failed_ips, port_activity = analyze_logs(log_file)

    return render_template(
        "dashboard.html",
        successful_logins=successful_logins,
        failed_logins=failed_logins,
        failed_ips=failed_ips,
        port_activity=port_activity,
        uploaded_filename=uploaded_filename
    )


if __name__ == "__main__":
    app.run(debug=True)
