from pygame import mixer #importa o mixer da lib pygame

mixer.init() #inicia a função de reprodução de áudio

mixer.music.load(r'C:\Users\Guilherme\Downloads\thinking-time-ticking-power-223023.mp3') #carrega a música da máquina, o R é para tratar o texto como ele aparece, sem interpretar como outra coisa
mixer.music.play() #inicia a música

stop = input('Digite algo para parar a reprodução: ') #digitar qualquer coisa + enter pra parar a reprodução