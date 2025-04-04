"""Tests for the BOM SDK models."""

import pytest
from pydantic import ValidationError

from cognyx_bom_sdk.models import (
    Attribute,
    AttributeUpdatePayload,
    Bom,
    BomInstance,
    BomInstanceSystemStatus,
    BomUpdates,
    Diversity,
    InstanceUpdatePayload,
    Object,
    ObjectType,
    UpdatePayload,
    VariabilityConfiguration,
)


class TestAttribute:
    """Tests for the Attribute model."""

    def test_attribute_creation(self):
        """Test creating an attribute."""
        attr = Attribute(
            id="attr-123",
            name="color",
            description="Color attribute",
            slug="color",
            type="string",
            value="blue",
        )
        assert attr.id == "attr-123"
        assert attr.name == "color"
        # The type field is not directly accessible in the model
        assert attr.value == "blue"
        assert attr.options is None

    def test_attribute_with_options(self):
        """Test creating an attribute with options."""
        options = {"min": 0, "max": 100}
        attr = Attribute(
            id="attr-456",
            name="quantity",
            description="Quantity attribute",
            slug="quantity",
            type="number",
            value=50,
            options=options,
        )
        assert attr.id == "attr-456"
        assert attr.name == "quantity"
        # The type field is not directly accessible in the model
        assert attr.value == 50
        assert attr.options == options


