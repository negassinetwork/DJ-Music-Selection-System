import random

# Sample dataset of songs
songs = [
    {"title": "Song A", "artist": "DJ X", "genre": "EDM", "BPM": 128, "energy": "high", "key": "C Major"},
    {"title": "Song B", "artist": "DJ Y", "genre": "Hip-Hop", "BPM": 95, "energy": "medium", "key": "A Minor"},
    {"title": "Song C", "artist": "DJ Z", "genre": "Pop", "BPM": 115, "energy": "low", "key": "G Major"},
    {"title": "Song D", "artist": "DJ A", "genre": "EDM", "BPM": 130, "energy": "high", "key": "C Major"},
    {"title": "Song E", "artist": "DJ B", "genre": "Hip-Hop", "BPM": 92, "energy": "medium", "key": "A Minor"},
]

# Function to suggest a song based on user input
def suggest_song(event_type, genre, bpm_range, energy, last_song_bpm, key_match=False, crowd_mood="neutral"):
    filtered_songs = [song for song in songs if 
                      song["genre"] == genre and 
                      song["energy"] == energy and
                      bpm_range[0] <= song["BPM"] <= bpm_range[1]]

    if key_match:
        # Prioritize songs in the same key for harmonic mixing
        filtered_songs = [song for song in filtered_songs if song["key"] == "C Major"]

    # Adjust BPM dynamically based on crowd mood
    if crowd_mood == "low energy":
        filtered_songs = [song for song in filtered_songs if song["BPM"] > last_song_bpm]
    elif crowd_mood == "high energy":
        filtered_songs = [song for song in filtered_songs if song["BPM"] < last_song_bpm]

    # Sort by BPM closeness for smooth transitions
    filtered_songs.sort(key=lambda song: abs(song["BPM"] - last_song_bpm))

    return filtered_songs[0] if filtered_songs else "No matching song found."

# User input
event_type = input("Enter event type (Club, Wedding, House Party, Lounge): ").strip()
genre = input("Enter preferred genre (EDM, Hip-Hop, Pop): ").strip()
bpm_min = int(input("Enter minimum BPM: "))
bpm_max = int(input("Enter maximum BPM: "))
energy = input("Enter energy level (low, medium, high): ").strip()
last_song_bpm = int(input("Enter BPM of last song played: "))
key_match = input("Enable key matching? (yes/no): ").strip().lower() == "yes"
crowd_mood = input("Enter crowd mood (low energy, neutral, high energy): ").strip()

# Suggest a song
suggested_song = suggest_song(event_type, genre, (bpm_min, bpm_max), energy, last_song_bpm, key_match, crowd_mood)
print("Recommended Song:", suggested_song)
