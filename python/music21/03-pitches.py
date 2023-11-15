from music21 import *

# pitch: tom, altura
# o que torna uma nota, de fato, uma nota: altura e duração
# bflat = note.Note(B-4), print(bflat, bflat.pitch) # <music21.note.Note B-> B-4

# # ou - : sustenido, bemol
# nome da nota, acidente e número da oitava
p1 = pitch.Pitch('b-4') 

print(p1) # B-4
print(p1.octave) # 4

# classe de notas é um conjunto com as notas separadas por um número inteiro de oitavas
# c.pitch.pitchClass = 0, c#.pitch.pitchClass = 1, d.pitch.pitchClass = 2, ...
print(p1.pitchClass) # 10

print(p1.name) # B-
print(p1.accidental.alter) # -1.0
print(p1.nameWithOctave) # B-4

# pitchClass retorna um valor para a altura na antiga representação MIDI; é um número entre 0 e 127; Dó central (C4) é 60, C#4, 61, assim por diante
print(p1.midi) # 70

# a maioria dessas propriedades pode ser alterada (settable properties)
# quando um atributo é alterado, outros valores também mudam para refletir a mudança feita
p1.name = 'd#'
p1.octave = 3
print(p1.nameWithOctave) # 'D#3'

p2 = p1.transpose('M7')
print(p2) # <music21.pitch.Pitch C##4>

csharp = note.Note('C#4')
print(csharp.name) # 'C#'
print(csharp.pitch.name) # 'C#'
print(csharp.octave) # 4
print(csharp.pitch.octave) # 4

print(csharp.pitch.spanish) # 'do sostenido'
# print(csharp.spanish) # não funciona com notas

print(csharp.pitch.unicodeName) # C♯

print(csharp.pitch.getEnharmonic()) # D-4
print(csharp.pitch.getLowerEnharmonic()) # B##3

# para que uma nota ocupe um espaço musical, ela precisa ter uma duração (quantidade de tempo que elas são tocadas)
halfDur = duration.Duration('half')
# notação em inglês: whole, half, quarter, eighth, 16th, 32nd, 64th
# em português: semibreve(1), mínima(1/2), semínima(1/4), colcheia(1/8), semicolcheia(1/16), fusa(1/32), semifusa(1/64)

# podemos criar uma duração passando um número; esse número representa a duração em semínimas
halfDur = duration.Duration(2) # 2 * (1/4) = 1/2 (mínima)

print(halfDur.quarterLength) # 2.0 - duração em termos de semínima
print(halfDur.type) # 'half'

dottedQuarter = duration.Duration(1.5)
print(dottedQuarter.quarterLength) # 1.5
print(dottedQuarter.type) # 'quarter'
print(dottedQuarter.dots) # 1
dottedQuarter.dots = 4
print(dottedQuarter.quarterLength) # 1.9375

# quarterLenght é uma medida muito importante e muito usada no music21

# ========//========

# esta é a vantagem de trabalhar usando Note: com Note, manipulamos no mesmo objeto Pitch e Duration
# além disso, Note pode fazer coisas que Pitch e Duration não podem; ela pode ter letras!
# setamos o atributo lyric
otherNote = note.Note("F6")
otherNote.lyric = "Tip tip tai, tip tip tai, Tarantellaaaaa"
otherNote.addLyric(otherNote.nameWithOctave)
otherNote.addLyric(otherNote.pitch.pitchClassString)
# otherNote.show()

# ========//========

'''
stream e suas subclasses é um container fundamental que contém outros objetos 
importantes, como Note, Chord, Clef, ...

um container é como uma lista/array

objetos armazenados em um stream são espaçados no tempo; cada objeto tem um deslocamento 
representando quantas semínimas ele está a partir do início do stream. Por exemplo, em um 
compasso 4/4 de duas mínimas, a primeira nota estará no deslocamento 0,0 e a segunda no 
deslocamento 2,0.

streams podem armazenar outros streams; subclasses comumente usadas de streams incluem Score, 
Part e Measure.

um objeto pode ser armazenado (referenciado) simultaneamente em mais de um stream;

há uma limitação: o mesmo objeto não deve aparecer duas vezes em uma estrutura hierárquica 
de streams. Por exemplo, você não deve colocar um objeto nota no compasso 3 e no compasso 
5 da mesma peça
'''

# streams são similares a listas no sentido de que armazenam elementos em uma ordem
stream1 = stream.Stream()
# o uso mais comum de streams é de guardar notas
nota1 = note.Note("C4")
nota2 = note.Note("D4")
nota3 = note.Note("E4")
stream1.append(nota1)
stream1.append(nota2)
stream1.append(nota3)
# mas isso seria muito trabalhoso; então, podemos usar repeatAppend()
# repeatAppend() - adiciona N cópias únicas das notas (não referências)

stream2 = stream.Stream()
n4 = note.Note("F4")
stream2.repeatAppend(n4, 4)
# stream2.show()
print(len(stream1)) # 4
stream1.show('text') # exibe o que há no stream em forma de texto - nota e duração no stream
# stream1.show()

for thisNote in stream1:
    print(thisNote.step)

print(stream1[0].nameWithOctave)
note3Index = stream1.index(nota3) # index() fornece o índice da primeira 'nota3' do stream

# stream1.pop(note3Index) # podemos remover um elemento dando um índice, com pop()

'''
podemos reunir elementos com base na classe (tipo de objeto) do elemento, por faixa 
de deslocamento ou por identificadores específicos anexados ao elemento. A coleta de 
elementos de um Stream com base na classe do elemento fornece uma maneira de filtrar 
o Stream para os tipos de objetos desejados. O método getElementsByClass() itera sobre 
um Stream de elementos que são instâncias ou subclasses das classes fornecidas.
'''

for thisNote in stream1.getElementsByClass(note.Note): # podemos passar como parâmetro: 'Note'
    print(thisNote, thisNote.offset)

# também podemos passar uma lista:
for thisNote in stream1.getElementsByClass(['Note', 'Rest']):
    print(thisNote, thisNote.offset) # não incluímos nenhuma pausa no stream, então nada muda

# https://web.mit.edu/music21/doc/usersGuide/usersGuide_04_stream1.html#separating-out-elements-by-class-with-getelementsbyclass