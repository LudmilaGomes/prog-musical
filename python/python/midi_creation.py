from music21 import stream, note, midi
from midiutil import MIDIFile
from midi2audio import FluidSynth

midi_file_name = "./example_track.mid"

notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]

score = stream.Score()
part = stream.Part()
score.append(part)

for note_name in notes:
    new_note = note.Note(note_name)
    part.append(new_note)

midi_file = midi.translate.music21ObjectToMidiFile(score)
midi_file.open(midi_file_name, "wb")
midi_file.write()
midi_file.close()

midi_file.open(midi_file_name, "rb")

soundfont_file = "./piano.sf2"
wave_file = "./out.wav"

FluidSynth(soundfont_file).midi_to_audio(midi_file_name, wave_file)
