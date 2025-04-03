try:
    from gtts import gTTS
    import IPython.display as ipd
except ImportError:
    print("⚠️ Missing dependency: gtts. Install it using `pip install gtts`.")

def speak(text: str):
    """Convert text to speech and play it in Google Colab."""
    try:
        tts = gTTS(text)
        tts.save("output.mp3")
        return ipd.Audio("output.mp3", autoplay=True)
    except Exception as e:
        print(f"Error in speech synthesis: {e}")
