from music21 import *

'''
notação musical: uma sequência de notas; colocadas uma após a outra ou simultaneamente
na pauta. Há outros elementos, mas a essência são as notas
'''

f = note.Note("F5")
# music21 usa a convenção de que o Dó central é C4

# exibe a nota e atributos da nota
print(f)
print(f.name)
print(f.octave)
print(f.pitch)

# também há sub-atributos
print(f.pitch.frequency)
print(f.pitch.pitchClassString) # pitch class is 5 (C = 0, C# e Db = 1, etc)

# dó sustenido
csharp = note.Note("C#4")
print(csharp.pitch)

# si bemol
bflat = note.Note("B-2")
print(bflat.pitch.accidental) # mostra qual o acidente

accid = bflat.pitch.accidental
print(accid.alter) # mostra em quantos semitons esse acidente muda a nota

print(accid.displayLocation) # mostra em que lugar o acidente é exibido na partitura
# por padrão, o acidente é exibido ao lado da nota; podemos alterar isso para que ele seja exibido acima da nota:
accid.displayLocation = 'above' # essa instrução altera 'bflat.pitch.accidental.displayLocation'

# f.show() # exibe a nota na pauta com o MuseScore4
# f.show('midi') # áudio da nota

# transpose() cria uma nova nota ao transpor a nota para um certo intervalo, ao invés de alterar a nota original
d = bflat.transpose("M3")
print(d, bflat)

bflat.transpose("P4", inPlace=True) # altera a nota original
print(bflat)

# nem todas as notas possuem acidente
print(d.pitch.accidental)

# print(d.pitch.accidental.name) # cria um erro, se a nota não tiver acidente

if d.pitch.accidental is not None:
    print(d.pitch.accidental.name)

r = note.Rest()
r.show() # exibe na partitura uma pausa
# print(r.pitch)

# não declare variáveis com nome 'note'!!!
# note = note.Note("C#3") # nome reservado do módulo music21