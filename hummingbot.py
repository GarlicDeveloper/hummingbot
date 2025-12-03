import sounddevice as sd
from scipy.io.wavfile import write
from acrcloud.recognizer import ACRCloudRecognizer
from lyricsgenius import Genius
import json

# CONFIG

ACR_HOST = "identify-ap-southeast-1.acrcloud.com"  
ACR_KEY = "b24c7cdbdfa5910204d2b9a36309b2c1"
ACR_SECRET = "eJXYMkKzJgGr6UaiVIXoxtoEIvC1UsBGz8Yvq2Di"

GENIUS_API_KEY = "0FRfcy3eeU5PzlU8TK5H4apwKDc887URoN4JJkPnt87JEETU11I5HjcCgDiqwq38"


RECORD_SECONDS = 10
FILENAME = "hum.wav"

def record_audio():
    print("\n Start humming the song…")
    fs = 44100  
    audio = sd.rec(int(RECORD_SECONDS * fs), samplerate=fs, channels=1)
    sd.wait()
    write(FILENAME, fs, audio)
    print(" Humming recorded.\n")


def recognize_song():
    config = {
        "host": ACR_HOST,
        "access_key": ACR_KEY,
        "access_secret": ACR_SECRET,
        "timeout": 10
    }

    print(" Identifying song…")
    recognizer = ACRCloudRecognizer(config)
    result = recognizer.recognize_by_file(FILENAME, 0)

    data = json.loads(result)

    if "metadata" in data:
        title = data["metadata"]["music"][0]["title"]
        artist = data["metadata"]["music"][0]["artists"][0]["name"]
        print(f" Song recognized: {title} — {artist}\n")
        return title, artist
    else:
        print(" No song identified.")
        return None, None


def get_lyrics(title, artist):
    print(" Fetching lyrics…")
    genius = Genius(GENIUS_API_KEY, skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"])

    song = genius.search_song(title, artist)

    if song:
        print(f"\n\n Lyrics for: {title} — {artist}\n")
        print(song.lyrics)
    else:
        print(" Lyrics not found.")

# MAIN

record_audio()
title, artist = recognize_song()

if title:
    get_lyrics(title, artist)
else:
    print("Try humming clearer or closer to mic.")

