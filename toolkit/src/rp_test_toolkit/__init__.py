"""rp-test-toolkit: Test toolkit package for release-please experimentation."""

from dataclasses import dataclass


@dataclass
class Config:
    debug: bool = False
    timeout: int = 30


_config = Config()


def configure(debug: bool = False, timeout: int = 30) -> Config:
    global _config
    _config = Config(debug=debug, timeout=timeout)
    return _config
