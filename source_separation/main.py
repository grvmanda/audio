import librosa
import numpy as np
from algorithms.nmf import Nmf




if __name__=='__main__':
    # Load the audio file
    filename = '../mp3/chameleon.wav'  # Replace with your file path
    y, sr = librosa.load(filename, sr=None)  # Load audio, preserving the original sample rate

    test = Nmf(y=y, enable_plot=True)


