from SECRET import token
import nextcord, time, datetime, asyncio, csv, random
from nextcord import Interaction, Intents
from nextcord.ext import commands

#import logging
#import os
#from typing import Optional

#logging.basicConfig(level=logging.INFO)
#activity = nextcord.Activity(type=nextcord.ActivityType.listening, name="/hello")

intents = Intents.all()
# creates an instance of commands.Bot class
bot = commands.Bot(intents=intents)

#lets bot run offline from replit for an hour
# from stay_alive import stay_alive # or whatever you named your file and function
# stay_alive() # call the function

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
        await self.ask_activity_level(interaction)
    
    async def ask_activity_level(self, interaction: Interaction):
        activity_level_view = activityLevelView()
        await interaction.send("How active are you?", view=activity_level_view)
        await activity_level_view.wait()

class activityLevelView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
    
    @nextcord.ui.button(label="Little to no physical activity", style=nextcord.ButtonStyle.primary)
    async def no_activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1.2
        self.stop()
        await interaction.response.edit_message(content="You have selected little to no physical activity (Activity level: 1.2).")

    @nextcord.ui.button(label="Light activity/exercise, 1-3 times", style=nextcord.ButtonStyle.primary)
    async def light_activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1.375
        self.stop()
        await interaction.response.edit_message(content="You have selected light activity/exercise (Activity level: 1.375).")

    @nextcord.ui.button(label="Moderate activity/exercise, 3-5 times", style=nextcord.ButtonStyle.primary)
    async def moderate_activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1.55
        self.stop()
        await interaction.response.edit_message(content="You have selected moderate activity/exercise (Activity level: 1.55).")

    @nextcord.ui.button(label="Heavy activity/exercise, 5-7 times", style=nextcord.ButtonStyle.primary)
    async def heavy_activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1.725
        self.stop()
        await interaction.response.edit_message(content="You have selected heavy activity/exercise (Activity level: 1.725).")

    @nextcord.ui.button(label="Very heavy activity/exercise, more than once a day", style=nextcord.ButtonStyle.primary)
    async def very_heavy_activity(self, button: nextcord.ui.Button, interaction: Interaction):
        self.value = 1.9
        self.stop()
        await interaction.response.edit_message(content="You have selected very heavy activity/exercise (Activity level: 1.9).")

