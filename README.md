# BottyBuilder 2.0

Saves your name, age, height, weight, and maintenance calorie level into a file

## Setting up the Bot

![image](https://github.com/sadjake/BottyBuilder-New-/assets/66497192/309185f4-41e5-499d-9a1b-2d4d7b45a87b)
Get your discord bot token and put it inside a SECRET.py file

If you haven't installed the dependencies yet, do so with the following commands (for python 3.0 versions)
```
pip install nextcord
pip3 install requests
```
If you already have discord.py installed, it might clash with nextcord and not work so use ```pip uninstall``` discord.py to uninstall it.

Run the main.py file and it should be good to go :thumbsup:

## Commands

Calculates your maintenance calorie level using Harris Benedict Equation
When calculating maintenance calorie level, the following is needed to calculate it using the Harris Benedict Equation:
(NOTE: DISCORD BOT WILL SAVE THIS INFO TO CSV FILE OR SOMETHING RELATED TO KEEP TRACK OF USER’S INFO)
Name/discord user
AGE
HEIGHT
WEIGHT
How active during the week


For men: BMR = 66.5 + (13.75 × weight in kg) + (5.003 × height in cm) - (6.75 × age)
For women: BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) - (4.676 × age)
