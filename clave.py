import requests
import string
import random
import pandas as pd

URL = "https://jsonplaceholder.typicode.com/users"
data = requests.get(URL);

data = data.json()
new_data = []


for x in data:

    n = random.randint(8, 16)
    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    numeros = list(string.digits)
    simbolos = ['*','/','-','+','.',',','?','=']
    password = ''.join(random.choices(mayus + numeros + minus + simbolos, k=n)) 
    new_data.append([x['name'], x['username'], password])


df = pd.DataFrame(new_data, columns=['name', 'username', 'password'])
df.to_csv("jhei_test.csv", sep=';')