import pytest  # type: ignore
from pathlib import Path
import logging
from typer import Typer, Option  # type: ignore
from click.testing import Result
from typer.testing import CliRunner  # type: ignore
from typing import Annotated, Optional
import sys

from multilevellogger import (
    MultiLevelLogger,
    getMultiLevelLogger,
    VERBOSE,
    MESSAGE,
)

# from icecream import ic  # type: ignore

app = Typer()


@app.command()
def mlogger(
    level: int = logging.NOTSET,
    log: Annotated[Optional[Path], Option(help="log to FILE", metavar="FILE")] = None,
) -> None:
    """MultilevelLogger demo"""
    try:
        print(f"log_level: {level}, log: {log}")
        handler: logging.Handler = logging.StreamHandler(sys.stderr)
        mlogger: MultiLevelLogger = getMultiLevelLogger(
            __name__, level=level, handler=handler
        )
        if log is not None:
            mlogger.addLogFile(log_file=log)

        mlogger.debug("debug")
        mlogger.info("info")
        mlogger.verbose("verbose")
        mlogger.message("message")
        mlogger.warning("warning")
        mlogger.error("error")
    except Exception as err:
        mlogger.error(f"{err}")
        raise SystemExit(4)


@pytest.mark.parametrize(
    "args,lines",
    [
        ([], 3),
        (["--level", f"{logging.DEBUG}"], 7),
        (["--level", f"{logging.INFO}"], 6),
        (["--level", f"{VERBOSE}"], 5),
        (["--level", f"{MESSAGE}"], 4),
        (["--level", f"{logging.WARN}"], 3),
        (["--level", f"{logging.WARN}", "--log", "test.log"], 3),
        (["--level", f"{logging.ERROR}"], 2),
    ],
)
def test_1_multilevellogger(args: list[str], lines: int) -> None:
    result: Result = CliRunner().invoke(app, [*args])

    assert result.exit_code == 0, (
        f"test failed: LOG_LEVEL= {' '.join(args)}\n{result.output}"
    )

    lines_output: int = len(result.output.splitlines())
    assert lines_output == lines, f"incorrect output {lines_output} != {lines}"

    if len(args) > 0:
        log_level: int = int(args[1])
        if log_level == logging.DEBUG:
            param: str = "debug"
        elif log_level == logging.INFO:
            param = "info"
        elif log_level == MESSAGE:
            param = "message"
        elif log_level == VERBOSE:
            param = "verbose"
        elif log_level == logging.WARN:
            param = "warning"
        elif log_level == logging.ERROR:
            param = "error"
        else:
            raise ValueError(f"unknown log level: {log_level}")
        assert result.stdout.find(param) >= 0, f"no expected output found: '{param}'"
    else:
        assert result.stdout.find("warning") >= 0, (
            f"no expected output found: 'warning': {result.stdout}"
        )
    assert result.stdout.find("error") >= 0, "no expected output found: 'error'"


if __name__ == "__main__":
    app()
