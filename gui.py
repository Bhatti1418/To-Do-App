import PySimpleGUI as sg
label = sg.Text("Text in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
window = sg.Window('My to do app', layout=[[label,input_box,add_button]])
window.read()
window.close()
