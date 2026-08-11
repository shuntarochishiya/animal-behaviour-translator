SIGNALS = [
    {
        "slug": "slow-blinking",
        "name": "Slow blinking",
        "category": "facial",
        "description": (
            "A sequence involving half-blinks, eye narrowing or prolonged "
            "eye closure during social interaction. Experimental research "
            "supports a positive communicative role in cat-human interaction."
        ),
    },
    {
        "slug": "tail-up",
        "name": "Tail held upright",
        "category": "posture",
        "description": (
            "The tail is held vertically upright without piloerection. "
            "This posture is commonly associated with friendly approach "
            "and affiliative social interaction."
        ),
    },
    {
        "slug": "purring",
        "name": "Purring",
        "category": "vocalization",
        "description": (
            "A low-frequency rhythmic vocalization used in several "
            "social and behavioural contexts. Purring should not be "
            "treated as a universal indicator of happiness."
        ),
    },
    {
        "slug": "hissing",
        "name": "Hissing",
        "category": "vocalization",
        "description": (
            "A forceful open-mouth vocalization commonly associated "
            "with defensive, threatening or high-arousal interactions."
        ),
    },
    {
        "slug": "ears-flattened",
        "name": "Flattened ears",
        "category": "facial",
        "description": (
            "The ears are rotated backward or flattened against the head. "
            "This position may occur during fear, anxiety or defensive "
            "behaviour and should be interpreted together with context."
        ),
    },
    {
        "slug": "meowing",
        "name": "Meowing",
        "category": "vocalization",
        "description": (
            "A vocalization commonly directed toward humans. "
            "Domestic cats modify meowing depending on social context, "
            "attention seeking, feeding situations or interaction needs."
        ),
    },
    {
        "slug": "tail-twitching",
        "name": "Tail twitching",
        "category": "movement",
        "description": (
            "Small repeated movements of the tail, especially the tip. "
            "Depending on context this may indicate focused attention, "
            "arousal or increasing irritation."
        ),
    },
    {
        "slug": "tail-lashing",
        "name": "Tail lashing",
        "category": "movement",
        "description": (
            "Forceful sweeping or striking movements of the tail. "
            "This behaviour may occur during frustration, conflict "
            "or high arousal."
        ),
    },
]


SOURCES = [
    {
        "key": "humphrey_2020",
        "title": (
            "The role of cat eye narrowing movements in "
            "cat-human communication"
        ),
        "authors": (
            "Humphrey T., Proops L., Forman J., Spooner R., McComb K."
        ),
        "year": 2020,
        "journal": "Scientific Reports",
        "doi": "10.1038/s41598-020-73426-0",
        "url": (
            "https://www.nature.com/articles/s41598-020-73426-0"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Two experiments found that cats produced more eye narrowing "
            "after human slow-blink stimuli and were more likely to approach "
            "an unfamiliar experimenter after a slow-blink interaction."
        ),
    },
    {
        "key": "deputte_2021",
        "title": (
            "Heads and Tails: An Analysis of Visual Signals "
            "in Cats, Felis catus"
        ),
        "authors": (
            "Deputte B. L., Jumelet E., Gilbert C., Titeux E."
        ),
        "year": 2021,
        "journal": "Animals",
        "doi": "10.3390/ani11092752",
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8469685/"
        ),
        "source_type": "review",
        "evidence_notes": (
            "Analysis and review of visual signalling in domestic cats. "
            "Tail-up is described as an affiliative or friendly social signal."
        ),
    },
    {
        "key": "rodan_2011",
        "title": (
            "AAFP and ISFM Feline-Friendly Handling Guidelines"
        ),
        "authors": (
            "Rodan I., Sundahl E., Carney H., Gagnon A.-C., "
            "Heath S., Landsberg G., Seksel K., Yin S."
        ),
        "year": 2011,
        "journal": "Journal of Feline Medicine and Surgery",
        "doi": "10.1016/j.jfms.2011.03.012",
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11107994/"
        ),
        "source_type": "guideline",
        "evidence_notes": (
            "Guidelines describing behavioural indicators of feline fear, "
            "anxiety and defensive responses, including changes in ear "
            "position, posture, facial expression and vocal behaviour."
        ),
    },
    {
        "key": "tavernier_2020",
        "title": "Feline vocal communication",
        "authors": (
            "Tavernier C., Ahmed S., Houpt K. A., Yeon S. C."
        ),
        "year": 2020,
        "journal": "Journal of Veterinary Science",
        "doi": "10.4142/jvs.2020.21.e18",
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC7000907/"
        ),
        "source_type": "review",
        "evidence_notes": (
            "Review of the domestic cat vocal repertoire and the "
            "context-dependent use of vocalizations including purrs, "
            "meows, growls and hisses."
        ),
    },
]


