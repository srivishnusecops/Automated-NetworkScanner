# tts.py - Text-to-Speech Library
import pyttsx3

# Initialize the engine once (better performance)
_engine = pyttsx3.init()


def talk(text, rate=150, volume=0.9, voice_index=0):
    """
    Convert text to speech with customizable settings

    Parameters:
        text (str): Text to speak
        rate (int): Words per minute (default: 150)
        volume (float): Volume level 0.0 to 1.0 (default: 0.9)
        voice_index (int): Voice selection (default: 0)
    """
    try:
        # Configure voice settings
        _engine.setProperty('rate', rate)
        _engine.setProperty('volume', volume)

        # Get available voices and select one
        voices = _engine.getProperty('voices')
        if voice_index < len(voices):
            _engine.setProperty('voice', voices[voice_index].id)

        # Speak and wait for completion
        _engine.say(text)
        _engine.runAndWait()

    except Exception as e:
        print(f"TTS Error: {e}")


# Example usage
if __name__ == "__main__":
    talk("Hello, this is a test message")
    talk("You can customize speed and volume", rate=120, volume=0.7)