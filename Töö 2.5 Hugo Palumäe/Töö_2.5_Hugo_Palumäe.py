print("Ruutvõrrandi lahendamine") 
# lisasin juttumärgi
a=float(input("Sisesta a => "))
b=float(input("Sisesta b => "))
# lisasin sulu
c=input("Sisesta c => ")
D=b*b-4*a*c
if D>0:
    x1=(-b+D**0.5)/2*a
    x2=(-b-D**0.5)/(2*a)
    print("Kaks lahendit:", x1, x2)
else:
# lisasin kooloni
 if D==0:
# lisasin =
    x=-b/(2*a)
    print("Üks lahend:", x)
else:
print("Reaalarvulised lahendid puuduvad")
print()
print("Palga arvutamine")
tunnid=float(input("Sisesta töötunnid nädalas => "))
tunnitasu=float(input("Sisesta tunnitasu (€) => "))
if tunnid<0 and tunnid>168:
    print("Vigane tundide arv")
elif tunnid<=40:
    palk=tunnid*tunnitasu
    print("Nädalapalk:", palk, "€")
else:
    palk=40*tunnitasu+(tunnid-40)*tunnitasu*1,5
    print("Nädalapalk koos ületundidega:", palk, "€")
print()
print("Parkimise hind")
tunnid=int(input("Sisesta parkimise aeg tundides => "))
if tunnid<=0:
# muutsin < asukohta
    print("Vigane aeg")
elif tunnid>=3:
    print("Hind: 5 €")
elif tunnid>=8:
    print("Hind: 10 € (päevapilet)")
else:
# lisasin kooloni
    print("Hind: 2 €") 
# lisasin sulu