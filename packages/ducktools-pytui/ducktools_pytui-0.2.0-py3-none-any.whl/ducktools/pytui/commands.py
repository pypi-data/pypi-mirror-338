# ducktools-pytui
# MIT License
#
# Copyright (c) 2025 David C Ellis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import os.path
import shutil
import subprocess
import sys

import shellingham
from ducktools.pythonfinder import PythonInstall
from ducktools.pythonfinder.venv import PythonVEnv

from .util import run


ACTIVATE_FOLDER = os.path.join(os.path.dirname(__file__), "shell_scripts")

WIN_HISTORY_FIXED = False


def fix_win_history():
    """
    Fix the windows history and set a global flag that it has been set
    :return:
    """
    global WIN_HISTORY_FIXED
    from .util.win32_terminal_hist import set_console_history_info
    set_console_history_info()
    WIN_HISTORY_FIXED = True


def launch_repl(python_exe: str) -> None:
    if os.name == "nt" and not WIN_HISTORY_FIXED:
        fix_win_history()
    run([python_exe])  # type: ignore


def create_venv(
    python_runtime: PythonInstall,
    venv_path: str = ".venv",
    include_pip: bool = True,
    latest_pip: bool = True
) -> PythonVEnv:
    # Unlike the regular venv command defaults this will create an environment
    # and download the *newest* pip (assuming the parent venv includes pip)

    if os.path.exists(venv_path):
        raise FileExistsError(f"VEnv '{venv_path}' already exists.")

    python_exe = python_runtime.executable
    # These tasks run in the background so don't need to block ctrl+c
    # Capture output to not mess with the textual display
    # 3.8 support is going in the next pip update
    # Also always include the pip bundled with graalpy and don't update
    if (
        include_pip and (not latest_pip or python_runtime.version < (3, 9))
        or python_runtime.implementation == "graalpy"
    ):
        subprocess.run(
            [python_exe, "-m", "venv", venv_path],
            capture_output=True,
            check=True
        )
    else:
        subprocess.run(
            [python_exe, "-m", "venv", "--without-pip", venv_path],
            capture_output=True,
            check=True
        )
        if include_pip:
            # This actually seems to be faster than `--upgrade-deps`
            extras = ["pip"]
            if python_runtime.version < (3, 12):
                extras.append("setuptools")
            # Run the subprocess using *this* install to guarantee the presence of pip
            subprocess.run(
                [
                    sys.executable, "-m", "pip",
                    "--python", venv_path,
                    "install", *extras
                ],
                capture_output=True,
                check=True,
            )

    config_path = os.path.join(os.path.realpath(venv_path), "pyvenv.cfg")

    return PythonVEnv.from_cfg(config_path)


def delete_venv(venv_path: str):
    shutil.rmtree(venv_path, ignore_errors=True)


def install_requirements(
    *,
    venv: PythonVEnv,
    requirements_path: str,
    no_deps: bool = False,
):
    base_python = venv.parent_executable
    venv_path = venv.folder

    command = [
        base_python,
        "-m", "pip",
        "--python", venv_path,
        "install",
        "-r", requirements_path,
    ]
    if no_deps:
        command.append("--no-deps")

    run(command)  # type: ignore


