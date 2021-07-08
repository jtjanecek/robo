import os
import sys
import json

with open("cloud.json", "r") as f:
	cloud_config = json.loads(f.read())

username = cloud_config['username']
ip = cloud_config['ip']
ssh_key_location = cloud_config['ssh_key_location']

print("Executing initialization script ...")
command = f"ssh -i {ssh_key_location} {username}@{ip} 'bash -s' < initialize.sh"
print(command)
os.system(command)
print("Done.")
