from kalkulacka import Kalkulacka

class Main:
    kalkulacka = Kalkulacka()
    print("kalkulačka 4. verze\n")
    pokracovat = True
    while pokracovat:
        prvni_cislo = kalkulacka.nacti_cislo("Zadej první číslo: ", "Neplatné číslo!\n")
        druhe_cislo = kalkulacka.nacti_cislo("Zadej druhé číslo: ", "Neplatné číslo!\n")
        kalkulacka.volba(prvni_cislo, druhe_cislo)
        if kalkulacka.dalsi_priklad():
            pass
        else:
            pokracovat = False
    input("\nStiskněte klávesu Enter...")
