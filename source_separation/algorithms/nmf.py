import typing
import numpy as np
import librosa
from sklearn.decomposition import NMF

class Nmf:

    def __init__(self, y: np.ndarray):
        self.__y = y
        self.n_fft = 16384
        self.W : np.ndarray() = None
        self.H : np.ndarray() = None

    def run(self, n_components):
        # TODO: i want to be able to output a certain class of variables here
        
        # Generate a spectrogram with a Hanning window
        X = np.abs(librosa.stft(self.__y, window='hann', n_fft=self.n_fft))

        model = NMF(n_components=n_components, init='random', random_state=0, max_iter=1000)

        self.W = model.fit_transform(X=X)
        self.H = model.components_

    
        
