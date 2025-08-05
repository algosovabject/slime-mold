to oracle:

from datetime import datetime

def get_oracle_mood():
    hour = datetime.now().hour
    if 6 <= hour < 11:
        return "early_morning"
    elif 11 <= hour < 14:
        return "lunch"
    elif 14 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 22:
        return "evening"
    else:
        return "night"




add to run_oracle:

mood = get_oracle_mood()

if mood == "lunch":
    print("The ooze is out to lunch—leave a telepathic message.")
    exit()
elif mood == "night":
    print("The ooze is asleep and dreaming of forgotten books.")
    exit()
