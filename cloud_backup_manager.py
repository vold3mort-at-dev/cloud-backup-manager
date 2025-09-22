#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import getpass
import pwd
import configparser
from pathlib import Path
import readline

def input_tty(prompt=""):
    tty_path = "/dev/tty"
    with open(tty_path, "r") as tty_in, open(tty_path, "w") as tty_out:
        fd_in = tty_in.fileno()
        fd_out = tty_out.fileno()

        saved_stdin = os.dup(0)
        saved_stdout = os.dup(1)

        try:
            os.dup2(fd_in, 0)
            os.dup2(fd_out, 1)
            line = input(prompt)
            return line.rstrip("\n")
        finally:
            os.dup2(saved_stdin, 0)
            os.dup2(saved_stdout, 1)
            os.close(saved_stdin)
            os.close(saved_stdout)

def clear():
    os.system("clear" if os.name == "posix" else "cls")
    print_banner()

import random
from colorama import Fore, Style
import shutil

def print_banner():
    banners = [
        """ 
██╗░░░██╗░█████╗░██╗░░░░░██████╗░██████╗░███╗░░░███╗░█████╗░██████╗░████████╗
██║░░░██║██╔══██╗██║░░░░░██╔══██╗╚════██╗████╗░████║██╔══██╗██╔══██╗╚══██╔══╝
╚██╗░██╔╝██║░░██║██║░░░░░██║░░██║░█████╔╝██╔████╔██║██║░░██║██████╔╝░░░██║░░░
░╚████╔╝░██║░░██║██║░░░░░██║░░██║░╚═══██╗██║╚██╔╝██║██║░░██║██╔══██╗░░░██║░░░
░░╚██╔╝░░╚█████╔╝███████╗██████╔╝██████╔╝██║░╚═╝░██║╚█████╔╝██║░░██║░░░██║░░░
░░░╚═╝░░░░╚════╝░╚══════╝╚═════╝░╚═════╝░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""",
        """
 █████   █████          ████      █████  ████████                                      █████   
░░███   ░░███          ░░███     ░░███  ███░░░░███                                    ░░███    
 ░███    ░███   ██████  ░███   ███████ ░░░    ░███ █████████████    ██████  ████████  ███████  
 ░███    ░███  ███░░███ ░███  ███░░███    ██████░ ░░███░░███░░███  ███░░███░░███░░███░░░███░   
 ░░███   ███  ░███ ░███ ░███ ░███ ░███   ░░░░░░███ ░███ ░███ ░███ ░███ ░███ ░███ ░░░   ░███    
  ░░░█████░   ░███ ░███ ░███ ░███ ░███  ███   ░███ ░███ ░███ ░███ ░███ ░███ ░███       ░███ ███
    ░░███     ░░██████  █████░░████████░░████████  █████░███ █████░░██████  █████      ░░█████ 
     ░░░       ░░░░░░  ░░░░░  ░░░░░░░░  ░░░░░░░░  ░░░░░ ░░░ ░░░░░  ░░░░░░  ░░░░░        ░░░░░  
""",
        """
'##::::'##::'#######::'##:::::::'########:::'#######::'##::::'##::'#######::'########::'########:
 ##:::: ##:'##.... ##: ##::::::: ##.... ##:'##.... ##: ###::'###:'##.... ##: ##.... ##:... ##..::
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##:..::::: ##: ####'####: ##:::: ##: ##:::: ##:::: ##::::
 ##:::: ##: ##:::: ##: ##::::::: ##:::: ##::'#######:: ## ### ##: ##:::: ##: ########::::: ##::::
. ##:: ##:: ##:::: ##: ##::::::: ##:::: ##::...... ##: ##. #: ##: ##:::: ##: ##.. ##:::::: ##::::
:. ## ##::: ##:::: ##: ##::::::: ##:::: ##:'##:::: ##: ##:.:: ##: ##:::: ##: ##::. ##::::: ##::::
::. ###::::. #######:: ########: ########::. #######:: ##:::: ##:. #######:: ##:::. ##:::: ##::::
:::...::::::.......:::........::........::::.......:::..:::::..:::.......:::..:::::..:::::..:::::
""",
        """
                                                                                           
@@@  @@@   @@@@@@   @@@       @@@@@@@   @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@@@@@  
@@@  @@@  @@@@@@@@  @@@       @@@@@@@@  @@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@  
@@!  @@@  @@!  @@@  @@!       @@!  @@@      @@@  @@! @@! @@!  @@!  @@@  @@!  @@@    @@!    
!@!  @!@  !@!  @!@  !@!       !@!  @!@      @!@  !@! !@! !@!  !@!  @!@  !@!  @!@    !@!    
@!@  !@!  @!@  !@!  @!!       @!@  !@!  @!@!!@   @!! !!@ @!@  @!@  !@!  @!@!!@!     @!!    
!@!  !!!  !@!  !!!  !!!       !@!  !!!  !!@!@!   !@!   ! !@!  !@!  !!!  !!@!@!      !!!    
:!:  !!:  !!:  !!!  !!:       !!:  !!!      !!:  !!:     !!:  !!:  !!!  !!: :!!     !!:    
 ::!!:!   :!:  !:!   :!:      :!:  !:!      :!:  :!:     :!:  :!:  !:!  :!:  !:!    :!:    
  ::::    ::::: ::   :: ::::   :::: ::  :: ::::  :::     ::   ::::: ::  ::   :::     ::    
   :       : :  :   : :: : :  :: :  :    : : :    :      :     : :  :    :   : :     :     
""",
        """
============================================================================================
=  ====  ====    ====  ========       ======   =====  =====  ====    ====       ===        =
=  ====  ===  ==  ===  ========  ====  ===   =   ===   ===   ===  ==  ===  ====  =====  ====
=  ====  ==  ====  ==  ========  ====  ==   ===   ==  =   =  ==  ====  ==  ====  =====  ====
=  ====  ==  ====  ==  ========  ====  =======   ===  == ==  ==  ====  ==  ===   =====  ====
=   ==   ==  ====  ==  ========  ====  =====    ====  =====  ==  ====  ==      =======  ====
==  ==  ===  ====  ==  ========  ====  =======   ===  =====  ==  ====  ==  ====  =====  ====
==  ==  ===  ====  ==  ========  ====  ==   ===   ==  =====  ==  ====  ==  ====  =====  ====
===    =====  ==  ===  ========  ====  ===   =   ===  =====  ===  ==  ===  ====  =====  ====
====  =======    ====        ==       ======   =====  =====  ====    ====  ====  =====  ====
============================================================================================
"""
    ]

    banner = random.choice(banners)

    print(Fore.CYAN + banner + Style.RESET_ALL)

    terminal_width = shutil.get_terminal_size((80, 20)).columns
    footer_items = [
        f"Report issues : https://github.com/vold3mort-at-dev/cloud-backup-manager/issues",
        f"Version       : v1.0.0",
        f"GitHub        : https://github.com/vold3mort-at-dev"
    ]

    left_margin = int(terminal_width * 0.175)
    for item in footer_items:
        print(Fore.CYAN + " " * left_margin + item + Style.RESET_ALL)
    print("\n\n")


