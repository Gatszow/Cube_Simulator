#-*- coding: utf-8 -*-
import random
import time
print("# "*40, end ="")
print(" $ $ $ $ $ $ $ $ $ $ $ $ $ SYMULATOR RZUTU KOSTKAMI $ $ $ $ $ $ $ $ $ $ $ $ $ ")
print("# "*40, end ="")
#Czy wyjść czy nie
wyjscie = False
while wyjscie == False:
#Tryb działania
    tryb = str(input("Tryb:\n1. Pokazanie z zgadywaniem\n2. Pokazanie bez zgadywania\n3. Rzutowanie kostki\nWybieram tryb - "))
    tryb = tryb.upper()
    tryb = tryb.replace(" ", "")
    T = True
    while (T == True):
        if tryb == ("1" or "POKAZYWANIEZZGADYWANIEM" or "1.") or ("2" or "POKAZANIEBEZZGADYWANIA" or "2.") or ("3" or "3." or "RZUTOWANIEKOSTKI"):
            print("#"*80, end ="")
            T = False
        else:
            tryb = str(input("\nBłędne dane, wprowadź tryb raz jeszcze - "))
#liczba kostek
    l_k = str(input("Ile masz kostek? - "))
    print("#"*80, end ="")
    T = True
    while (T == True):
        try:
            l_k = int(l_k)
            if l_k > 0:
                T = False
            else:
#Jeśli liczba kostek jest mniejsza niż 0
                print("Jak nie masz kostek, to je:\n$$$$ kup $$$$ \nlub \n^.^ zmyśl ^.^")
                print("#"*80, end="")
                l_k = input("Zmyśliłeś lub kupiłeś? Powiedz więc ile masz\n")
                print("#"*80, end="")
        except ValueError:
            print("Skoro nie wprowadzasz \"liczby\" (1, 2, 3, 4...) kostek, \nto jak mam wylosować ci ilość oczek na nich? :C")
            l_k = str(input("Popraw się i wpisz tu ilość swoich kostek: "))
            print("#"*80, end="")
#Liczba oczek
    oczka = input("Ile oczek jest na jednej kostce? - ")
    print("#"*80, end="")
    T = True
    while (T == True):
        try:
            oczka = int(oczka)
            if oczka > 0:
                T = False
            else:
                oczka = str(input("Nieprawidłowa liczba oczek, wpisz poprawną liczbę (całkowita dodatnia liczba): "))
                print("#"*80, end="")
        except ValueError:
            oczka = str(input("Nieprawidłowa liczba oczek, wpisz poprawną liczbę (całkowita dodatnia liczba): "))
            print("#"*80, end="")
#tryb 3 - długość drogi do przebycia
    if tryb == ("3" or "RZUTOWANIEKOSTKI" or "3."):
        p_dl = 0
        d_dl = input("Wprowadź docelowy dystans do przebycia - ")
        T = True
        while (T == True):
            try:
                d_dl = int(d_dl)
                if l_k*oczka >= d_dl > 0:
                    T = False
                else:
                    d_dl = str(input("\nNieprawidłowy dystans (dystans musi być wyrażony w całkowitej liczbie dodatniej oraz musi być mniejszy niż liczba wprowadzonych kostek razy ilość oczek na nich) \nWprowadź prawidłowy dystans - "))
            except ValueError:
                str(input("Nieprawidłowy dystans (dystans musi być wyrażony w całkowitej liczbie dodatniej oraz musi być mniejszy niż liczba wprowadzonych kostek razy ilość oczek na nich) \nWprowadź prawidłowy dystans - "))
