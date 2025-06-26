# Shell Scripting for Cybersecurity

This folder holds Bash scripts and command-line utilities for system automation and forensics.

## Example Topics
- Automated log collection
- File integrity checks
- Backup and restoration scripts

## How to Use

- Scripts are documented with comments.
- Reference the main [README](../README.md) for my learning plan.
- ill be using Arch linux for this purpose

# Study Roadmap: Shell Scripting for Cybersecurity

All scripts are written and tested on Arch Linux. My goal is to automate real-world security tasks.

---

## Week 1: Bash Basics
- Variables, loops, conditionals, functions
- File/directory operations (`cp`, `mv`, `find`, `cut`, `awk`, `sed`)

## Week 2: Log Collection & Analysis
- Extract `/var/log` data (e.g., `syslog`, `auth.log`)
- Monitor login attempts
- Detect suspicious log entries

## Week 3: File Integrity Checks
- Use `sha256sum`, `md5sum`, `diff` to verify file integrity
- Build a script to watch for unauthorized file changes

## Week 4: Backup & Restore Scripts
- Auto-backup `/etc`, `/home`, and important files
- Create compressed `.tar.gz` archives
- Restore from backups easily

## Week 5: System Monitoring & Alerts
- Monitor CPU, RAM, disk space
- Send email or local alerts if thresholds exceeded

## Week 6: Advanced Scripting
- Crontab for automation
- Secure file transfers (`rsync`, `scp`)
- Simulate log poisoning or log cleanup (for forensics)


## ⚠️ Disclaimer

This code is for educational purposes only. Do not use it in unauthorized environments.
