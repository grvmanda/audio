import librosa
import numpy as np
from algorithms.nmf import Nmf
import matplotlib.pyplot as plt




if __name__=='__main__':
    # Load the audio file
    filename = '../mp3/chameleon.wav'  # Replace with your file path
    y, sr = librosa.load(filename, sr=None)  # Load audio, preserving the original sample rate

    nmf = Nmf(y)

    n_components = 6
    nmf.run(n_components)

    fig, axs = plt.subplots(n_components, 2, figsize=(15, 20))
    freq_limit = 150
    for i in range(n_components):
        axs[i, 0].plot(nmf.H[i])
        axs[i, 0].set_title(f'H Component {i+1}')
        axs[i, 0].set_xlabel('Time')
        axs[i, 0].set_ylabel('Amplitude')
        axs[i, 1].plot(nmf.W[:freq_limit, i])
        axs[i, 1].set_title(f'W Component {i+1}')
        axs[i, 1].set_xlabel('Frequency')
        axs[i, 1].set_ylabel('Amplitude')
        axs[i, 1].set_xlim(0, freq_limit)

    plt.tight_layout()
    plt.show()


