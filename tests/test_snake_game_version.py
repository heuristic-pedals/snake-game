"""Simple, top level, unit test for `snake_game`."""

from importlib import metadata


def test_snake_game_version():
    """Test the pacakge version."""
    assert metadata.version("snake_game") == "0.0.0a0"
