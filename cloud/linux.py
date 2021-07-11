import pipes
import os
import sys
import json

#########################################################
################## Robo server ##########################
#########################################################

with open("cloud.json", "r") as f:
	cloud_config = json.loads(f.read())

username = cloud_config['username']
ip = cloud_config['ip']
ssh_key_location = cloud_config['ssh_key_location']

commands = '''
sudo apt-get update;
sudo apt-get install zip -y;
sudo apt-get install python3.9 -y;
sudo apt-get install python3.9-venv -y;
screen -XS robo quit;
rm -rf robo;
rm -rf robo_env;
python3.9 -m venv robo_env;
mkdir robo;
unzip robo.zip -d robo/;
rm robo.zip;
cd robo;
rm logs/*;
../robo_env/bin/pip3 install -r requirements.txt;
sed -i 's@.*ip.*@"ip":"0.0.0.0",@g' config.json;
screen -Sdm robo ../robo_env/bin/python3.9 robo.py;
'''

with open('_temp.sh', 'w+') as f:
	f.write(commands)

##### 1. Send the current robo setup to remote
os.system("zip -r robo.zip ../")
command = f'sftp -i {ssh_key_location} {username}@{ip}:/home/ubuntu/ <<< "put robo.zip"'
command = f"bash -c '{command}'"
print(f"Executing {command} ...")
os.system(command)

##### 2. initialize the instance
print("Executing init script ...")
command = f"ssh -i {ssh_key_location} {username}@{ip} 'bash -s' < _temp.sh"
os.system(command)

##### 3. cleanup
os.system('rm robo.zip; rm _temp.sh')

#########################################################
################## DNS server ###########################
#########################################################


