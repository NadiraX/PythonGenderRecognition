import sys
import wave

def main():
    print("tak")
    if len(sys.argv) > 1:
        # Read file

        signal, sample_rate = wave.open(sys.argv[1])
        if len(signal.shape) == 2:
            signal = [s[0] for s in signal]

if __name__ == '__main__':
    main()
