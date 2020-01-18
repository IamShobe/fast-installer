from .link import make_links
from .shell import run_shell

CONFIG_TO_HANDLER = {
    "links": make_links,
    "shell": run_shell
}
