import random

MOOD_RESPONSES = {
    "bubbling with ideas": [
        "The ooze is effervescent and eager to answer.",
        "Ideas are fizzing on the surface!",
        "The ooze vibrates like a thought about to hatch.",
        "*glooop* It seems excited to speak today.",
        "An idea sloshes to the surface... it's yours now."
    ],
    "secretive and still": [
        "The ooze coils into itself, reluctant to speak.",
        "A single slow bubble rises... and pops.",
        "The ooze doesn't blink. Or move. Or breathe.",
        "You feel watched. There's no sound.",
        "The silence is... almost sticky."
    ],
    "wild and cryptic": [
        "*POP* You hear a voice, but it’s backwards.",
        "The ooze grins at you without a mouth.",
        "The ooze screeches in three tones simultaneously.",
        "*SPLAT!* A vision lands at your feet.",
        "It barks. Was that an answer or a threat?"
    ],
     "curious and optimistic": [
        "The ooze wiggles as if it has a question *for you*.",
        "*boing* It wants to know what you think too.",
        "A glowing tendril pokes out expectantly."
    ],
    "chaotic and bold": [
        "The oracle leaps into a jar and smashes it.",
        "*THWAP* You have its full attention.",
        "It is vibrating at frequencies unknown to man."
    ],
    "withdrawn and tired": [
        "The ooze is... taking a nap? You guess?",
        "*blub blub*—is that snoring?",
        "It rolls away slowly, but stops for you."
    ],
    "visibly annoyed": [
        "*blorp* The ooze flattens in protest.",
        "You again? It squelches begrudgingly.",
        "*slap* A pseudopod flails. You've been warned."
    ],
    "uncertain": [
        "The oracle looks around like it just woke up.",
        "Is it... shy? Maybe it forgot your name.",
        "The ooze makes a low... shrugging noise?"
    ],

    "pre-dawn": ["The ooze trembles in the shadows..."],
    "morning": ["It stretches like a sleepy tide pool."],
    "afternoon": ["The ooze perks up and spits out a syllable."],
    "evening": ["A calm ripple spreads across the goo."],
    "night": ["The oracle gurgles under moonlight."],
    
    "new": ["It is still. Watching. Waiting."],
    "waxing": ["The ooze seems eager to grow."],
    "full": ["The ooze is BOLD and LOUD today."],
    "waning": ["It exhales a single, echoing bubble."],
    
    "repetitive": ["It blorps in passive-aggressive protest."],
    "varied": ["The ooze seems intrigued by your shifting thoughts."],
    "unknown": ["The oracle looks a little lost today."],
}

SEASON_RESPONSES = {
    "spring": [
        "The ooze twitches like a sprouting seed.",
        "Oozey hums a pollen-heavy tune.",
        "It tries to bloom... then forgets why."
    ],
    "summer": [
        "The ooze glistens in the heat. It’s cranky.",
        "A sunbeam hits the jar. Oozey evaporates a little.",
        "The oracle sighs, ‘Too bright for thinking...’"
    ],
    "fall": [
        "The ooze weeps amber droplets.",
        "Dead thoughts float to the surface.",
        "It whispers, ‘Everything decays beautifully.’"
    ],
    "winter": [
        "Frost gathers on the glass. The ooze barely stirs.",
        "It’s coiled into itself, dreaming of warmth.",
        "A chill ripple passes through. You are not welcome."
    ]
}

def get_flavor_line(mood_phrase):
    return random.choice(MOOD_RESPONSES.get(mood_phrase, ["The ooze oozes in silence."]))

def get_season_flavor(season_key):
    return random.choice(SEASON_RESPONSES.get(season_key, ["The ooze exists out of season."]))
