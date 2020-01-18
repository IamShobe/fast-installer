import os
import subprocess

from attrdict import AttrDict

from .utils import Colors


TIMEOUT = 10  # seconds


def run_shell(base_dir, commands, args, counter=None):
    for index, command in enumerate(commands):
        if not isinstance(command, dict):
            command = AttrDict(command=command)

        command.setdefault("timeout", TIMEOUT)
        command.setdefault("allow_fail", False)
        print(f"  {Colors.fg.lightred}[+]{Colors.ENDC} "
              f"Running {Colors.BOLD}{Colors.fg.pink}`{command.command}"
              f"`{Colors.ENDC}",
              end=" ")
        pipe = subprocess.Popen(command.command, shell=True)
        try:
            pipe.wait(command.timeout)

        except subprocess.TimeoutExpired:
            pipe.kill()
            if not command.allow_fail:
                if counter is not None:
                    counter["errors"] += 1
                return False, "Timeout expired running command..."

            print(f"{Colors.WARNING}timeout running command, "
                  f"skipping!{Colors.ENDC}")
            if counter is not None:
                counter["warnings"] += 1
            continue

        if pipe.returncode != os.EX_OK:
            if not command.allow_fail:
                if counter is not None:
                    counter["errors"] += 1
                return False, f"Bad exit code {pipe.returncode}"

            print(f"{Colors.WARNING}bad exit code {pipe.returncode}, "
                  f"skipping!{Colors.ENDC}")
            if counter is not None:
                counter["warnings"] += 1
            continue

        print(f"{Colors.OKGREEN}command done!{Colors.ENDC}")
        if counter is not None:
            counter["ok"] += 1

    return True, ""
