# What is this?
This is a simulation of FRSXP for Jedi in Star Wars Galaxies.

2 files are outputted with data:<br />
frsxp_data.csv (End Data)<br />
frsxp_audit.log (This is a log of every increase and decrease of xp to validate data)

At the top of swg_frsxp_sim.py you can edit ```frsExperienceValues``` and ```frsRanks``` for testing new values.

# How does it work?
Based on user input, it creates random data of Rebels, Imperials, and Bounty Hunters. It then grabs a random group from both factions and checks to see if they are willing to fight eachother based on how many came to the fight (get_battle_ratio can be updated as seen fit). If the fight is on, it then grabs another random group from the fighters and checks winrate (random number) of both groups and to see who won. It then grabs another even smaller group from the winners as if those are the characters that killed the other and 1 person from the losers. One more time it selects 1 person from the winners as the Death Blower. If the person that died was a Non-Jedi they are removed from the fighters list and repeats. If a Jedi dies it gives FRS XP based on frsExperienceValues and if FRSXP is split and decreases for the loser. It will continues running the fight over and over until one side disengages.

Every 3rd "round" or battle, 2 Jedi are randomly selected to fight and it is based on win ratio. It's possible that both ratio's end in True and as if someone got away. Who ever wins gets FRSXP based on frsExperienceValues and decreases for the loser.

Every 5th "round" or battle, a BH and Jedi are randomly selected to fight and it is based on win ratio. It's possible that both ratio's end in True and as if someone got away. If the Jedi wins they get FRSXP based on frsExperienceValues and decreases if they lose.

# Requirements Instructions
## Check if all things are installed
Open Command Prompt
```Windows Key and cmd and Enter```

Type<br />
```python --version```<br />
```git --version```<br />
```pip --version```<br />
Do not close Command Prompt yet

If Python is over >= 3.0 you are good to skip Downloading Python 

If Git shows a version, then you are good to skip Downloading Git

If pip shows a version, then you are good to skip Downloading pip

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
