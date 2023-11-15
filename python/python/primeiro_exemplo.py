from pydub import AudioSegment
from pydub.playback import play


# wav_file_p - instance of AudioSegment
def print_info(wav_file_p):
#    print('file: '+ str(wav_file_p.filename))
    print('type: ' + str(type(wav_file_p)))
    print('frame rate: ' + str(wav_file_p.frame_rate))
    print('channels: ' + str(wav_file_p.channels))
    print('sample width: ' + str(wav_file_p.sample_width) + ' bytes')
    print('len: ' + str(len(wav_file_p)))

    

# song = AudioSegment.from_wav("teste.wav")
wav_file = AudioSegment.from_file(file = "teste.wav", 
                                  format = "wav")

print_info(wav_file)

wav_file_melo = AudioSegment.from_wav("melody.wav")

print_info(wav_file_melo)

wav_file_seq = wav_file + wav_file_melo

louder_wav_file = wav_file_seq + 10

both_chan = louder_wav_file.split_to_mono()

print('mono(0): ')
print_info(both_chan[0])
play(both_chan[0])

# both_chan[0].export(...)

play(both_chan[1])

# play(louder_wav_file)

print('export: ')

louder_wav_file.export(out_f = "louder_wav_file_seq.wav",
                       format = "wav")

print_info(louder_wav_file)

# play(wav_file)

# play(wav_file_melo)

# + 10 dB
# wav_file_louder = wav_file + 10 
# play(wav_file_louder)

# - 5 dB
# wav_file_quieter = wav_file - 5
# play(wav_file_quieter)


