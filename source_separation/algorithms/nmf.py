import typing
import numpy as np
import matplotlib.pyplot as plt
import librosa
from sklearn.decomposition import NMF

class Nmf:

    def __init__(self, y: np.ndarray, enable_plot: bool = False):
        self.__y = y
        self.__n_fft = 16384
        self.__enable_plot = enable_plot
        self.run(6)

    def run(self, n_components):
        # TODO: i want to be able to output a certain class of variables here
        
        # Generate a spectrogram with a Hanning window
        X = np.abs(librosa.stft(self.__y, window='hann', n_fft=self.__n_fft))

        model = NMF(n_components=n_components, init='random', random_state=0, max_iter=1000)

        W = model.fit_transform(X=X)
        H = model.components_

        if self.__enable_plot:
            fig, axs = plt.subplots(n_components, 2, figsize=(15, 20))
            freq_limit = 150
            for i in range(n_components):
                axs[i, 0].plot(H[i])
                axs[i, 0].set_title(f'H Component {i+1}')
                axs[i, 0].set_xlabel('Time')
                axs[i, 0].set_ylabel('Amplitude')
                axs[i, 1].plot(W[:freq_limit, i])
                axs[i, 1].set_title(f'W Component {i+1}')
                axs[i, 1].set_xlabel('Frequency')
                axs[i, 1].set_ylabel('Amplitude')
                axs[i, 1].set_xlim(0, freq_limit)

            plt.tight_layout()
            plt.show()


        
