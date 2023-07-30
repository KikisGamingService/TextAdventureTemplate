#################################################################################
#										#
#										#
#	Text Adventure Template, by Daniel Kass - KikisGamingService.com	#
#										#
#										#
#################################################################################


This is a template to create your own short text adventure that can be extended as needed. The current example includes a quick story of someone gathering up all items they need before being able to go to work.

- Required Software:
Current Python installation to run the main file. This was created and tested with Python 3.10.
A text editor to edit any Python files. Data files for a PyCharm project are included. If PyCharm project files are needed, make sure to extract both the venv and the .idea folders.

- Main files:
TextBasedGame.py is the main Python file. Edit the text in here to create your own stories, rooms, and more.
.idea and venv folders are for the PyCharm project and virtual environment. These are optional to the functionality of the .py file.

- Changing the level map and items:
Under the "rooms" variable, any amount of additional rooms can be added or removed. The example ones are aligned with north, south, east, west directions. However, secret directions or phrases like "up the stairs" can be used as well. Just make sure that rooms are connected to other rooms, as they will be inaccessible otherwise.

- Adding items:
The "rooms" variable also includes a parameter for items in the current room. Any additional items to be picked up can be added here. If a long list of items should be added to a room or an item should be added to multiple rooms, I suggest creating a list variable for them first, then using the variable in the item slot.
