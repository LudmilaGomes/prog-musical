from pydub import AudioSegment
from pydub.playback import play
import q2, q3 # garante que ambas as questões executem e, portanto, os arquivos .wav existam

'''
Mixagem de som usando Python (4 pontos)
Faça um programa em Python que faça uma mixagem Stereo dos dois arquivos WAVE 
gerados nas questões 2 e 3. Faça o arquivo da questão 2 ter mais 3dB de volume
e ser reproduzido com mais intensidade no canal da esquerda; faça o arquivo da
questão 3 ter mais 5dB de volume e ser reproduzido com mais intensidade no 
canal da direita. Gere o arquivo da mixagem e reproduza o seu conteúdo no 
programa em Python.
'''

# nomes dos arquivos
arq_output = "teste1.wav"; arq_wav = "output2.wav"

# armazena os áudios a partir dos respectivos .wav
audio_quest2 = AudioSegment.from_wav(arq_output)
audio_quest3 = AudioSegment.from_wav(arq_wav)

# definimos os dois áudios como tendo a mesma duração (7 segundos)
audio_quest2 = audio_quest2[0:7000]
audio_quest3 = audio_quest3[0:7000]

# + 3dB; reproduzido com mais intensidade no canal da esquerda
audio_quest2 = audio_quest2 + 3 
audio_quest2 = audio_quest2.pan(-0.9)

# + 5dB; reproduzido com mais intensidade no canal da direita
audio_quest3 = audio_quest3 + 5
audio_quest3 = audio_quest3.pan(0.7)

# 'une' os dois áudios (mixagem)
audio_mix = audio_quest2.overlay(audio_quest3)

# salva o arquivo gerado 'audio_mix'
audio_mix.export("audio_mix.wav", format="wav")
print('Reprodução do áudio mixado.')
play(audio_mix)