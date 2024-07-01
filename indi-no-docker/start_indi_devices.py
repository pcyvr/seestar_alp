import toml
import subprocess
from os import path

with open('./device/config.toml', 'r') as inf:
	config = toml.load(inf)
	seestars = config['seestars']
	
	for seestar in seestars:
		name = seestar['name']
		number = seestar['device_num']
		driver = path.join(path.dirname(path.abspath(__file__)), 'seestar.py')
		cmd = f'echo "start {driver} -n \\"{name}\\" -c \\"{number}\\"" > /tmp/seestar'
		print(cmd)
		subprocess.run(cmd, shell = True, executable="/bin/bash")