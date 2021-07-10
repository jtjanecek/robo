import pipes
import os
import sys
import json


with open("cloud.json", "r") as f:
	cloud_config = json.loads(f.read())

username = cloud_config['username']
ip = cloud_config['ip']
ssh_key_location = cloud_config['ssh_key_location']

##### 1. Send the current robo setup to remote
os.system("zip -r robo.zip ../../")
command = f'sftp -i {ssh_key_location} {username}@{ip}:/home/ubuntu/ <<< "put robo.zip"'
command = f"bash -c '{command}'"
print(f"Executing {command} ...")
os.system(command)

##### 1. initialize the instance
print("Executing init script ...")
command = f"ssh -i {ssh_key_location} {username}@{ip} 'bash -s' < commands.sh"
os.system(command)
