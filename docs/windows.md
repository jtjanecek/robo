# Building & Running on Windows
## Download PCSX2
Download PCSX2 1.6.0 from here:

https://github.com/PCSX2/pcsx2/releases/tag/v1.6.0

Installer link: 

https://github.com/PCSX2/pcsx2/releases/download/v1.6.0/pcsx2-v1.6.0-windows-32bit-installer.exe

## Download CLR DEV9 Plugin for PCSX2
Download CLR DEV9 for networking on PCSX2:

https://github.com/TheLastRar/CLR-DEV9/releases/tag/V0.9.1

I downloaded the x86 version: 

https://github.com/TheLastRar/CLR-DEV9/releases/download/V0.9.1/CLR_DEV9.X86.7z

Place the .dll file into C:\Program Files (x86)\PCSX2\Plugins

Boot up PCSX2, and load the CLR DEV9 plugin instead of the DEV9 plugin.

It will generate an ini config file here: Documents/PCSX2/inis/CLR_DEV9.ini

Now we need to find our local ip address. We can do this by typing CTRL+R, then type `cmd`. At the terminal, type `ipconfig`. Your IP will likely show up as 192.168.x.x
In this next step, replace `YOUR_IP` with the IP you found

Replace
```
        <Hosts>
                <ConfigHost>
                        <Desc>Set DNS to 192.0.2.1 to use this host list</Desc>
                        <Enabled>false</Enabled>
                        <IP>0.0.0.0</IP>
                        <URL>www.example.com</URL>
                </ConfigHost>
        </Hosts>
        <LogLevelConsole>Information</LogLevelConsole>
        <LogLevelFile>Information</LogLevelFile>
        <SocketConnectionSettings>
                <AutoDNS1>true</AutoDNS1>
                <AutoDNS2>true</AutoDNS2>
                <DNS1>0.0.0.0</DNS1>
                <DNS2>0.0.0.0</DNS2>
                <IncomingPorts />
                <LANMode>true</LANMode>
        </SocketConnectionSettings>
```
With:
```
        <Hosts>
                <ConfigHost>
                        <Desc>Set DNS to 192.0.2.1 to use this host list</Desc>
                        <Enabled>true</Enabled>
                        <IP>YOUR_IP</IP>
                        <URL>ratchet3-prod1.pdonline.scea.com</URL>
                </ConfigHost>
                <ConfigHost>
                        <Desc>Set DNS to 192.0.2.1 to use this host list</Desc>
                        <Enabled>true</Enabled>
                        <IP>45.7.228.197</IP>
                        <URL>gate1.us.dnas.playstation.org</URL>
                </ConfigHost>
                <ConfigHost>
                        <Desc>Set DNS to 192.0.2.1 to use this host list</Desc>
                        <Enabled>true</Enabled>
                        <IP>YOUR_IP</IP>
                        <URL>randc3-master.online.scee.com</URL>
                </ConfigHost>
                <ConfigHost>
                        <Desc>Set DNS to 192.0.2.1 to use this host list</Desc>
                        <Enabled>true</Enabled>
                        <IP>YOUR_IP</IP>
                        <URL>randc3-prod.rt.au.playstation.com</URL>
                </ConfigHost>



        </Hosts>
        <LogLevelConsole>Information</LogLevelConsole>
        <LogLevelFile>Information</LogLevelFile>

        <SocketConnectionSettings>
                <AutoDNS1>false</AutoDNS1>
                <AutoDNS2>false</AutoDNS2>
                <DNS1>192.0.2.1</DNS1>
                <DNS2>0.0.0.0</DNS2>
                <IncomingPorts />
                <LANMode>false</LANMode>
        </SocketConnectionSettings>
```

## Install Docker
1. Install docker desktop here: https://docs.docker.com/desktop/windows/install/
2. Clone robo from this repo. Open Powershell and run:
```
cd Documents
git clone https://github.com/jtjanecek/robo/
```
4. In the `config.json` file, change the DME UDP port to be 10071 (I had to do this for some weird windows reason)
5. Open powershell, cd into the robo directory and run the following to build Robo
```
docker build -t robo .
```
6. Start robo:
```
 docker run -it --log-opt max-size=50m -p 10075:10075/tcp -p 10078:10078/tcp -p 10079:10079/tcp -p 10071:10071/udp  -p 10070:10070/udp  -p 8281:8281/tcp  -v $PWD/logs:/logs robo
```
