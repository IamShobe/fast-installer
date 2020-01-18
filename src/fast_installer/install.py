#!/usr/bin/env python3
"""Usage:
install.py show
install.py [options]

-a --all                    install all in config.
-f --force                  force linking new paths [default: False].
-s --safe                   stop at a warning.
--config=<config_path>      config file of the install script [default: config.yaml].
--base-dir=<base_dir>       base directory of all assets [default: .].
"""
import os
from collections import Counter

import yaml
import docopt
import inquirer
from inquirer.themes import GreenPassion
from attrdict import AttrDict

from .methods import CONFIG_TO_HANDLER
from .methods.utils import Colors


def get_config(path):
    if not os.path.exists(path):
        print(f"{Colors.FAIL}"
              f"Config file not found: `{path}`!"
              f"{Colors.ENDC}")
        os._exit(1)

    with open(path) as config_f:
        return AttrDict(yaml.load(config_f))


def get_filtered_options(options):
    print(f"{Colors.OKBLUE}Config loaded successfully!{Colors.ENDC}")
    settings = [setting["key"] for setting in options]

    questions = [
        inquirer.Checkbox('interests',
                          message="What are you interested in?",
                          choices=settings),
    ]
    answers = inquirer.prompt(questions, theme=GreenPassion())
    if answers is None:
        answers = {
            "interests": []
        }

    return [setting for setting in options
            if setting["key"] in answers["interests"]]


def install(args):
    config = get_config(args["--config"])
    if args["--all"]:
        options = config.options
    else:
        options = get_filtered_options(config.options)

    base_dir = os.path.abspath(args["--base-dir"])

    for setting in options:
        total_steps = len(setting.steps)
        print(f"Running settings of "
              f"{Colors.fg.lightred}{setting.key}{Colors.ENDC} - "
              f"{Colors.OKBLUE}{setting.description}{Colors.ENDC}")
        for index, step in enumerate(setting.steps):
            counter = Counter()
            print(f"- Running step {1 + index}/{total_steps} - "
                  f"{step.description}")
            for key, handler in CONFIG_TO_HANDLER.items():
                if hasattr(step, key):
                    try:
                        should_continue, error_message = handler(base_dir,
                            getattr(step, key), args=args, counter=counter)

                    except Exception as e:
                        should_continue = False
                        error_message = str(e)

                    if not should_continue:
                        print(f"{Colors.FAIL}Failed!{Colors.ENDC}")
                        if error_message:
                            print(f"{Colors.FAIL}{error_message}{Colors.ENDC}")
                        return

            print(f"- Done step {1 + index}/{total_steps} - "
                  f"{Colors.OKGREEN}"
                  f"successes: {counter['ok']}"
                  f"{Colors.ENDC}, {Colors.WARNING}"
                  f"warnings: {counter['warnings']}"
                  f"{Colors.ENDC}, {Colors.FAIL}"
                  f"errors: {counter['errors']}"
                  f"{Colors.ENDC}")
            if counter['warnings'] > 0:
                print(f"{Colors.WARNING}"
                      f"***Try running with -f to force install***"
                      f"{Colors.ENDC}")
                if args["--safe"]:
                    return

    print(f"{Colors.fg.green}Done!{Colors.ENDC}")


def show_config(args):
    config = get_config(args["--config"])
    for setting in config.options:
        print(f"{setting.key} - {setting.description}")
        for index, step in enumerate(setting.steps):
            print(f" step {index + 1} - {step.description}")


def main():
    args = docopt.docopt(__doc__)

    if args["show"]:
        show_config(args)

    else:
        install(args)


if __name__ == '__main__':
    main()
