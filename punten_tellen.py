def punten_tellen(punten_lijst):
    specialisatie_lijst = ["BDaM", "FICT", "SE", "IaT"]

    hoogst_behaalde_punten = max(punten_lijst)
    gekozen_specialisatie_lijst = []

    for index, val in enumerate(punten_lijst):
        if val == hoogst_behaalde_punten:
            gekozen_specialisatie_lijst.append(specialisatie_lijst[index])
        index += 1

    return gekozen_specialisatie_lijst