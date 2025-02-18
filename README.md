DJ Music Selection System

Description
This is a rule-based AI system designed to help DJs select the best songs for their events based on:
- Event type (Club, Wedding, House Party, etc.)
- Preferred genre (EDM, Hip-Hop, Pop, etc.)
- BPM range for smooth transitions
- Energy level to match the crowd's vibe
- Key matching for harmonic mixing
- Crowd mood analysis to adjust music dynamically

This system operates without machine learning and relies on predefined rules to generate song recommendations.

Features
Smart rule-based song selection  
Real-time crowd mood adaptation
User preference tracking for personalized suggestions  
BPM & Key Matching for smooth transitions  
Expandable with music API integrations (e.g., Spotify, Apple Music)  

Installation
1. Clone the Repository
```bash
git clone https://github.com/your-username/DJ-Music-Selection.git
cd DJ-Music-Selection
```

2. Install Dependencies
This project does not require external dependencies. However, ensure you have Python installed.

3. Run the Script
```bash
python dj_music_selection.py
```

Usage
1. The system will prompt you for event type, genre, BPM range, and energy level.
2. It will then suggest a song based on predefined rules.
3. Optionally, you can enable key matching or consider crowd mood dynamics for better song transitions.

Example Input/Output

Example 1: Club Event (High Energy EDM)
User Input:
```
Event Type: Club
Genre: EDM
BPM Range: 120 - 140
Energy Level: High
Last Song BPM: 128
Enable Key Matching? Yes
Crowd Mood: Low Energy
```

System Output:
```
Recommended Song: 'Song A' (128 BPM, High Energy, C Major)
```

Example 2: Wedding (Romantic Pop Song)
User Input:
```
Event Type: Wedding
Genre: Pop
BPM Range: 90 - 110
Energy Level: Low
Last Song BPM: 100
Enable Key Matching? No
Crowd Mood: Neutral
```

System Output:
```
Recommended Song: 'Song C' (98 BPM, Low Energy, G Major)
```

Project Structure
```
DJ-Music-Selection/
│── dj_music_selection.py   Main script for song selection
│── requirements.txt        Project dependencies (empty for built-in modules)
│── README.md               Documentation for the project
│── DJ_Music_Selection_System.docx  # Project report
```

Future Enhancements
Spotify API Integration to pull real-time song recommendations  
Machine Learning to predict crowd mood dynamically  
GUI Interface using Tkinter or Streamlit for better usability  

License
This project is open-source under the MIT License.

Author
- P.J. McCoy
- GitHub: NegassiNetwork(https://github.com/negassinetwork)
