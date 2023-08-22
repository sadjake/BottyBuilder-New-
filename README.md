# BottyBuilder 2.0

(Because the prototype bot Jake made had too many problems and needed fresh restart lol)

Saves your name, age, height, weight, gender, and maintenance/daily calorie level into a csv file 

Bot includes option to allow the user to update their information

## Setting up the Bot

![image](https://github.com/sadjake/BottyBuilder-New-/assets/66497192/309185f4-41e5-499d-9a1b-2d4d7b45a87b)
Get your discord bot token and put it inside a SECRET.py file

If you haven't installed the dependencies yet, do so with the following commands (for python 3.0 versions)
```
python3 -m pip install -U nextcord
pip3 install requests
pip install flask
```
If you already have discord.py installed, it might clash with nextcord and not work so use ```pip uninstall``` discord.py to uninstall it.

Run the main.py file and it should be good to go :thumbsup:

## Commands
/commands - list of commands for the bot

/bmr - calculates your BMR and includes options to calculate Daily Maintenance Calorie Level, Bulk, and Cut.

/exercises - 

Calculates your BMR using Harris Benedict Equation
When calculating maintenance calorie level, the following is needed to calculate it using the Harris Benedict Equation:

(NOTE: DISCORD BOT WILL SAVE THIS INFO TO CSV FILE TO KEEP TRACK OF USER’S INFO)
Name/discord user
AGE
HEIGHT
WEIGHT
GENDER
How active during the week

BMR:
For men: BMR = 66.5 + (13.75 × weight in kg) + (5.003 × height in cm) - (6.75 × age)
For women: BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) - (4.676 × age)

Daily Caloric Intake:
Multiply BMR by weekly activity level

Bulk:
Multiply Daily Caloric Intake by 1.1~1.2

Cut:
Multiply Daily Caloric Intake by 0.9~0.8


