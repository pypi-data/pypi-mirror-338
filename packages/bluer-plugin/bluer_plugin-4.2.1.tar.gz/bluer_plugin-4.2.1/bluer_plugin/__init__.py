NAME = "bluer_plugin"

ICON = "🌀"

DESCRIPTION = f"{ICON} a git template for an awesome-bash-cli plugin."

VERSION = "4.2.1"

REPO_NAME = "bluer-plugin"

MARQUEE = "https://github.com/kamangir/assets/raw/main/blue-plugin/marquee.png?raw=true"

ALIAS = "@plugin"


def fullname() -> str:
    return f"{NAME}-{VERSION}"
