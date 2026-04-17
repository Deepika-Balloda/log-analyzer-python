import re
from collections import Counter

def analyze_log(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    error_count = 0
    warning_count = 0
    info_count = 0

    for line in lines:
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

    print("===== Log Summary =====")
    print(f"Total lines: {len(lines)}")
    print(f"Errors: {error_count}")
    print(f"Warnings: {warning_count}")
    print(f"Info messages: {info_count}")

    with open("log_report.txt", "w") as report:
        report.write("===== Log Summary =====\n")
        report.write(f"Total lines: {len(lines)}\n")
        report.write(f"Errors: {error_count}\n")
        report.write(f"Warnings: {warning_count}\n")
        report.write(f"Info messages: {info_count}\n")

if __name__ == "__main__":
    analyze_log("sample.log")