import PySimpleGUI as sg
import os
import json

# Very basic form.  Return values as a list
def cred():
	form = sg.FlexForm('Simple data entry form')  # begin with a blank form

	layout = [
	          [sg.Text('Please enter your Name, Address, Phone')],
	          [sg.Text('un', size=(15, 1)), sg.InputText('')],
	          [sg.Text('pin', size=(15, 1)), sg.InputText('')],
	          [sg.Submit(), sg.Cancel()]
	         ]

	button, values = form.Layout(layout).Read()

	a = values[0]
	b = values[1]

	c = {'username' : a, 'password' : b}

	return c

with open('cred.json', 'w') as json_file:
	json.dump(cred(), json_file, indent = 2)
