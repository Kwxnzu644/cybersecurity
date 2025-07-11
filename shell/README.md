# 🐚 Shell Scripting for Cybersecurity

This folder contains **Bash scripts** and command-line utilities tailored for **system automation**, **forensics**, and **security hardening** — all developed and tested on **Arch Linux**.

---

## 📂 Example Topics

- 🔄 Automated log collection
- 🧾 File integrity monitoring
- 💾 Backup and restoration scripts
- 📊 System monitoring and alerting
- 🕵️ Log poisoning and cleanup (forensics simulation)

---

## 💡 How to Use

- Scripts are well-commented for clarity.
- Tested on Arch Linux (`bash`, `coreutils`, `cron`, `rsync`, etc.)
- Refer to the [main repo README](../README.md) for the complete roadmap.

---

## 🧭 Study Roadmap: Shell Scripting for Cybersecurity

> Goal: Automate real-world offensive/defensive security tasks using Bash on Arch Linux.

---

### 🗓️ Week 1: Bash Fundamentals
- ✅ Variables, loops, conditionals, functions
- ✅ File/directory operations: `cp`, `mv`, `find`, `cut`, `awk`, `sed`

### 🗓️ Week 2: Log Collection & Analysis
- 📥 Collect logs from `/var/log` (`syslog`, `auth.log`, etc.)
- 🔍 Monitor login attempts and SSH sessions
- ⚠️ Detect brute-force or suspicious activity from logs

### 🗓️ Week 3: File Integrity Checks
- 🔐 Use `sha256sum`, `md5sum`, `diff` for file verification
- 🛡️ Build a script to watch for unauthorized file changes (e.g., `/etc/passwd`, `/var/www`)

### 🗓️ Week 4: Backup & Restore Scripts
- 💽 Auto-backup critical directories (`/etc`, `/home`)
- 📦 Compress with `tar`, archive with timestamps
- 🔁 Restore script with safety checks

### 🗓️ Week 5: System Monitoring & Alerts
- 📈 Monitor CPU, RAM, and disk space usage
- 🚨 Send alerts (local, email, log entry) when thresholds are breached
- 📋 Logging with timestamps

### 🗓️ Week 6: Advanced Topics
- ⏱️ Crontab for automation and scheduled scans
- 🔐 Secure file transfers with `scp`, `rsync`, SSH keys
- 🕵️ Simulate log poisoning, wiping, or obfuscation for forensic practice

---

## 🛠️ Tools You’ll Use
- `bash`, `awk`, `sed`, `cron`, `diff`, `md5sum`, `sha256sum`, `tar`, `scp`, `rsync`
- Optional: `mail`, `journalctl`, `netstat`, `inotifywait`, `auditd`

---

## ⚠️ Disclaimer

This content is for **educational and authorized environments only**. Do **not** use these scripts in any unauthorized system or against systems you do not own or have permission to test.

---

📌 *Follow this folder to see how automation can power security.*  
