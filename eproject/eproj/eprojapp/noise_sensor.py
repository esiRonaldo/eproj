import logging
import pyaudio
import struct
import datetime
import alsaaudio
import matplotlib.pyplot as plt
import numpy as np

##--------------------------Start of ploting--------------------------------#
i=0
f,ax = plt.subplots(2)
x = np.arange(10000)
y = np.random.randn(10000)
li, = ax[0].plot(x, y)
ax[0].set_xlim(0,1000)
ax[0].set_ylim(-5000,5000)
ax[0].set_title("Raw Audio Signal")
li2, = ax[1].plot(x, y)
ax[1].set_xlim(0,5000)
ax[1].set_ylim(-100,100)
ax[1].set_title("Fast Fourier Transform")
plt.pause(0.01)
plt.tight_layout()
##--------------------------End of ploting--------------------------------#


FORMAT = pyaudio.paInt16  # We use 16bit format per sample
CHANNELS = 1
RATE = 44100
CHUNK = 1024  # 1024bytes of data red from a buffer

MIXER = alsaaudio.Mixer()

MUTE_HOLD_TIME = datetime.timedelta(seconds=5)
MUTE_LOCKED = datetime.datetime.min
VOLUME = None


def plot_data(in_data):
    global MUTE_LOCKED
    global VOLUME
    global MIXER
    # get and convert the data to float
    audio_data = struct.unpack("h", in_data[:2])
    ct = datetime.datetime.now()
    if audio_data[0] > 18000:
        if VOLUME != 0:
            MIXER.setvolume(0)  # Set the volume to 0%.
            VOLUME = 0
            print("A voice of more than 6000 DB Detected")
        MUTE_LOCKED = ct + MUTE_HOLD_TIME
    elif ct > MUTE_LOCKED:
        if VOLUME != 100:
            MIXER.setvolume(100)  # Set the volume to 100%.
            VOLUME = 100
            print("unmute_command")
    print("current time:-", ct)
    print("volume:", VOLUME)

#---------------------------------Start of Rendering-------------------------------------
    audio_data = np.fromstring(in_data, np.int16)
    scale_variable = 10.*np.log10(abs(np.fft.rfft(audio_data)))
    li.set_xdata(np.arange(len(audio_data)))
    li.set_ydata(audio_data)
    li2.set_xdata(np.arange(len(scale_variable))*10.)
    li2.set_ydata(scale_variable)
    plt.pause(0.01)
#---------------------------------End of Rendering-------------------------------------

def main():
    logging.basicConfig(filename='logFile.log', level=logging.DEBUG)
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True)  # ,
    stream.start_stream()
    print("\n+---------------------------------+")
    print("| Press Ctrl+C to Break Recording |")
    print("+---------------------------------+\n")

    keep_going = True
    while keep_going:
        try:
            plot_data(stream.read(CHUNK, exception_on_overflow=False))
        except KeyboardInterrupt:
            keep_going = False

    stream.stop_stream()
    stream.close()

    audio.terminate()


if __name__ == "__main__":
    main()
