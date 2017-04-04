from util import *
import random, string
from random import randint		
from KA  import *

def lema_o_napuhavanju(automat):
		
	p = input("Unesi broj p: ")
	print("Unešen broj je:", p)	
	riječ = input("Unesi riječ: ")
	print("Unesena riječ je:", riječ)	

	def partition(lst):
		division = len(lst)/3
		return [lst[round(division * i):round(division * (i + 1))] for i in range(3)]
	x,y,z = partition(riječ)

	def konkatenacija_riječi(riječ, koliko):
		lista=[]			
		lista.extend([riječ for i in range(int(koliko))])
		riječNova =''.join(lista)
		return riječNova 

	i = input("Unesi broj i: ")
	print("Unešen broj je:", i)	

	yi = konkatenacija_riječi(y,i)
	print("y^i", yi)
	riječ= []
	riječ.append(x)
	riječ.append(yi)
	riječ.append(z)
	print("riječ", riječ)
	napuhanaRiječ = ''.join(riječ)
	print("napuhanaRiječ", napuhanaRiječ)
	
		
	return automat.prihvaća(napuhanaRiječ)

C = NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q1'), ('q1', '0', 'q1' ),('q1', '1', 'q1' )}, 'q1', {'q2'})
D =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2'},
        {'0', '1'}, {('q1', ε, 'q2'), ('q1', '0', 'q2' ),('q1', '1', 'q2' )}, 'q1', {'q2'})
E =  NedeterminističkiKonačniAutomat.iz_komponenti({'q1','q2','q3','q4'},
        {'0', '1'}, {('q1','0','q2'), ('q1','0','q3'),('q2',ε,'q4'), ('q4',ε,'q2')}, 'q1', {'q3'})

print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(E))
print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(C))
print(NedeterminističkiKonačniAutomat.lema_o_napuhavanju(D))
