# Minus is Jump plus automated downloader and archiver.
# (C) 2020 Mitsuhiro Hashimoto (@Adolfoi_) All rights reserved.
# LICENCE: MIT License

import PySimpleGUI as sg

sg.theme('DarkBlue')	# Add a touch of color
# All the stuff inside your window.
layout = [  # [sg.Text('Some text on Row 1')],
            [sg.Text('ジャンププラスの漫画のURL'), sg.InputText()],
            [sg.Button('スタート'), sg.Button('キャンセル')] ]

# Create the Window

window = sg.Window('Minus', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':	# if user closes window or clicks cancel
        break

    if event == sg.WIN_CLOSED or event == 'スタート':	# if user closes window or clicks cancel
        print('You entered ', values[0])
        break
window.close()