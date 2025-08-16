# 05_networking
# 📡 Python Network Recon Tools

This folder contains lightweight **network reconnaissance tools** built in Python for offensive security and red team learning.  

> 🛠️ Developed under **Secverse**, focusing on practical offensive security automation.

---

## 📂 Tools Included

### 🔍 1. TCP Port Scanner
- Scans specified TCP ports on a target.  
- Detects **open, closed, or filtered** ports.  
- Uses `socket` for raw network connections.  

**Usage:**  
```bash
python tcp_scanner.py <target> -p 22 80 443

