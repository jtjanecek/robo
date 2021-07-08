import os
import sys
import json

with open("cloud.json", "r") as f:
	cloud_config = json.loads(f.read())

username = cloud_config['username']
ip = cloud_config['ip']
ssh_key_location = cloud_config['ssh_key_location']

# Stop current running instance
print("Executing stop script ...")
command = f"ssh -i {ssh_key_location} {username}@{ip} 'bash -s' < stop.sh"
print(command)
os.system(command)

# Send the current robo setup to remote
os.system("zip -r robo.zip ../../")
command = f'sftp -i {ssh_key_location} {username}@{ip}:/home/ubuntu/ <<< "put robo.zip"'
command = f"bash -c '{command}'"
print(f"Executing {command} ...")
os.system(command)

# Start running
print("Executing start script ...")
# Start up the remote Robo instance
command = f"ssh -i {ssh_key_location} {username}@{ip} 'bash -s' < start.sh"
print(command)
os.system(command)

# clean up
os.system('rm robo.zip')
