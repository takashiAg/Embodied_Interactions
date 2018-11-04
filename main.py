def prinf_process(d):
    import pyaudio
    import sys
    import time
    import wave
    import numpy as np

    chunk = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=chunk
    )

    d["data"] = np.arange(1)
    while True:
        data = stream.read(chunk)
        #         dd=[int(x) for x in np.frombuffer(data, dtype="int16")]
        #         d["data"].extend(dd)
        # d["data"].append(np.frombuffer(data, dtype="int16"))
        d["data"] = np.concatenate([d["data"], np.frombuffer(data, dtype="int16")], axis=0)[-44100:]

    stream.close()
    p.terminate()

    data = b''.join(all)


from multiprocessing import Manager, Process

d = Manager().dict()
p = Process(target=prinf_process, args=(d,))
p.start()
print(d)
len(d)
import numpy as np
import matplotlib.pyplot as plt
import time

# %matplotlib inline

# 図1を定義
fig1 = plt.figure()

fig1.suptitle("trigonometric function", fontsize=16)

# 図の中にサブプロットを追加する
fig1_a = fig1.add_subplot(2, 1, 1)
fig1_b = fig1.add_subplot(2, 1, 2)
fig1.tight_layout()
fig1.subplots_adjust(top=0.85)
# 図１(a)にプロットする

time.sleep(1)

data = d["data"][:] / 32768.0
fig1_a_1, = fig1_a.plot(data)
fig1_b_1, = fig1_b.plot(data)
while True:
    data = d["data"][:] / 32768.0
    x = range(len(data))

    fft_data = np.fft.fft(data).real[:int(len(x)/2)]
    x_axis_fft=list(range(len(fft_data)))

    fig1_a_1.set_data(x, data)
    fig1_a.set_ylim(-1, 1)

    fig1_b_1.set_data(x_axis_fft,fft_data)
    fig1_b.set_ylim(fft_data.min(), fft_data.max())
    fig1_b.set_xlim(min(x_axis_fft), max(x_axis_fft))

    plt.pause(0.1)


