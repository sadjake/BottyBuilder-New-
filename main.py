from SECRET import token
import nextcord, time, datetime, asyncio
from nextcord import Interaction
from nextcord.ext import commands

#import logging
#import os
#from typing import Optional

#logging.basicConfig(level=logging.INFO)
#activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="/hello")

#intents = nextcord.Intents.default()
#intents.members = True

#lets bot run offline from replit for an hour
from stay_alive import stay_alive # or whatever you named your file and function
stay_alive() # call the function

# creates an instance of commands.Bot class
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# list of commands
# commands - a list of commands to use
# BMR - for calculating BMR and daily calorie needs
# bulk - include message "to know the amount you need to bulk, use the !BMR command" and include list of foods for bulking
# cut - include message "to know the amount you need to cut, use the !BMR command" and include list of foods for cutting
# dietplan - 

# buttons for the user's info
class yourinfo(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "Name", style = nextcord.ButtonStyle.primary)
    async def name(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'name'
        self.stop()
        
    @nextcord.ui.button(label = "Gender", style = nextcord.ButtonStyle.primary)
    async def gender(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'gender'
        self.stop()

    @nextcord.ui.button(label = "Age", style=nextcord.ButtonStyle.primary)
    async def age(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'age'
        self.stop()

    # which tree is better? i like the third 
    @nextcord.ui.button(label = "Height", style=nextcord.ButtonStyle.primary)
    async def height(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'height'
        self.stop()

    @nextcord.ui.button(label = "Weight", style=nextcord.ButtonStyle.primary)
    async def weight(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'weight'
        self.stop()
    
    @nextcord.ui.button(label = "Activity Level", style=nextcord.ButtonStyle.primary)
    async def activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'activity'
        self.stop()

class update(nextcord.ui.View, message, column):
    def  __init__(self):
        super().__init__()
        self.value = None

        self.value = 'changed'
        self.stop()

# hello message command
@bot.slash_command(description="My first slash command")
async def hello(interaction: nextcord.Interaction):
    await interaction.send("Hello!")

# update user health info
@bot.slash_command(name = "updateinfo", description="Updating health information")
async def update_info(ctx):
    view = yourinfo()
    await ctx.send("What would you like to update?", view=view)
    await view.wait()
    
    if view.value == 'name':
        await ctx.send("Please enter your name")
        try:
            reply = await bot.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author)
            view = update(0)
        except asyncio.TimeoutError:
            await ctx.send("Timeout!")
            return
        await view.wait()

        if view.value == 'changed':
            await ctx.send(f"Your name has been changed to stupid {view.answer}")

    elif view.value == 'gender':
        view = update()
        await ctx.send("Please enter your gender")
        await view.wait()

        if view.value == 'changed':
            await ctx.send("Your age has been changed to male")
            
    elif view.value == 'age':
        view = update()
        await ctx.send("Please enter your age")
        await view.wait()

        if view.value == 'changed':
            await ctx.send("Your age has been changed to 69")
    
    elif view.value == 'height':
        view = update()
        await ctx.send("Please enter your height")
        await view.wait()

        if view.value == 'changed':
            await ctx.send("Your height has been changed to 420")
    
    elif view.value == 'weight':
        view = update()
        await ctx.send("Please enter your weight")
        await view.wait()

        if view.value == 'changed':
            await ctx.send("Your weight has been changed to 666")
    
    elif view.value == 'activity':
        view = update()
        await ctx.send("Please enter your activity level")
        await view.wait()

        if view.value == 'changed':
            await ctx.send("Your activity level has been changed to 420")

# die
@bot.slash_command(name = "die", description="death")
async def die(interaction: nextcord.Interaction):
    await interaction.send("die")

# List of commands for the discord bot
@bot.slash_command(name = "commands", description="List of commands for the discord bot")
async def commands(interaction: nextcord.Interaction):
    await interaction.send("Here is the list of available commands.\n\n/commands - List of commands to use\n/BMR - Let BottyBuilder calculate your BMR, daily calorie needs, and how much you need to eat to bulk/cut.\n/bulkfoods - A list of foods that are beneficial for bulking. To know the AMOUNT you need to eat to bulk, use the !BMR command.\n/cutfoods - A list of foods that are beneficial for cutting. To know the AMOUNT you need to eat to cut, use the !BMR command.")

# BMR command + buttons
class bmr(nextcord.ui.View):
    def  __init__(self):
        super().__init__()
        self.value = None
    
    @nextcord.ui.button(label = "BMR", style = nextcord.ButtonStyle.primary)
    async def bmr(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value  = 'BMR'
        self.stop()

    @nextcord.ui.button(label = "Daily Calorie Needs", style=nextcord.ButtonStyle.primary)
    async def dcn(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'Daily Calorie Needs'
        self.stop()

    @nextcord.ui.button(label = "Bulk (Calories)", style=nextcord.ButtonStyle.primary)
    async def bulk(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'Bulk (Calories)'
        self.stop()

    @nextcord.ui.button(label = "Cut (Calories)", style=nextcord.ButtonStyle.primary)
    async def cut(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 'Cut (Calories)'
        self.stop()
    
# buttons for the bmr stuff
@bot.slash_command(name = "bmr", description="BMR, Daily Calorie Needs, Bulk (Calories), Cut (Calories)")
async def bmr_info(ctx):
    view = bmr()
    await ctx.send("What would you like to calculate?", view=view)
    await view.wait()
    
# Use Harris Benedict equation for BMR
# determine gender of user first
# for male:
# float bmpValue = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
# for female:
# float bmpValue = 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)
# present value of bmp to the user when they use the command
# round to 2 decimal places

# Daily caloric maintenance level:
# float dcml = bmpValue*activity
# round to 2 decimal places
# present value of dcml to the user when they use the command

# Bulk:
# float bulk = dcml*1.15

# Cut:
# float cut = dcml*0.85

# open file
    file = open("info.csv")
    file.readline()
    # for loop not needed below
    #for line in file:
    userdata = line.strip().split(",")

    age = float(userdata[1])
    height = float(userdata[2])
    weight = float(userdata[3])
    activity = float(userdata[4])

    if () #if statement for checking user's gender (male/female), just need to add extra column in file
        # can make the if statement using the csv file as an array
        # this one is for when the user is male
        # round to 2 decimal places
        bmpValue = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
    
    if () #if statement for checking user's gender (male/female), just need to add extra column in file
        # can make the if statement using the csv file as an array
        # this one is for when the user is male
        # round to 2 decimal places
        bmpValue = 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)

    # present value of bmp to the user when they use the command 
    # (go back to the button part of the code)

    # daily calorie maintenance level
    # round to 2 decimal places
    dcml = bmpValue*activity

    # value for bulk
    bulk = dcml*1.15

    # value for cut
    cut = dcml*0.85

    # present value of dcml/bulk/cut to the user when they use the command 
    # (go back to the button part of the code)

  
# bmpValue = 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)
# present value of bmp to the user when they use the command
# round to 2 decimal places

# Daily caloric maintenance level:
# dcml = bmpValue*activity
# round to 2 decimal places
# present value of dcml to the user when they use the command

# Bulk:
# bulk = dcml*1.15

# Cut:
# cut = dcml*0.85

# open file
    file = open("info.csv")
    file.readline()
    # for loop not needed below
    #for line in file:
    userdata = line.strip().split(",")

    age = float(userdata[1])
    height = float(userdata[2])
    weight = float(userdata[3])
    activity = float(userdata[4])

    if () #if statement for checking user's gender (male/female), just need to add extra column in file
        # can make the if statement using the csv file as an array
        # this one is for when the user is male
        # round to 2 decimal places
        bmpValue = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
    


# Use Harris Benedict equation for BMR
# determine gender of user first
# for male:
# bmpValue = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
# for female:
# bmpValue = 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)
# present value of bmp to the user when they use the command
# round to 2 decimal places

# Daily caloric maintenance level:
# dcml = bmpValue*activity
# round to 2 decimal places
# present value of dcml to the user when they use the command

# Bulk:
# bulk = dcml*1.15

# Cut:
# cut = dcml*0.85

# open file
#    file = open("info.csv")
#    file.readline()
    # for loop not needed below
    #for line in file:
#    userdata = line.strip().split(",")

#    age = float(userdata[1])
 #   height = float(userdata[2])
#    weight = float(userdata[3])
#    activity = float(userdata[4])

 #   if () #if statement for checking user's gender (male/female), just need to add extra column in file
        # can make the if statement using the csv file as an array
        # this one is for when the user is male
        # round to 2 decimal places
#        bmpValue = 66.5 + (13.75*weight) + (5.003*height) - (6.75*age)
    
#    if () #if statement for checking user's gender (male/female), just need to add extra column in file
        # can make the if statement using the csv file as an array
        # this one is for when the user is male
        # round to 2 decimal places
#        bmpValue = 655.1 + (9.563*weight) + (1.850*height) - (4.676*age)

    # present value of bmp to the user when they use the command 
    # (go back to the button part of the code)

    # daily calorie maintenance level
    # round to 2 decimal places
#    dcml = bmpValue*activity

    # value for bulk
#    bulk = dcml*1.15

    # value for cut
#    cut = dcml*0.85

# make a function instead?!??!??!?!?!?!?! RAHHHHH
def calculate_bmr(gender, age, height, weight):
    # will get gender another way instead of doing this
    if gender == "male":
        bmpValue = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
    elif gender == "female":
        bmpValue = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)

@bot.slash_command(name="bmr", description="BMR, Daily Calorie Needs, Bulk (Calories), Cut (Calories)")
async def bmr_info(ctx):
    view = bmr()
    await ctx.send("What would you like to calculate?", view=view)
    await view.wait()

    if view.value == "BMR":
        # Get user data from CSV file
        file = open("info.csv")
        file.readline()  # Skip header
        userdata = file.readline().strip().split(",")
        file.close()

        name, gender, age, height, weight, activity = userdata

        # Calculate BMR based on gender, age, height, and weight
        bmr_value = calculate_bmr(gender, float(age), float(height), float(weight))

        await ctx.send(f"Your BMR: {bmr_value}")
        # Calculate and send other values (daily calorie needs, bulk, cut) if needed

    

    # present value of dcml/bulk/cut to the user when they use the command 
    # (go back to the button part of the code)

# List of muscle groups to train command + buttons
bot.run(token)
