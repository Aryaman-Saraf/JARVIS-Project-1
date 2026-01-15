#Make notes of all this

import pyaudio
import numpy as np
from openwakeword.model import Model

# ----------------------------
# Configuration
# ----------------------------

def wakeWordDetect():
    SAMPLE_RATE = 16000
    CHANNELS = 1
    CHUNK_SIZE = 1280   # 80 ms @ 16kHz
    FORMAT = pyaudio.paInt16

    # ----------------------------
    # Load wake-word model
    # ----------------------------

    model = Model(
        wakeword_models=["hey_jarvis"],
        inference_framework="onnx"
    )

    # ----------------------------
    # Initialize PyAudio
    # ----------------------------
    audio = pyaudio.PyAudio()

    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=SAMPLE_RATE,
        input=True,
        frames_per_buffer=CHUNK_SIZE
    )

    print("Listening for wake word: JARVIS...")

    # ----------------------------
    # Continuous listening loop
    # ----------------------------
    try:
        while True:
            # Read raw audio bytes from microphone
            audio_data = stream.read(CHUNK_SIZE, exception_on_overflow=False)

            # Convert bytes → NumPy array
            audio_np = np.frombuffer(audio_data, dtype=np.int16)

            # Run wake-word detection
            prediction = model.predict(audio_np)

            # Check confidence score for any wake word detected
            for wake_word, score in prediction.items():
                if score > 0.25:
                    print(f"Wake word '{wake_word}' detected with confidence: {score:.2f}")
                    return

    except KeyboardInterrupt:
        print("\nStopping wake word detection...")
    finally:
        # ----------------------------
        # Cleanup
        # ----------------------------
        stream.stop_stream()
        stream.close()
        audio.terminate()