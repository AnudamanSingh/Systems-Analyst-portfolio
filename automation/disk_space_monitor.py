import os
import csv
from datetime import datetime

# Define the path to monitor
drive = "C:\\"

# Get disk usage statistics
stat = os.statvfs(drive)
total = stat.f_blocks * stat.f_frsize
available = stat.f_bavail * stat.frsize
used = total - available
percent_used = (used / total) * 100

# Prepare data
data = [
    ["Timestamp", "Total (GB)", "Used (GB)", "Available (GB)", "Percent Used"],
    [datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
     round(total / (1024**3), 2),
     round(used / (1024**3), 2),
     round(available / (1024**3), 2),
     round(percent_used, 2)]
]

# Write to CSV
file_path = "disk_usage_log.csv"
if not os.path.exists(file_path):
    with open(file_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data[0])

with open(file_path, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(data[1])

print(f"Disk usage logged to {file_path}")
