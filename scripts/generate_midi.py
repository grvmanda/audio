import mido

# Note data: [note, velocity, start_ms, end_ms]
class MidiNote:
    def __init__(self, note: int, velocity: int, start_ms: int, end_ms: int):
        self.note = note
        self.velocity = velocity
        self.start_ms = start_ms
        self.end_ms = end_ms
    
    def write_note(self, track, ms_per_tick, previous_tick):
        start_tick = int(self.start_ms / ms_per_tick)
        end_tick = int(self.end_ms / ms_per_tick)

        # Add a note-on event
        track.append(mido.Message('note_on', note=self.note, velocity=self.velocity, time=start_tick - previous_tick))
        previous_tick = start_tick

        # Add a note-off event
        track.append(mido.Message('note_off', note=self.note, velocity=0, time=end_tick - previous_tick))
        previous_tick = end_tick

if __name__ == "__main__":
    notes = [
        MidiNote(note=40, velocity=100, start_ms=0, end_ms=200),
        MidiNote(note=43, velocity=90, start_ms=200, end_ms=400),
        MidiNote(note=45, velocity=80, start_ms=400, end_ms=600),
        MidiNote(note=47, velocity=70, start_ms=600, end_ms=800),
        MidiNote(note=48, velocity=60, start_ms=800, end_ms=1000),
        MidiNote(note=50, velocity=100, start_ms=1000, end_ms=2000)
    ]

    # Create a new MIDI file with one track
    midi_file = mido.MidiFile()
    track = mido.MidiTrack()
    midi_file.tracks.append(track)

    # Set the instrument to Electric Bass (MIDI Program Number 33)
    track.append(mido.Message('program_change', program=32))

    # Convert ms to ticks (assuming 480 ticks per beat, 500ms per beat)
    ms_per_tick = 500 / 480

    # Add notes to the track
    previous_tick = 0
    for note in notes:
        note.write_note(track, ms_per_tick, previous_tick, note)

    # Save the MIDI file
    midi_file.save('output.mid')
    print("MIDI file saved as 'output.mid'")
