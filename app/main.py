import sys
import shlex
import subprocess


def App():

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

        else:
            # If command is not found treat it as an external command
            try:
                subprocess.run(tokens)
            except FileNotFoundError:
                print(f"{tokens[0]}: command not found")
            except Exception as e:
                print(f"error running command: {e}")


if __name__ == "__main__":
    App()
