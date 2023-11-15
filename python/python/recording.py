import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

chunk = 1024 # record in chunks of 1024 samples
sample_format = pyaudio.paInt16 # 16 bits per sample
channels = 2 # stereo - 2 channels
sample_rate = 44100 # 44100 samples per second
duration = 10 # 10 seconds of recording
filename = "output.wav"

p = pyaudio.PyAudio() 

print('Recording audio...')

stream = p.open(format=sample_format,
                channels=channels, 
                rate=sample_rate, 
                frames_per_buffer=chunk,
                input=True)

frames = [] # array to store captured frames

for i in range(0, int(sample_rate / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()

p.terminate()

print('Audio recording finished!')

wave_file = wave.open(filename, 'wb')
wave_file.setnchannels(channels)
wave_file.setsampwidth(p.get_sample_size(sample_format))
wave_file.setframerate(sample_rate)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print('Playing recorded wave file...')

play_file = AudioSegment.from_file(file = "output.wav", 
                                  format = "wav")

play(play_file)

print('Finished!')




