#!/usr/bin/python3


commandlist = [
	"button_clicked",
	"cycle_complete",
	"button_clicked",
	"button_clicked",
	"button_clicked",
	"button_clicked",
	"button_clicked",
	"cycle_complete" ]

state = "closed"

for command in commandlist:
	print("Door: " + state)
	print("> " + command)

	# all the way closed before click
	if command == "button_clicked" and state == "closed":
		state = "opening"
	# all the way open, before click
	elif command == "button_clicked" and state == "open":
		state = "closing"
	# click while opening
	elif command == "button_clicked" and state == "opening":
		state = "stopped_while_opening"
	# click after stopped while opening
	elif command == "button_clicked" and state == "stopped_while_opening":
		state = "closing"
	# click while closing
	elif command == "button_clicked" and state == "closing":
		state = "stopped_while_closing"
	# click after stopped while closing
	elif command == "button_clicked" and state == "stopped_while_closing":
		state = "opening"
	# finished opening	
	elif command == "cycle_complete" and state == "opening":
		state = "open"
	# finished closing
	elif command == "cycle_complete" and state == "closing":
		state = "open"
	else:
		print("ERROR! state: " + state + "Command" + command)


