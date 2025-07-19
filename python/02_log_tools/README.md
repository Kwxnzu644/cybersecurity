# 02_tools
# 🛡️ ThreatSuite: Python Red Team Scanner

> A modular Python script combining **ping checks**, **common port scanning**, and **log file analysis** into one red team utility.

---

## 🚀 Features

- ✅ **Ping Scanner**: Check if a target IP is online using `subprocess`
- ✅ **Port Scanner**: Scan top ports (21, 22, 80, 443, etc.) using `socket`
- ✅ **Log File Scanner**: Analyze `.log` or `.txt` files for:
  - Suspicious keywords (e.g., `hack`, `breach`, `unauthorized`)
  - Known bad IP addresses
- ✅ **Timestamped Logging**: All results are saved to a log file with scan times
- ✅ **Custom Banner & Arguments** via CLI

---

## 🧪 Usage

```bash
python3 SecTool.py -t 192.168.1.1 -f auth.log syslog.txt -o output.log -m "SECVERSE MINI THREAT SCAN"
