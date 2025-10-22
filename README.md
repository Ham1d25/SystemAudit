# SystemAudit — Ethical System Information & Diagnostic Collector

**Short description (GitHub project description):**  
A consent-first Python utility for collecting non-sensitive system diagnostics and environment metadata for authorized audits and troubleshooting.

> ⚠️ **Important:** This tool is intended for legitimate, authorized use only — e.g., local diagnostics, collecting environment information for bug reports, or penetration tests where you have explicit written permission. Do **not** use this tool to access, collect, or transmit credentials, browser data, or any private user files.

---

## Table of contents

- [What it does](#what-it-does)
- [Why this exists](#why-this-exists)
- [Installation](#installation)
- [Usage](#usage)
- [Authorized penetration testing workflow](#authorized-penetration-testing-workflow)
- [Privacy & safety](#privacy--safety)
- [Extending the tool](#extending-the-tool)
- [Contributing](#contributing)
- [License](#license)

---

## What it does

SystemAudit collects non-sensitive system and environment information useful for debugging and diagnostics, such as:

- OS and platform details
- Python runtime information
- CPU counts and basic frequency
- Total RAM and disk usage (summary)
- Hostname and basic network addresses (local IPs)
- Timestamps and a collection manifest

**It does not** collect or transmit saved passwords, browser login files, cookies, SSH keys, or any other secrets by default.

---

## Why this exists

When debugging software or performing authorized audits, maintainers and security engineers often need consistent environment metadata. SystemAudit standardizes that collection so teams can reproduce issues and understand the host environment quickly — without exposing user secrets.

---

## Installation

Requires Python 3.8+.

```bash
git clone https://github.com/yourusername/SystemAudit.git
cd SystemAudit
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
