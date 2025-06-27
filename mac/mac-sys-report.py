import subprocess
import os
from datetime import datetime

def run(cmd):
    return subprocess.getoutput(cmd).strip()

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
username = run("whoami")
computer_name = run("scutil --get ComputerName")
macos_version = run("sw_vers -productVersion")
uptime = run("uptime | awk '{print $3 $4}' | sed 's/,//'")
disk_usage = run("df -h / | tail -1 | awk '{print $3 \" used / \" $2}'")
battery = run("pmset -g batt | grep -Eo '\\d+%\\s*;\\s*(charging|discharging|charged)'")
local_ip = run("ipconfig getifaddr en0")
public_ip = run("curl -s ifconfig.me")

report = f"""
🔧 Weekly Mac System Report
🕒 {timestamp}

👤 Username: {username}
💻 Computer Name: {computer_name}
🖥️ macOS Version: {macos_version}
🔋 Battery: {battery}
⏱️ Uptime: {uptime}
💾 Disk Usage: {disk_usage}
🌐 Local IP: {local_ip}
🌍 Public IP: {public_ip}
"""

report_file = os.path.expanduser("~/Desktop/mac_system_report.txt")
with open(report_file, "w") as f:
    f.write(report.strip())

print(f"✅ Report saved to: {report_file}")
