import pytest
from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
from inv2 import DEVICES

@pytest.mark.parametrize("device", DEVICES)
def test_number_interfaces(device):
	
	with IOSXEDriver(
		host=device["host"],
		auth_username="admin",
		auth_password="admin",
		auth_strict_key=False,
		ssh_config_file=True,
	) as conn: 
		response = conn.send_command("show interfaces")
	structured_result = response.textfsm_parse_output()
#		rprint(structured_result)
#		print("\n\n")
	assert len(structured_result) == 16 


