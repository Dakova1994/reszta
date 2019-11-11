
nominaly = [200.00, 100.00, 50.00, 20.00, 10.00, 5.00, 2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]

print("\n\n     Podaj nominały, których nie chcesz użyć\n     jeżeli chcesz użyć wszystkich wpisz 'd' //dalej.\n     Aby wyświetlić liste nominałów wpisz 'n' //nominały\n\n")
decyzja = ""
print("Dostępne nominały", *nominaly)
while decyzja!="dalej":
    decyzja = input()
    if decyzja=="d":
        break
    if decyzja=="n":
        print(*nominaly)
        decyzja = input()
    decyzja = float(decyzja)
    nominaly.remove(decyzja)
    print("Usunąłeś nominał:", decyzja)
    decyzja = str(decyzja)



print("Podaj reszte do wypłacenia:")
reszta = float(input("kwota:"))

i=0
while reszta>0.00:
    if reszta >= nominaly[i]:
        ilosc=reszta/nominaly[i]
        ilosc=int(ilosc)
        reszta=reszta-(nominaly[i]*ilosc)
        print(nominaly[i],"zł x", ilosc)
        reszta = round(reszta,2)
    i=i+1
