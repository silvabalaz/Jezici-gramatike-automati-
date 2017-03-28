# Interpretacija programa
https://web.math.pmf.unizg.hr/nastava/ip/

### 1.9 i 1.10

**Konkatenacija** nedeterminističkog automata N1 (prihvaća riječi čija je duljina najviše 5) i N2 (svaka neparna pozicija u riječi je znak '1'). Najprije zadamo automate kao konačne,  metodom *.iz_konačnog_automata()* konstruiramo ekvivalentni nedeterministički k. automat. Sada konkatenaciju N1 i N2 dobijemo metodom *N1.konkatenacija(N2)*, koja vraća novi automat koji ima ε-prijelaze sa završnih stanja (koja više nisu završna) automata N1 na početno stanje od N2, a završno stanje novog automata su završna stanja automata N2.
Isto tako za automate N3 (prihvaća riječi koje sadrže bar tri jedinice) i N4(prepoznaje prazan jezik)

**Kleenijeva zvijezda** nedeterminističkog automata N1 koji metodom *.zvijezda()* nad N1 konstruira novi automat N1zvijezda, koji ima novo početno stanje (koje je ujedno jedno od završnih),ε-prijelazom povezano na početno stanje od N1 i povezano ε-prijelazima sa završnih stanja od N1 na početno stanje od N1. Završna stanja N1zvijezda su: novo početno stanje i završna stanja od N1.

### 1. Analogna funkcija funkciji *prirodni* iz KA.py, za nedeterminističke konačne automate.

Skup prijelaza više nije mapa *(polaznoStanje, znak): dolaznoStanje* već skup uređenih trojki *(polaznoStanje, znak, dolaznoStanje)*.

### 2. Funkcija *ε_ciklus*, koja prima nedeterministički konačni automat i njegovo stanje r1, te vraća postoje li njegova stanja r2, ..., rk takva da je r1 povezan s r2, r2 s r3, …, rk s r1, ε-prijelazima. Moguće je i k=1.

Stanja su prirodni brojevi.
Iz skupa prijalaza (uređenih trojki prirodnih brojeva) pospremljenih iz skupa u listu, izdvojimo one trojke koje imaju ε-prijalaze u rječnik prirodnih brojeva koje za key (polaznoStanje) dobiva vrijednost listu mogući dolaznihStanja.

Metoda *postoji_ciklus()*
Inicijaliziramo rječnik *boja* koji označava je li čvor (stanje) bilo posjećeno , bojama:  *bijela,siva,crna* .
Posjećujemo sva stanja, koristimo rekurziju *dfs_posjeti()*

Metoda *dfs_posjeti()* Svaki puta kada posjetimo stanje odznačimo ga *sivo* te označava da je na našem trenutnom putu (mogućeg ciklusa).
Posjećujemo susjede od stanja, koji su *bijeli* (ta stanja, susjedi , nisu još bili posjećeni).
Ako posjetimo susjeda koji je *sivi* tada smo dobili ciklus. Inače, ako takav susjed ne postoji, ciklus ne postoji.
Nakon što smo posjetili sve susjede trenutnog stanja, označimo ga *crnim*.


### 3. Funkciju *beskonačna_petlja*, koja prima nedeterministički konačni automat i vraća (neku) riječ njegove abecede takvu da se automat može zavrtjeti u beskonačnoj petlji čitajući tu riječ. Ako takva riječ ne postoji, funkcija vraća None.
**beskonačna petlja: automat nije u završnom stanju (prihvaćanja), nije ni u ne završnom stanju(odbijanja),već u petlji jer izračunavanje nikada ne staje**

Metoda *random_string(duljina)* nasumično generira riječ duljine koju prima kao parametar (koji smo također nasumično odabrali metodom *randomint()* kao neki proizvoljan broj od 1 do duljinaRiječi) 

Metoda *prihvaća(ulaz)* vraća riječ koja je u *ulaz* ako smo u beskonačnoj petlji (varijablom counter označim koja je granica za beskonačnost, npr. 10). 
Ako pročitamo riječ u manji broj koraka i imamo *moguća* stanja prijelaza za svaki znak riječi, to znači da smo na kraju riječi ili u stanju prihvaćanja ili odbijanja, te funkcija vraća None. 
