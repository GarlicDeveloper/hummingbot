# 🎶 HummingBot — Hum-To-Song Recognition + Lyrics Fetcher

HummingBot is a Python-based AI tool that can detect a song based on a user humming into a microphone — just like Google’s “Hum to Search” — and then fetch the song’s lyrics.

---

## ✨ Features

✔ Hum or sing a melody — no lyrics needed
✔ Identifies song name & artist using ACRCloud
✔ Retrieves lyrics using Genius API
✔ Works on Windows / macOS / Linux
✔ Command-line based

---

## 🔧 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

`requirements.txt` contains:

```
acrcloud
sounddevice
scipy
lyricsgenius
python-dotenv
pydub
librosa
numpy
```

---

## 🧠 Prerequisites (IMPORTANT)

You need two external services:

---

### 1️⃣ ACRCloud Setup (for humming recognition)

1. Go to [https://acrcloud.com/](https://acrcloud.com/)
2. Create a free account
3. Create a **Music Recognition** project
4. Enable **Humming Recognition**
5. Copy your:

```
Host
Access Key
Access Secret
```

---

### 2️⃣ Genius Setup (for lyrics)

1. Go to [https://genius.com/](https://genius.com/)
2. Create account
3. Go to [https://genius.com/api-clients](https://genius.com/api-clients)
4. Create API client
5. Copy your:

```
Client Access Token
```

⚠️ Use the **access token**, NOT client ID or secret.

---

## 🗂 Project Structure

```
📁 HummingBot
 │
 ├── hummingbot.py         # main program
 ├── requirements.txt
 ├── README.md
 └── .env (optional)
```

Example `.env`:

```
ACR_HOST=identify-xxxx.acrcloud.com
ACR_KEY=xxxxxxxxxxxxxxxx
ACR_SECRET=xxxxxxxxxxxxx
GENIUS_API_KEY=xxxxxxxxxxxxxxxx
```

---

## ▶️ Running the Program

Start the bot:

```bash
python hummingbot.py
```

You will see:

```
🎤 Start humming the song…
```

Hum for ~10 seconds.

Example output:

```
✔ Song recognized: Perfect — Ed Sheeran
📜 Fetching lyrics…
🎼 Lyrics:
...
```
### Setup for ACRCloud SDK (Installation)

```
git clone https://github.com/acrcloud/acrcloud_sdk_python.git
cd acrcloud_sdk_python
pip install .
```
---

## 🛠 Troubleshooting

### ❗ ACRCloud returns “No result”

* hum the chorus, not the verse
* reduce background noise
* hum louder
* closer microphone

---

### ❗ Genius returns 401 invalid_token

* your access token expired
* your token is wrong
* generate a new one at: [https://genius.com/api-clients](https://genius.com/api-clients)

---

### ❗ Lyrics not found

Some songs may not exist on Genius.
We can optionally add fallback sources like

* Musixmatch
* JioSaavn
* Gaana
* MetroLyrics

---

## 🛡 Legal Notice

Song recognition is done via ACRCloud (licensed).
Lyrics are fetched for personal use only.
Do NOT publicly republish lyrics online.

---

## 👨‍💻 Author

Developed by **Vikrant**
