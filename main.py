import pandas as pd
from classes.Person import Person
from mapas import mapa01

person = Person('Felipe' , 12);

df = pd.read_csv ('./mapas/mapa_01.csv')
print (df)

print(person)