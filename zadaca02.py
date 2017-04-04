from KA import *
from RI import *


#Implementirajte sučelje prema lemi o napuhavanju za regularne jezike: funkciju koja prima KonačniAutomat (ili NedeterminističkiKonačniAutomat ili RegularanIzraz), te pita korisnika za riječ duljine bar p (kaže mu koliko je p). Nakon što korisnik upiše riječ, funkcija je rastavlja na riječi x, y i z iz leme o napuhavanju (ako postoje), te pita korisnika za broj i i ispisuje varijantu x y^i z. Za interakciju koristite funkciju input. 

C = NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q1'), ('q1', '0', 'q1' ),('q1', '1', 'q1' )}, 'q1', {'q2'})
D =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q1', '0', 'q2' ),('q1', '1', 'q2' )}, 'q1', {'q2'})

E = NedeterminističkiKonačniAutomat.iz_komponenti({'q1', 'q2', 'q3', 'q4'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q2', ε, 'q3'), ('q3', ε, 'q4'),
                     ('q2', '0', 'q3'), ('q2', '1', 'q3'), ('q3', ε, 'q4'),
                     ('q4', ε, 'q1'), ('q1',ε,'q1')}, 'q1', {'q1'})

print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(E))

print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(C))

print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(D))
