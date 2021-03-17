import PySimpleGUIWeb as sg

import webbrowser

layout = [[sg.Text('Clickable Link Here', enable_events=True, key='-LINK-')],

          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop

    event, values = window.read()

    print(event, values)

    if event in (None, 'Exit'):
        break

    if event == 'Go' or event == '-LINK-':
        webbrowser.open(r'www.bing.com')

window.close()