# update user info
# update user info
async def update(ctx, message:str, column:int):
    user_found = False

    # Read data from the CSV file and update the user's info
    rows = []
    with open("info.csv", "r+", encoding="utf-8") as file:
        userdata = csv.reader(file)
        rows = list(userdata)

        for i, row in enumerate(rows):
            data = row[0].split(",")
            if data[0] == str(ctx.user.id):
                rows[i][column] = message
                user_found = True
                break

        # If user doesn't exist, add them to the file
        if not user_found:
            new_row = [str(ctx.user.id)] + ["N/A"] * 7
            update(ctx, message, column)
            rows.append(new_row)

        # Write the data back to the CSV file (appending)
        with open("info.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)

# # hello message command
# @bot.slash_command(description="My first slash command")
# async def hello(interaction: nextcord.Interaction):
#     await interaction.send("Hello!")

# update user health info
@bot.slash_command(name = "updateinfo", description="Updating health information")
async def update_info(ctx):
    view = yourinfo()
    await ctx.send("What would you like to update?", view=view)
    await view.wait()

    if view.value == 'name':
        await ctx.send("Please enter your name")
        try:
            msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
            name_value = msg.content.strip()
            if name_value:
                await update(ctx, name_value, 1)
                await ctx.send(f"Your name has been changed to {name_value}")
            else:
                await ctx.send("Name cannot be empty. Please try again.")
        except asyncio.TimeoutError:
            await ctx.send("Timed out!")
            return

    elif view.value == 'gender':
        await ctx.send("Please enter your gender")
        try:
            # reply gets the entire object of the message
            msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
            gender_value = msg.content.strip()
            if gender_value:
                await update(ctx, gender_value, 2)
                await ctx.send(f"Your gender has been changed to {gender_value}")
            else:
                await ctx.send("Gender cannot be empty. Please try again.")
        except asyncio.TimeoutError:
            await ctx.send("Timed out!")
            return
        
    elif view.value == 'age':
        while True:
            await ctx.send("Please enter your age (in years)")
            try:
                # reply gets the entire object of the message
                msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
                age_value = msg.content.strip()

                if age_value.isdigit():
                    age_value = int(age_value)
                    await update(ctx, age_value, 1)
                    await ctx.send(f"Your age has been changed to {age_value}.")
                    break  # Exit the loop if a valid integer is provided
                else:
                    await ctx.send("Invalid input. Please enter a valid number value.")
            except asyncio.TimeoutError:
                await ctx.send("Timed out!")
                return

    elif view.value == 'height':
        while True:
            await ctx.send("Please enter your height (in cm)")
            try:
                # reply gets the entire object of the message
                msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
                height_value = msg.content.strip()

                if height_value.isdigit():
                    height_value = float(height_value)
                    await update(ctx, height_value, 1)
                    await ctx.send(f"Your height has been changed to {height_value}cm.")
                    break  # Exit the loop if a valid integer is provided
                else:
                    await ctx.send("Invalid input. Please enter a valid number value.")
            except asyncio.TimeoutError:
                await ctx.send("Timed out!")
                return
    
    elif view.value == 'weight':
        while True:
            await ctx.send("Please enter your weight (in kg)")
            try:
                # reply gets the entire object of the message
                msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
                weight_value = msg.content.strip()

                if weight_value.isdigit():
                    weight_value = float(weight_value)
                    await update(ctx, weight_value, 1)
                    await ctx.send(f"Your weight has been changed to {weight_value}kg.")
                    break  # Exit the loop if a valid integer is provided
                else:
                    await ctx.send("Invalid input. Please enter a valid number value.")
            except asyncio.TimeoutError:
                await ctx.send("Timed out!")
                return
    
    elif view.value == 'activity':
        # await ctx.send("Please enter your activity level")
        try:
            msg = await bot.wait_for("message", timeout=60, check=lambda message: message.author != bot.user)
            # Check if the content is non-empty before trying to convert to float
            if msg.content.strip():
                activity_value = float(msg.content)
                await update(ctx, activity_value, 6)  # Change the column number to match the activity column
                await ctx.send(f"Your activity level has been changed to {activity_value}.")
            else:
                await ctx.send("Activity level value cannot be empty. Please try again.")
        except asyncio.TimeoutError:
            await ctx.send("Timed out!")
            return

# motivation/encouragement
@bot.slash_command(name="quotes", description="Quotes for motivation and encouragement")
async def motivation(interaction: nextcord.Interaction):
    # Open the quotes CSV file and read the quotes
    with open("quotes_filtered_2.csv", "r", encoding="utf-8") as file:
        quotes_reader = csv.reader(file)
        quotes = [row[0] for row in quotes_reader]

    # Randomly choose a quote from the list
    selected_quote = random.choice(quotes)

    # Present the quote to the user
    await interaction.send(selected_quote) 

# # List of commands for the discord bot
# @bot.slash_command(name = "commands", description="List of commands for the discord bot")
# async def commands(interaction: nextcord.Interaction):
#     await interaction.send("Here is the list of available commands.\n\n/commands - List of commands to use\n/BMR - Let BottyBuilder calculate your BMR, daily calorie needs, and how much you need to eat to bulk/cut.\n/bulkfoods - A list of foods that are beneficial for bulking. To know the AMOUNT you need to eat to bulk, use the !BMR command.\n/cutfoods - A list of foods that are beneficial for cutting. To know the AMOUNT you need to eat to cut, use the !BMR command.")

# Exercise recommendations command
@bot.slash_command(name="exercises", description="List of home or gym exercises for certain muscle groups")
async def exercise_recommendations(interaction: nextcord.Interaction):
    # Create the initial view with options for gym and home exercises
    exercise_options_view = ExerciseOptionsView()
    await interaction.send("Please choose an exercise category:", view=exercise_options_view)

class ExerciseOptionsView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.is_gym = None  # Attribute to store exercise category

    @nextcord.ui.button(label="Gym Exercises", style=nextcord.ButtonStyle.primary, custom_id="gym_exercises")
    async def gym_exercises(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.clear_items()  # Clear the existing buttons
        self.is_gym = True
        await self.show_muscle_group_buttons(interaction)

    @nextcord.ui.button(label="Home Exercises", style=nextcord.ButtonStyle.primary, custom_id="home_exercises")
    async def home_exercises(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        self.clear_items()  # Clear the existing buttons
        self.is_gym = False
        await self.show_muscle_group_buttons(interaction)

    async def show_muscle_group_buttons(self, interaction: nextcord.Interaction):
        # Define muscle groups based on the exercise category (gym or home)
        muscle_groups = {
            "Chest": ["Bench press", "Dumbbell flyes", "Cable crossovers"],
            "Back": ["Lat pulldowns", "Barbell rows", "Deadlifts"],
            "Arms": ["Bicep curls", "Tricep pushdowns", "Hammer curls"],
            "Abdominals": ["Crunches", "Leg raises", "Planks"],
            "Legs": ["Squats", "Leg press", "Lunges"],
            "Shoulders": ["Overhead press", "Lateral raises", "Front raises"]
        }

        content = "Please choose a muscle group:\n\n"
        for muscle_group, exercises in muscle_groups.items():
            # Use the muscle group name as a custom ID to identify the selected group later
            self.add_item(nextcord.ui.Button(label=muscle_group, style=nextcord.ButtonStyle.primary, custom_id=f"exercise_{muscle_group}"))

        await interaction.response.edit_message(content=content, view=self)

@bot.event
async def on_button_click(interaction: nextcord.Interaction):
    print("Button clicked!")
    try:
        if interaction.custom_id.startswith("exercise_") and interaction.view and interaction.view.is_valid():
            print("Exercise button clicked!")
            muscle_group = interaction.custom_id[len("exercise_"):]

            # Retrieve the exercises based on the selected muscle group and exercise category
            is_gym = interaction.view.is_gym
            exercises = {
                "Chest": ["Bench press", "Dumbbell flyes", "Cable crossovers"],
                "Back": ["Lat pulldowns", "Barbell rows", "Deadlifts"],
                "Arms": ["Bicep curls", "Tricep pushdowns", "Hammer curls"],
                "Abdominals": ["Crunches", "Leg raises", "Planks"],
                "Legs": ["Squats", "Leg press", "Lunges"],
                "Shoulders": ["Overhead press", "Lateral raises", "Front raises"]
            }

            selected_exercises = exercises.get(muscle_group, [])

            if selected_exercises:
                # Build the message dynamically based on the selected muscle group
                message_content = f"Exercises for {muscle_group}:\n\n{', '.join(selected_exercises)}"
                await interaction.edit_original_message(content=message_content)
            else:
                await interaction.edit_original_message(content=f"No exercises found for {muscle_group}")

    except nextcord.errors.NotFound:
        # Handle the case where the interaction is no longer valid
        print("Interaction not found. Ignoring the button click.")
        

# # List of recommended foods to eat during a bulk or cut
# @bot.slash_command(name="Food", description="List of recommended foods for bulking or cutting")
# async def food_recommendations(interaction: nextcord.Interaction):
#     # Create the initial view with options for bulking and cutting
#     food_options_view = FoodOptionsView()

#     await interaction.send("Please choose a dietary goal:", view=food_options_view)
#     await food_options_view.wait()

# class FoodOptionsView(nextcord.ui.View):
#     def __init__(self):
#         super().__init__()

#     @nextcord.ui.button(label="Bulking", style=nextcord.ButtonStyle.primary, custom_id="bulking")
#     async def bulking(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
#         self.clear_items()  # Clear the existing buttons
#         await self.show_food_recommendations(interaction, is_bulking=True)

#     @nextcord.ui.button(label="Cutting", style=nextcord.ButtonStyle.primary, custom_id="cutting")
#     async def cutting(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
#         self.clear_items()  # Clear the existing buttons
#         await self.show_food_recommendations(interaction, is_bulking=False)

#     async def show_food_recommendations(self, interaction: nextcord.Interaction, is_bulking: bool):
#         food_recommendations = {
#             "Bulking": [
#                 "Lean protein sources (chicken, turkey, fish)",
#                 "Complex carbohydrates (brown rice, quinoa, oats)",
#                 "Healthy fats (avocado, nuts, olive oil)",
#                 "Dairy products (Greek yogurt, cottage cheese)",
#                 "Leafy greens and vegetables",
#                 "Fruits (berries, bananas)",
#                 "Protein shakes or bars"
#             ],
#             "Cutting": [
#                 "Lean protein sources (chicken breast, turkey, fish)",
#                 "Non-starchy vegetables (broccoli, spinach, kale)",
#                 "Low-calorie fruits (berries, grapefruit)",
#                 "Complex carbohydrates in moderation (sweet potatoes, quinoa)",
#                 "Healthy fats in moderation (avocado, almonds)",
#                 "Water and herbal tea (to stay hydrated)",
#                 "Lean protein shakes or bars (as snacks)"
#             ]
#         }

#         selected_recommendations = food_recommendations["Bulking" if is_bulking else "Cutting"]

#         await interaction.response.edit_message(content=f"Here are some recommended foods for {'bulking' if is_bulking else 'cutting'}:\n\n" + "\n".join(selected_recommendations))

# # Workout plans/routines
# @bot.slash_command(name="Routines", description="List of workout routines to follow")
# async def workout(interaction: nextcord.Interaction):
#     # Create the initial view with options for workout plans
#     workout_options_view = WorkoutOptionsView()

#     await interaction.send("Please choose a workout plan:", view=workout_options_view)
#     await workout_options_view.wait()

# class WorkoutOptionsView(nextcord.ui.View):
#     def __init__(self):
#         super().__init__()

#     @nextcord.ui.button(label="Beginners", style=nextcord.ButtonStyle.primary, custom_id="beginners")
#     async def beginners(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
#         self.clear_items()  # Clear the existing buttons
#         await self.show_workout_plan(interaction, plan="Beginners")

#     @nextcord.ui.button(label="Push-Pull-Leg Split", style=nextcord.ButtonStyle.primary, custom_id="push_pull_leg_split")
#     async def push_pull_leg_split(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
#         self.clear_items()  # Clear the existing buttons
#         await self.show_workout_plan(interaction, plan="Push-Pull-Leg Split")

#     async def show_workout_plan(self, interaction: nextcord.Interaction, plan: str):
#         workout_plans = {
#             "Beginners": {
#                 "Monday - Arms and Shoulders": [
#                     "Bicep curls",
#                     "Shoulder press",
#                     "Tricep dips",
#                     "Lateral raises"
#                 ],
#                 "Wednesday - Legs and Abdominals": [],
#                 "Friday - Chest and Back": []
#             },
#             "Push-Pull-Leg Split": {
#                 "Monday - Push": [
#                     "Bench Press",
#                     "Seated Dumbbell Shoulder Press",
#                     "Incline Dumbbell Press",
#                     "Side Lateral Raises",
#                     "Triceps Pressdowns",
#                     "Overhead Triceps Extension"
#                 ],
#                 "Wednesday - Pull": [],
#                 "Friday - Leg": []
#             }
#         }

#         selected_workout_plan = workout_plans.get(plan, {})

#         if selected_workout_plan:
#             workout_plan_text = "\n".join([f"{day}\n" + "\n".join(exercises) for day, exercises in selected_workout_plan.items()])
#             await interaction.response.edit_message(content=f"Here is the {plan} workout plan:\n\n{workout_plan_text}")
#         else:
#             await interaction.response.edit_message(content=f"No workout plan found for {plan}")


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


# List of exercises to do for certain muscle groups based on home or gym exercises

# List of recommended foods to eat during a bulk

# List of recommended foods to eat during a cut
    
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

#if () #if statement for checking user's gender (male/female), just need to add extra column in file
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

# make a function instead?!??!??!?!?!?!?!  wuzzup
def calculate_bmr(gender, age, height, weight, activity):
    # Convert gender to lowercase and remove whitespace
    #gender = gender.strip().lower()
    
    # will get gender another way instead of doing this
    if gender == "male":
        bmpValue = 66.5 + (13.75 * weight) + (5.003 * height) - (6.75 * age)
        dclm = bmpValue*activity
        bulk = dclm*1.15
        cut = dclm*0.85
    elif gender == "female":
        bmpValue = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
        dclm = bmpValue*activity
        bulk = dclm*1.15
        cut = dclm*0.85

    return bmpValue

# buttons for the bmr stuff
@bot.slash_command(name="bmr", description="BMR, Daily Calorie Needs, Bulk (Calories), Cut (Calories)")
async def bmr_info(ctx):
    view = bmr()
    await ctx.send("What would you like to calculate?", view=view)
    await view.wait()

    if view.value == "BMR":
        # Get user data from CSV file
        with open("info.csv", "r", encoding="utf-8") as file:
            userdata = csv.reader(file)
            next(userdata)  # Skip header row

            for row in userdata:
                data = row[0].split(",")  # Split each row by comma
                if data[0] == str(ctx.user.id): # user ID is the many numbers
                    # Extract needed values from the row
                    name = str(row[1])
                    gender = str(row[2])
                    age = float(row[3])
                    height = float(row[4])
                    weight = float(row[5])
                    activity = float(row[6])

                    # Calculate BMR based on gender, age, height, and weight
                    bmr_value = calculate_bmr(gender, age, height, weight, activity)
                    await ctx.send(f"{name}, your BMR is {bmr_value}")
                    file.close()
                    return
                    # Calculate and send other values (daily calorie needs, bulk, cut) if needed
            else:
                await ctx.send("You have not set your information yet. Please use the ```/updateinfo``` command to set your information.")
                file.close()

        # present value of dcml/bulk/cut to the user when they use the command 
        # (go back to the button part of the code)
 
# List of muscle groups to train command + buttons
bot.run(token)