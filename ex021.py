from pygame import mixer #importa o mixer da lib pygame

mixer.init() #inicia a função de reprodução de áudio

mixer.music.load('audio.mp3') #seleciona a música dentro da pasta do projeto
mixer.music.play() #inicia a música

stop = input('Digite algo para parar a reprodução: ') #digitar qualquer coisa + enter pra parar a reprodução