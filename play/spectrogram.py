import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio file
filename = 'your_song_file.mp3'  # Replace with your file path
y, sr = librosa.load(filename, sr=None)  # Load audio, preserving the original sample rate

# Generate a spectrogram
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

# Plot the spectrogram
plt.figure(figsize=(10, 6))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.tight_layout()
plt.show()