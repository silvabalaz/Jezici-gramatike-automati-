import random
import string
from random import randint		
Σ=set()
Σ.add('0')
Σ.add('1')
print("lista(Σ)",list(Σ))
duljinaRiječi = len(list(Σ))
def random_string(length):
   return ''.join(random.choice(list(Σ)) for i in range(length))		
print(random_string(randint(1,duljinaRiječi)))

print("duljinaRiječi:", duljinaRiječi)
#print("ulaz:", ulaz)
