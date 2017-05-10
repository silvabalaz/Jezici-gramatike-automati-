from KA import *
from BKG import *
from PA import *
from RI import *


tests = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
tests |= {21, 22, 23, 24, 25, 26, 27, 28, 29,44}


if 1 in tests:  # page 34 figure 1.4  # page 36 figure 1.6
    M1 = KonačniAutomat.iz_tablice('''
           0  1
        q1 q1 q2
        q2 q3 q2 #
        q3 q2 q2   ''')
    print(*M1.izračunavanje('1101'))
    for riječ in '1','01','11','0101010101','100','0100','110000','0101000000':
        assert M1.prihvaća(riječ)
    for riječ in '0', '10', '101000':
        assert not M1.prihvaća(riječ)
    provjeri(M1, lambda ulaz: djeljiv(ulaz[::-1].find('1'), 2))

print("_________________________________________________")
if 2 in tests:  # page 37 example 1.7 figure 1.8
    M2 = KonačniAutomat.iz_tablice('''
           0  1
        q1 q1 q2
        q2 q1 q2 # ''')
    print(*M2.izračunavanje('1101'), *M2.izračunavanje('110'))
    provjeri(M2, lambda ulaz: ulaz.endswith('1'))

print("_________________________________________________")


if 3 in tests:  # page 38 example 1.9 figure 1.10
    M3 = KonačniAutomat.iz_tablice('''
           0  1
        q1 q1 q2 #
        q2 q1 q2   ''')
    provjeri(M3, lambda ulaz: ulaz == ε or ulaz.endswith('0'))

print("_________________________________________________")

if 4 in tests:  # page 38 example 1.11 figure 1.12
    M4 = KonačniAutomat.iz_tablice('''
           a  b
        s  q1 r1
        q1 q1 q2 #
        q2 q1 q2
        r1 r2 r1 #
        r2 r2 r1    ''')
    for riječ in 'a', 'b', 'aa', 'bb', 'bab':
        assert M4.prihvaća(riječ)
    for riječ in 'ab', 'ba', 'bbba':
        assert not M4.prihvaća(riječ)
    provjeri(M4, lambda ulaz: ulaz and ulaz[0] == ulaz[~0])

print("_________________________________________________")

if 5 in tests:  # page 39 example 1.13 figure 1.14
    M5 = KonačniAutomat.iz_tablice('''
           R  0  1  2
        q0 q0 q0 q1 q2 #
        q1 q0 q1 q2 q0
        q2 q0 q2 q0 q1   ''')
    print(*M5.izračunavanje('10R22R012'))  # page 41 example 1.17

    def M5_spec(ulaz):
        zbroj = 0
        for znak in ulaz:
            if znak == 'R': zbroj = 0
            else: zbroj += int(znak)
        return djeljiv(zbroj, 3)
    provjeri(M5, M5_spec)

if 6 in tests:  # page 40 example 1.15
    for i in range(1, 10):
        def Ai(ulaz):
            zbroj = 0
            for znak in ulaz:
                if znak == '<RESET>': zbroj = 0
                else: zbroj += int(znak)
            return djeljiv(zbroj, i)
        Qi = set(range(i))
        Σ = {'<RESET>', 0, 1, 2}
        δi = {}
        for j in Qi:
            δi[j, '<RESET>'] = 0
            δi[j, 0] = j
            δi[j, 1] = (j + 1) % i
            δi[j, 2] = (j + 2) % i
        Bi = KonačniAutomat.iz_komponenti(Qi, Σ, δi, 0, {0})
        provjeri(Bi, Ai)
        print(i, end=' OK  ')

print("_________________________________________________")

if 44 in tests:  # page 105 example 2.4
    G4 = BeskontekstnaGramatika.iz_strelica('''
        E -> E + T | T
        T -> T * F | F
        F -> ( E ) | a
    ''')
    print("desnolinearna",BeskontekstnaGramatika.desnolinearna(G4))
    print("validan",BeskontekstnaGramatika.validan(G4, 'a+a*a'))
    print("Chomsky",BeskontekstnaGramatika.Chomskyjeva(G4))
    #print("simboli",BeskontekstnaGramatika.simboli(G4))
    print("G4", G4)
    print("komponente",BeskontekstnaGramatika.komponente(G4))
    print(G4.CYK('a+a*a'), G4.CYK('(a+a)*a'))
    #print(assert G4.validan('E E+T T+T F+T a+T a+T*F a+F*F a+a*F a+a*a'.split()))
    #print(assert G4.validan('''E T T*F T*a F*a (E)*a (E+T)*a(T+T)*a (T+F)*a (F+F)*a (a+F)*a (a+a)*a'''.split()))
    print("_________________________________________________")

    print(G4.CYK('a+a'),G4.CYK('((a))'))