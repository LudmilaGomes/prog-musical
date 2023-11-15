from music21 import stream, note, midi
from midiutil import MIDIFile
from midi2audio import FluidSynth

'''
Geração de arquivo WAVE a partir de um arquivo MIDI em Python (2,5 pontos)
Faça um programa em Python que gere um arquivo MIDI com uma melodia simples. 
Faça o programa gerar um arquivo WAVE (.wav) a partir do MIDI, usando a 
biblioteca FluidSynth e um arquivo SoundFont à sua escolha (verificar opções 
na pasta da disciplina). 
'''

# ============// GERAÇÃO DE ARQUIVO MIDI

# arquivo midi definido e as notas da melodia
arq_midi = "./meu_midi.mid"
array_notas = ["C", "D", "E", "F", "F", "F", "C", "D", "C", "D", "D", "D", "C", "G", "F", "E", "E", "E", "C", "D", "E", "F", "F", "F"]

score = stream.Score() # objeto de Partitura
part = stream.Part() # uma 'unidade' de melodia da Partitura
score.append(part) # Part integrada ao Score (melodia é integrada à Partitura)

for nota in array_notas:
  nota_Note = note.Note(nota) # cada nota se torna um objeto Note
  part.append(nota_Note) # as notas (Note) são adicionadas na melodia

escreve_midi = midi.translate.music21ObjectToMidiFile(score) # Partitura é traduzida em arquivo midi
# abertura e escrita dos dados no arquivo
escreve_midi.open(arq_midi, "wb")
escreve_midi.write()
escreve_midi.close()

# ============// MIDI PARA WAV

arq_soundfont = "./piano.sf2"; arq_wav = "./output2.wav"
FluidSynth(arq_soundfont).midi_to_audio(arq_midi, arq_wav) # transforma midi (passamos .mid, .wav e .sf2) em .wav