from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
from inv2 import DEVICES

def test_number_interfaces():
	for device in DEVICES:
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
		assert len(structured_result) == 15 

test_number_interfaces()
