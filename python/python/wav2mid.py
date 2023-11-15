from pydub import AudioSegment
from midiutil import MIDIFile
import numpy as np
import aubio

# Load an audio file
audio = AudioSegment.from_file("out.wav")

# Create an empty MIDI file
midi_file = MIDIFile()

# Add a single track
track = 0

# Configure MIDI parameters
channel = 0
volume = 100

# Set the sample rate for aubio (sample rate of the audio)
sample_rate = audio.frame_rate

# Create an aubio pitch detection object
pitch_detection = aubio.pitch("yin", 2048, 1024, sample_rate)

# Create a buffer to store audio data for pitch detection
buffer_size = 1024

# Initialize time in milliseconds
time_ms = 0
sample_duration = 1000  # Duration of 1 second

while time_ms < len(audio):
    # Get a segment of audio (1 second)
    segment = audio[time_ms:time_ms + sample_duration]
    
    # Convert the segment to a NumPy array
    audio_data = np.array(segment.get_array_of_samples(), dtype=np.float32)
    
    # Calculate the pitch using aubio in smaller overlapping chunks
    pitches = []
    for i in range(0, len(audio_data) - buffer_size, buffer_size):
        chunk = audio_data[i:i + buffer_size]
        chunk_pitch = pitch_detection(chunk)[0]
        if not np.isnan(chunk_pitch):
            pitches.append(chunk_pitch)
    
    # Check if any pitch values were detected
    if len(pitches) > 0:
        pitch = int(np.median(pitches))
    else:
        pitch = 0  # Default to no note if pitch cannot be detected
    
    # Map the detected pitch to MIDI notes (adjust as needed)
    if pitch != 0:
        midi_pitch = int(np.interp(pitch, [40, 90], [36, 84]))  # Map to MIDI notes between C3 (36) and C6 (84)
    else:
        midi_pitch = 0  # 0 means no note (a rest)
    
    duration = 1  # Duration of 1 unit of MIDI time (adjust as needed)
    
    # Add the note to the MIDI file
    midi_file.addNote(track, channel, midi_pitch, time_ms // 1000, duration, volume)
    
    # Advance to the next segment
    time_ms += sample_duration

# Save the resulting MIDI file
with open("audio_to_midi.mid", "wb") as output_file:
    midi_file.writeFile(output_file)

print("Audio to MIDI conversion completed and saved as 'audio_to_midi.mid'.")
