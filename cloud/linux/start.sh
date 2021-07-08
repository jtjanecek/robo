unzip robo.zip -d robo/
rm robo.zip
cd robo
rm logs/*
../robo_env/bin/pip3 install -r requirements.txt 
sed -i 's/.*ip.*/"ip":"0.0.0.0",/g' config.json
screen -Sdm robo ../robo_env/bin/python3 robo.py
