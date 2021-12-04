import pipes
import os
import sys
import json

#########################################################
################## Robo server ##########################
#########################################################

with open("cloud.json", "r") as f:
    cloud_config = json.loads(f.read())

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
command = f'sftp -i {cloud_config["robo"]["ssh_key_location"]} {cloud_config["robo"]["username"]}@{cloud_config["robo"]["ip"]}:/home/{cloud_config["robo"]["username"]}/ <<< "put robo.zip"'
command = f"bash -c '{command}'"
print(f"Executing {command} ...")
os.system(command)

##### 2. Initialize the instance
print("Executing init script ...")
command = f"ssh -i {cloud_config['robo']['ssh_key_location']} {cloud_config['robo']['username']}@{cloud_config['robo']['ip']} 'bash -s' < _temp.sh"
os.system(command)

##### 3. Cleanup
os.system('rm robo.zip; rm _temp.sh')

#########################################################
################## DN/A/S server ########################
#########################################################

# In development
commands = f'''
screen -XS dnas quit;
sudo systemctl enable systemd-resolved;
sudo systemctl start systemd-resolved;
sudo apt-get update;
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg -y;
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null;
sudo apt-get update;
sudo apt-get install docker-ce docker-ce-cli containerd.io -y;
git clone https://github.com/jtjanecek/clank-dnas;
cd clank-dnas;

sudo bash build.sh {cloud_config['robo']['ip']};

# Disable current DNS server
sudo systemctl disable systemd-resolved;
sudo systemctl stop systemd-resolved;

screen -Sdm dnas sudo bash run.sh
'''

'''
with open('_temp.sh', 'w+') as f:
    f.write(commands)

##### 1. Initialize the instance
print("Executing dnas script ...")
command = f"ssh -i {cloud_config['dnas']['ssh_key_location']} {cloud_config['dnas']['username']}@{cloud_config['dnas']['ip']} 'bash -s' < _temp.sh"
#os.system(command)

##### 2. Cleanup
#os.system('rm _temp.sh')
'''
