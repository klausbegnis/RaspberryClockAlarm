import pandas as pd 

df = pd.read_csv('/home/pi/Desktop/CLOCK/leitura.txt')

hora = list(df.iloc[:, 1])
data = list(df.iloc[:, 0])
despertador = []
for i in range(len(hora)):
    despertador.append([data[i], hora[i]])

if [1,2] in despertador:
    print("YES")

print(despertador)