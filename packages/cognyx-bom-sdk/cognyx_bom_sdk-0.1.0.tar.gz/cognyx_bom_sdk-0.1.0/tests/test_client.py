"""Tests for the BOM client."""

from unittest.mock import Mock

import pytest

from cognyx_bom_sdk.client import BomClient, _parse_bom_data
from cognyx_bom_sdk.models import (
    Attribute,
    Bom,
    BomUpdates,
    ObjectType,
)


@pytest.fixture
def sample_object_type():
    """Create a sample object type for testing."""
    return ObjectType(
        id="type-123",
        name="Component",
        description="A component type",
        slug="component",
        bom_attributes=[
            Attribute(
                id="attr-1",
                name="weight",
                description="Weight attribute",
                slug="weight",
                type="number",
                value=0,
            ),
            Attribute(
                id="attr-2",
                name="material",
                description="Material attribute",
                slug="material",
                type="string",
                value="",
            ),
        ],
    )


@pytest.fixture
def sample_bom_data(sample_object_type):
    """Create sample BOM data for testing."""
    return {
        "id": "bom-123",
        "name": "Test BOM",
        "reference": "REF-123",
        "description": "Test BOM description",
        "status": "active",
        "instances": [
            {
                "id": "instance-1",
                "name": "Instance 1",
                "description": "First test instance",
                "bom_id": "bom-123",
                "view_id": "view-123",
                "parent_id": "parent-123",
                "object_type": sample_object_type,
                "object_type_id": "type-123",
                "quantity": 5,
                "custom_attributes": [
                    {
                        "id": "attr-1",
                        "name": "weight",
                        "description": "Weight attribute",
                        "slug": "weight",
                        "type": "number",
                        "value": 10,
                    },
                    {
                        "id": "attr-2",
                        "name": "material",
                        "description": "Material attribute",
                        "slug": "material",
                        "type": "string",
                        "value": "steel",
                    },
                ],
            },
            {
                "id": "instance-2",
                "name": "Instance 2",
                "description": "Second test instance",
                "bom_id": "bom-123",
                "view_id": "view-123",
                "parent_id": "parent-123",
                "object_type": sample_object_type,
                "object_type_id": "type-123",
                "quantity": 3,
                "custom_attributes": [
                    {
                        "id": "attr-1",
                        "name": "weight",
                        "description": "Weight attribute",
                        "slug": "weight",
                        "type": "number",
                        "value": 5,
                    },
                    {
                        "id": "attr-2",
                        "name": "material",
                        "description": "Material attribute",
                        "slug": "material",
                        "type": "string",
                        "value": "aluminum",
                    },
                ],
            },
        ],
    }


def test_parse_bom_data(sample_bom_data):
    """Test parsing BOM data."""
    bom = _parse_bom_data(sample_bom_data)
    assert isinstance(bom, Bom)
    assert bom.id == "bom-123"
    assert bom.name == "Test BOM"