def launch_shell(venv: PythonVEnv) -> None:
    # Launch a shell with a virtual environment activated.
    env = os.environ.copy()
    old_path = env.get("PATH", "")
    old_venv_prompt = os.environ.get("VIRTUAL_ENV_PROMPT", "")

    venv_prompt = f"pytui: {os.path.basename(venv.folder)}"
    venv_bindir = os.path.dirname(venv.executable)

    try:
        shell_name, shell = shellingham.detect_shell()
    except shellingham.ShellDetectionFailure:
        if os.name == "posix":
            shell_name, shell = "UNKNOWN", os.environ["SHELL"]
        elif os.name == "nt":
            shell_name, shell = "UNKNOWN", os.environ["COMSPEC"]
        else:
            raise RuntimeError(f"Shell detection failed")

    # dedupe and construct the PATH for the shell here
    if sys.platform == "win32" and shell_name == "bash":
        # Git bash needs special env handling as it follows linux conventions
        # And does not provide the PATH variable to child processes
        drive, venv_dir = os.path.splitdrive(venv_bindir)
        if ":" in drive:
            drive = drive.replace(":", "").lower()
            drive = f"/{drive}"
        venv_dir = venv_dir.replace("\\", "/")
        new_venv_bindir = "".join([drive, venv_dir])

        # Get the current git bash PATH
        prompt_getter = subprocess.run(
            [shell, "-ic", "echo $PATH"],
            text=True,
            capture_output=True
        )
        git_bash_path = prompt_getter.stdout.strip()
        deduped_path = []
        for p in git_bash_path.split(":"):
            if p in deduped_path:
                continue
            deduped_path.append(p)
        venv_env_path = ":".join([new_venv_bindir, *deduped_path])

    else:
        # In other cases follow the OS conventions
        deduped_path = []
        for p in old_path.split(os.pathsep):
            if p in deduped_path:
                continue
            deduped_path.append(p)

        venv_env_path = os.pathsep.join([venv_bindir, *deduped_path])

    # Environment variables may get overwritten so also create PYTUI versions
    env["PATH"] = env["PYTUI_PATH"] = venv_env_path
    env["VIRTUAL_ENV"] = env["PYTUI_VIRTUAL_ENV"] = venv.folder
    env["VIRTUAL_ENV_PROMPT"] = env["PYTUI_VIRTUAL_ENV_PROMPT"] = venv_prompt

    if os.name == "nt" and not WIN_HISTORY_FIXED:
        fix_win_history()

    if shell_name == "cmd":
        # Windows cmd prompt - history doesn't work for some reason
        shell_prompt = env.get("PROMPT", "$P$G")
        if old_venv_prompt and old_venv_prompt in shell_prompt:
            # Some prompts have colours etc
            new_prompt = shell_prompt.replace(old_venv_prompt, f"pytui: {venv_prompt}")
        else:
            new_prompt = f"({venv_prompt}) {shell_prompt}"
        env["PROMPT"] = new_prompt
        cmd = [shell, "/k"]  # This effectively hides the copyright message

    elif shell_name == "powershell":
        rcfile = os.path.join(ACTIVATE_FOLDER, "activate_pytui.ps1")
        with open(rcfile, encoding="utf8") as f:
            prompt_command = f.read()
        cmd = [shell, "-NoExit", prompt_command]

    elif shell_name == "bash":
        # Invoke our custom activation script as the rcfile
        # This includes ~/.bashrc but handles activation from Python
        rcfile = os.path.join(ACTIVATE_FOLDER, "activate_pytui.sh")
        cmd = [shell, "--rcfile", rcfile]

    elif shell_name == "zsh":
        # Try to get the shell PS1 from subprocess
        prompt_getter = subprocess.run(
            [shell, "-ic", "echo $PS1"],
            text=True, 
            capture_output=True
        )
        shell_prompt = prompt_getter.stdout.strip()
        
        if old_venv_prompt:
            shell_prompt = shell_prompt.removeprefix(old_venv_prompt)
        
        if not shell_prompt:
            shell_prompt = "%n@%m %1~ %#"
        
        shell_prompt = f"({venv_prompt}) {shell_prompt} "
        env["PS1"] = shell_prompt
        cmd = [shell, "--no-rcs"]

    else:
        # We'll probably need some extra config here
        print(f"UNSUPPORTED SHELL: {shell_name!r}.")
        print(
            "PATH may not have been correctly modified. "
            "Check if $PATH matches $PYTUI_PATH"
        )
        cmd = [shell]

    print("\nVEnv shell from ducktools.pytui: type 'exit' to close")
    run(cmd, env=env)  # type: ignore
