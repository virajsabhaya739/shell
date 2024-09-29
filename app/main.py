import sys
import os

valid_cs = ["exit", "echo", "type"]

def main():
    PATH = os.environ.get("PATH")
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command_full = input()

        cmd_split = command_full.split()
        # print(cmd_split[0])

        if cmd_split[0] not in valid_cs:
            command_not_found(command_full)
        elif cmd_split[0] == "exit":
            # handle exit commands
            handle_exit_command(cmd_split, command_full)
        elif cmd_split[0] == 'echo':
            handle_echo_command(cmd_split, command_full)
        elif cmd_split[0] == 'type':
            handle_type_command(cmd_split, command_full, PATH)
        else:
            command_not_found(command_full)


def handle_type_command(cmd_split: list, cmd_full: str, path: str) -> None:
    if len(cmd_split) > 1:
        is_found = False
        paths = path.split(":")
        for path in paths:
            if os.path.isfile(f"{path}/{cmd_split[1]}"):
                print(f"{cmd_split[1]} is {path}/{cmd_split[1]}")
                is_found = True
                break
        if not is_found:
            if cmd_split[1] in valid_cs:
                print(f"{cmd_split[1]} is a shell builtin")
            else:
                print(f"{cmd_split[1]}: not found")
    else:
        command_not_found(cmd_full)


def handle_echo_command(cmd_split: list, cmd_full: str) -> None:
    if len(cmd_split) > 1:
        plain_cmd = cmd_full.replace('"', "").replace("'", "")
        print(plain_cmd[len(cmd_split[0]) + 1:])
    else:
        command_not_found(cmd_full)


def handle_exit_command(cmd_split: list, cmd_full: str) -> None:
    if len(cmd_split) > 1:
        if cmd_split[1] == "0":
            exit()
        else:
            command_not_recognaized(cmd_full)
    else:
        command_not_found(cmd_full)


def command_not_found(cmd: str) -> None:
    print(f"{cmd}: command not found")


def command_not_recognaized(cmd: str) -> None:
    print(f"{cmd}: command not recognaized")

if __name__ == "__main__":
    main()
