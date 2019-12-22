import sys
import wave
import numpy as np
import scipy.io.wavfile
import librosa
def main():
    print(sys.argv[1])
    if len(sys.argv) > 1:
        # Read file

        y, sr = librosa.load(sys.argv[1])

        params = spectral_properties(y,sr)
        print(params)

def spectral_properties(y,fs):
    spec = np.abs(np.fft.rfft(y))
    freq = np.fft.rfftfreq(len(y), d=1 / fs)
    spec = np.abs(spec)
    amp = spec / spec.sum()
    mean = (freq * amp).sum()
    sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))
    amp_cumsum = np.cumsum(amp)
    median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
    mode = freq[amp.argmax()]
    Q25 = freq[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
    Q75 = freq[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
    IQR = Q75 - Q25
    z = amp - amp.mean()
    w = amp.std()
    skew = ((z * 3).sum() / (len(spec) - 1)) / w * 3
    kurt = ((z * 4).sum() / (len(spec) - 1)) / w * 4

    result_d = {
        'mean': mean,
        'sd': sd,
        'median': median,
        'mode': mode,
        'Q25': Q25,
        'Q75': Q75,
        'IQR': IQR,
        'skew': skew,
        'kurt': kurt
    }
    return result_d
if __name__ == '__main__':
    main()
