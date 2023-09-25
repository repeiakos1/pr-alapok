#szorgalmi001
'''Csinálj egy olyan programot, ahol ha be írsz egy számot, és ha kisebb 100-nál akkor azt írja ki hogy: "Ez a szám nagyobb mint 100"
ha 200-nál nagyobbat írsz akkor írja azt hogy : A szám nagyobb mint 200, ha 300-nál nagyobb szám akkor írja azt hogy: "A szám nagyobb mint 300-nál.
'''


szam = int(input('Írj be egy számot: '))

if szam > 100:
    print('A szám nagyobb mint 100')
elif szam < 100:
    print('A szám kisebb mint 100')
elif szam > 200:
    print('A szám nagyobb mint 200')
elif szam > 300:
    print('A szám nagyobb mint 300')
elif szam == 100:
    print('A szám pont 100')