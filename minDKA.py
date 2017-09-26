    def BrojRazlicitihKlasa(tempNovi):
        lista = []
        for vrijednost in tempNovi.values():
            lista.append(vrijednost)
        skup = set(lista)
        brojRazlicitihKlasa = len(skup)
        return brojRazlicitihKlasa

    def usporedi(stara,nova):
        # stara podjela i nova imaju ista stanja samo sa razlicitim brKlasa ako je doslo do podjele
        for stanje,brojKlase in stara.items():
            if nova[stanje] != brojKlase:
                return True #razlizcit brKlase za neko stanje tj. true    
        return False #sva stanja u oba rjecnika imaju iste brKlasa, jednaki rjecnici, tj. False, nisu razliciti

    def podijeli(trenutnaKlasa,automat,brKlase,prethodnaPodjela,najveći):
       
        Q, Σ, δ, q0, F = automat.komponente
        trenutnaKlasa.sort()
        novaKlasa = trenutnaKlasa
        fiksnoStanje = trenutnaKlasa[0]
        def odredi(stanje):
            for znak in Σ:
                if prethodnaPodjela[δ[stanje,znak]] !=  prethodnaPodjela[δ[fiksnoStanje,znak]]:
                    return True
            return False

        trenutnaKlasa = [stanje for stanje in trenutnaKlasa if not odredi(stanje)]
        novaKlasa = [stanje for stanje in novaKlasa if odredi(stanje)]
        trenutniRječnik = {}
       
        for stanje in trenutnaKlasa:
            trenutniRječnik[stanje] = brKlase
        for stanje in novaKlasa:
            trenutniRječnik[stanje] = najveći + 1
        najveći += 1
        return trenutniRječnik,najveći

    def NovaPodjela(prethodnaPodjela,automat):
        trenutnaKlasa = []
        trenutniRječnik = {}
        najveći = 2
        izbroji = KonačniAutomat.BrojRazlicitihKlasa(prethodnaPodjela)
        for i in range(1,izbroji + 1):
            trenutnaKlasa = []
            for stanje,brKlase in prethodnaPodjela.items():
                if brKlase == i:
                    trenutnaKlasa.append(stanje)
            rj, najveći = KonačniAutomat.podijeli(trenutnaKlasa,automat,i,prethodnaPodjela,najveći)
            trenutniRječnik.update(rj)
    

        return trenutniRječnik  #to treba biti rječnik sa svim stanjima kao u sortiranomrječniku samo sa svojim br.klasa

    def PromjenaNazivaStanja(rječnik, automat, najveći):
        Q, Σ, δ, q0, F = automat.komponente
        lista= []
        reverzni = {}
        for stanje, brKlase in rječnik.items():
            reverzni.setdefault(brKlase, set()).add(stanje)

        for klasa in reverzni.values():
            if len(klasa) > 1 :
                temp = klasa.pop()
                if q0 in klasa:
                    q0 = temp
                for el in klasa:
                    lista.append(el)
                #tu treba deltu funkciju odmah mjenjat za stanja u klasi u delta,promijenit u temp naziv  
                klasa.clear()
                klasa.add(temp)

        for stanje in lista:
            Q.remove(stanje)
            if stanje in F:
                F.remove(stanje)
        #delta
        d = {}
        for key,stanje in δ.items():
            izlazno = key
            ulazno = δ[key]
            promjena = 0
            if key[0] in lista:
                izlazno = (temp,key[1]); 
                promjena = 1
            if δ[key] in lista: 
                ulazno = temp
                promjena = 1
            if promjena == 1:
                for k,v in δ.items():
                    if k[0] not in lista and v not in lista:
                        d.update({k : v})
                        d[izlazno] = ulazno
                    
        δ = d
        return KonačniAutomat.iz_komponenti(Q, Σ, δ, q0, F )

    def minDKA(automat):
        "DKA koji prihvaća isti regularan jezik kao i zadani DKA"
        #jednostavni dict koji preslikava stanja u prirodne brojeve
        #tako da ista vrijednost u koju su preslikana znači istu klasu kojoj pripadaju
        Q, Σ, δ, q0, F = automat.komponente
        # na početku je prazan
        rječnik = {}
        #podjela na temelju uvjeta podudarnosti,skupa stanja Q
        #rječnik ima dvije vrijednosti (prirodne brojeve 1 i 2)
        #to su dvije klase, F i F-komplement
        for stanje in Q:
            if stanje in F:
                rječnik[stanje] = 2
            else: 
                rječnik[stanje] = 1

        automatRadi = 1
        najveći = 2 #najveći prirodan broj do kojeg ide oznaka u trenutnoj podjeli, prva je za F i F - komplement
        izbroji = 2 #broj različitih klasa u trenutnoj podjeli
        novaPodjela = {}
        sortiraniRječnik = OrderedDict(sorted(rječnik.items())) #po nazivima stanja p1,p2,...
        novaPodjela,prethodnaPodjela = {}, {}
        while automatRadi:
            if len(novaPodjela) == 0 :
                novaPodjela = KonačniAutomat.NovaPodjela(sortiraniRječnik,automat)
                prethodnaPodjela = sortiraniRječnik
            else:
                jeLiBilaPodjela = KonačniAutomat.usporedi(prethodnaPodjela, novaPodjela) #True, bilo je podjele, djeli dalje
                if jeLiBilaPodjela:
                    prethodnaPodjela = novaPodjela
                    #izbroji = KonačniAutomat.BrojRazlicitihKlasa(novaPodjela)
                    novaPodjela = KonačniAutomat.NovaPodjela(prethodnaPodjela,automat)
                else: 
                    podjelaGotova = 1
                    automatRadi = 0
                    break
        novaPodjelaSortirana = OrderedDict(sorted(novaPodjela.items()))
        najveći = KonačniAutomat.BrojRazlicitihKlasa(novaPodjela)
        mindka = KonačniAutomat.PromjenaNazivaStanja(novaPodjela,automat,najveći)
        return mindka



if __name__ == '__main__':

    M1 = KonačniAutomat.iz_tablice('''
           0  1
        p1 p6 p3
        p2 p7 p3 
        p3 p1 p5 
        p4 p4 p6
        p5 p7 p3 #
        p6 p4 p1 # 
        p7 p4 p2 #
          ''')
   # print(*M1.izračunavanje('1101'))
   # for riječ in '1','01','11','0101010101','100','0100','110000','0101000000':
        #assert M1.prihvaća(riječ)
   # for riječ in '0', '10', '101000':
        #assert not M1.prihvaća(riječ)
    #provjeri(M1, lambda ulaz: djeljiv(ulaz[::-1].find('1'), 2))
    print(KonačniAutomat.minDKA(M1))