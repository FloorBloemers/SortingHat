def punten_toevoegen(punten_lijsten, kenmerk_punten_lijst):
    index = 0
    for x in kenmerk_punten_lijst:
        punten_lijsten[index] += x
        index += 1
    return punten_lijsten