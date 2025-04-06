"""Basic tests for the llamafind package."""

import pytest


def test_import():
    """Test that the main package can be imported."""
    try:
        import llamafind
    except ImportError as e:
        pytest.fail(f"Failed to import llamafind: {e}")


def test_version():
    """Test that the package has a version attribute."""
    import llamafind

    assert hasattr(llamafind, "__version__")
    assert isinstance(llamafind.__version__, str)


# Add more core tests here later, e.g.:
# - Test configuration loading
# - Test basic search engine functionality (mocked)
# - Test utility functions
