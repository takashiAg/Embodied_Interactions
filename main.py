import matplotlib.pyplot as plt
import pyaudio
import threading
import numpy as np
import time

CHUNK = 1024
RATE = 44100
p = pyaudio.PyAudio()

input_value = [0 for x in range(1024)]


class ThreadJob(threading.Thread):
    def __init__(self, v=[]):
        threading.Thread.__init__(self)
        self.line = v
        self.kill_flag = False

    def run(self):
        old = []
        while not (self.kill_flag):
            plt.plot(self.line[:])
            plt.pause(0.001)
            print(self.line)


def main():
    t = ThreadJob()
    t.start()
    try:
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, frames_per_buffer=CHUNK, input=True,
                        output=False)  # inputとoutputを同時にTrueにする
        while stream.is_active():
            input = stream.read(CHUNK)

            data = [x for x in np.frombuffer(input, dtype="int16")]
            t.line = np.append(t.line, data)
            # output = stream.write(input)

        stream.stop_stream()
        stream.close()
        p.terminate()

        print("Stop Streaming")
    except Exception as e:
        print(e)
    finally:
        t.kill_flag = True


if __name__ == '__main__':
    # thread_1 = threading.Thread(target=func1)
    # thread_1.start()
    main()
