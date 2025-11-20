import sys
import os
import shlex
import subprocess

def find_path(cmd):
    paths = os.environ.get("PATH", "").split(os.pathsep)
    for p in paths:
        full = os.path.join(p, cmd)
        if os.path.isfile(full) and os.access(full, os.X_OK):
            return full
    return None

def App():

    BUILTINS = ["exit", "echo", "cd", "type"]

    while True:
        try:
            command = input("$ ")
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(0)

        if not command or not command.strip():
            continue

        try:
            tokens = shlex.split(command)
        except ValueError as e:
            print(f"parse error: {e}")
            continue

        if not tokens:
            continue

        cmd = tokens[0].lower()

        if cmd == "exit":
            code = 0
            if len(tokens) > 1:
                try:
                    code = int(tokens[1])
                except ValueError:
                    print("exit: numeric argument required")
                    continue
            sys.exit(code)

        elif cmd == "echo":
            print(" ".join(tokens[1:]))

        elif cmd == "cd":
            target = ""
            if len(tokens) < 2:
                target = os.path.expanduser("~")
            else:
                target = tokens[1]

            try:
                os.chdir(target)
            except Exception as e:
                print(e)

        elif cmd == "type":
            if len(tokens) < 2:
                print("type: missing argument")
                continue

            target = tokens[1]

            if target in BUILTINS:
                print(f"{target} is a shell builtin")
                continue

            path = find_path(target)
            if path:
                print(f"{target} is {path}")
            else:
                print(f"{target}: not found")


        else:
            try:
                subprocess.run(tokens)
            except FileNotFoundError:
                print(f"{tokens[0]}: command not found")
            except Exception as e:
                print(f"{e}: ran into an error. Please try again later.")


if __name__ == "__main__":
    App()
