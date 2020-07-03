command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car Started")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif command == "help":
        print('''
start -  To start the car
stop -  To Stop the car
Quit - Quit
        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand that")


