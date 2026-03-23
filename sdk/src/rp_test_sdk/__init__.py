"""rp-test-sdk: Test SDK package for release-please experimentation."""

from importlib.metadata import version


def get_version() -> str:
    return version("rp-test-sdk")
def hello(): return "hello"
