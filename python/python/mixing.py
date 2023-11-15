from pydub import AudioSegment
from pydub.playback import play

print('Mixing teste.wav and melody.wav...')
audio1 = AudioSegment.from_wav("teste.wav")
audio2 = AudioSegment.from_wav("melody.wav")

audio1 = audio1.pan(-0.8) # panorama: -1 left, 0 center, 1 right
audio1 = audio1 + 5 # volume 5dB increase

audio2 = audio2.pan(0.8)
audio2 = audio2 + 3

mixed_audio = audio1.overlay(audio2)

print('Playing mixed audio...')
play(mixed_audio)

print('Saving mixed file')

mixed_audio.export("mix.wav", format="wav")



