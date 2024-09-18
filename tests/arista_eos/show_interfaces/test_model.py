import yaml
from pydantic import ValidationError
import pytest
from arista_eos_show_interfaces_schema import Interface, InterfaceList  # Import your models


def test_interface_model():
    with open("arista_eos_show_interfaces.yml", "r") as file:
        yaml_data = yaml.safe_load(file)
        tfsm_data = yaml_data["parsed_sample"]

    try:
        interface_list = InterfaceList(root=tfsm_data)
    except ValidationError as e:
        pytest.fail(f"Validation error: {e}")

    assert len(interface_list.interfaces) > 0, "Interface list is empty"

    # Test individual interfaces
    first_interface = interface_list.interfaces[0]
    assert isinstance(first_interface, Interface)
    assert first_interface.hardware_type != ""
    assert first_interface.interface != ""
    assert first_interface.link_status in ["up", "down"]
    assert first_interface.protocol_status != ""
