# Pomodoro-cli
Simple command line pomodoro program to focus.

|Menu|
|-|
|![img](https://github.com/0kron/pomodoro-cli/blob/main/pomodoro-menu.png)|
|Concentration Timer|
|![img](https://github.com/0kron/pomodoro-cli/blob/main/concentration-timer.png)|
|Break Timer|
|![img](https://github.com/0kron/pomodoro-cli/blob/main/break-timer.png)

The pomodoro-cli program alows the user to have a simple and visually attractive pomodoro timer on their terminal.

## Installation
To install the program you can do one of the following methods: 

### Linux
`cd` to the directory where you want to install the program and run: 
```
$ git clone https://github.com/0kron/pomodoro-cli
```
You can run the program using
```
$ python3 $HOME/path/to/the/git_clone/pomodoro/main.py
```
Or assaign an `alias` to the command on `.bashrc`: 
```
alias pomodoro='python3 $HOME/path/to/the/git_clone/pomodoro/main.py
```

### MacOS
Open the Terminal application and use the comand `cd` to go into the chosen directory, for example dir *programs*: 
```
cd Desktop/programs/
```

Then, make sure Python is working on your Mac with the following: 
```
python -V
python3 -V
```
> Expected output: Python 2.7.16 or higher.

Then, use the following command: 
```
 git clone https://github.com/0kron/pomodoro-cli
```
The program will download and clone inside a folder called *pomodoro* in the chosen directory, if it is your first time installing a project from a Git repository probably you will need to add the **Development tools** to your enviroment, if a window opens just click the `Install` button, there is no need to add *Xcode* to your computer. 
Finally run the program inside your terminal with: 

```
python pomodoro-cli/pomodoro/main.py
```
For not using the absolute path when running the program there are two easy ways to add an *alias* to the program. The methods can be founded [here](https://wpbeaches.com/make-an-alias-in-bash-or-zsh-shell-in-macos-with-terminal/). 
If an error like: 
> SyntaxError: Non-ASCII character '\xe2' in file pomodoro-cli/pomodoro/main.py on line 9.

Follow this guide to change your terminal font. Recommended fonts: 
- Nerd Fonts. 
- Source Code Pro. 
- Hack. 
- DejaVu Sans Mono. 
- Roboto Mono.


### Windows
Copy the files in this repository to a folder of your combenience and make sure you have Python in your PATH by running: 
```
python --version
Python 3.10.X
```
Note that this program works with some new features just included on Python 3.10, an update version of Python can be located [here](https://www.python.org/downloads/). 

To run the program follow the following command: 
```
> python3 C:\Users\user\path\of\the\folder\main.py
```
Or create and alias using the `DOSKEY` command like: 
```
> DOSKEY pomodoro=python3 C:\Users\user\path\of\the\folder\main.py
```
To that last option follow [this](https://shivamethical.medium.com/create-command-line-alias-in-windows-76684635b4c4) guide for creating a `*.bat` file.


**Note:** this program is for free use, recommendations and questions may be asked through this repository.
