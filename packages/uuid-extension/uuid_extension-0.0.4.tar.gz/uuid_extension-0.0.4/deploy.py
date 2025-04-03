import subprocess
from argparse import ArgumentParser
from pathlib import Path
from shlex import split
from sys import version
from typing import Optional

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

ENC = "utf-8"
PYPROJECT = Path("pyproject.toml")


def shell(
    command: str,
    check: bool = True,
    shell: bool = False,
) -> tuple[int, str, str]:
    """
    Execute a command and return its results.

    Args:
        command: The command to execute
        check: If True, raise an exception on command failure
        shell: If True, runs command through the shell (security risk)
            Only use shell=True when absolutely necessary and with
            trusted input

    Returns:
        A tuple containing (return_code, stdout, stderr)

    Raises:
        subprocess.CalledProcessError: If check is True and the command fails
        ValueError: If the command is empty
    """
    if not command:
        msg = "Cannot execute empty command"
        raise ValueError(msg)

    args = command if shell else split(command)

    process = subprocess.run(  # noqa: S603
        args,
        shell=shell,
        text=True,
        capture_output=True,
        check=check,
    )

    return process.returncode, process.stdout, process.stderr


parser = ArgumentParser()
parser.add_argument("-v", "--version", help="New Version", required=False)
parser.add_argument(
    "-p",
    "--publish",
    action="store_true",
    help="Publish package after building",
    default=False,
)
parser.add_argument(
    "--no-build",
    action="store_true",
    help="Do not build project",
    default=False,
)
args = parser.parse_args()
logger.info(args)
exit()

# -------------------------------------------------------- #
#               CHECKING FOR CURRENT VERSION               #
# -------------------------------------------------------- #
pyproject = PYPROJECT.read_text(ENC)
for line in pyproject.splitlines():
    if line.startswith("version"):
        _, version = line.split(" = ")
        current_version = version.replace('"', "").lstrip().rstrip()
        logger.info(f"Current Version: {current_version}")
        major, minor, patch = [int(i) for i in current_version.split(".")]
        current_version_int = int(f"{major}{minor}{patch}")
        pass

args_version = args.version
if args_version:
    major, minor, patch = [int(i) for i in args_version.split(".")]
else:
    patch += 1

new_version = f"{major}.{minor}.{patch}"
new_version_int = int(f"{major}{minor}{patch}")

if new_version_int < current_version_int:
    msg = (
        "New version must be bigger than current_version! "
        f"{current_version=} vs. {new_version=}"
    )
    logger.error(msg)
    exit(1)

logger.info(f"New Version: {new_version}")


# -------------------------------------------------------- #
#                 BUILDING PROJECT USING UV                #
# -------------------------------------------------------- #
if not args.no_build:
    # CREATING NEW PYPROJECT FILE               #
    new_pyproject = pyproject.replace(
        f'version = "{current_version}"',
        f'version = "{new_version}"',
    )

    PYPROJECT.write_text(new_pyproject, encoding=ENC)
    logger.info("Replaced version in `pyproject.toml`")

    logger.info("Building project")
    cmd = "uv build"
    logger.warning(f"Running: {cmd}")

    return_code, stdout, stderr = shell(cmd)
    if return_code != 0:
        msg = f"Build failed with error: {stderr}"
        logger.error(msg)
        exit(1)

    logger.info("Build successful")

# -------------------------------------------------------- #
#                      PUBLISH PROJECT                     #
# -------------------------------------------------------- #
if args.publish:
    logger.info("Publishing project")

    cmd = "uv publish"
    logger.warning(f"Running: {cmd}")

    return_code, stdout, stderr = shell(cmd)
    if return_code != 0:
        msg = f"Build failed with error: {stderr}"
        logger.error(msg)
        exit(1)

    logger.info("Publish successful")