RULES = [
    {
        "key": "cat_slow_blink_social_interaction",
        "primary_signal_slug": "slow-blinking",
        "context_slug": "human-interaction",
        "supporting_signals": "",
        "interpretation_label": (
            "Positive or affiliative social communication"
        ),
        "interpretation_description": (
            "Slow blinking during interaction with a human is consistent "
            "with a positive or affiliative communicative interaction."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Humphrey et al. experimentally compared slow-blink interaction "
            "with control conditions. Cats showed more eye narrowing during "
            "slow-blink interactions and were more likely to approach a "
            "human after receiving a slow-blink stimulus."
        ),
        "limitations": (
            "Slow blinking should not be treated as a literal statement "
            "of affection or as proof of a single internal emotional state. "
            "Individual variation and surrounding context still matter."
        ),
        "source_keys": [
            "humphrey_2020",
        ],
    },
    {
        "key": "cat_tail_up_greeting",
        "primary_signal_slug": "tail-up",
        "context_slug": "greeting",
        "supporting_signals": "",
        "interpretation_label": (
            "Friendly or affiliative greeting"
        ),
        "interpretation_description": (
            "An upright tail during social approach or greeting is "
            "consistent with friendly or affiliative social intent."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Research on domestic cat visual communication identifies "
            "the upright tail display as a friendly social signal that "
            "commonly occurs during approach and greeting."
        ),
        "limitations": (
            "Tail posture should be evaluated together with the rest of "
            "the body. An upright tail with piloerection or other signs "
            "of arousal may represent a different context."
        ),
        "source_keys": [
            "deputte_2021",
        ],
    },
    {
        "key": "cat_hissing_threat",
        "primary_signal_slug": "hissing",
        "context_slug": "threat",
        "supporting_signals": "ears-flattened",
        "interpretation_label": (
            "Defensive or fear-related response"
        ),
        "interpretation_description": (
            "Hissing in a threatening or highly uncomfortable situation, "
            "especially when accompanied by flattened ears, is consistent "
            "with defensive signalling and an attempt to increase distance "
            "from a perceived threat."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Veterinary behaviour guidelines and reviews of feline "
            "communication identify hissing, altered ear position and "
            "defensive posture as signals occurring during fear, anxiety "
            "and defensive responses."
        ),
        "limitations": (
            "This behaviour does not mean that the cat will attack. "
            "Defensive signals frequently function to avoid or stop "
            "an unwanted interaction."
        ),
        "source_keys": [
            "rodan_2011",
            "tavernier_2020",
        ],
    },
    {
        "key": "cat_meowing_attention",
        "primary_signal_slug": "meowing",
        "context_slug": "attention-seeking",
        "supporting_signals": "",
        "interpretation_label": (
            "Human-directed communication attempt"
        ),
        "interpretation_description": (
            "Meowing directed toward humans in an attention-seeking "
            "context is consistent with a request for interaction, "
            "resources or social contact."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Domestic cats use vocalizations, especially meows, "
            "as part of communication with humans. The meaning "
            "depends strongly on context and individual learning history."
        ),
        "limitations": (
            "A meow alone does not identify a specific request. "
            "Cats may vocalize for food, attention, greeting, "
            "discomfort or other reasons."
        ),
        "source_keys": [
            "tavernier_2020",
        ],
    },
    {
        "key": "cat_tail_twitching_arousal",
        "primary_signal_slug": "tail-twitching",
        "context_slug": "interaction",
        "supporting_signals": "",
        "interpretation_label": (
            "Focused attention or increasing arousal"
        ),
        "interpretation_description": (
            "Tail twitching during interaction may indicate "
            "high attention, excitement or rising arousal."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Feline body language studies describe tail movements "
            "as important visual signals whose interpretation depends "
            "on the surrounding interaction."
        ),
        "limitations": (
            "Tail twitching is not a direct indicator of anger. "
            "The same movement may appear during hunting, play "
            "or focused observation."
        ),
        "source_keys": [
            "deputte_2021",
        ],
    },
    {
        "key": "cat_tail_lashing_irritation",
        "primary_signal_slug": "tail-lashing",
        "context_slug": "interaction",
        "supporting_signals": "ears-flattened",
        "interpretation_label": (
            "Possible irritation or defensive arousal"
        ),
        "interpretation_description": (
            "Strong tail lashing during interaction, especially "
            "combined with flattened ears, is consistent with "
            "increasing irritation or defensive arousal."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Visual communication research identifies tail movement "
            "and ear position as important components of feline "
            "emotional and social signalling."
        ),
        "limitations": (
            "Tail movements are context-dependent. The same behaviour "
            "may occur during play, hunting or frustration."
        ),
        "source_keys": [
            "deputte_2021",
            "rodan_2011",
        ],
    },
]
