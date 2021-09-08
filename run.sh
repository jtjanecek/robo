docker run -it \
	-p 10075:10075/tcp \
	-p 10078:10078/tcp \
	-p 10079:10079/tcp \
	-p 51000:51000/udp \
	-p 10070:10070/udp \
	-p 8281:8281/tcp \
	-v /logs:/logs \
	robo
