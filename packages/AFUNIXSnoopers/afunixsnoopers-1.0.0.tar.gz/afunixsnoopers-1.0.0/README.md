# AFUNIXSnoopers

Listen on an AF_UNIX socket and log who connects

## Installing

Example systemd unit files and friends are in `daemon-files` of this repo

- create a venv, say in `~/.local/var/lib/AFUNIXSnoopers`, and source it
- `$ pip install AFUNIXSnoopers`
- place the systemd unit file and shell script into the correct folders, for example I use `~/.local/var/lib/systemd/{etc/user,usr/bin}`
- adjust the `WorkingDirectory` path in the `.service` unit if not using `~/.local/var/lib/AFUNIXSnoopers`. Snoopers files logs will be stored in here under `Snoopers`
- enable / start the template unit with `systemctl --user enable --now af-unix-snoopers@my-socket-path` where `my-socket-path` is the path to bind the socket to, with `/` replaced with `-` as per systemd unit templating rules