def set_immutable(path: Path, enable=True):
    if not path.exists():
        return
    cmd = ["sudo", "chattr", "+i" if enable else "-i", str(path)]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except Exception as e:
        print(f"[!] Failed to set immutability on {path}: {e}")

from contextlib import contextmanager

@contextmanager
def unlocked(path: Path):
    set_immutable(path, enable=False)
    try:
        yield
    finally:
        set_immutable(path, enable=True)


def run(cmd, check=True, env=None):
    return subprocess.run(cmd, shell=True, check=check, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)

def run_interactive(cmd_list, env=None):
    with open("/dev/tty", "rb", buffering=0) as tty_in, \
         open("/dev/tty", "wb", buffering=0) as tty_out:

        proc = subprocess.Popen(
            cmd_list,
            env=env,
            stdin=tty_in,
            stdout=tty_out,
            stderr=tty_out
        )
        proc.wait()
        return proc.returncode

def run_sudo(cmd, check=True):
    return subprocess.run(cmd, shell=True, check=check, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def enforce_non_root():
    clear()
    if os.geteuid() == 0: 
        print("❌ Error: Do not run this script as root or with sudo.")
        print("👉 Please run it as a normal user. Elevated actions are handled automatically.")
        sys.exit(1)

def get_target_user():
    user = os.environ.get("SUDO_USER") or os.environ.get("LOGNAME") or getpass.getuser()
    info = pwd.getpwnam(user)
    return user, Path(info.pw_dir), info.pw_uid, info.pw_gid

def apt_install_if_missing(pkg, bin_name=None):
    bin_name = bin_name or pkg

    if pkg == "inotify-tools":
        result = run("dpkg -s inotify-tools", check=False)
        if result.returncode != 0:
            print(f"→ Installing {pkg} ... (sudo will be used)")
            run_sudo("sudo apt-get update -y", check=True)
            run_sudo(f"sudo apt-get install -y {pkg}", check=True)
        else:
            print(f"✓ {pkg} already installed (via dpkg).")
        return

    result = run(f"command -v {bin_name}", check=False)
    if result.returncode != 0:
        print(f"→ Installing {pkg} ... (sudo will be used)")
        run_sudo("sudo apt-get update -y", check=True)
        run_sudo(f"sudo apt-get install -y {pkg}", check=True)
    else:
        print(f"✓ {pkg} already installed.")


def ensure_dir(path: Path, uid: int, gid: int, mode=0o700):
    if not path.exists():
        path.mkdir(parents=True)
    try:
        os.chown(str(path), uid, gid)
    except PermissionError:
        pass
    os.chmod(str(path), mode)

def write_file(path: Path, content: str, uid=None, gid=None, mode=0o600):
    with open(path, "w") as f:
        f.write(content)
    if uid is not None and gid is not None:
        try:
            os.chown(str(path), uid, gid)
        except PermissionError:
            pass
    os.chmod(str(path), mode)

def make_executable(path: Path):
    mode = path.stat().st_mode
    path.chmod(mode | 0o111)

def get_rclone_config_path(env=None):
    try:
        res = subprocess.run("rclone config file", shell=True, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True, env=env)
        if res.returncode == 0:
            for line in res.stdout.splitlines():
                line = line.strip()
                if line and (line.startswith("/") or (len(line) > 3 and line[1:3] == ':\\')):
                    return line
    except Exception:
        pass
    home = Path(env.get("HOME") if env and "HOME" in env else Path.home())
    return str(home / ".config" / "rclone" / "rclone.conf")

def fix_rclone_conf_perms(rclone_conf: Path, uid: int, gid: int):
    parent = rclone_conf.parent
    parent.mkdir(parents=True, exist_ok=True)
    try:
        os.chown(str(parent), uid, gid)
    except PermissionError:
        pass
    os.chmod(str(parent), 0o700)
    if rclone_conf.exists():
        try:
            os.chown(str(rclone_conf), uid, gid)
        except PermissionError:
            pass
        os.chmod(str(rclone_conf), 0o600)

def list_rclone_remotes(env=None):
    res = run("rclone listremotes", check=False, env=env)
    if res.returncode != 0:
        return []
    return [line.strip().rstrip(':') for line in res.stdout.splitlines() if line.strip()]

def validate_remote(remote_name, env):
    remotes = list_rclone_remotes(env=env)
    if remote_name not in remotes:
        return False
    res = run(f"rclone ls {remote_name}:", check=False, env=env)
    return res.returncode == 0

def initial_rclone_config(env, uid, gid):
    time.sleep(1)
    clear()
    print("You will now configure your rclone remote using the wizard.")
    print(f"Using rclone config file: {env.get('RCLONE_CONFIG')}")
    input_tty("Press Enter to launch the 'rclone config' wizard (a browser window may open)...")
    try:
        run_interactive(["rclone", "config"], env=env)
    except subprocess.CalledProcessError as e:
        print(f"rclone config exited with code {e.returncode}. If you cancelled, you can re-run later.")
    rclone_conf_path = Path(env["RCLONE_CONFIG"])
    fix_rclone_conf_perms(rclone_conf_path, uid, gid)
    time.sleep(0.5)
    while True:
        clear()
        remote_name = input_tty("Enter the exact name of your configured rclone remote: ").strip()
        if not remote_name:
            print("Remote name cannot be empty.")
            time.sleep(1)
            continue
        if validate_remote(remote_name, env):
            print(f"✓ Remote '{remote_name}' validated.")
            time.sleep(0.6)
            return remote_name
        else:
            print(f"✗ Remote '{remote_name}' invalid or inaccessible.")
            if input_tty("Retry rclone config wizard? (y/n): ").strip().lower() == 'y':
                try:
                    run_interactive(["rclone", "config"], env=env)
                except subprocess.CalledProcessError:
                    pass
                fix_rclone_conf_perms(rclone_conf_path, uid, gid)
            else:
                print("Cannot proceed without a valid remote. Exiting.")
                sys.exit(1)

def prompt(text, default):
    time.sleep(1)
    clear()
    print(text)
    print(f"\nLeave blank to use default: [{default}]")
    val = input_tty("Enter value: ").strip()
    return val if val else default

def create_backup_script(sh_path: Path, local_dir, remote_name, remote_dir, log_file):
    content = f"""#!/bin/bash
set -e

WATCH_DIR="{local_dir}"
REMOTE="{remote_name}:{remote_dir}"
ARCHIVE_DIR="{remote_name}:{remote_dir}-archive"
LOGFILE="{log_file}"
: "${{SYNC_INTERVAL_MINUTES:=5}}"
SYNC_INTERVAL=$((SYNC_INTERVAL_MINUTES * 60))
LAST_SYNC_FILE="$HOME/.{remote_name}_last_full_sync"

[ ! -f "$LAST_SYNC_FILE" ] && echo 0 > "$LAST_SYNC_FILE"

notify() {{
    if command -v notify-send >/dev/null 2>&1; then
        notify-send "CLOUD BACKUP: {remote_name}" "$1" >/dev/null 2>&1 || true
    fi
    echo "$(date) - $1" >> "$LOGFILE"
}}

network_up() {{
    targets=("8.8.8.8" "1.1.1.1" "google.com")
    for target in "${{targets[@]}}"; do
        if ping -q -c 1 -W 1 "$target" &>/dev/null; then
            return 0
        fi
    done
    return 1
}}

full_sync() {{
    notify "🔄 Performing full sync..."
    if rclone sync "$WATCH_DIR" "$REMOTE" \\
        --backup-dir "$ARCHIVE_DIR/$(date +'%Y-%m-%d_%H-%M-%S')" \\
        --log-level INFO \\
        --log-file "$LOGFILE" \\
        --create-empty-src-dirs; then
        notify "✅ Full sync successful."
        date +%s > "$LAST_SYNC_FILE"
    else
        notify "❌ Full sync failed."
    fi
}}

sync_file() {{
    local file_path="$1"
    local rel_path="${{file_path#$WATCH_DIR/}}"

    if ! network_up; then
        notify "⚠️ No network. Skipping file sync for $rel_path"
        return
    fi

    notify "📤 Syncing $rel_path"
    if rclone copyto "$file_path" "$REMOTE/$rel_path" --log-level INFO --log-file "$LOGFILE"; then
        notify "✅ File synced: $rel_path"
    else
        notify "❌ File sync failed: $rel_path"
    fi
}}

try_full_sync() {{
    now=$(date +%s)
    last_sync=$(cat "$LAST_SYNC_FILE" 2>/dev/null || echo 0)
    elapsed=$((now - last_sync))

    if [ "$elapsed" -lt "$SYNC_INTERVAL" ]; then
        return
    fi

    full_sync
}}

if network_up; then
    full_sync
else
    notify "⚠️ No network at startup. Skipping initial full sync."
fi

(
    while true; do
        try_full_sync
        sleep 10
    done
) &

inotifywait -m -r -e close_write,moved_to,create,delete --format '%w%f %e' "$WATCH_DIR" |
while read -r changed_file event; do
    if [[ "$event" == *DELETE* ]]; then
        rel_path="${{changed_file#$WATCH_DIR/}}"
        notify "🗑️ File deleted locally: $rel_path"
        echo "$(date) - File deleted locally: $rel_path" >> "$LOGFILE"
        try_full_sync
    elif [ -f "$changed_file" ]; then
        sync_file "$changed_file"
    fi
done
"""
    write_file(sh_path, content)
    make_executable(sh_path)


def create_service_only(service_base: str, sh_path: Path, user: str, home: Path, interval_minutes: int, uid: int):
    service_name = f"{service_base}.service"
    tmp_service = Path("/tmp") / service_name
    service_content = f"""[Unit]
Description=Cloud Backup (rclone) for {user}
After=network-online.target

[Service]
Type=simple
User={user}
Environment=HOME={home}
Environment=DISPLAY=:0
Environment=DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/{uid}/bus
Environment=SYNC_INTERVAL_MINUTES={interval_minutes}
ExecStart=/bin/bash "{sh_path}"
Restart=always
Nice=10

[Install]
WantedBy=default.target
"""
    write_file(tmp_service, service_content, mode=0o644)
    svc_dst = f"/etc/systemd/system/{service_name}"
    print("→ Moving service unit file into /etc/systemd/system (sudo may prompt)...")
    run_sudo(f"sudo mv {tmp_service} {svc_dst}", check=True)
    run_sudo(f"sudo systemctl daemon-reload", check=True)
    run_sudo(f"sudo systemctl enable --now {service_name}", check=True)
    return service_name

def main_create_new():
    time.sleep(1)
    clear()
    user, home, uid, gid = get_target_user()
    script_dir = Path(__file__).parent.resolve()

    config_dir = script_dir / "config"
    log_dir = script_dir / "logs"
    ensure_dir(config_dir, uid, gid)
    ensure_dir(log_dir, uid, gid)

    apt_install_if_missing("rclone")
    apt_install_if_missing("libnotify-bin", "notify-send")
    apt_install_if_missing("inotify-tools")

    base_env = os.environ.copy()
    base_env["HOME"] = str(home)
    rclone_conf_str = get_rclone_config_path(env=base_env)
    rclone_conf = Path(rclone_conf_str)
    rclone_env = base_env.copy()
    rclone_env["RCLONE_CONFIG"] = str(rclone_conf)
    fix_rclone_conf_perms(rclone_conf, uid, gid)

    print(f"Running as user: {user}")
    print(f"Using rclone config: {rclone_conf}")
    remote_name = initial_rclone_config(rclone_env, uid, gid)

    config_path = config_dir / f"{remote_name}_config.ini"
    if config_path.exists():
        print(f"A backup for remote '{remote_name}' already exists.")
        print("Please choose a different remote name or edit the existing one.")
        time.sleep(2)
        return

    log_file = log_dir / f"{remote_name}_backup.log"
    if not log_file.exists():
        log_file.touch()
        try:
            os.chown(str(log_file), uid, gid)
        except PermissionError:
            pass
        os.chmod(str(log_file), 0o600)

    default_local = str(home / "Documents")
    local_dir = prompt("Enter the full local directory path to back up.\nMake sure this directory exists.", default_local)
    remote_dir = prompt("Enter the remote directory path on your cloud remote (e.g., 'Linux_Backup'). \nMake sure this path/directory exists.", "Linux_Backup")

    while True:
        interval_in = prompt("Enter the backup interval in minutes (min=1, recommended 3-5).", "5")
        try:
            interval_val = int(interval_in)
            if interval_val < 1:
                raise ValueError()
            break
        except ValueError:
            print("Invalid input - please enter an integer >= 1.")
            time.sleep(1)

    sh_path = home / f".{remote_name}_realtime_sync.sh"
    print("Creating backup runner script...")
    create_backup_script(sh_path, local_dir, remote_name, remote_dir, log_file)
    try:
        os.chown(str(sh_path), uid, gid)
    except PermissionError:
        pass
    os.chmod(str(sh_path), 0o755)

    service_base = f"{remote_name}_{user}"
    print("Creating systemd service and timer (sudo will be used)...")
    service_name = create_service_only(service_base, sh_path, user, home, interval_val, uid)

    cfg = configparser.ConfigParser()
    cfg["SETTINGS"] = {
    "remote_name": remote_name,
    "local_dir": local_dir,
    "remote_dir": remote_dir,
    "log_file": str(log_file),
    "interval_minutes": str(interval_val),
    "service_name": service_name,
    "service_file": f"/etc/systemd/system/{service_name}",
    "backup_runner_file": str(sh_path),
    }
    with unlocked(config_path):
        with open(config_path, "w") as cf:
            cfg.write(cf)
            try:
                os.chown(str(config_path), uid, gid)
            except PermissionError:
                pass
                os.chmod(str(config_path), 0o600)

    set_immutable(config_path, enable=True)


    clear()
    print("="*60)
    print("Backup Service Installed Successfully 🎉")
    print("="*60)
    print(f"Systemd Service: {service_name}")
    print(f"Timer:           {service_name}  (every {interval_val} minute(s))")
    print(f"Log File:        {log_file}")
    print(f"Config File:     {config_path}")

    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    important_box = f"""
    {RED}{BOLD}
    ╔══════════════════════════════════════════════════════╗
    ║                      IMPORTANT                       ║
    ╠══════════════════════════════════════════════════════╣
    ║ ➤ Tokens expire! If backups fail, renew your token.  ║
    ║ ➤ Suggest renewing every ~15 days (any cloud).       ║
    ╚══════════════════════════════════════════════════════╝
    {RESET}
    """
    print(important_box)
    while True:
        confirm = input("⚠️ Please save or screenshot the above details. Continue? (y/n): ").strip().lower()
        if confirm == "y":
            break
        elif confirm == "n":
            print("Okay, take your time. I'll wait...")
        else:
            print("Invalid choice. Please type y or n.")

def edit_existing_backup():
    import re
    time.sleep(1)
    clear()
    user, home, uid, gid = get_target_user()
    script_dir = Path(__file__).parent.resolve()
    config_dir = script_dir / "config"
    configs = sorted(config_dir.glob("*_config.ini"))

    if not configs:
        print("No existing backups found.")
        time.sleep(2)
        return

    print("Select a backup config to edit:")
    for i, cfg in enumerate(configs, 1):
        print(f"{i}. {cfg.name}")

    try:
        idx = int(input_tty("Enter number to edit: ").strip())
        selected = configs[idx - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        time.sleep(1)
        return

    cfg = configparser.ConfigParser()
    cfg.read(selected)
    settings = cfg["SETTINGS"]

    remote_name   = settings.get("remote_name")
    log_file      = settings.get("log_file")
    service_name  = settings.get("service_name")
    service_file  = settings.get("service_file")
    sh_path       = Path(settings.get("backup_runner_file"))
    local_dir_cur  = settings.get("local_dir", "")
    remote_dir_cur = settings.get("remote_dir", "")
    interval_cur   = settings.get("interval_minutes", "5")

    print("\nEditing values. Press Enter to keep current.")
    print(f"(remote_name and log_file are locked and cannot be changed here)")
    print(f"remote_name: {remote_name}")
    print(f"log_file:    {log_file}\n")

    new_local_dir  = input_tty(f"Enter the full local directory path to back up.\nMake sure this directory exists. [{local_dir_cur}]: ").strip() or local_dir_cur
    new_remote_dir = input_tty(f"Enter the remote directory path on your cloud remote (e.g., 'Linux_Backup'). \nMake sure this path/directory exists. [{remote_dir_cur}]: ").strip() or remote_dir_cur

    while True:
        raw = input_tty(f"interval_minutes [{interval_cur}]: ").strip()
        if not raw:
            new_interval = int(interval_cur)
            break
        try:
            val = int(raw)
            if val < 1:
                raise ValueError()
            new_interval = val
            break
        except ValueError:
            print("Invalid input - please enter an integer >= 1.")

    settings["local_dir"] = new_local_dir
    settings["remote_dir"] = new_remote_dir
    settings["interval_minutes"] = str(new_interval)

    with unlocked(selected):
        with open(selected, "w") as f:
            cfg.write(f)
            try:
                os.chown(str(selected), uid, gid)
            except PermissionError:
                pass
                os.chmod(str(selected), 0o600)

                print("✅ Config updated on disk.")
    set_immutable(selected, enable=True)

    if not sh_path.exists():
        print(f"⚠️ Runner script not found at {sh_path}. Skipping script update.")
    else:
        txt = sh_path.read_text()

        txt, n1 = re.subn(r'(?m)^\s*WATCH_DIR=.*$', f'WATCH_DIR="{new_local_dir}"', txt)
        txt, n2 = re.subn(r'(?m)^\s*REMOTE=.*$', f'REMOTE="{remote_name}:{new_remote_dir}"', txt)
        txt, n3 = re.subn(r'(?m)^\s*ARCHIVE_DIR=.*$', f'ARCHIVE_DIR="{remote_name}:{new_remote_dir}-archive"', txt)
        txt, n4 = re.subn(r'(?m)^\s*: *"\$\{SYNC_INTERVAL_MINUTES:=[^}]*\}"', f': "${{SYNC_INTERVAL_MINUTES:=5}}"', txt)
        txt, n5 = re.subn(r'(?m)^\s*SYNC_INTERVAL=.*$', f'SYNC_INTERVAL=$(({new_interval} * 60))', txt)

        sh_path.write_text(txt)
        try:
            os.chown(str(sh_path), uid, gid)
        except PermissionError:
            pass
        os.chmod(str(sh_path), 0o755)

        print(f"✅ Runner script updated ({n1+n2+n3+n4+n5} substitutions).")

    svc_unit = service_name if service_name.endswith(".service") else f"{service_name}.service"
    svc_path = Path(service_file or f"/etc/systemd/system/{svc_unit}")

    if not svc_path.exists():
        print(f"⚠️ Service file {svc_path} not found; skipping systemd update/restart.")
        return

    sed_replace_cmd = (
        f"sudo sed -i 's/^Environment=SYNC_INTERVAL_MINUTES=.*/Environment=SYNC_INTERVAL_MINUTES={new_interval}/' {svc_path}"
    )
    rc = run_sudo(sed_replace_cmd, check=False).returncode

    found = run_sudo(f"sudo grep -q '^Environment=SYNC_INTERVAL_MINUTES=' {svc_path}", check=False).returncode == 0
    if not found:
        awk_cmd = (
            f"sudo awk '1; /^\\[Service\\]$/ {{ print \"Environment=SYNC_INTERVAL_MINUTES={new_interval}\" }}' "
            f"{svc_path} | sudo tee /tmp/_svc.tmp >/dev/null"
        )
        run_sudo(awk_cmd, check=True)
        run_sudo(f"sudo mv /tmp/_svc.tmp {svc_path}", check=True)

    run_sudo("sudo systemctl daemon-reload", check=True)
    run_sudo(f"sudo systemctl restart {svc_unit}", check=True)

    print(f"🔄 Service '{svc_unit}' reloaded and restarted with new interval = {new_interval} minutes.")
    time.sleep(1.0)


def uninstall_backups():
    import configparser
    import subprocess
    from pathlib import Path

    time.sleep(1)
    clear()
    print("Backup Service Uninstallation")
    print("=============================\n")
    print("You have two options:")
    print("1) Remove ALL backup services")
    print("2) Remove a SINGLE backup service\n")

    choice = input_tty("Enter your choice (1/2): ").strip()
    if choice not in ("1", "2"):
        print("Invalid choice. Aborted.")
        time.sleep(1)
        return

    user, home, uid, gid = get_target_user()
    script_dir = Path(__file__).parent.resolve()
    config_dir = script_dir / "config"
    cfg_files = sorted(config_dir.glob("*_config.ini"))

    if not cfg_files:
        print("No backup configs found in", config_dir)
        time.sleep(1)
        return

    def _load_settings(cfg_path: Path):
        cfg = configparser.ConfigParser()
        cfg.read(cfg_path)
        s = cfg["SETTINGS"]

        rn = s.get("remote_name", "").strip()
        svc_name = s.get("service_name", "").strip()
        if not svc_name and rn:
            svc_name = f"{rn}_{user}.service"
        elif svc_name and not svc_name.endswith(".service"):
            svc_name = f"{svc_name}.service"

        svc_file = s.get("service_file", "").strip()
        if svc_file:
            svc_path = Path(svc_file)
        else:
            svc_path = Path("/etc/systemd/system") / svc_name if svc_name else None

        sh_str = s.get("backup_runner_file", "").strip()
        if sh_str:
            sh_path = Path(sh_str)
        else:
            sh_path = home / f".{rn}_realtime_sync.sh" if rn else None

        log_str = s.get("log_file", "").strip()
        log_path = Path(log_str) if log_str else None

        return {
            "cfg_path": cfg_path,
            "remote_name": rn,
            "service_name": svc_name,
            "service_path": svc_path,
            "runner_path": sh_path,
            "log_path": log_path,
        }

    def _remove_one(sinfo: dict):
        rn          = sinfo["remote_name"]
        svc_name    = sinfo["service_name"]
        svc_path    = sinfo["service_path"]
        runner_path = sinfo["runner_path"]
        log_path    = sinfo["log_path"]

        print(f"\n— Removing '{rn}' —")

        if svc_name:
            run_sudo(f"sudo systemctl stop {svc_name}", check=False)
            run_sudo(f"sudo systemctl disable {svc_name}", check=False)

        if svc_path and svc_path.exists():
            try:
                run_sudo(f"sudo rm {svc_path}", check=False)
                print(f"  ✓ Removed service file: {svc_path}")
            except Exception as e:
                print(f"  ⚠️ Could not remove service file {svc_path}: {e}")
        else:
            if svc_path:
                print(f"  ⚠️ Service file not found: {svc_path}")

        if runner_path and runner_path.exists():
            try:
                runner_path.unlink()
                print(f"  ✓ Removed runner script: {runner_path}")
            except Exception as e:
                print(f"  ⚠️ Could not remove runner script {runner_path}: {e}")
        else:
            if runner_path:
                print(f"  ⚠️ Runner script not found: {runner_path}")

        if log_path and log_path.exists():
            try:
                log_path.unlink()
                print(f"  ✓ Removed log file: {log_path}")
            except Exception as e:
                print(f"  ⚠️ Could not remove log file {log_path}: {e}")

        return True

    if choice == "1":
        confirm1 = input_tty("⚠️ You selected to remove ALL services. Continue? (yes/no): ").strip().lower()
        if confirm1 != "yes":
            print("Aborted.")
            return

        confirm2 = input_tty("⚠️ Are you REALLY sure? Type 'yes' to confirm or 'no' to go back: ").strip().lower()
        if confirm2 != "yes":
            print("Aborted.")
            return

        confirm3 = input_tty("Type 'remove-all-services' to FINALIZE: ").strip()
        if confirm3 != "remove-all-services":
            print("Aborted. You must type exactly 'remove-all-services'.")
            return

        to_delete_cfgs = []
        for cfgp in cfg_files:
            s = _load_settings(cfgp)
            _remove_one(s)
            to_delete_cfgs.append(s["cfg_path"])

        run_sudo("sudo systemctl daemon-reload", check=False)
        print("\n✅ All services stopped/disabled and files removed (service, runner, logs).")

        while True:
            print("\nWould you like to remove the rclone remote(s) associated with these services?")
            ans = input_tty("Type 'yes' to launch rclone config, 'no' to skip: ").strip().lower()
            if ans == "yes":
                os.system("rclone config")
                again = input_tty("\nHave you deleted the remote(s)? (yes/no): ").strip().lower()
                if again == "yes":
                    remotes = subprocess.check_output(["rclone", "listremotes"], text=True).splitlines()
                    if remotes:
                        print("\n⚠️ The following remotes still exist:\n")
                        for r in remotes:
                            print(" -", r)
                        print("\nIf needed, re-run 'rclone config' to delete them.")
                    else:
                        print("\n✅ No remotes left. Clean removal complete.")
                    break
                else:
                    print("Okay, skipping remote deletion.")
                    break
            elif ans == "no":
                print("Skipping remote removal.")
                break
            else:
                print("Invalid input. Please type yes or no.")

        print("\n⚠️ FINAL WARNING: Deleting ALL backup config files is irreversible.")
        print(f"   Files to delete ({len(to_delete_cfgs)}):")
        for p in to_delete_cfgs:
            print(f"   - {p}")
        confirm_cfg = input_tty("Type 'delete-all-configs' to confirm, or anything else to cancel: ").strip()
        if confirm_cfg == "delete-all-configs":
            for p in to_delete_cfgs:
                try:
                    set_immutable(p, enable=False)
                    p.unlink(missing_ok=True)
                except Exception as e:
                    print(f"  ⚠️ Could not delete {p}: {e}")
            print("\n🗑️ All config files deleted. Uninstallation complete ✅")
        else:
            print("\nConfig files kept. Uninstallation complete (without deleting configs).")

        time.sleep(2)
        return

    else:
        print("\nAvailable configurations:\n")
        entries = []
        for i, cfgp in enumerate(cfg_files, 1):
            s = _load_settings(cfgp)
            rn = s["remote_name"] or "(unknown-remote)"
            svc = s["service_name"] or "(unknown-service)"
            print(f"{i}) remote={rn}  service={svc}  file={cfgp.name}")
            entries.append(s)

        print()
        try:
            pick = int(input_tty("Select a number to remove: ").strip())
            s = entries[pick - 1]
        except Exception:
            print("Invalid selection. Aborted.")
            return

        rn = s["remote_name"] or "(unknown-remote)"
        svc_unit = s["service_name"] or "(unknown-service)"
        confirm = input_tty(f"⚠️ Are you sure you want to remove service '{svc_unit}' for remote '{rn}'? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Aborted.")
            return

        _remove_one(s)
        run_sudo("sudo systemctl daemon-reload", check=False)
        print(f"\n✅ Service '{svc_unit}' and related files removed.\n")

        while True:
            print("\nWould you like to remove the rclone remote(s) associated with this service?")
            ans = input_tty("Type 'yes' to launch rclone config, 'no' to skip: ").strip().lower()
            if ans == "yes":
                os.system("rclone config")
                again = input_tty("\nHave you deleted the remote? (yes/no): ").strip().lower()
                if again == "yes":
                    remotes = subprocess.check_output(["rclone", "listremotes"], text=True).splitlines()
                    if remotes:
                        print("\n⚠️ The following remotes still exist:\n")
                        for r in remotes:
                            print(" -", r)
                        print("\nPlease re-run 'rclone config' to delete them if needed.")
                    else:
                        print("\n✅ No remotes left. Clean removal complete.")
                    break
                else:
                    print("Okay, skipping remote deletion.")
                    break
            elif ans == "no":
                print("Skipping remote removal.")
                break
            else:
                print("Invalid input. Please type yes or no.")

        cfg_path = s["cfg_path"]
        if cfg_path and cfg_path.exists():
            print("\n⚠️ FINAL WARNING: You are about to permanently delete this backup config file.")
            print(f"   {cfg_path}")
            confirm_del = input_tty("Type 'delete' to confirm, or anything else to cancel: ").strip().lower()
            if confirm_del == "delete":
                try:
                    set_immutable(cfg_path, enable=False)
                    cfg_path.unlink()
                    print("\n🗑️ Config file deleted. Uninstallation complete ✅")
                except Exception as e:
                    print("⚠️ Could not delete config file:", e)
            else:
                print("\nConfig file kept. Uninstallation partially complete.")

        time.sleep(2)


def menu():
    while True:
        time.sleep(1)
        clear()
        print("="*60)
        print("🔧  CLOUD BACKUP MANAGER")
        print("="*60)
        print("1. Create a new backup service")
        print("2. Edit an existing backup service")
        print("3. Uninstall all backup services")
        print("4. Exit")
        print("="*60)

        choice = input_tty("Enter your choice (1-4): ").strip()
        if choice == "1":
            main_create_new()
        elif choice == "2":
            edit_existing_backup()
        elif choice == "3":
            uninstall_backups()
        elif choice == "4":
            print("Exiting...")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")
            time.sleep(1)

if __name__ == "__main__":
    try:
        enforce_non_root()
        menu()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(0)
    