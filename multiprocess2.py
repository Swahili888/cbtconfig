from  time import perf_counter
from concurrent.futures import ProcessPoolExecutor
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

start = perf_counter()

def send_cmd(device):
        with IOSXEDriver(
                host=device["host"],
                auth_username="admin",
                auth_password="admin",
                auth_strict_key=False,
                ssh_config_file=True,
        ) as conn:
                response = conn.send_command("show version")
                print(response.result)

if __name__ == "__main__":
	with ProcessPoolExecutor() as executor:
		results = executor.map(send_cmd, DEVICES)

	for result in results:
		print(result)


	end = perf_counter()
	total_time = end - start 
	print(total_time)
