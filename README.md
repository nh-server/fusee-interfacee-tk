![A cute rocket in outerspace!](icon.png)
# Fusée Launcher Interfacée (Nintendo Homebrew Version)
A mod of [falquinhos](https://github.com/falquinho/fusee-interfacee-tk) Fusée Launcher for use with Nintendo Homebrew Switch Guide. It also adds the ability to mount SD while in RCM.

A very simple GUI for applying [Team {Re}Switched Fusée Launcher script](https://github.com/reswitched/fusee-launcher) onto your Nintendo Switch.


## Disclaimer
* As always, use at your own discretion. I take no reponsibility for any damages caused to your device.
* I'm assuming you understand how the exploit is done and the setup needed, this README is to help you run this specific app.
* Although Fusée is able to exploit any Tegra X1 device, this app is designed to work with Nintendo Switches only.
* The Fusée Launcher script included in this project is slightly modified to be used as a module.
* Binaries built and tested on Ubuntu 18.10 and OS X (or macOS) 10.9.5. If your platform is older you may not be able to run the executables.


## Running this app
You can run this app as a simple python script or by executing the binary file for your platform.

### Running as a script
* Have latest [python 3](https://www.python.org/downloads/) and [pyusb](https://github.com/pyusb/pyusb) installed.
* __On Linux__ have libusb1 installed (you probably already have).
* Download/clone this repo and simply run `app.py` like you would any python script.

<details>
	<summary>Mac Install Tutorial (Apple Silicon M1/M2 & Intel Macs)</summary>
	It's recommended you have a basic understanding of how to use Terminal, as this will makes things a bit easier.

	If you don't have Homebrew already installed, [install homebrew](https://brew.sh/).

	1. Open Terminal
	2. Install the dependencies:
	```sh
	brew install libusb python3 tcl-tk python-tk
	```

	3. Reopen Terminal, as there will be some new paths.

	4. `python3 --version` should return `Python 3.xxx.yyy`, where `xxx` is a major version such as 11, 12, etc. yyy is the minor version.

	> As of April 2023, Python 3.11 is the current stable version of Python. Future versions, *should* work. If the below steps don't work with `Python 3.12` etc, you can install Python 3.11 & Python-tk for Python3.11 via `brew install python@3.11 python-tk@3.11`. Then in the following steps, instead of using `python3`, use `python@3.11` to run Python 3.11.

	5. `git clone` the repository, `cd` into it:
	```sh
	git clone https://github.com/nh-server/fusee-interfacee-tk
	cd fusee-interfacee-tk
	```

	> If you have issues with Git, you can also download the repository directly [here](https://github.com/nh-server/fusee-interfacee-tk/archive/refs/heads/master.zip), extract it then cd into it. Mac does come with Git, so it should work.

	```sh
	# Run the below steps only if Git doesn't work.
	curl -L https://github.com/nh-server/fusee-interfacee-tk/archive/refs/heads/master.zip --output fusee-interfacee-tk.zip
	unzip fusee-interfacee-tk.zip
	cd fusee-interfacee-tk.zip
	```

	6. Create a "virtual environment", which means that packages will be installed within this directory instead of system wide, which might cause conflicts and other issues.
	```sh
	python3 -m venv .venv
	```

	7. Install the needed Python packages:
	```sh
	./.venv/bin/pip install pyusb
	```

	> You can also use`source .venv/bin/activate`, which activates a "virtual environment". But as we are just running a couple of steps, prefixing our commands with `.venv/bin/` is fine.

	8. Now you should be able to run the script. Running this command should show the GUI. In future you should just be able to run this command and not need to perform steps 1-7:

	```sh
	./.venv/bin/python3 app.py
	```

	## Copy+paste, once you have installed Homebrew:
	```sh
	brew install libusb python3 tcl-tk python-tk
	git clone https://github.com/nh-server/fusee-interfacee-tk
	cd fusee-interfacee-tk
	python3 -m venv .venv
	./.venv/bin/pip install pyusb
	./.venv/bin/python3 app.py
	```
</details>

### Running the binary file
### Linux
* You need to have `libc ver. 2.61` or higher (if you use a modern distro you probably already have).
* Download the linux binary from the [releases page](https://github.com/nh-server/fusee-interfacee-tk/releases) and run it. It *should* simply work.

### Mac
* Download the mac binary from the [releases page](https://github.com/nh-server/fusee-interfacee-tk/releases) and run it. It *should* simply work.


## Using Fusée Launcher Interfacée
The app is very simple, it should be very intuitive to use:

![App looking for a device.](https://image.ibb.co/n1CEv8/fusee_interfacee_ss0.png) ![App found a device and is ready!](https://image.ibb.co/ep6ra8/fusee_interfacee_ss1.png)
* Click the `Select Payload` button to browse your files and select the desired payload.
* Connect your Switch in RCM mode to the computer. The progress bar will stop and fill up when the device is detected.
* When the `Launch Fusée!` button activate simply click it.


## Freezing
If the binary executable won't run in your machine you can build it yourself. The tool I used was [pyinstaller](https://www.pyinstaller.org/).

### A note on freezing on Linux:
If you want to freeze using `pyinstaller` on linux there's a bug on the pip version of it that prevents the `libusb` to 
be bundled. You need to donwload [the develop branch of pyinstaller](https://github.com/pyinstaller/pyinstaller/tree/develop) and use it as a script. 

## Credits
- [Kate Temkin](https://github.com/ktemkin) / [Fusée Launcher](https://github.com/Cease-and-DeSwitch/fusee-launcher)
- [Rajkosto](https://github.com/rajkosto) / [memloader](https://github.com/rajkosto/memloader), Mounting Tool
- [falquinho](https://github.com/rajkosto) / [Fusée Launcher Interfacée](https://github.com/falquinho/fusee-interfacee-tk), Original Author