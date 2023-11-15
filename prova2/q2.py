import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

'''
Captura e reprodução de som usando Python (2,5 pontos)
Faça um programa em Python que capture som através de uma interface de 
áudio/microfone e faça o programa reproduzir o arquivo gerado com um acréscimo 
de 5dB no volume. 
'''

# ============// CAPTURA DE ÁUDIO

quant_amost = 1024 # quantidade de amostras a cada iteração (amostrar por bloco)
formato_amost = pyaudio.paInt16 # cada amostra é armazenada como um inteiro de 16 bits
quant_canal = 2 # estéreo
samp_rate = 44100 # taxa de amostragem (quant de amostras capturadas por segundo - em Hz)

py_aud = pyaudio.PyAudio() # instância do PyAudio para a gravação

print('Gravando.')
# abertura de arquivo para gravação - entrada de áudio
stream = py_aud.open(format=formato_amost, channels=quant_canal, rate=samp_rate, 
                     frames_per_buffer=quant_amost, input=True)

blocos = [] # guarda blocos de áudio capturados
dur = 7 # duração da gravação (7 segundos)
# samp_rate / quant_amost * duration é a quantidade de blocos de áudio gravados
for i in range(0, int(samp_rate / quant_amost * dur)):
  # dados lidos são adicionados como blocos de áudio
  dados = stream.read(quant_amost)
  blocos.append(dados)

stream.stop_stream() # para entrada de áudio
stream.close() # fecha arquivo
py_aud.terminate() # encerra objeto PyAudio

# ============// REPRODUÇÃO DE ÁUDIO GRAVADO

arq_output = "teste1.wav" # nome do arquivo do áudio

# cria e configura parâmetros do arquivo .wav
arq_audio = wave.open(arq_output, 'wb') # habilita escrita - write binary
arq_audio.setnchannels(quant_canal)
arq_audio.setsampwidth(py_aud.get_sample_size(formato_amost))
arq_audio.setframerate(samp_rate)
arq_audio.writeframes(b''.join(blocos))
arq_audio.close()

print('Reprodução do arquivo!')
arq_reprod = AudioSegment.from_file(file = arq_output, format = "wav") # indicamos arquivo que será reproduzido
arq_volume = arq_reprod + 5 # aumenta em 5 dB o volume
play(arq_volume) # reprodução