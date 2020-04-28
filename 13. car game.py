print("Type 'help' for help: ")
started = False
stopped = True
command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
            stopped = False
            print("Car started!")
    elif command == "stop":
        if stopped:

            print("Car is already stopped")
        else:
            print("Car stopped")
            stopped = True
            started = False
    elif command == "help":
        print("""
> Type "start" to start the car
> Type "stop" to stop the car
> Type "quit" to quit the program
        """)
    elif command == "quit":
        break
    else:
        print("Sorry i don't understand")
        print("Type 'help' for help")
else:
    print("You quit")
