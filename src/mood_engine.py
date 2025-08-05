import datetime
import pytz 
from astral import Astral

a = Astral()
a.solar_depression = 'civil'

# Define city where Lil Oozey lives
city = a['Atlanta']

now = datetime.datetime.now()
hour = now.hour

# Mood definitions based on time of day
TIME_MOODS = {
    "pre-dawn": "hushed and twitchy",
    "morning": "slow and thoughtful",
    "afternoon": "bubbling with ideas",
    "evening": "moody and introspective",
    "night": "wild and cryptic"
}

# Mood definitions based on moon phase
MOON_MOODS = {
    "new": "secretive and still",
    "waxing": "curious and optimistic",
    "full": "chaotic and bold",
    "waning": "withdrawn and tired"
}

# Mood definitions based on season
SEASON_MOODS = {
    "spring": "bright and playful",
    "summer": "lazy and dreamy",
    "autumn": "reflective and melancholy",
    "winter": "sluggish and frostbitten"
}

def get_time_of_day():
    if 5 <= hour < 9:
        return "pre-dawn"
    elif 9 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

def get_moon_phase_name():
    phase = a.moon_phase(datetime.date.today())

    if phase == 0:
        return "new"
    elif 1 <= phase < 7:
        return "waxing"
    elif 7 <= phase < 14:
        return "full"
    elif 14 <= phase < 21:
        return "waning"
    elif 21 <= phase < 28:
        return "waning"
    else:
        return "new"

def get_season(date=None):
    if date is None:
        date = datetime.date.today()
        
    year = date.year
    spring = datetime.date(year, 3, 20)
    summer = datetime.date(year, 6, 21)
    fall = datetime.date(year, 9, 22)
    winter = datetime.date(year, 12, 21)

    if spring <= date < summer:
        return "spring"
    elif summer <= date < fall:
        return "summer"
    elif fall <= date < winter:
        return "fall"
    else:
        return "winter"      

def get_usage_pattern(log_path="data/query_log.csv"):
    try:
        with open(log_path, "r") as f:
            recent = f.readlines()[-5:]
            questions = [line.split(",")[0].strip() for line in recent]
            if len(set(questions)) <= 2:
                return "repetitive"
            return "varied"
    except FileNotFoundError:
        return "unknown"

def get_oracle_mood():
    time_mood_key = get_time_of_day()
    moon_mood_key = get_moon_phase_name()
    usage_mood = get_usage_pattern()

    time_mood = TIME_MOODS.get(time_mood_key, "indescribable")
    moon_mood = MOON_MOODS.get(moon_mood_key, "unfathomable")

    season_key = get_season()
    season_mood = SEASON_MOODS.get(season_key, "timeless")

    vibe = f"{time_mood}, {moon_mood}, {season_mood}"

    if usage_mood == "repetitive":
        vibe += ", visibly annoyed"
    elif usage_mood == "unknown":
        vibe += ", uncertain"

    return {
        "time": time_mood_key,
        "moon": moon_mood_key,
        "season": season_key,
        "usage": usage_mood,
        "vibe": vibe
    }
