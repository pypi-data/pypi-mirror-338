import sys

from .plugin_template.plugin_handler import projetly_plugin_create
# from plugin_template.plugin import projetly_plugin

module_available = ["plugin"]
sub_command_available = ["create"]

def projetly_plugins(module, subcommand, name):
    if module not in module_available:
        sys.exit(f"Wrong module {module}. Available option {', '.join(module_available)}")
    if subcommand not in sub_command_available:
        sys.exit(f"Wrong subcommand {subcommand}. Available option {', '.join(sub_command_available)}")

    if module == "plugin" and subcommand == "create":
        projetly_plugin_create(module, subcommand, name)


if __name__ == "__main__": 
    module = "plugin"
    subcommand = "create"
    plugin_name= "jira"
    projetly_plugins(module, subcommand, plugin_name)