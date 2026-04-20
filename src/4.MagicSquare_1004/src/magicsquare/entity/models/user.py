"""User aggregate for the MagicSquare domain (entity layer)."""

from __future__ import annotations

import re
from dataclasses import dataclass

_EMAIL_RE = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


class UserValidationError(ValueError):
    """Raised when ``User`` field values break domain invariants."""


@dataclass(frozen=True, slots=True)
class User:
    """Application user identified by stable id and contact fields.

    This class belongs to the **entity** layer: it encodes domain data and
    invariants only. It must not depend on control or boundary packages.

    Attributes:
        user_id: Non-empty stable identifier (e.g. UUID string), stripped.
        email: Non-empty normalized email (stripped, lowercased) matching a
            pragmatic ``local@domain`` pattern.
        display_name: Non-empty human-readable name (stripped of outer space).
    """

    user_id: str
    email: str
    display_name: str

    def __post_init__(self) -> None:
        """Validate and normalize fields after construction.

        Raises:
            UserValidationError: If ``user_id``, ``email``, or
                ``display_name`` violates domain rules.
        """
        user_id = self.user_id.strip()
        if not user_id:
            raise UserValidationError("user_id must be non-empty.")
        object.__setattr__(self, "user_id", user_id)

        display_name = self.display_name.strip()
        if not display_name:
            raise UserValidationError("display_name must be non-empty.")
        object.__setattr__(self, "display_name", display_name)

        email = self.email.strip().lower()
        if not email:
            raise UserValidationError("email must be non-empty.")
        if not _EMAIL_RE.match(email):
            raise UserValidationError("email format is invalid.")
        object.__setattr__(self, "email", email)

    def with_display_name(self, new_display_name: str) -> User:
        """Return a new ``User`` with an updated display name.

        Args:
            new_display_name: Replacement display name; same validation as
                the constructor applies (non-empty after strip).

        Returns:
            A new immutable ``User`` instance; ``user_id`` and ``email`` are
            unchanged.

        Raises:
            UserValidationError: If ``new_display_name`` is invalid.
        """
        return User(
            user_id=self.user_id,
            email=self.email,
            display_name=new_display_name,
        )

    def with_email(self, new_email: str) -> User:
        """Return a new ``User`` with an updated email address.

        Args:
            new_email: Replacement email; normalized and validated like
                ``email`` at construction.

        Returns:
            A new immutable ``User`` instance; ``user_id`` and
            ``display_name`` are unchanged.

        Raises:
            UserValidationError: If ``new_email`` is invalid.
        """
        return User(
            user_id=self.user_id,
            email=new_email,
            display_name=self.display_name,
        )
