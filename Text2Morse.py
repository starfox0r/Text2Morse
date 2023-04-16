import os
import time
import wave
from pydub import AudioSegment
from pydub.generators import Sawtooth


MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}


def text_to_morse_code(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += ' '
    return morse_code


def morse_code_to_audio(morse_code, filename):
    # Define the sound properties
    dot_duration = 0.1
    dash_duration = 3 * dot_duration
    space_duration = dot_duration

    # Create an empty audio file
    morse_audio = AudioSegment.silent(duration=100)

    for char in morse_code:
        if char == '.':
            sound = Sawtooth(600).to_audio_segment(duration=int(dot_duration * 1000)).apply_gain(-10)
        elif char == '-':
            sound = Sawtooth(600).to_audio_segment(duration=int(dash_duration * 1000)).apply_gain(-10)
        else:
            sound = AudioSegment.silent(duration=int(space_duration * 1000))

        # Add the sound to the audio file
        morse_audio += sound + AudioSegment.silent(duration=100)

    # Export the Morse code sound as an MP3 file
    morse_audio.export(filename, format='mp3')

if __name__ == '__main__':
    # Get the text input from the user
    text = "Hello World!"
    
    # Convert the text to Morse code
    morse_code = text_to_morse_code(text)

    # Save the Morse code sound as an MP3 file
    filename = 'output.mp3'
    morse_code_to_audio(morse_code, filename)

    print(f'Morse code saved as {filename}.')