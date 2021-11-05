from vragenlijst_functies import Vraag
from punten_tellen import punten_tellen
from punten_toevoegen import punten_toevoegen
import PySimpleGUI as sg
import json

f = open('database.json', errors='ignore')
data = json.load(f)

# punten
punten_lijst = [0, 0, 0, 0]

# variables
vragenlijst_index = 0

for i in range(0, len(list(data.keys()))):
    x = list(data.keys())[i]

def get_kenmerk(vragenlijst_index):
    kenmerken = []
    x = list(data.keys())[vragenlijst_index]
    for key in data[x]:
        kenmerken.append(list(data[x][key].values())[0])
    return kenmerken


def get_punten(vragenlijst_index):
    punten = []
    x = list(data.keys())[vragenlijst_index]
    for key in data[x]:
        punten.append(list(data[x][key].values())[1])
    return punten


vraag1 = Vraag(list(data.keys())[0], list(data[list(data.keys())[0]]), get_kenmerk(0), get_punten(0))
vraag2 = Vraag(list(data.keys())[1], list(data[list(data.keys())[1]]), get_kenmerk(1), get_punten(1))
vraag3 = Vraag(list(data.keys())[2], list(data[list(data.keys())[2]]), get_kenmerk(2), get_punten(2))
vraag4 = Vraag(list(data.keys())[3], list(data[list(data.keys())[3]]), get_kenmerk(3), get_punten(3))
vraag5 = Vraag(list(data.keys())[4], list(data[list(data.keys())[4]]), get_kenmerk(4), get_punten(4))
vraag6 = Vraag(list(data.keys())[5], list(data[list(data.keys())[5]]), get_kenmerk(5), get_punten(5))
vraag7 = Vraag(list(data.keys())[6], list(data[list(data.keys())[6]]), get_kenmerk(6), get_punten(6))
vraag8 = Vraag(list(data.keys())[7], list(data[list(data.keys())[7]]), get_kenmerk(7), get_punten(7))
vraag9 = Vraag(list(data.keys())[8], list(data[list(data.keys())[8]]), get_kenmerk(8), get_punten(8))
vraag10 = Vraag(list(data.keys())[9], list(data[list(data.keys())[9]]), get_kenmerk(9), get_punten(9))
vraag11 = Vraag(list(data.keys())[10], list(data[list(data.keys())[10]]), get_kenmerk(10), get_punten(10))
vraag12 = Vraag(list(data.keys())[11], list(data[list(data.keys())[11]]), get_kenmerk(11), get_punten(11))
vraag13 = Vraag(list(data.keys())[12], list(data[list(data.keys())[12]]), get_kenmerk(12), get_punten(12))
vraag14 = Vraag(list(data.keys())[13], list(data[list(data.keys())[13]]), get_kenmerk(13), get_punten(13))
vraag15 = Vraag(list(data.keys())[14], list(data[list(data.keys())[14]]), get_kenmerk(14), get_punten(14))
vraag16 = Vraag(list(data.keys())[15], list(data[list(data.keys())[15]]), get_kenmerk(15), get_punten(15))
vraag17 = Vraag(list(data.keys())[16], list(data[list(data.keys())[16]]), get_kenmerk(16), get_punten(16))
vraag18 = Vraag(list(data.keys())[17], list(data[list(data.keys())[17]]), get_kenmerk(17), get_punten(17))

vragenlijst = [vraag1, vraag2, vraag3, vraag4, vraag5, vraag6, vraag7, vraag8, vraag9, vraag10, vraag11, vraag12,
               vraag13, vraag14, vraag15, vraag16, vraag17, vraag18]

def result():
    specialisatie = punten_tellen(punten_lijst)
    print(specialisatie)
    gekozen_specialisaties = ''

    if len(punten_tellen(punten_lijst)) == 1:
        pass
    elif len(punten_tellen(punten_lijst)) == 4:
        print("Je hebt alle 4 de scores gelijk! Magie!!! Jij moet wel een tovenaar zijn")
    else:
        print("Je hebt een gelijke score voor:")
        for x in punten_tellen(punten_lijst):
            print(x)

    for i in specialisatie:
        gekozen_specialisaties += i + '. '

    window['_vraag_'].update('Gefeliciteerd! De specialisatie die het beste bij je past is: ' + gekozen_specialisaties)
    window['_1_'].update(visible=False)
    window['_2_'].update(visible=False)
    window['_3_'].update(visible=False)
    window['_4_'].update(visible=False)


def update():
    global vragenlijst_index,vragenlijst
    vragenlijst_index += 1
    window['_vraag_'].update(vragenlijst[vragenlijst_index].tekst)
    window['_1_'].update(vragenlijst[vragenlijst_index].antwoorden[0])
    window['_2_'].update(vragenlijst[vragenlijst_index].antwoorden[1])
    window['_3_'].update(vragenlijst[vragenlijst_index].antwoorden[2])
    window['_4_'].update(vragenlijst[vragenlijst_index].antwoorden[3])
    print(list(data.keys())[vragenlijst_index])

# window
sg.theme('DarkBlue14')
key: object
layout = [
    [sg.Text(vragenlijst[vragenlijst_index].tekst, size=(400, 1), pad=(25,25), key='_vraag_', visible=True, justification='center', font =('Any15', 12))],
    [sg.Button(vragenlijst[vragenlijst_index].antwoorden[0], border_width=2, size=(60,2), pad=(10,10), key='_1_', visible=True, font =('Any15', 12))],
    [sg.Button(vragenlijst[vragenlijst_index].antwoorden[1], border_width=2, size=(60,2), pad=(10,10), key='_2_', visible=True, font =('Any15', 12))],
    [sg.Button(vragenlijst[vragenlijst_index].antwoorden[2], border_width=2, size=(60,2), pad=(10,10), key='_3_', visible=True, font =('Any15', 12))],
    [sg.Button(vragenlijst[vragenlijst_index].antwoorden[3], border_width=2, size=(60,2), pad=(10,10), key='_4_', visible=True, font=('Any15', 12))],
]
window = sg.Window('RatIT Sorting Quiz', layout, size=(1400, 500), element_justification='c')

while True:
    event, values = window.read()
    if event == '_1_':
        punten_toevoegen(punten_lijst, get_punten(vragenlijst_index)[0])
        print(punten_lijst)
        if vragenlijst_index == 17:
            result()
        elif vragenlijst_index != 17:
            update()
    if event == '_2_':
        punten_toevoegen(punten_lijst, get_punten(vragenlijst_index)[1])
        if vragenlijst_index == 17:
            result()
        elif vragenlijst_index != 17:
            update()
    if event == '_3_':
        punten_toevoegen(punten_lijst, get_punten(vragenlijst_index)[2])
        print(punten_lijst)
        if vragenlijst_index == 17:
            result()
        elif vragenlijst_index != 17:
            update()
    if event == '_4_':
        punten_toevoegen(punten_lijst, get_punten(vragenlijst_index)[3])
        print(punten_lijst)
        if vragenlijst_index == 17:
            result()
        elif vragenlijst_index != 17:
            update()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break

window.close()
