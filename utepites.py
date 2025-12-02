import sys

bemenet = sys.stdin.readline  # Gyorsabb beolvasás nagy adathalmaznál

def keres(x):
    # Megkeressük a gyökér elemet (útkompresszióval)
    if szulok[x] != x:
        szulok[x] = keres(szulok[x])
    return szulok[x]

def osszekapcsol(a, b):
    # Összekapcsoljuk a két komponenst
    belsoa, belsob = keres(a), keres(b)
    if belsoa != belsob:
        szulok[belsob] = belsoa  # belsob gyökerét az belsoa gyökeréhez kapcsoljuk

def kereso():
    n, m = map(int, bemenet().split())

    # Kezdetben minden város saját komponens
    global szulok
    szulok = [i for i in range(n + 1)]

    # Beolvassuk az utakat és összekapcsoljuk a városokat
    for _ in range(m):
        a, b = map(int, bemenet().split())
        osszekapcsol(a, b)

    # Komponensek gyűjtése: minden gyökérhez tartozó városok
    elemek = {}
    for i in range(1, n + 1):
        kezdopont = keres(i)
        if kezdopont not in elemek:
            elemek[kezdopont] = []
        elemek[kezdopont].append(i)

    # Rendezés minden komponensben
    komponensek = [sorted(varosok) for varosok in elemek.values()]

    # Új utak száma = komponensek száma - 1
    k = len(komponensek) - 1
    print(k)

    # Példa szerint: az első komponens legnagyobb eleme és a következő legkisebb eleme
    for i in range(k):
        print(komponensek[i][-1], komponensek[i + 1][0])

if __name__ == '__main__':
    kereso()
