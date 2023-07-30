# Original creator: Daniel Kass - KikisGamingService.com

# Introduction - Edit this to change how the player is greeted in the very beginning.
# Tutorials and further information should go here.
print()
print('Get to work! - the game')
print('Make sure you get everything you need before going to your car and driving to work:')
print('Clothes, hairbrush, lunch, laptop, toothbrush, and car keys')
print('Move commands: go South, go North, go East, go West, exit')
print("Add to Inventory: get 'item name'")
print()
print(' --------------------------------')


def main():
    # Default map - The dictionary links a room to other rooms and includes items.
    rooms = {
        'Closet': {'East': 'Bedroom', 'Item': 'Clothes'},
        'Bedroom': {'North': 'Office', 'West': 'Closet', 'South': 'Hallway', 'East': 'Entrance'},
        'Hallway': {'North': 'Bedroom', 'East': 'Kitchen', 'Item': 'Hairbrush'},
        'Kitchen': {'West': 'Hallway', 'Item': 'Lunch'},
        'Office': {'South': 'Bedroom', 'East': 'Bathroom', 'Item': 'Laptop'},
        'Bathroom': {'West': 'Office', 'Item': 'Toothbrush'},
        'Driveway': {'South': 'Entrance', 'Item': 'Car'},
        'Entrance': {'North': 'Driveway', 'West': 'Bedroom', 'Item': 'Keys'}
    }

    # This sets the starting room, empties the inventory, and removes the steps taken.
    # Edit this for a change in starting inventory and starting room.
    current_room = 'Bedroom'
    inventory = []
    steps = 0

    # Main loop to keep the game going and actions repeating.
    while True:
        # Returning current status and getting next move.
        print()
        print('You are in the', current_room)
        print('Inventory:', inventory)
        if rooms.get(current_room).get('Item') is None:
            print('There is no item in this room.')
        else:
            print('You see:', rooms.get(current_room).get('Item'))
        print('You have taken', steps, 'steps so far.')
        print('Enter your move:')
        user_input = input()
        steps += 1

        # Checking for win condition.
        if current_room == 'Driveway' and user_input == 'get Car':
            if len(inventory) == 6:
                print('You got everything set and got to work on time, good job!')
                break
            else:
                print('You did not get everything set and have to go back.')
                print('This causes you to be late at work. Maybe try again tomorrow.')
                break

        # try/catch to make sure no unexpected errors crash the program.
        try:
            # Check if user wants to exit.
            if user_input.startswith('exit'):
                break
            # Moving between rooms.
            elif user_input.startswith('go'):
                # Check if the second word of the user input matches an available room in the
                # current entry of the dictionary.
                if user_input.split()[1] in rooms.get(current_room):
                    current_room = rooms.get(current_room).get(user_input.split()[1])
                else:
                    print("You can't go that way, try again.")
            # Receiving items.
            elif user_input.startswith('get'):
                if user_input.split()[1] in rooms.get(current_room).values():
                    inventory += [rooms.get(current_room).get('Item')]
                    print('You took:', rooms.get(current_room).get('Item'))
                    rooms.get(current_room).pop('Item')
                else:
                    print('That object does not exist, try again.')
            else:
                print('Invalid input, try again.')
        except (IndexError, NameError, TypeError, RuntimeError):
            print('Invalid input, try again.')

    # Goodbye message and steps taken.
    print('Thank you for playing the game. Have a nice day!')
    print('Final score:', steps, 'steps')


# Calling main function. Any other functions would only be a couple lines long and were removed for legibility.
if __name__ == "__main__":
    main()
