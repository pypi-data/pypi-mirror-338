import os

try:
    from gtts import gTTS
    import IPython.display as ipd
except ImportError:
    print("⚠️ Missing dependency: gtts. Install it using `pip install gtts`.")

def speak(text: str, filename: str = "output.mp3"):
    try:
        # Generate speech
        tts = gTTS(text)
        tts.save(filename)

        # Detect if running in Google Colab
        if "google.colab" in str(get_ipython()):  # type: ignore
            return ipd.Audio(filename, autoplay=True)

        # Play audio based on OS
        if os.name == "nt":  # Windows
            os.system(f"start {filename}")
        elif os.uname().sysname == "Darwin":  # macOS
            os.system(f"afplay {filename}")
        else:  # Linux
            os.system(f"mpg321 {filename} || cvlc {filename} --play-and-exit || aplay {filename}")

    except Exception as e:
        print(f"⚠️ Error in speech synthesis: {e}")

