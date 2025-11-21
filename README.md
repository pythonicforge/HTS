# HTS

A minimal, experimental shell implemented in Python for learning and prototyping how a shell (like ZSH, bash or shell) actually works in the real world

## Overview

`app/main.py` implements a simple REPL that supports a few builtins and can run external commands. It's intended as a starting point if you're building your own shell and want a small, readable foundation.

## Features

- Builtins: `exit [code]`, `echo`, `cd [dest]`, `type [command]`
- Executes external programs using `subprocess.run`
- Robust prompt handling and basic parse-error reporting using `shlex`

## Requirements

- Python 3.8+

## Run

Activate your virtual environment (optional) and run the shell:

```sh
# Optionally activate the provided venv
source env/bin/activate

# Run the tiny shell
python3 app/main.py
```

Example usage:

```
$ echo hello world
hello world
... (external command output)
$ exit 0
$ cd app/
$ type ls
```


## Contributing

Feel free to open issues or add improvements. Keep changes small and focused; prefer adding unit tests for new behavior.