class TestBomClient:
    """Tests for the BomClient class."""

    @pytest.fixture
    def client(self, sample_bom_data):
        """Create a BomClient instance for testing."""
        return BomClient(bom_data=sample_bom_data)

    @pytest.fixture
    def client_with_callback(self, sample_bom_data):
        """Create a BomClient instance with a callback for testing."""
        callback_mock = Mock()
        client = BomClient(bom_data=sample_bom_data, update_callback=callback_mock)
        return client, callback_mock

    def test_client_initialization(self, sample_bom_data):
        """Test that the client initializes correctly."""
        client = BomClient(bom_data=sample_bom_data)
        assert isinstance(client.bom, Bom)
        assert client.bom.id == "bom-123"
        assert client.update_callback is None

        callback_mock = Mock()
        client = BomClient(bom_data=sample_bom_data, update_callback=callback_mock)
        assert client.update_callback is callback_mock

    def test_get_bom_instance(self, client):
        """Test getting a BOM instance by name."""
        instance = client.get_bom_instance("Instance 1")
        assert instance is not None
        assert instance.id == "instance-1"
        assert instance.name == "Instance 1"

        # Test with non-existent instance
        instance = client.get_bom_instance("Non-existent")
        assert instance is None

    def test_get_bom_instance_by_id(self, client):
        """Test getting a BOM instance by ID."""
        instance = client.get_bom_instance_by_id("instance-1")
        assert instance is not None
        assert instance.id == "instance-1"
        assert instance.name == "Instance 1"

        # Test with non-existent instance
        instance = client.get_bom_instance_by_id("non-existent")
        assert instance is None

    def test_find_bom_instance(self, client):
        """Test finding a BOM instance using a predicate."""
        # Find instance with material = steel
        instance = client.find_bom_instance(
            lambda i: next((a for a in i.custom_attributes if a.name == "material"), None).value
            == "steel"
        )
        assert instance is not None
        assert instance.id == "instance-1"

        # Find instance with material = aluminum
        instance = client.find_bom_instance(
            lambda i: next((a for a in i.custom_attributes if a.name == "material"), None).value
            == "aluminum"
        )
        assert instance is not None
        assert instance.id == "instance-2"

        # Test with non-matching predicate
        instance = client.find_bom_instance(
            lambda i: next((a for a in i.custom_attributes if a.name == "material"), None).value
            == "plastic"
        )
        assert instance is None

    def test_list_bom_instances(self, client):
        """Test listing all BOM instances."""
        instances = client.list_bom_instances()
        assert len(instances) == 2
        assert instances[0].id == "instance-1"
        assert instances[1].id == "instance-2"

    def test_get_instance_attribute(self, client):
        """Test getting an attribute value from a BOM instance."""
        value = client.get_instance_attribute("instance-1", "weight")
        assert value == 10

        value = client.get_instance_attribute("instance-2", "material")
        assert value == "aluminum"

        # Test with non-existent attribute
        value = client.get_instance_attribute("instance-1", "non-existent")
        assert value is None

        # Test with non-existent instance
        with pytest.raises(ValueError, match="BOM instance with ID non-existent not found"):
            client.get_instance_attribute("non-existent", "weight")

    def test_set_instance_attribute(self, client_with_callback):
        """Test setting an attribute value on a BOM instance."""
        client, callback_mock = client_with_callback

        # Set an existing attribute
        client.set_instance_attribute("instance-1", "weight", 15)
        instance = client.get_bom_instance_by_id("instance-1")
        assert instance.get_attribute("weight") == 15

        # Verify callback was called with correct payload
        callback_mock.assert_called_once()
        args = callback_mock.call_args[0][0]
        assert args["type"] == BomUpdates.ATTRIBUTE_UPDATE
        assert args["payload"]["instance_id"] == "instance-1"
        assert args["payload"]["attribute_id"] == "attr-1"
        assert args["payload"]["attribute_value"] == 15

        # Test with non-existent instance
        with pytest.raises(ValueError, match="BOM instance with ID non-existent not found"):
            client.set_instance_attribute("non-existent", "weight", 20)

    def test_update_bom_instance(self, client_with_callback):
        """Test updating multiple attributes of a BOM instance."""
        client, callback_mock = client_with_callback
        callback_mock.reset_mock()

        # Update instance properties
        client.update_bom_instance("instance-1", name="New Name", quantity=10)
        instance = client.get_bom_instance_by_id("instance-1")
        assert instance.name == "New Name"
        assert instance.quantity == 10

        # Verify callback was called with correct payload
        callback_mock.assert_called_once()
        args = callback_mock.call_args[0][0]
        assert args["type"] == BomUpdates.INSTANCE_UPDATE
        assert args["payload"]["instance_id"] == "instance-1"
        assert args["payload"]["properties"]["name"] == "New Name"
        assert args["payload"]["properties"]["quantity"] == 10

        # Test with non-existent instance
        with pytest.raises(ValueError, match="BOM instance with ID non-existent not found"):
            client.update_bom_instance("non-existent", name="New Name")

    def test_attribute_not_found_in_object_type(self, client):
        """Test the case where an attribute is not found in the object type."""
        # This tests line 146 in client.py

        # Modify the object type to remove all attributes
        instance = client.get_bom_instance_by_id("instance-1")
        instance.object_type.bom_attributes = []

        # Now try to set an attribute that doesn't exist in the object type
        with pytest.raises(ValueError, match="Attribute 'non-existent' not found in object type"):
            client.set_instance_attribute("instance-1", "non-existent", 20)
