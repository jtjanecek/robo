# Running on Linux
1. Clone the repo
```
git clone https://github.com/jtjanecek/robo/
```
2. If you want to run the server locally, change the `public_ip` to your local IP address in `config.json`
3. Build the docker image
```
bash build.sh
```
4. Run
```
bash run.sh
```
### Running fully locally on linux
1. Set Robo `public_ip` in `config.json` to your local ip
2. Disable DNS server locally
```
# Disable systemd so that the local DNAS can run
sudo systemctl stop systemd-resolved
```
3. Run DNAS locally to point to your local ip
4. Edit CLRDEV9.ini to your local IP
5. Run PCSX2
