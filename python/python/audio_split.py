from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("melody.wav")

# audio.play()

seg1_start = 0
seg1_stop = 2000 # value in millisseconds
seg2_start = 2000
seg2_stop = 3000

segment1 = audio[seg1_start:seg1_stop] 
segment2 = audio[seg2_start:seg2_stop]

play(segment1)

play(segment2)

segment1.export("seg1.wav", format="wav")
segment2.export("seg2.wav", format="wav")

