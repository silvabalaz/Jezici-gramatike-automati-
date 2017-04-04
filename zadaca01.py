from KA import *
from RI import *

#Sipser strana: 85. zadatak 1.9a (strana 84., zadatak 1.6. b) i m))
M1 = KonačniAutomat.iz_tablice('''
       0  1
    q0 q0 q1
    q1 q1 q2 
    q2 q2 q3   
	q3 q3 q3 # ''')
print(*M1.izračunavanje('1101'))
for riječ in '0101010101','111','01011','110011','0101000111':
    assert M1.prihvaća(riječ)
for riječ in '0', '10', '101000':
    assert not M1.prihvaća(riječ)

M2 = KonačniAutomat.iz_tablice('''
       0  1
    q0 q0 q0 ''')
for riječ in '0', '10', '101000':
    assert not M2.prihvaća(riječ)


N1 = NedeterminističkiKonačniAutomat.iz_konačnog_automata(M1)

N2 = NedeterminističkiKonačniAutomat.iz_konačnog_automata(M2)

N12konkatenacija = N1.konkatenacija(N2)

#Sipser strana: 85. zadatak 1.9b (strana 84., zadatak 1.6. g) i i))

M3 = KonačniAutomat.iz_tablice('''
       0  1
    q0 q1 q1 #
    q1 q2 q2 #
    q2 q3 q3 #  
	q3 q4 q4 # 
	q4 q5 q5 # 
	q5 q6 q6 #
	q6 q6 q6 ''')
print(*M3.izračunavanje('1101'))
for riječ in '01010','111','01011','1100','01':
    assert M3.prihvaća(riječ)
for riječ in '011111000000', '10111111', '101000':
    assert not M3.prihvaća(riječ)

M4 = KonačniAutomat.iz_tablice('''
       0  1
    q0 q2 q1 #
	q1 q0 q0 #
	q2 q2 q2 ''')

for riječ in '0', '010', '11100000':
    assert not M4.prihvaća(riječ)


N3 = NedeterminističkiKonačniAutomat.iz_konačnog_automata(M3)
N4 = NedeterminističkiKonačniAutomat.iz_konačnog_automata(M4)

N34konkatenacija = N3.konkatenacija(N4)

#Sipser strana: 85. zadatak 1.10b (strana 84., zadatak 1.6. b))

N1zvijezda = NedeterminističkiKonačniAutomat.zvijezda(N1)

#Sipser strana: 85. zadatak 1.10b (strana 84., zadatak 1.6. j))

M5 = KonačniAutomat.iz_tablice('''
       0  1
    q0 q1 q3 
    q1 q2 q4 
    q2 q2 q5 #  
	q3 q4 q6 
	q4 q5 q6  
	q5 q5 q6 #
	q6 q6 q6 ''')
print(*M3.izračunavanje('0001'))
for riječ in '01000','100','00001','10000','00000':
    assert M3.prihvaća(riječ)
for riječ in '011111000000', '10111111', '101000':
    assert not M3.prihvaća(riječ)

N5 = NedeterminističkiKonačniAutomat.iz_konačnog_automata(M5)
N5zvijezda = NedeterminističkiKonačniAutomat.zvijezda(N5)

#Sipser strana: 85. zadatak 1.10b (strana 84., zadatak 1.6. m))

N2zvijezda = NedeterminističkiKonačniAutomat.zvijezda(N2)


#[1] Implementirajte analognu funkciju funkciji prirodni iz KA.py, za nedeterminističke konačne automate.

A = NedeterminističkiKonačniAutomat.prirodni(N5)

#[2] Implementirajte funkciju ε_ciklus, koja prima nedeterministički konačni automat i njegovo stanje r1, te vraća postoje li njegova stanja r2, ..., rk takva da je r1 povezan s r2, r2 s r3, …, rk s r1, ε-prijelazima. Moguće je i k=1!


N = NedeterminističkiKonačniAutomat.iz_komponenti({'q1', 'q2', 'q3', 'q4'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q2', ε, 'q3'), ('q3', ε, 'q4'),
                     ('q2', '0', 'q3'), ('q2', '1', 'q3'), ('q3', ε, 'q4'),
                     ('q4', ε, 'q1'), ('q1',ε,'q1')}, 'q1', {'q1'})
B = NedeterminističkiKonačniAutomat.iz_komponenti({'q1', 'q2', 'q3'},{'0', '1'}, {('q1', ε, 'q1'), ('q2', '0', 'q3'), ('q2', '1', 'q3') }, 'q1', {'q1'})


NedeterminističkiKonačniAutomat.ciklus(N,'q3')
NedeterminističkiKonačniAutomat.ciklus(B,'q1')

#[3] Implementirajte funkciju beskonačna_petlja, koja prima nedeterministički konačni automat i vraća (neku) riječ njegove abecede takvu da se automat može zavrtjeti u beskonačnoj petlji čitajući tu riječ. Ako takva riječ ne postoji, funkcija vraća None.

C = NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q1'), ('q1', '0', 'q1' ),('q1', '1', 'q1' )}, 'q1', {'q2'})
D =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q1', '0', 'q2' ),('q1', '1', 'q2' )}, 'q1', {'q2'})
E =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2','q3','q4'},
        {'0', '1'}, {('q1','0','q2'), ('q1','0','q3'),('q2',ε,'q4'), ('q4',ε,'q2')}, 'q1', {'q3'})
#NedeterminističkiKonačniAutomat.beskonačna_petlja(C)
#NedeterminističkiKonačniAutomat.beskonačna_petlja(D)
print("BESKONAČNA PETLJA")
print(NedeterminističkiKonačniAutomat.beskonačna_petlja(E))

