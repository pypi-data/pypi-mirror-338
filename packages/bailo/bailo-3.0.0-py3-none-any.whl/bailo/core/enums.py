from __future__ import annotations

from enum import Enum


class ValuedEnum(str, Enum):
    def __str__(self) -> str:
        return str(self.value)


class ModelVisibility(ValuedEnum):
    """Whether a model is publicly visible or not."""

    PRIVATE = "private"
    PUBLIC = "public"


class SchemaKind(ValuedEnum):
    """A type of schema."""

    MODEL = "model"
    ACCESS_REQUEST = "accessRequest"


class Role(ValuedEnum):
    """A reviewing role."""

    OWNER = "owner"
    MODEL_TECHNICAL_REVIEWER = "mtr"
    MODEL_SENIOR_RESPONSIBLE_OFFICER = "msro"


class EntryKind(ValuedEnum):
    """The type of model."""

    MODEL = "model"
    DATACARD = "data-card"


class MinimalSchema(ValuedEnum):
    """A minimal schema."""

    MODEL = "minimal-general-v10"
    DATACARD = "minimal-data-card-v10"
    ACCESS_REQUEST = "minimal-access-request-general-v10"
