# ☁️✨ Cloud Backup Manager

A secure, interactive, no-root-needed backup tool for Linux.  
**Monitors, syncs, and archives any folder (or many!) to any cloud—instantly and with perfect logs.**

---

## 🚀 Key Features

- **🧙‍♂️ Guided, Real TTY Setup**  
  - Super-clear modular prompts and a friendly interactive wizard for rclone cloud remote setup.

- **🗂️ Unlimited, Flexible Backups**  
  - Create, edit, or delete as many backup configurations as you want—each links one local folder to any rclone-supported cloud target (Google Drive, OneDrive, Dropbox, S3, etc).
  - Manage multiple active backup services in parallel (different folders, clouds, frequencies—no collision).

- **👁️‍🗨️ Blazing Real-Time Monitoring**
  - Watches your chosen folder ** and all subfolders** recursively using efficient Linux inotify.
  - Detects **every file create, edit, or save** event and triggers a fast, one-file upload **within seconds**—no matter how deeply nested or renamed.
  - **Deletes are archived!** Even if you wipe a file locally (with delete or Shift+Delete), a full copy is already safely uploaded in cloud storage thanks to versioned rclone sync and frequent archive rotation.

- **🔁 Scheduled Full Sync**  
  - A full, safe folder-to-cloud sync runs every _N_ minutes (you choose; as little as 1 min).
  - Catches any missed changes, repairs accidental local or remote modifications, and re-archives or re-uploads anything missed between real-time events.

- **🔨 One-Click Service Management**
  - Every backup = one systemd-managed Linux service.
  - Create/edit/delete backup jobs any time, from the friendly CLI menu.
  - All critical state (what’s backed up, where, scheduling, log paths) is human-readable and easy to change—no mystery files.

- **🗒️ Ironclad Audit Logging**
  - Every backup, upload, or conflict is logged—so you can always see a full timeline for every backup service.
  - **Automatic weekly rotation:** Logs auto-reset every 7 days, so no more log bloat.
  - All events, errors, and file changes are timestamped and classified for troubleshooting (plus color bash notifies if on desktop).

- **🌈 User-focused Experience**
  - Colorful, randomly chosen ASCII art banners for every run
  - Menu, logging, and error messages are all TTY-clean
  - **Instant desktop notifications** for backup success/failure if in a graphical environment

- **🦺 Security by Design**
  - Safe for shared machines: strictly never runs as root
  - All sensitive install/cleanup uses granular `sudo` when required
  - No shell injection risk (user input is properly handled)
  - Correct file and process permissions applied everywhere

---

## ⚡ How It Works—In Plain English

- Instantly syncs any file you save, edit, or add—**as soon as you do it**, not just once an hour.  
- If you delete a file locally, your backup archive keeps a snapshot in the cloud.
- Every backup job is 100% independent: you can monitor `~/Work`, `~/Photos`, `/mnt/usb`, and more—all at the same time, each with its own settings and schedule.
- If you break a config, service, or log—just edit or rebuild with one menu command, no manual systemd or backup script editing needed.

---

## 🔒 Why Trust It For Your Strongest Data?

- **No more “oops I Shift+Deleted!”** That document is still in your cloud archive, even the last few minutes’ version.
- **You always know what happened, and when:** every sync/upload/error is logged with a timestamp and reason.
- **Storage-efficient:** Weekly log cleanup = no more gigabytes of forgotten logs eating up disk.

---

## 🗃️ Quickstart

```
git clone https://github.com/vold3mort-at-dev/cloud-backup-manager.git
cd cloud-backup-manager
pip3 install -r requirements.txt
python3 cloud_backup_manager.py
```
- Script will check/install `rclone`, `inotify-tools`, and `notify-send` if needed (Linux with sudo).
- Just use the menu!  
    - [1] New backup (choose folder, cloud, schedule)
    - [2] Edit backup settings at any time
    - [3] Completely remove any or all backup jobs (safe with double-confirmation)
    - [4] Quit, or repeat above as desired

---

## 🛠️ Tech Stack / Requirements

- **Linux** desktop/server with systemd
- **rclone**, **inotify-tools**, **libnotify-bin** (will be installed for you)
- **Python 3.7+**
- No external or cloud vendor lock-in; all backups are readable with any rclone tool.

---

## 🤩 Want to add a new feature or improve it?
PRs and Issues are welcome! Open an issue at [GitHub Issues](https://github.com/vold3mort-at-dev/cloud-backup-manager/issues)  
or fork and send a Pull Request.

---

## 💜 Credits

Built with love and care by [Vold3mort](https://github.com/vold3mort-at-dev).

---

## 📝 License

MIT (see LICENSE file)

---

> **Never lose a file again, even if you hit Shift+Delete. Let your backups work for you—not the other way around!**
