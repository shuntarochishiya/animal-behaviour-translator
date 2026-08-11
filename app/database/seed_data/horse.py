SIGNALS = [
    {
        "slug": "ears-forward",
        "name": "Ears forward",
        "category": "facial",
        "description": (
            "Ears directed forward toward a stimulus. "
            "This position is commonly associated with attention, "
            "interest or orientation toward something in the environment."
        ),
    },
    {
        "slug": "ears-pinned-back",
        "name": "Pinned back ears",
        "category": "facial",
        "description": (
            "Ears rotated strongly backward or flattened toward "
            "the neck. This signal may occur during conflict, "
            "discomfort, threat or high arousal situations."
        ),
    },
    {
        "slug": "tail-swishing",
        "name": "Tail swishing",
        "category": "movement",
        "description": (
            "Repeated sweeping movements of the tail. "
            "Depending on context, this behaviour may indicate "
            "irritation, discomfort, arousal or simple fly avoidance."
        ),
    },
    {
        "slug": "nuzzling",
        "name": "Nuzzling",
        "category": "social",
        "description": (
            "Gentle touching or rubbing with the muzzle during "
            "social interaction with another horse or a human."
        ),
    },
    {
        "slug": "snorting",
        "name": "Snorting",
        "category": "vocalization",
        "description": (
            "A forceful nasal sound that may occur during alertness, "
            "investigation, excitement or emotional arousal."
        ),
    },
    {
        "slug": "whinny",
        "name": "Whinny",
        "category": "vocalization",
        "description": (
            "A long-distance vocalization used in social contact "
            "and communication between horses."
        ),
    },
    {
        "slug": "pawing",
        "name": "Pawing",
        "category": "movement",
        "description": (
            "Repeated striking or scraping of the ground with a hoof. "
            "This behaviour may occur during anticipation, frustration "
            "or stressful situations."
        ),
    },
    {
        "slug": "head-lowering",
        "name": "Head lowering",
        "category": "posture",
        "description": (
            "Lowering the head and neck. This posture is commonly "
            "observed during relaxed states, but interpretation "
            "depends on the surrounding situation."
        ),
    },
]


SOURCES = [
    {
        "key": "wathan_2014",
        "title": (
            "The eyes and ears are key features of facial expressions "
            "in horses"
        ),
        "authors": (
            "Wathan J., Burrows A.M., Waller B.M., McComb K."
        ),
        "year": 2014,
        "journal": "PLOS ONE",
        "doi": "10.1371/journal.pone.0087017",
        "url": (
            "https://journals.plos.org/plosone/article?id=10.1371/"
            "journal.pone.0087017"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Research identifying facial expressions in horses. "
            "The study highlights ears and eyes as important "
            "components of horse facial communication."
        ),
    },
    {
        "key": "proops_2018",
        "title": (
            "The importance of individual recognition in horse-human "
            "communication"
        ),
        "authors": (
            "Proops L., Rayner J., Taylor A.M."
        ),
        "year": 2018,
        "journal": None,
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/"
            "articles/PMC5890092/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Research investigating horse social cognition and "
            "communication with humans."
        ),
    },
    {
        "key": "mcdonnell_2003",
        "title": (
            "The Equid Ethogram: A Practical Field Guide to Horse Behavior"
        ),
        "authors": "Sue McDonnell",
        "year": 2003,
        "journal": None,
        "doi": None,
        "url": (
            "https://www.amazon.com/Equid-Ethogram-Practical-Guide-Behavior/dp/0938666900"
        ),
        "source_type": "behavioural_reference",
        "evidence_notes": (
            "Reference work describing equine behaviour, "
            "including social behaviour, vocalizations and body signals."
        ),
    },
    {
        "key": "hall_2018",
        "title": (
            "The influence of temperament and environment on horse behaviour"
        ),
        "authors": "Hall C. et al.",
        "year": 2018,
        "journal": None,
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/"
            "articles/PMC6069402/"
        ),
        "source_type": "review",
        "evidence_notes": (
            "Review discussing behavioural responses in horses "
            "and the influence of context on interpretation."
        ),
    },
]


RULES = [
    {
        "key": "horse_social_interaction",
        "primary_signal_slug": "nuzzling",
        "context_slug": "social-interaction",
        "supporting_signals": (
            "ears-forward,head-lowering"
        ),
        "interpretation_label": (
            "Calm affiliative social interaction"
        ),
        "interpretation_description": (
            "Nuzzling combined with relaxed body signals such as "
            "forward ears or lowered head position is consistent "
            "with a calm social interaction."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Horse social behaviour research describes physical "
            "contact, facial expressions and posture as important "
            "components of equine communication."
        ),
        "limitations": (
            "Touching behaviour can have different motivations "
            "depending on the relationship between the horse and "
            "the interaction partner."
        ),
        "source_keys": [
            "mcdonnell_2003",
            "proops_2018",
        ],
    },
    {
        "key": "horse_attention_interest",
        "primary_signal_slug": "ears-forward",
        "context_slug": "observation",
        "supporting_signals": "",
        "interpretation_label": (
            "Attention or interest toward a stimulus"
        ),
        "interpretation_description": (
            "Forward-directed ears are consistent with a horse "
            "orienting attention toward something in the environment."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Research on equine facial expressions identifies "
            "ear position as an important component of horse "
            "communication and attention."
        ),
        "limitations": (
            "Forward ears indicate orientation, not necessarily "
            "positive emotion. The surrounding context remains important."
        ),
        "source_keys": [
            "wathan_2014",
        ],
    },
    {
        "key": "horse_irritation",
        "primary_signal_slug": "tail-swishing",
        "context_slug": "interaction",
        "supporting_signals": (
            "ears-pinned-back"
        ),
        "interpretation_label": (
            "Possible irritation or discomfort"
        ),
        "interpretation_description": (
            "Strong tail movements combined with pinned-back ears "
            "may indicate irritation, discomfort or defensive arousal."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Equine behaviour references describe tail movements "
            "and ear positions as important indicators of emotional "
            "and social states."
        ),
        "limitations": (
            "Tail swishing can also occur because of insects or "
            "normal movement. It should not be interpreted alone."
        ),
        "source_keys": [
            "mcdonnell_2003",
            "wathan_2014",
        ],
    },
    {
        "key": "horse_vocal_social_contact",
        "primary_signal_slug": "whinny",
        "context_slug": "social-interaction",
        "supporting_signals": "",
        "interpretation_label": (
            "Social contact vocalization"
        ),
        "interpretation_description": (
            "Whinnying is consistent with long-distance social "
            "communication between horses."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Horse vocalizations are used for maintaining contact "
            "with other horses and communicating social information."
        ),
        "limitations": (
            "A vocalization alone does not reveal a specific "
            "emotional state or intention."
        ),
        "source_keys": [
            "mcdonnell_2003",
        ],
    },
    {
        "key": "horse_stress_frustration",
        "primary_signal_slug": "pawing",
        "context_slug": "stressful-situation",
        "supporting_signals": (
            "tail-swishing"
        ),
        "interpretation_label": (
            "Possible frustration or stress-related behaviour"
        ),
        "interpretation_description": (
            "Repeated pawing, especially combined with other signs "
            "of arousal, is consistent with frustration, anticipation "
            "or stress-related behaviour."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Behavioural references describe pawing as a behaviour "
            "that may occur during frustration, anticipation or "
            "elevated arousal."
        ),
        "limitations": (
            "Pawing is not specific to stress and may occur in "
            "feeding anticipation or other contexts."
        ),
        "source_keys": [
            "mcdonnell_2003",
            "hall_2018",
        ],
    },
]
