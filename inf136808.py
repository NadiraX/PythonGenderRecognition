import sys
import wave

def main():
    print(sys.argv[1])
    if len(sys.argv) > 1:
        # Read file

        signal = wave.open(sys.argv[1])
        print(signal)
if __name__ == '__main__':
    main()
