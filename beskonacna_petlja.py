from util import *
import random, string
from random import randint	
from KA import *


def beskonačna_petlja(automat):
		"""beskonačna_petlja ako je unos neka riječ abecede automata"""
		Q, Σ, δ, q0, F = automat.komponente	

		duljinaRiječi = len(list(Σ))*10

		def random_string(duljina):
		   return ''.join(random.choice(list(Σ)) for i in range(duljina))
		
		ulaz = random_string(randint(1,duljinaRiječi))
		#ulaz = '11111111111111111111111111111111111111'
		print("e-ciklus", NedeterminističkiKonačniAutomat.ciklus(automat,q0))
		def prihvaća(ulaz):
			"""Prihvaća li automat zadani ulaz?"""

			δ = automat.funkcija_prijelaza
			moguća = ε_ljuska(δ, {automat.početno})	
			a = NedeterminističkiKonačniAutomat.ciklus(automat,automat.početno)
			#counter = 0
			
		'''	while True:
				for znak in ulaz: 
					moguća = set(ε_ljuska(δ, dohvatljiva(δ, moguća, znak)))
					counter +=1
					if(len(moguća) == 0):return None
					if(counter >= 10):return ulaz #moguća beskonačna petlja
				return None
		'''
		return prihvaća(ulaz)


#[3] Implementirajte funkciju beskonačna_petlja, koja prima nedeterministički konačni automat i vraća (neku) riječ njegove abecede takvu da se automat može zavrtjeti u beskonačnoj petlji čitajući tu riječ. Ako takva riječ ne postoji, funkcija vraća None.

C = NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q1'), ('q1', '0', 'q1' ),('q1', '1', 'q1' )}, 'q1', {'q2'})
D =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q1', '0', 'q2' ),('q1', '1', 'q2' )}, 'q1', {'q2'})
E =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2','q3','q4'},
        {'0', '1'}, {('q1','0','q2'), ('q1','0','q3'),('q2',ε,'q4'), ('q4',ε,'q2')}, 'q1', {'q3'})

#beskonačna_petlja(E)
#beskonačna_petlja(C)
#beskonačna_petlja(D)

