##Step 1: Install Git##
Git is an awesome version control system invented by the *Benevolent Dictator For Life*: Linus Torvalds. You will need git to clone this repository and follow along during the workshop!
###Windows###
- Go to https://git-scm.com/download/win
- Download & run the 32/64 bit installer as applicable
- 32 bit link: https://github.com/git-for-windows/git/releases/download/v2.10.1.windows.1/Git-2.10.1-32-bit.exe
- 64 bit link: https://github.com/git-for-windows/git/releases/download/v2.10.1.windows.1/Git-2.10.1-64-bit.exe

###Linux(Debian)###
- Run this in a terminal: `sudo apt-get install git`

###Mac###
- Run this in a terminal: `brew install git`
- No Homebrew? Install it from the guide here: http://blog.manbolo.com/2013/02/04/how-to-install-python-3-and-pydev-on-osx#1 

##Step 2: Install Python 3.5##
Python needs no introduction! Another awesome Open Source contribution from yet another *Benevolent Dictator For Life*: Guido Van Rossum!
###Windows###
- Download and install the Python executable from here: https://www.python.org/downloads/release/python-352/
- Remember to check **Add Python to Path** during installation.

###Linux###
- Run `sudo apt-get install python3`

###Mac###
- Run `brew install python3` or follow the guide on DjangoGirls below

- DjangoGirls has a great step-by-step guide for installing Python: 
https://tutorial.djangogirls.org/en/installation/#install-python

##Step 3: Install Virtualenv##
Virtualenv or Virtual environments allow us run multiple projects from a single machine, by creating virutal Python environments for each! Think of it like virtualization for Python environments!

- Run `pip3 install virtualenv`

##Step 4: Install Virtualenvwrapper##
Virtualenv on Steroids!

- You should already have `pip` as part of the python installation before. 
- If you do not have `pip` yet, you can get pip by following the steps here: https://pip.pypa.io/en/stable/installing.html

###Windows###
- Run `pip3 instsall virtualenvwrapper-win`

###Mac & Linux###
- Run `sudo pip install virtualenvwrapper`
- Add the following to the `~/.bashrc` or `~/.profile` file:
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
##Step 4: Use Virtualenv##
- Run `mkvirtualenv -p python3 django-ws`
- Run `workon django-ws`
- If you run `python -V` you should see the python version as v3.x.y

##Step 5: Install Latest Django##
Well, you know why we need this! Right?

- Run `pip install Django==1.10.2`
