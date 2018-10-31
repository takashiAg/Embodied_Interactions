import matplotlib.pyplot as plt
import pyaudio
import threading
from numpy import frombuffer, array
import time

CHUNK = 64
RATE = 4410
p = pyaudio.PyAudio()

input_value = [0 for x in range(1024)]


class ThreadJob(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill_flag = False

    def run(self):
        while not (self.kill_flag):
            plt.plot(data[-1000:])
            plt.pause(0.001)
            print(data)


data = []


def main():
    t = ThreadJob()
    t.start()
    try:
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, frames_per_buffer=CHUNK, input=True,
                        output=False)  # inputとoutputを同時にTrueにする
        while stream.is_active():
            input = stream.read(CHUNK)
            data.extend([x for x in frombuffer(input, dtype="int16")])

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
