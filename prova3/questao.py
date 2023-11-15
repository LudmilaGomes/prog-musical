'''
===============   Instruções para uso do programa   ===============

 - usando o comando pip install no terminal (com permissão de administrador!),
 importar os seguintes módulos: midiutil, midi2audio, pydub, pyaudio; também ter 
 realizado instalação corretamente do FluidSynth (https://www.fluidsynth.org; 
 ver configuração nas variáveis de ambiente do sistema);
 - usuário é recebido; deve decidir se áudio reproduzido será o do programa ou
 um áudio do próprio usuário; para o segundo caso, é necessário que o áudio do
 usuário esteja presente na mesma pasta que o presente .py;
 - após isso, o usuário define qual será o timbre usado para a reprodução do
 áudio, podendo ser um dos timbres oferecidos pelo programa ou um timbre próprio;
 para o segundo caso, é necessário que o timbre do usuário esteja presente na mesma 
 pasta que o presente .py;
 - enfim, o programa solicita que o usuário digite um nome para o .wav de saída do
 programa, para que seja feita, por fim, a conversão de .mid para .wav;
 - então, um outro menu surge na tela, indicando uma opção ao usuário relativa ao
 andamento do áudio, se ele deseja acelerar ou desacelerar sua reprodução;
 - por fim, o programa verifica qual o sistema operacional usado e abre o áudio
 com o reprodutor de mídia equivalente; se tudo ocorrer da forma apropriada, o 
 áudio é reproduzido a partir das escolhas e interações do usuário com o programa!

 !!! Ao escrever os arquivos .mid, .sf2 e .wav, é necessário que o usuário digite
 também a extensão; ex.: 
 Digite o nome do seu arquivo .mid aqui: 'SEU_MIDI.mid'

 - Possíveis melhorias: Usar forma mais intuitiva para escolha de arquivo .mid; 
 oferecer mais possibilidades de timbres usados no programa (tentei usar outros
 .sf2 disponibilizados no drive da disciplina, mas, ao escolher estes no programa,
 o arquivo de áudio não funcionava); não foram feitos testes em relação ao uso de
 outros sistemas operacionais que não o Windows!

'''

# importa módulos usados
from music21 import *
from midiutil import MIDIFile
from midi2audio import FluidSynth
from pydub.playback import play
from pydub import AudioSegment
from subprocess import Popen
from os import name

# função para alterar andamento do áudio de entrada; resulta em um áudio de saída com o valor de andamento passado
def alterar_andamento(arq_ent, arq_saida, valor_andamento):
  audio = AudioSegment.from_file(arq_ent)
  # altera andamento
  altered_audio = audio.speedup(playback_speed=valor_andamento)
  # salva o áudio, agora com andamento diferente
  altered_audio.export(arq_saida, format="wav")

print('Bem-vindo!')
print()
print('Este é um programa interativo para reprodução de áudio.')
print('Opções de interação: timbre, andamento e reprodução do áudio.')
print()

# variáveis usadas
arq_wav = './'; arq_midi = './'; arq_soundfont = './'; var_estado = 1

# programa oferece reprodução de arquivo próprio do programa ou algum que o usuário queria (contanto que esteja na mesma pasta do .py)
print('''Reprodução de áudio do programa ou próprio (do usuário):
  1 - Programa
  2 - Próprio
''')

# ifs para opções do menu acima
while (var_estado): # loop para o caso de a entrada ser um valor inadequado
  escolha_usuario = int(input('Sua escolha: '))
  if escolha_usuario == 1:
    arq_midi = "./meu_midi.mid"
    var_estado = 0
  elif escolha_usuario == 2:
    arq = input('Digite o nome do seu arquivo .mid aqui: ')
    arq_midi = arq_midi + arq
    print('Nome .mid: ' + arq_midi)
    var_estado = 0
  else:
    print('Valor não indicado, tente novamente.')
    var_estado = 1

# opções de timbre oferecidos pelo programa
print('''Há 4 opções de timbres:
  1 - Piano
  2 - Teremim
  3 - Timbre próprio do usuário (contanto que esteja na mesma pasta do .py)
''')

# ifs para opções do menu acima
var_estado = 1
while (var_estado): # loop para o caso de a entrada ser um valor inadequado
  escolha_usuario = int(input('Sua escolha: '))
  if escolha_usuario == 1:
    arq_soundfont = './piano.sf2'
    var_estado = 0
  elif escolha_usuario == 2:
    arq_soundfont = './Theremin.sf2'
    var_estado = 0
  elif escolha_usuario == 3:
    arq = input('Digite o nome do seu arquivo .sf2 aqui: ')
    arq_soundfont = arq_soundfont + arq
    print('Nome .sf2: ' + arq_soundfont)
    var_estado = 0
  else:
    print('Valor não indicado, tente novamente.')
    var_estado = 1

print()
arq = input('Digite um nome para o áudio .wav aqui: ') # solicita nome para o arquivo .wav
arq_wav = arq_wav + arq
print('Nome .wav: ' + arq_wav)
print()
print('Geração de .wav a partir de .mid!')
print()
print('=======   Dados do FluidSynth   =======')
print(arq_soundfont)
print(arq_midi)
# converte .mid para .wav para que possa ser reproduzido pelo python; usa o .sf2 escolhido pelo usuário
FluidSynth(arq_soundfont).midi_to_audio(arq_midi, arq_wav) 
print('======= =======')
print()

# definir andamento !!!
print('''Escolha um valor para o novo andamento do áudio:
  1 - 0.5
  2 - x0.75
  3 - x1 (não altera andamento)
  4 - x1.25
  5 - x1.5
''')
andamento_valor = 0

# ifs para opções do menu acima
var_estado = 1
while (var_estado): # loop para o caso de a entrada ser um valor inadequado
  escolha_usuario = int(input('Sua escolha: '))
  if escolha_usuario == 1:
    andamento_valor = 0.5
    var_estado = 0
  elif escolha_usuario == 2:
    andamento_valor = 0.75
    var_estado = 0
  elif escolha_usuario == 3:
    andamento_valor = 1
    var_estado = 0
  elif escolha_usuario == 4:
    andamento_valor = 1.25
    var_estado = 0
  elif escolha_usuario == 5:
    andamento_valor = 1.5
    var_estado = 0
  else:
    print('Valor não indicado, tente novamente.')
    var_estado = 1

# alteramos o andamento usando a função definida no começo do programa
if andamento_valor != 1:
  alterar_andamento(arq_wav, arq_wav, andamento_valor)

# reprodução do áudio
print('Reprodução do áudio (abrindo reprodutor multimídia)...')
# verificação do sistema operacional usado a fim de abrir o reprodutor multimídia apropriadamente
sistema_operacional = name
if sistema_operacional == 'nt':
  Popen(['start', arq_wav], shell=True)
elif sistema_operacional == 'posix':
  Popen(['xdg-open', arq_wav])
else:
  print("Sistema operacional não suportado.")

print('Saindo do programa...')