from pydub import AudioSegment

sound = AudioSegment.from_wav('melody.wav')

sound.export('melody.mp3', format='mp3')

print('Converted melody.wav to melody.mp3')
