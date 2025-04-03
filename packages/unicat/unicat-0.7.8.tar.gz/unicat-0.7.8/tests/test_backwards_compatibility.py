import pytest
from unicat.mutate import UnicatMutate
from unicat.utils import MockFeatures


def test_definition_metadata(unicat):
    unicat._features = MockFeatures()
    unicat.mutate = UnicatMutate(unicat)
    definition = unicat.get_definition("<definition-1>")
    with pytest.raises(AttributeError):
        definition.metadata


def test_class_metadata(unicat):
    unicat._features = MockFeatures()
    unicat.mutate = UnicatMutate(unicat)
    class_ = unicat.get_class("<class-1>")
    with pytest.raises(AttributeError):
        class_.metadata


def test_field_metadata(unicat):
    unicat._features = MockFeatures()
    unicat.mutate = UnicatMutate(unicat)
    field = unicat.get_field("<field-1>")
    with pytest.raises(AttributeError):
        field.metadata
