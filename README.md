# HTS — Tiny Shell

A minimal, experimental shell implemented in Python for learning and prototyping.

## Overview

`app/main.py` implements a simple REPL that supports a few builtins and can run external commands. It's intended as a starting point if you're building your own shell and want a small, readable foundation.

## Features

- Builtins: `exit [code]`, `echo`
- Executes external programs using `subprocess.run`
- Robust prompt handling and basic parse-error reporting using `shlex`

## Requirements

- Python 3.8+ (the repository includes a `env/` virtual environment; use it if you want)

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
```

## Notes & Next Steps

- Add `readline` for history and line editing.
- Implement I/O redirection (`>`, `<`) and piping (`|`) via `subprocess.Popen`.
- Add job control and background execution (`&`).
- Add unit tests for builtins and command execution.
- Consider reorganizing into a `Shell` class for easier extension and testing.

## Contributing

Feel free to open issues or add improvements. Keep changes small and focused; prefer adding unit tests for new behavior.

