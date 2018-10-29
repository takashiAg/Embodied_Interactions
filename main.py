import pyaudio

CHUNK = 1024
RATE = 44100
p = pyaudio.PyAudio()


def main():
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, frames_per_buffer=CHUNK, input=True,
                    output=True)  # inputとoutputを同時にTrueにする
    while stream.is_active():
        input = stream.read(CHUNK)
        # output = stream.write(input)

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Stop Streaming")


if __name__ == '__main__':
    main()
