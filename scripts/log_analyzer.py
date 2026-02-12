import os
from datetime import datetime

log_file_path = "../logs/system.log"
report_path = "../reports/validation_report.txt"

error_count = 0
critical_count = 0

if os.path.exists(log_file_path):
    with open(log_file_path, "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                error_count += 1
            if "CRITICAL" in line:
                critical_count += 1

status = "PASS"
if critical_count > 0:
    status = "FAIL"

with open(report_path, "w") as report:
    report.write("Linux Patch Validation Report\n")
    report.write(f"Generated on: {datetime.now()}\n")
    report.write(f"Errors Found: {error_count}\n")
    report.write(f"Critical Issues Found: {critical_count}\n")
    report.write(f"Validation Status: {status}\n")

print("Validation Completed.")
print(f"Errors: {error_count}, Critical: {critical_count}")
