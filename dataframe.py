import pandas as pd
import numpy as np 

class Assistant():
    def __init__(self):
        print("======== BEM VINDO AO CALENDÁRIO ========")
        print('')
        self.inputs()

    def inputs(self):
        print('Inserir data:')
        self.data = input()
        print('Inserir horário:')
        self.horas = input()
        print('Iserir nome do evento:')
        self.nome = input()
        self.inserir_na_tabela()


    def inserir_na_tabela(self):
        df = pd.read_csv('leitura.txt')
        df = df.append({"Data" : self.data, "Horas" : self.horas, "Nome" : self.nome}, ignore_index=True)
        df.to_csv("leitura.txt", header=True, index=False, sep=",")





assistente = Assistant()