import os

try:
    from gtts import gTTS
    import IPython.display as ipd
except ImportError:
    print("⚠️ Missing dependency: gtts. Install it using `pip install gtts`.")

def speak(text: str, filename: str = "output.mp3"):
    try:
        tts = gTTS(text)
        tts.save(filename)

        if "google.colab" in str(get_ipython()):  # type: ignore
            return ipd.Audio(filename, autoplay=True)

        if os.name == "nt":  
            os.system(f"start {filename}")
        elif os.uname().sysname == "Darwin":  
            os.system(f"afplay {filename}")
        else:  
            os.system(f"mpg321 {filename} || cvlc {filename} --play-and-exit || aplay {filename}")

    except Exception as e:
        print(f"⚠️ Error in speech synthesis: {e}")