#Część główna programu
    wynik = 0
    for nr_k in range(1, l_k+1):
        if type(l_k) == int:
            c_na_k = random.randint(1, oczka)
            
            if tryb == ("1" or "POKAZYWANIEZZGADYWANIEM" or "1."):
                if l_k == 1:
                    choice = int(input("Zgadnij ile oczek wypadło na kostce - "))
                    if choice == c_na_k:
                        print("Gratuluję, liczba oczek na kostce została zgadnięta! \nWybrano - {}\nLiczba oczek na kostce - {}\n".format(choice, c_na_k))
                        print("#"*80, end="")
                        print("Symulacja zakończona")
                    elif choice != c_na_k:
                        print("Liczba oczek nie została zgadnięta, na kostce było {} oczek".format(c_na_k))
                        print("Symulacja zakończona")
                elif l_k > 1:
                    choice = int(input("Zgadnij ile oczek wypadło na kostce nr {} - ".format(nr_k)))
                    if choice == c_na_k:
                        print("Gratulację!!! Kostka nr {} ma tyle oczek: {}\n".format(nr_k, choice))
                        wynik = wynik + 1
                        if l_k > nr_k:
                            print("Czy zgadniesz ile oczek ma następna kostka?")
                        elif l_k == nr_k:
                            if wynik == l_k:
                                print("$"*80, end="")
                                print("Wszystkie liczby zgadnięte - wygrana!!!")
                            else:
                                continue
                    elif choice != c_na_k:
                        print("Liczba oczek nie została zgadnięta, na kostce było {} oczek\nprzechodzimy więc do następnej kostki\n".format(c_na_k))

            elif tryb == ("2" or "POKAZANIEBEZZGADYWANIA" or "2."):
                if l_k == 1:
                    print("Rzucanie kostki...")
                    time.sleep(3)
                    print("Ilość oczek na kostce - {}\n".format(c_na_k))
                    print("#"*80, end="")
                    print("Symulacja zakończona")
                elif l_k > 1:
                    if nr_k != l_k:
                        print("Rzucanie kostki nr {}...".format(nr_k))
                        time.sleep(3)
                        print("Ilość wypadniętych oczek = {}\n".format(c_na_k))
                    elif nr_k == l_k:
                        print("Rzucanie kostki nr {}...".format(nr_k))
                        time.sleep(3)
                        print("Ilość wypadniętych oczek = {}".format(c_na_k))
                        time.sleep(1)
                        print("#"*80, end="")
                        print("Symulacja zakończona")
                        
            elif tryb == ("3" or "RZUTOWANIEKOSTKI" or "3."):
                print("#"*80, end="")
                if l_k == 1:
                    print("Rzucanie kostki...")
                elif l_k > 1:
                    print("Rzucanie {} kostki...".format(nr_k))
                time.sleep(3)
                if c_na_k > 4:
                    print("Na kostce widnieje {} oczek".format(c_na_k))
                elif c_na_k == 1:
                    print("Na kostce widnieje 1 oczko")
                else:
                    print("Na kostce widnieją {} oczka".format(c_na_k))
                print("\nZostało kostek - {}\n".format(l_k - nr_k))
                time.sleep(1.5)
                d_dl = d_dl - c_na_k
                
                if d_dl > 0:
                    if c_na_k > 4:
                        print("Obiekt poruszył się o {} pól".format(c_na_k))
                    elif c_na_k <= 3:
                        if c_na_k == 1:
                            print("Obiekt poruszył się o 1 pole")
                        else:
                            print("Obiekt poruszył się o {} pola".format(c_na_k))
                    if d_dl > 4:
                        print("Pozostało do przebycia {} pól".format(d_dl))
                    elif d_dl <= 3:
                        if d_dl == 1:
                            print("Pozostało do przebycia 1 pole")
                        else:
                            print("Pozostało do przebycia {} pola".format(d_dl))
                    if l_k == nr_k:
                        print("♥"*80, end="")
                        print("Przegrana")
                        break
                    elif l_k != nr_k:
                        continue
                        
                elif d_dl <= 0:
                    if c_na_k > 4:
                        if d_dl+c_na_k == 1:
                            print("Obiekt poruszył się o 1 pole")
                        else:
                            print("Obiekt poruszył się o {} pól".format(d_dl+c_na_k))
                    elif c_na_k <= 3:
                        if d_dl+c_na_k == 1:
                            print("Obiekt poruszył się o 1 pole")
                        else:
                            print("Obiekt poruszył się o {} pola".format(d_dl+c_na_k))
                    print("Ustawiony dystans został przebyty")
                    break
        else:
            print("O ja pierdole, rozjebało program")
#Tryb2: jeśli nie zgadnięto wszystkich oczek na kostkach
    if wynik != l_k and wynik != 0:
        print("Odgadłeś/aś ilości oczek na {} kostkach z {} kostek\nzabrakło do wygranej odgadnięcie {} wyniku/wyników".format(wynik, l_k, l_k - wynik))
        print("#"*80, end="")
        print("Przegrana")
#Czy wyjść z programu
    print("#"*80, end="")
    wybor = input("Czy chcesz zakończyć działanie programu: T/N - ")
    wybor = wybor.upper()
    print("♥"*80, end="")
    if wybor == "T":
        wyjscie = True
    elif wybor == "N":
        continue
    else:
        print("Kocham cię, kluseczko moja")
        wyjscie = True
#Zakończenie programu
input("Miłego dnia!\n")
