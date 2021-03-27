"""Tests for `flake8_name_migrations` package."""
import ast
from typing import Set

from flake8_name_migrations import Plugin


def _results(filename: str) -> Set[str]:
    tree = ast.parse('')
    plugin = Plugin(tree, filename)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_NMI001() -> None:
    assert _results('example.py') == set()
    assert _results('example.js') == set()
    assert _results('0003_this_is_properly_named.py') == set()
    assert _results('0001_auto_something.js') == set()

    for filename in [
        '0001_auto_something.py',
        '0029_auto_something.py',
        '9999_auto_example.py',
        '0004_auto_20210327_1738.py',
    ]:
        assert _results(filename) == {f'1:0 NMI001: Rename {filename} to something human readable'}


def test_plugin_version() -> None:
    assert isinstance(Plugin.version, str)
    assert '.' in Plugin.version


def test_plugin_name() -> None:
    assert isinstance(Plugin.name, str)
