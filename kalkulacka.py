class Kalkulacka:
    def nacti_cislo(self, text_zadani, text_chyba):
        spatne = True
        while spatne:
            try:
                cislo = float(input(text_zadani))
                spatne = False
            except ValueError:
                print(text_chyba)
        return cislo

    def dalsi_priklad(self):
        nezadano = True
        while nezadano:
            odpoved = input("\nPřejete si zadat další příklady? y / n: ").lower()
            if odpoved == "y":
                return True
            elif odpoved == "n":
                return False
            else:
                pass

    def volba(self, prvni_cislo, druhe_cislo):
        print(f"První číslo: {prvni_cislo}")
        print(f"Druhé číslo: {druhe_cislo}")
        print("1 sčítání \n2 - odčítání \n3 - násobení \n4 - dělení \n5 - umocňování")
        cislo_operace = self.nacti_cislo("Zadej volbu: ", "Neplatné zadání!\n")
        if cislo_operace == 1:
            print("Jejech součet je:", prvni_cislo + druhe_cislo)
        elif cislo_operace == 2:
            print("Jejech rozdíl je:", prvni_cislo - druhe_cislo)
        elif cislo_operace == 3:
            print("Jejech součin je:", prvni_cislo * druhe_cislo)
        elif cislo_operace == 4:
            if druhe_cislo == 0:
                print("Dělení nulou, nelze!")
            else:
                print("Jejich podíl je:", prvni_cislo / druhe_cislo)
        elif cislo_operace == 5:
            print(prvni_cislo, "na", druhe_cislo, "je:", prvni_cislo ** druhe_cislo)
        else:
            print("Neplatná volba!")