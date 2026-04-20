"""Tests for :class:`magicsquare.entity.models.user.User`."""

from __future__ import annotations

import pytest

from magicsquare.entity.models.user import User, UserValidationError


def test_user_creation_strips_and_normalizes_fields() -> None:
    """Valid raw fields are normalized (id strip, email lower, name strip)."""
    # Arrange
    raw_id = "  usr-1  "
    raw_email = " Foo@Example.COM "
    raw_name = "  Alice  "

    # Act
    user = User(user_id=raw_id, email=raw_email, display_name=raw_name)

    # Assert
    assert user.user_id == "usr-1"
    assert user.email == "foo@example.com"
    assert user.display_name == "Alice"


def test_user_rejects_blank_user_id() -> None:
    """Empty ``user_id`` after strip raises ``UserValidationError``."""
    # Arrange
    blank_id = "   "

    # Act / Assert
    with pytest.raises(UserValidationError, match="user_id"):
        User(user_id=blank_id, email="a@b.co", display_name="Bob")


def test_user_rejects_blank_display_name() -> None:
    """Empty ``display_name`` after strip raises ``UserValidationError``."""
    # Arrange
    blank_name = "\t  "

    # Act / Assert
    with pytest.raises(UserValidationError, match="display_name"):
        User(user_id="u1", email="a@b.co", display_name=blank_name)


def test_user_rejects_invalid_email_format() -> None:
    """Malformed email raises ``UserValidationError``."""
    # Arrange
    bad_email = "not-an-email"

    # Act / Assert
    with pytest.raises(UserValidationError, match="email format"):
        User(user_id="u1", email=bad_email, display_name="Cara")


def test_user_rejects_blank_email() -> None:
    """Whitespace-only email raises ``UserValidationError``."""
    # Arrange
    blank_email = "   "

    # Act / Assert
    with pytest.raises(UserValidationError, match="email"):
        User(user_id="u1", email=blank_email, display_name="Dan")


def test_with_display_name_returns_new_user_and_preserves_ids() -> None:
    """``with_display_name`` keeps ids and replaces only the visible name."""
    # Arrange
    original = User(
        user_id="u-42",
        email="eve@example.com",
        display_name="Eve",
    )

    # Act
    renamed = original.with_display_name("  Eve Adams  ")

    # Assert
    assert renamed is not original
    assert renamed.user_id == "u-42"
    assert renamed.email == "eve@example.com"
    assert renamed.display_name == "Eve Adams"


def test_with_email_returns_new_user_and_preserves_others() -> None:
    """``with_email`` updates email only and re-validates format."""
    # Arrange
    original = User(
        user_id="u-7",
        email="old@example.com",
        display_name="Finn",
    )

    # Act
    updated = original.with_email(" NEW@Example.COM ")

    # Assert
    assert updated is not original
    assert updated.user_id == "u-7"
    assert updated.display_name == "Finn"
    assert updated.email == "new@example.com"
