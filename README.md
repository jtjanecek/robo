# Robo - Custom Medius Server for UYA
![Python Version](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python)
![OS](https://img.shields.io/badge/OS-GNU%2FLinux-red?style=for-the-badge&logo=linux)

A simple python medius implementation made specifically for Ratchet and Clank: Up Your Arsenal

### Installation
```
git clone https://github.com/jtjanecek/robo
pip install -r requirements.txt
mkdir logs
sudo python robo.py
```

### Features
- Once a game has started, cities will show `[IG]` to indicate that the world is "in-game"
- Players can use the `!tagg [number]` or `!uagg [number]` in cities to set the DME TCP(tagg)/UDP(uagg) times manually for the next world they create. If a player sets these, then joins a game, they will be reset. The TCP/UDP agg time is the amount of time the server will aggregate packets before sending the data to the other players. The default in the game is 30 for both. Recommended values range from 10-100. UDP(uagg), is responsible for player movement, and more, while TCP(tagg) is responsible for wrench, and more. 

### API
Current API endpoints:
- `/players`
- `/games`

### Code adapted and inspired by:
https://github.com/hashsploit/clank    
https://github.com/Dnawrkshp/deadlocked-server/
