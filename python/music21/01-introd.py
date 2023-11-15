'''
O music21 é baseado em Python e traz ferramentas para estudar música

Podemos usar o music21 para estudar uma grande base de dados de música, 
gerar exemplos musicais, ensinar fundamentos de teoria musical, editar
notação musical, estudar música e o cérebro e compor música (diretamente
e por meio de algoritmos)
'''
from music21 import *

# exibe a nota indicada
n = note.Note("C")         # dó
n.duration.type = 'eighth' # colcheia
n.show()

# exibe partitura e áudio da linha completa de notas
melody = converter.parse("tinynotation: 4/4 r2 r8 c8 d e f4 f8 f r c d c d4 d8 d r c g f e4 e8 e r c d e f4 f8 f") # dó ré mi fá fá fá
melody.show()
melody.show('midi')

# exibe como matriz 'linha de tom de abertura do quarteto da Quarta Corda de Schoenberg'
print(serial.rowToMatrix([2, 1, 9, 10, 5, 3, 4, 0, 8, 7, 6, 11]) )

# plota gráfico de tons comuns numa peça do século 14
dicant = corpus.parse('trecento/Fava_Dicant_nunc_iudei')
dicant.plot('histogram', 'pitch')
dicant.measures(1, 10).show()

# adiciona nomes em alemão das notas no coral de Bach BWV295
bwv295 = corpus.parse('bach/bwv295')
for thisNote in bwv295.recurse().notes:
  thisNote.addLyric(thisNote.pitch.german)
bwv295.show()

# exibe todo coral de Bach que tem tempo 3/4 (inicialmente com os 25 primeiros)
catalog = stream.Opus()
for work in corpus.chorales.Iterator(1, 26):
    firstTimeSignature = work.parts[0].measure(1).getTimeSignatures()[0]
    if firstTimeSignature.ratioString == '3/4':
        incipit = work.measures(0,2)
        catalog.insert(0, incipit.implode())
catalog.show()

# a função abaixo é usada para saber quão instável o perfil rítmico de uma peça é (função de Ani Patel)
s = corpus.parse('AlhambraReel')
analysis.patel.nPVI(s.flatten())
