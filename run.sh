#!/bin/sh

FILE_CRON=/usr/bin/crontab
FILE_PIP3=/usr/bin/pip3
FILE_PYTHON3=/usr/bin/python3

install_cron()
{
	echo '[-] Installing cron package'
	sudo apt update
	sudo apt install cron
	echo '[-] Enabling cron service'
	sudo systemctl enable cron
}


install_pip3()
{
	echo '[-] Installing pip3'
	sudo apt update
	sudo apt install python3-pip
}

install_python3()
{
	sudo apt update
	sudo apt install python3.6
}

install_dependences()
{
	pip3 install -r ./requirements.txt
}

if [ ! -f "$FILE_CRON" ]; then
	install_cron
fi

if [ ! -f "$FILE_PYTHON3" ]; then
	install_python3
fi

if [ ! -f "$FILE_PIP3" ]; then
	install_pip3
fi

install_dependences
crontab cronfile
