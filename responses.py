# commands
def commands(message) -> str:
    command = message.lower()

# list of commands
# !commands - a list of commands to use
# !BMR - for calculating BMR and daily calorie needs
# !bulk - include message "to know the amount you need to bulk, use the !BMR command" and include list of foods for bulking
# !cut - include message "to know the amount you need to cut, use the !BMR command" and include list of foods for cutting
# !dietplan - 
# !exercises - 


if command == '!commands':
    return 'Here is the list of available commands.\n!commands - list of commands to use\n!BMR - let BottyBuilder calculate your BMR, daily calorie needs, and how much you need to eat to bulk/cut.\n!bulk - A list of foods that are beneficial for bulking. To know the amount you need to eat to bulk, use the !BMR command.\n!cut - A list of foods that are beneficial for cutting. To know the amount you need to eat to cut, use the !BMR command.'

if 
