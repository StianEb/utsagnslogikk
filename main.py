from utsagnsLogikk import *

#Utsagnsvariabler
p = Atom('P')
q = Atom('Q')
r = Atom('R')

#Formler
formel1 = (p & q)
formel2 = ((p > q) > (-p | q))
formel3 = (((p | -r) & (-p > q) & (q > r)))

#Utsagnsvariabler
print(f"Utsagnsvariabler i formel1: {formel1.utsagnsvariabler()}")
print(f"Utsagnsvariabler i formel2: {formel2.utsagnsvariabler()}")
print(f"Utsagnsvariabler i formel3: {formel3.utsagnsvariabler()}")

#Sannhetsverditabeller
print("\nFormel 1:", formel1.sannhetsverditabell())
print("\nFormel 2:", formel2.sannhetsverditabell())
print("\nFormel 3:", formel3.sannhetsverditabell())

#Sannhetsverdi ved spesifikk valuasjon
print("Formel 3 sann ved p=1, q=1, r=0?", formel3.sannVedValuasjon({p, q}))
print("Formel 3 sann ved p=1, q=0, r=0?", formel3.sannVedValuasjon({p}))

#Lag en formel
lagFormel = -q > -p
print('\nFormel fra "Lag en formel":', lagFormel.sannhetsverditabell())

#Top og bot
top = Top()
bot = Bot()
formel4 = (top > p) | (q > bot)
print("\nTop og bot:", formel4.sannhetsverditabell())

#Gjensidig implikasjon
formel5 = (p > q) ^ (p & q)
print("\nGjensidig implikasjon:", formel5.sannhetsverditabell())

#Tautologi
print("\nTautologi:")
print(f"Formel 2: {str(formel2)} tautologi? {formel2.erTautologi()}")
print(f"Formel 5: {str(formel5)} tautologi? {formel5.erTautologi()}")

#Kontradiksjon
formel6 = bot
print("\nKontradiksjon:")
print(f"Formel 2: {str(formel2)} kontradiksjon? {formel2.erKontradiksjon()}")
print(f"Formel 6: {str(formel6)} kontradiksjon? {formel6.erKontradiksjon()}")

#Ekvivalens
print("\nEkvivalens:")
print(f"Formel 2: {str(formel2)} ekvivalent med Formel 4: {str(formel4)}?",
      formel2 % formel4)
print(f"Formel 2: {str(formel2)} ekvivalent med Top: {str(top)}?", formel2 % top)
