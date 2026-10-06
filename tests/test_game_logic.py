import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from logic_utils import check_guess


def test_winning_guess():
    """A guess equal to the secret should produce a win."""
    result, message = check_guess(50, 50)

    assert result == "Win"
    assert "Correct" in message


def test_guess_too_high():
    """A guess greater than the secret should be too high."""
    result, message = check_guess(60, 50)

    assert result == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    """A guess lower than the secret should be too low."""
    result, message = check_guess(40, 50)

    assert result == "Too Low"
    assert "HIGHER" in message