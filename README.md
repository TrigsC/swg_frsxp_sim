# What is this?
This is a simulation of FRSXP for Jedi in Star Wars Galaxies.

2 files are outputted with data:<br />
frsxp_data.csv (End Data)<br />
frsxp_audit.log (This is a log of every increase and decrease of xp to validate data)

At the top of swg_frsxp_sim.py you can edit ```frsExperienceValues``` and ```frsRanks``` for testing new values.

# Requirements Instructions
## Check if all things are intalled
Open Command Prompt
```Windows Key and cmd and Enter```

Type<br />
```python --version```<br />
```git --version```<br />
```pip --version```<br />
Do not close Command Prompt yet

If Python is over >= 3.0 you are good to skip Downloading Python 

If Git shows a version then you are good to skip Downloading Git

If pip shows a version then you are good to skip Downloading pip

otherwise continue

Download Python Version 3 or Higher (Use Stable Releases)<br />
During install select to Add Python to PATH checkbox<br />
https://www.python.org/downloads/windows/

Download git<br />
Just click through all the defaults<br />
https://git-scm.com/


Download pip<br />
In the Open Command Prompt <br />
```py -m pip install```

## At this point, if you have VSCode or editor you can go to Install section

Go to the folder you want Sim installed to<br />
Ex(C:\Users\)<br />
Right Click "Git Bash Here"

## Install
Type

```git clone https://github.com/TrigsC/swg_frsxp_sim.git```

Then

```pip install -r requirements.txt```

## Installation Complete

# Running Simulation

Either in Git Bash or your editor

```python swg_frsxp_sim.py```

Prompts = 
```
(A whole number over 0.)
How many Ranked Jedi are there?

(If the server is only Jedi enter 0 here but unlikely. Jedi death from a Non-Jedi has xp loss.)
How many Non-Jedi PVP players are there?

(Enter a whole number, BH gives xp and takes it.)
How many Bounty Hunters are there?

(XP is currently split between Jedi attackers)
(Answers = (no,false,f) (yes,true,t))
Do you want to split frsxp?

(This is getting the ratio of Imperials to Rebels. Do not add a % sign. (ex. 50))
What percent are Imperial?

(This is how many times the simulation will run. Enter a whole number. 2000 takes about 30 seconds.)
How many battles would you like to run?

Progress bar will show.

MAKE SURE THE 'frsxp_data.csv' IS CLOSED IF RUNNING AGAIN OR IT WILL ERROR TRYING TO OVERWRITE

Inside the installed folder you will find:
frsxp_data.csv
frsxp_audit.log
```
