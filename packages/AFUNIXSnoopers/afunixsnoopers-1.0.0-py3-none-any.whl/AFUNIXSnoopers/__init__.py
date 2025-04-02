"""AF_UNIX Snoopers"""

__version__ = "1.0.0"

import os
import argparse
import signal
import datetime
import socket
import socketserver
import struct
from pathlib import Path

from ShellContexts import set_umask

class ForkingUnixStreamServer(socketserver.ForkingMixIn, socketserver.UnixStreamServer):
    # my contribution to socketserver :)
    # however my VPS is still on Python 3.10
    pass

class PublicForkingUnixStreamServer(ForkingUnixStreamServer):
    def server_bind(self):
        with set_umask(0):
            super().server_bind()

class HandlerBase(socketserver.StreamRequestHandler):
    SNOOPERS_FILES_DIR = NotImplemented

    def setup(self) -> None:
        super().setup()
        pid = os.getpid()
        self.timestamp = datetime.datetime.now().replace(microsecond = 0).isoformat()
        self.dest_file = self.SNOOPERS_FILES_DIR / f"{self.timestamp}-{pid}"

    def communicate(self) -> bytes:
        self.wfile.write(b"Hello snooper! Do say hello in 64k bytes or less...\n")
        b = self.rfile.read(64 << 10)
        return b

    def log_communication(self, creds_struct, b: bytes) -> None:
        pid, uid, gid = struct.unpack("iii", creds_struct)

        with self.dest_file.open("wb") as f:
            lines = [f"{line}\n" for line in [
                f"sock = {self.server.server_address}",
                f"time = {self.timestamp}",
                f"pid  = {pid}",
                f"uid  = {uid}",
                f"gid  = {gid}",
                f"",
            ]]
            f.write("".join(lines).encode())
            f.write(b)

    def handle(self) -> None:
        creds_struct = self.connection.getsockopt(socket.SOL_SOCKET, socket.SO_PEERCRED, struct.calcsize("iii"))
        b = self.communicate()
        self.log_communication(creds_struct, b)

def get_handler_class(snoopers_files_dir: Path):
    # this feels a bit crappy but it's easier than extending all the socketserver methods
    # reminds me of asyncio protocol factories
    # metaclasses not necessary

    class Handler(HandlerBase):
        SNOOPERS_FILES_DIR = snoopers_files_dir

    return Handler

def on_SIGTERM(*args):
    raise KeyboardInterrupt

def daemonize() -> None:
    if os.fork():
        os._exit(0)

def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument("addr", metavar = "SOCKET-PATH", help = "Bind to this path")

    parser.add_argument("--snoopers-dir", metavar = "SNOOPERS-DIR",
        help = "Place logs in this directory",
        type = Path,
        default = Path("Snoopers")
    )

    parser.add_argument("--fork", "-f", action = "store_true")

    args = parser.parse_args()

    return args

def main() -> None:
    args = get_cli_args()

    signal.signal(signal.SIGTERM, on_SIGTERM)

    server_address:     str  = args.addr
    snoopers_files_dir: Path = args.snoopers_dir
    do_fork:            bool = args.fork

    snoopers_files_dir.mkdir(exist_ok = True, parents = True)

    Handler = get_handler_class(snoopers_files_dir)

    server = PublicForkingUnixStreamServer(server_address, Handler)

    if do_fork:
        daemonize()

    with server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("Shutting down server")
            try:
                Path(server_address).unlink()
            except Exception:
                pass