class TestObjectType:
    """Tests for the ObjectType model."""

    def test_object_type_creation(self):
        """Test creating an object type."""
        obj_type = ObjectType(
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
        assert obj_type.id == "type-123"
        assert obj_type.name == "Component"
        assert len(obj_type.bom_attributes) == 2

    def test_get_attribute_id(self):
        """Test getting an attribute ID by name."""
        obj_type = ObjectType(
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
        assert obj_type.get_attribute_id("weight") == "attr-1"
        assert obj_type.get_attribute_id("material") == "attr-2"
        assert obj_type.get_attribute_id("nonexistent") is None


class TestBomInstance:
    """Tests for the BomInstance model."""

    @pytest.fixture
    def sample_object_type(self):
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
    def sample_bom_instance(self, sample_object_type):
        """Create a sample BOM instance for testing."""
        return BomInstance(
            id="instance-123",
            name="Test Instance",
            description="A test instance",
            bom_id="bom-123",
            view_id="view-123",
            parent_id="parent-123",
            object_type=sample_object_type,
            object_type_id="type-123",
            quantity=5,
            custom_attributes=[
                Attribute(
                    id="attr-1",
                    name="weight",
                    description="Weight attribute",
                    slug="weight",
                    type="number",
                    value=10,
                ),
                Attribute(
                    id="attr-2",
                    name="material",
                    description="Material attribute",
                    slug="material",
                    type="string",
                    value="steel",
                ),
            ],
        )

    def test_bom_instance_creation(self, sample_object_type):
        """Test creating a BOM instance."""
        instance = BomInstance(
            id="instance-123",
            name="Test Instance",
            description="A test instance",
            bom_id="bom-123",
            view_id="view-123",
            parent_id="parent-123",
            object_type=sample_object_type,
            object_type_id="type-123",
            quantity=5,
            reference="REF-123",
            status="active",
        )
        assert instance.id == "instance-123"
        assert instance.name == "Test Instance"
        assert instance.description == "A test instance"
        assert instance.bom_id == "bom-123"
        assert instance.view_id == "view-123"
        assert instance.parent_id == "parent-123"
        assert instance.object_type_id == "type-123"
        assert instance.quantity == 5
        assert len(instance.custom_attributes) == 0

    def test_get_attribute(self, sample_bom_instance):
        """Test getting an attribute value."""
        assert sample_bom_instance.get_attribute("weight") == 10
        assert sample_bom_instance.get_attribute("material") == "steel"
        assert sample_bom_instance.get_attribute("nonexistent") is None

    def test_set_attribute_existing(self, sample_bom_instance):
        """Test setting an existing attribute value."""
        sample_bom_instance.set_attribute("weight", 15)
        assert sample_bom_instance.get_attribute("weight") == 15

    def test_set_attribute_new(self, sample_bom_instance):
        """Test setting a new attribute value."""
        sample_bom_instance.set_attribute("material", "metal")
        assert sample_bom_instance.get_attribute("material") == "metal"

    def test_set_attribute_invalid(self, sample_bom_instance):
        """Test setting an invalid attribute value."""
        with pytest.raises(ValueError, match="Attribute 'nonexistent' not found in object type"):
            sample_bom_instance.set_attribute("nonexistent", "value")

    def test_set_property(self, sample_bom_instance):
        """Test setting a property value."""
        sample_bom_instance.set_property("name", "New Name")
        assert sample_bom_instance.name == "New Name"

        sample_bom_instance.set_property("quantity", 10)
        assert sample_bom_instance.quantity == 10

    def test_set_property_invalid(self, sample_bom_instance):
        """Test setting an invalid property value."""
        with pytest.raises(ValueError, match='"BomInstance" object has no field "nonexistent"'):
            sample_bom_instance.set_property("nonexistent", "value")

    def test_is_optional(self, sample_bom_instance):
        """Test checking if a BOM instance is optional."""
        sample_bom_instance.system_attributes.statuses = [BomInstanceSystemStatus.IS_OPTIONAL]
        assert sample_bom_instance.is_optional() is True

        sample_bom_instance.system_attributes.statuses = []
        assert sample_bom_instance.is_optional() is False

    def test_has_variants(self, sample_bom_instance):
        """Test checking if a BOM instance has variants."""
        sample_bom_instance.system_attributes.statuses = [BomInstanceSystemStatus.HAS_VARIANTS]
        assert sample_bom_instance.has_variants() is True

        sample_bom_instance.system_attributes.statuses = []
        assert sample_bom_instance.has_variants() is False

    def test_check_not_empty_validator(self):
        """Test the check_not_empty validator for BomInstance."""
        # This tests line 147 in models.py

        # Test with empty ID
        with pytest.raises(ValidationError):
            BomInstance(
                id="",  # Empty ID should fail validation
                name="Test Instance",
                description="A test instance",
                bom_id="bom-123",
                view_id="view-123",
                parent_id="parent-123",
                object_type_id="type-123",
                quantity=5,
            )

        # Test with whitespace-only name
        with pytest.raises(ValidationError):
            BomInstance(
                id="instance-123",
                name="   ",  # Whitespace-only name should fail validation
                description="A test instance",
                bom_id="bom-123",
                view_id="view-123",
                parent_id="parent-123",
                object_type_id="type-123",
                quantity=5,
            )

    def test_set_attribute_add_new(self, sample_object_type):
        """Test setting a new attribute on a BOM instance."""
        # This tests line 181 in models.py

        instance = BomInstance(
            id="instance-123",
            name="Test Instance",
            description="A test instance",
            bom_id="bom-123",
            view_id="view-123",
            parent_id="parent-123",
            object_type=sample_object_type,
            object_type_id="type-123",
            quantity=5,
            custom_attributes=[],
        )

        # Set a new attribute that exists in the object type
        instance.set_attribute("weight", 15)

        # Verify the attribute was added
        assert len(instance.custom_attributes) == 1
        assert instance.custom_attributes[0].id == "attr-1"
        assert instance.custom_attributes[0].name == "weight"
        assert instance.custom_attributes[0].value == 15

    def test_find_variability_configuration(self):
        """Test finding a variability configuration using a predicate."""
        # This tests line 207 in models.py

        # Create required objects for VariabilityConfiguration
        diversity = Diversity(
            id="div-1", name="Diversity 1", description="Test diversity", reference="REF-DIV-1"
        )

        obj = Object(
            id="obj-1",
            name="Object 1",
            description="Test object",
            reference="REF-OBJ-1",
            status="active",
            object_type=ObjectType(
                id="type-1", name="Test Type", description="Test type description", slug="test-type"
            ),
            object_type_id="type-1",
        )

        instance = BomInstance(
            id="instance-123",
            name="Test Instance",
            description="A test instance",
            bom_id="bom-123",
            view_id="view-123",
            parent_id="parent-123",
            object_type_id="type-123",
            object_type=ObjectType(
                id="type-123",
                name="Test Type",
                description="Test type description",
                slug="test-type",
            ),
            quantity=5,
            variability_configurations=[
                VariabilityConfiguration(
                    id="var-1",
                    variability_id="div-1",
                    variability=diversity,
                    object_id="obj-1",
                    object=obj,
                ),
                VariabilityConfiguration(
                    id="var-2",
                    variability_id="div-1",
                    variability=diversity,
                    object_id="obj-1",
                    object=obj,
                ),
            ],
        )

        # Find by ID
        config = instance.find_variability_configuration(lambda c: c.id == "var-1")
        assert config is not None
        assert config.id == "var-1"

        # Find by name (using object name since VariabilityConfiguration doesn't have a name)
        config = instance.find_variability_configuration(lambda c: c.object.name == "Object 1")
        assert config is not None

        # Test with non-matching predicate
        config = instance.find_variability_configuration(lambda c: c.id == "non-existent")
        assert config is None


class TestUpdatePayloads:
    """Tests for the update payload TypedDicts."""

    def test_attribute_update_payload(self):
        """Test creating an attribute update payload."""
        payload = AttributeUpdatePayload(
            instance_id="instance-123", attribute_id="attr-123", attribute_value="new-value"
        )
        assert payload["instance_id"] == "instance-123"
        assert payload["attribute_id"] == "attr-123"
        assert payload["attribute_value"] == "new-value"

    def test_instance_update_payload(self):
        """Test creating an instance update payload."""
        properties = {"name": "New Name", "quantity": 10}
        payload = InstanceUpdatePayload(instance_id="instance-123", properties=properties)
        assert payload["instance_id"] == "instance-123"
        assert payload["properties"] == properties

    def test_update_payload(self):
        """Test creating an update payload."""
        attr_payload = AttributeUpdatePayload(
            instance_id="instance-123", attribute_id="attr-123", attribute_value="new-value"
        )
        update_payload = UpdatePayload(type=BomUpdates.ATTRIBUTE_UPDATE, payload=attr_payload)
        assert update_payload["type"] == BomUpdates.ATTRIBUTE_UPDATE
        assert update_payload["payload"] == attr_payload


class TestBom:
    """Tests for the Bom model."""

    def test_bom_creation(self):
        """Test creating a BOM."""
        bom = Bom(
            id="bom-123",
            name="Test BOM",
            reference="REF-123",
            description="Test BOM description",
            status="active",
        )
        assert bom.id == "bom-123"
        assert bom.name == "Test BOM"

    def test_bom_validation_error(self):
        """Test BOM validation error."""
        with pytest.raises(ValidationError):
            Bom(id="", name="Test BOM")  # Empty ID should fail

        with pytest.raises(ValidationError):
            Bom(id="bom-123", name="")  # Empty name should fail

    def test_bom_model_validation(self):
        """Test the Bom validate_model method."""
        # This tests lines 264-266 in models.py

        # Test with valid data
        bom = Bom(
            id="bom-123",
            name="Test BOM",
            reference="REF-123",
            description="Test BOM description",
            status="active",
        )
        validated_bom = bom.validate_model()
        assert validated_bom is bom

        # Create a bom with valid ID and name first to avoid validation errors
        bom = Bom(
            id="bom-123",
            name="Test BOM",
            reference="REF-123",
            description="Test BOM description",
            status="active",
        )

        # Then manually set the ID to empty to test validation
        bom.id = ""
        with pytest.raises(ValueError, match="BOM ID cannot be empty"):
            bom.validate_model()

        # Reset ID and set name to empty
        bom.id = "bom-123"
        bom.name = ""
        with pytest.raises(ValueError, match="BOM name cannot be empty"):
            bom.validate_model()
