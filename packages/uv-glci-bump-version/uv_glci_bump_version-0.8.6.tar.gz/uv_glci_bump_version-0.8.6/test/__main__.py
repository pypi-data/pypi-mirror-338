import sys

import cyclopts
import pytest

import uv_glci_bump_version

APP = cyclopts.App(version='0.0.0')


@APP.default
def main(*, expect_full: bool = False, verbosity: int = 0):
    args = [
        f'--cov={uv_glci_bump_version.__name__}',
        '--cov-branch',
        '--cov-report=html',
        '--numprocesses=auto',
        f'--verbosity={verbosity}',
    ]
    if expect_full:
        args.append('--cov-fail-under=100')

    return pytest.main(args)


if __name__ == '__main__':
    APP.__call__(sys.argv[1:], print_error=True, exit_on_error=False)
