#!/usr/bin/env bash
if [ "$EUID" -ne 0 ]
	then echo -e "\033[0;31m./configure.sh script requires root privileges"
	exit
fi

FILE=dist/main

if [ -f "$FILE" ]; then
	echo -e "\033[0;32mPreparing the executable..."
	cp dist/main /usr/bin/nitro-sense-no-launch
	touch /usr/bin/nitro-sense
	printf "#!/usr/bin/env bash\npkexec env DISPLAY=\$DISPLAY XAUTHORITY=\$XAUTHORITY /usr/bin/nitro-sense-no-launch" > /usr/bin/nitro-sense
	chmod +x /usr/bin/nitro-sense
	sleep 1
	echo -e "\033[0;32mCreating desktop entry..."
	touch /usr/share/applications/nitro-sense.desktop
	printf "[Desktop Entry]\nEncoding=UTF-8\nVersion=1.0\nType=Application\nTerminal=false\nExec=/usr/bin/nitro-sense\nName=Nitro Sense™\nComment=Application to control fan speed for Acer Nitro 5\nIcon=/usr/share/icons/nitro-sense" > /usr/share/applications/nitro-sense.desktop
	cp app_icon.ico /usr/share/icons/nitro-sense
	sleep 1
	echo -e "\033[0;32mInstalling custom fonts..."
	mkdir -p /usr/local/share/fonts/s
	cp fonts/* /usr/local/share/fonts/s
	sleep 1
	echo -e "\033[0;32mNitroSense was successfully installed\033[0m.\nUse \033[0;33mnitro-sense\033[0m or the desktop entry to launch the app."
else
	echo -e "\033[0;31mWrong command order.\nRefer to README.md"
	exit
fi
