#szorgalmi002
'''
Futtassuk így a programot. Így akár 100-nál nagyobb, akár kisebb értéket írunk be, mindig kapunk valamilyen eredményt, viszont ha pont 100-at írunk be, akkor azt kapjuk hogy A szám kisebb mint 100, ami egyáltalán nem igaz, ezért jó lenne ezt az esetet is kezelni.
'''


szam = int(input('Írj be egy számot: '))
if szam > 100:
    print('A szám nagyobb mint 100')
elif szam == 100:
    print('A szám pont 100')
else:
    print('A szám kisebb mint 100') 