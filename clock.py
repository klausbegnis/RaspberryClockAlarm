from datetime import datetime, date
from time import sleep
import RPi.GPIO as GPIO
import vlc
import pandas as pd
from gtts import gTTS
from subprocess import Popen


class Clock():
    def __init__(self, dataframe):
        self.dataframe = dataframe
        
        data = list(df.iloc[:, 0])
        hora = list(df.iloc[:, 1])
        self.nomes = list(df.iloc[:, 2])
        self.tipos = list(df.iloc[:, 3])
        self.wkd = list(df.iloc[:, 4])
        despertador = []
        despertador_semanal = []
        for i in range(len(hora)):
            despertador.append([data[i], hora[i]])
        for i in range(len(hora)):  
            despertador_semanal.append([hora[i], self.wkd[i]])
        
        self.despertar = despertador
        self.despertar_s = despertador_semanal
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(11, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        GPIO.setup(15, GPIO.OUT)
        GPIO.setup(19, GPIO.OUT)
        
    def tts_music(self, nome, tipo):
        tts = gTTS(nome, lang="pt-br")
        tts.save("/home/pi/CLOCK/Musics/tts.mp3")
        self.luzes_led(tipo)
        args = ["omxplayer", "/home/pi/CLOCK/Musics/tts.mp3"]
        Popen(args)
        sleep(10)
        
    def get_current_time(self):
        self.time_check = datetime.now()
        hour = self.time_check.strftime("%H:%M:%S")
        date1 = self.time_check.strftime("%d/%m/%y")
        self.current_time = [date1, hour]
        weekdate = date.today().weekday()
        self.weekly = [hour, weekdate]

    def despertador(self):
        if self.current_time in self.despertar:
            index = self.despertar.index(self.current_time)
            nome = self.nomes[index]
            tipo = self.tipos[index]
            self.tts_music(nome, tipo)
            self.luzes_led(tipo)
            return "DESPERTADO"
        if self.weekly in self.despertar_s:
            index = self.despertar_s.index(self.weekly)
            nome = self.nomes[index]
            tipo = self.tipos[index]
            self.tts_music(nome, tipo)
            self.luzes_led(tipo)
            return "DESPERTADO"
        else:
            return "DESLIGADO"
    
    def verde_on(self):
        GPIO.output(11, GPIO.HIGH)
        
    def verde_off(self):
        GPIO.output(11, GPIO.LOW)
    
    def amarelo_on(self):
        GPIO.output(13, GPIO.HIGH)
        
    def amarelo_off(self):
        GPIO.output(13, GPIO.LOW)
        
    def branco_on(self):
        GPIO.output(15, GPIO.HIGH)
        
    def branco_off(self):
        GPIO.output(15, GPIO.LOW)
        
    def luzes_led(self, tipo):
        tipo_acorda = tipo
        GPIO.output(19, GPIO.LOW)
        if tipo_acorda == "acordar":
            player = vlc.MediaPlayer("file:///home/pi/CLOCK/Musics/LOFI CAT - Windows 95.mp3")
        else:
            player = vlc.MediaPlayer("file:///home/pi/CLOCK/Musics/wii.mp3")
        player.play()
        i = 0
        while i < 25:
            self.verde_on()
            sleep(0.10)
            self.verde_off()
            self.amarelo_on()
            sleep(0.10)
            self.amarelo_off()
            self.branco_on()
            sleep(0.10)
            self.branco_off()
            i+=1
        b = 0
        for b in range(8):
            if (b % 2) == 0:
                self.verde_on()
                self.amarelo_on()
                self.branco_on()
                sleep(0.5)
            else:
                self.verde_off()
                self.amarelo_off()
                self.branco_off()
                sleep(0.5)
            b+=1
        GPIO.output(19, GPIO.HIGH)
        player.stop()
        
if __name__ == '__main__':
    while True:
        df = pd.read_csv('/home/pi/CLOCK/leitura.txt', sep=",")
        clock = Clock(df)
        clock.get_current_time()
        state = clock.despertador()
        if state == "DESLIGADO":
            continue
        else:
            continue       
