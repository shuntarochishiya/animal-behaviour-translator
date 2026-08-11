SIGNALS = [
    {
        "slug": "trunk-touching",
        "name": "Trunk touching",
        "category": "social",
        "description": (
            "Physical contact made with the trunk during interaction "
            "with another elephant. Trunk-mediated contact occurs in "
            "greeting and other social contexts."
        ),
    },
    {
        "slug": "trunk-raised",
        "name": "Raised trunk",
        "category": "posture",
        "description": (
            "The trunk is lifted upward, often while the elephant "
            "samples airborne chemical information or directs attention "
            "toward a stimulus."
        ),
    },
    {
        "slug": "ears-spread",
        "name": "Ears spread",
        "category": "posture",
        "description": (
            "The ears are extended outward, increasing the apparent "
            "size of the head. This display may occur during heightened "
            "attention, social signalling or threat-related situations."
        ),
    },
    {
        "slug": "ear-flapping",
        "name": "Ear flapping",
        "category": "movement",
        "description": (
            "Repeated movement of the ears. Ear flapping participates "
            "in thermoregulation and may also occur during social or "
            "high-arousal situations."
        ),
    },
    {
        "slug": "trumpeting",
        "name": "Trumpeting",
        "category": "vocalization",
        "description": (
            "A loud elephant vocalization generally associated with "
            "high arousal. Trumpets may occur in fearful, aggressive, "
            "playful or socially excited situations."
        ),
    },
    {
        "slug": "rumbling",
        "name": "Rumbling",
        "category": "vocalization",
        "description": (
            "A low-frequency vocalization widely used in elephant "
            "communication. Rumbles occur across multiple social and "
            "environmental contexts."
        ),
    },
    {
        "slug": "head-raising",
        "name": "Head raising",
        "category": "posture",
        "description": (
            "Raising the head during an interaction. This movement "
            "may accompany greeting, alertness or heightened attention."
        ),
    },
    {
        "slug": "rapid-retreat",
        "name": "Rapid retreat",
        "category": "movement",
        "description": (
            "Quick movement away from a stimulus. In an appropriate "
            "context this may form part of an avoidance or alarm response."
        ),
    },
]


SOURCES = [
    {
        "key": "allen_2021",
        "title": (
            "Function of Trunk-Mediated 'Greeting' Behaviours between "
            "Male African Elephants: Insights from Choice of Partners"
        ),
        "authors": "Allen C. R. B. et al.",
        "year": 2021,
        "journal": "Animals",
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8467434/"
        ),
        "source_type": "observational",
        "evidence_notes": (
            "Observational study of trunk-mediated greeting behaviour "
            "between male African elephants, examining the social "
            "function of trunk contact and partner choice."
        ),
    },
    {
        "key": "eleuteri_2024",
        "title": (
            "Multimodal communication and audience directedness "
            "in the greeting behaviour of African savannah elephants"
        ),
        "authors": "Eleuteri V. et al.",
        "year": 2024,
        "journal": "Communications Biology",
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11082179/"
        ),
        "source_type": "observational",
        "evidence_notes": (
            "Study of greeting interactions in African savannah elephants. "
            "Elephants used combinations of visual, tactile and acoustic "
            "signals and adjusted signal modality according to the "
            "recipient's visual attention."
        ),
    },
    {
        "key": "fuchs_2021",
        "title": (
            "Acoustic structure and information content of trumpets "
            "in African savanna elephants"
        ),
        "authors": "Fuchs E. et al.",
        "year": 2021,
        "journal": "Scientific Reports",
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8610244/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Study of elephant trumpets and their acoustic properties. "
            "Trumpeting was associated with highly stimulated states "
            "including fear, aggression, play and social excitement."
        ),
    },
    {
        "key": "king_2010",
        "title": (
            "Bee Threat Elicits Alarm Call in African Elephants"
        ),
        "authors": (
            "King L. E., Soltis J., Douglas-Hamilton I., "
            "Savage A., Vollrath F."
        ),
        "year": 2010,
        "journal": "PLoS ONE",
        "doi": "10.1371/journal.pone.0010346",
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC2859947/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Playback experiments showed that African elephants "
            "produced distinctive rumble vocalizations in response "
            "to bee threat and displayed coordinated avoidance behaviour."
        ),
    },
    {
        "key": "stoeger_2021",
        "title": (
            "Operant control and call usage learning in African elephants"
        ),
        "authors": "Stoeger A. S. et al.",
        "year": 2021,
        "journal": "Philosophical Transactions of the Royal Society B",
        "doi": None,
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC8419571/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Study demonstrating flexible production of several "
            "African elephant call types, supporting the complexity "
            "and context sensitivity of elephant vocal communication."
        ),
    },
]


RULES = [
    {
        "key": "elephant_trunk_touch_greeting",
        "primary_signal_slug": "trunk-touching",
        "context_slug": "greeting",
        "supporting_signals": "head-raising",
        "interpretation_label": (
            "Social greeting or affiliative contact"
        ),
        "interpretation_description": (
            "Trunk-mediated contact during greeting is consistent "
            "with socially directed greeting behaviour between elephants."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Observational research on African elephants documents "
            "trunk-mediated contact as part of greeting behaviour. "
            "Greeting interactions can combine tactile, visual and "
            "acoustic signals."
        ),
        "limitations": (
            "Trunk contact is not exclusive to greeting and may occur "
            "during reassurance, investigation or other social interactions. "
            "The relationship between the elephants and the wider interaction "
            "context should also be considered."
        ),
        "source_keys": [
            "allen_2021",
            "eleuteri_2024",
        ],
    },
    {
        "key": "elephant_multimodal_greeting",
        "primary_signal_slug": "head-raising",
        "context_slug": "greeting",
        "supporting_signals": "trunk-touching,ear-flapping",
        "interpretation_label": (
            "Multimodal greeting interaction"
        ),
        "interpretation_description": (
            "Head movement combined with tactile or audible body signals "
            "during reunion is consistent with a multimodal greeting display."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Research on African savannah elephant greetings found "
            "that elephants combine visual, tactile and acoustic behaviours "
            "and alter communication according to whether the recipient "
            "is visually attending."
        ),
        "limitations": (
            "No individual gesture should be treated as having one fixed "
            "meaning. Interpretation depends on the combination of signals, "
            "the recipient's attention and the social situation."
        ),
        "source_keys": [
            "eleuteri_2024",
        ],
    },
    {
        "key": "elephant_trumpet_high_arousal",
        "primary_signal_slug": "trumpeting",
        "context_slug": "high-arousal",
        "supporting_signals": "",
        "interpretation_label": (
            "High-arousal vocal communication"
        ),
        "interpretation_description": (
            "Trumpeting is consistent with a highly aroused state, "
            "but the emotional and behavioural context may vary."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Acoustic research reports trumpeting in several highly "
            "stimulating situations, including fear, aggression, play "
            "and social excitement."
        ),
        "limitations": (
            "Trumpeting does not uniquely indicate fear or aggression. "
            "The same call type may occur in positive and negative "
            "high-arousal situations."
        ),
        "source_keys": [
            "fuchs_2021",
            "stoeger_2021",
        ],
    },
    {
        "key": "elephant_rumble_alarm",
        "primary_signal_slug": "rumbling",
        "context_slug": "threat",
        "supporting_signals": "rapid-retreat",
        "interpretation_label": (
            "Possible alarm or threat-related response"
        ),
        "interpretation_description": (
            "Rumbling together with rapid avoidance behaviour in a "
            "threatening context is consistent with an alarm response."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Experimental playback research found distinctive rumbles "
            "and coordinated behavioural responses when African elephants "
            "were exposed to bee threat."
        ),
        "limitations": (
            "Rumbles form a broad and diverse vocal category and are "
            "used in many non-alarm situations. A rumble without information "
            "about the stimulus and accompanying behaviour is insufficient "
            "for an alarm interpretation."
        ),
        "source_keys": [
            "king_2010",
            "stoeger_2021",
        ],
    },
    {
        "key": "elephant_ears_spread_threat",
        "primary_signal_slug": "ears-spread",
        "context_slug": "threat",
        "supporting_signals": "trumpeting",
        "interpretation_label": (
            "Possible threat-related visual display"
        ),
        "interpretation_description": (
            "Ear spreading during a threatening interaction, particularly "
            "when accompanied by high-arousal vocal behaviour, is consistent "
            "with heightened attention or a threat-related display."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "African elephant communication is multimodal, with visual "
            "body displays occurring alongside acoustic and tactile signals. "
            "Trumpeting provides additional evidence of high arousal."
        ),
        "limitations": (
            "Ear position alone cannot determine aggression or intent. "
            "Ear movements also occur for non-communicative physiological "
            "reasons, including thermoregulation."
        ),
        "source_keys": [
            "eleuteri_2024",
            "fuchs_2021",
        ],
    },
    {
        "key": "elephant_ear_flapping_greeting",
        "primary_signal_slug": "ear-flapping",
        "context_slug": "greeting",
        "supporting_signals": "trunk-touching",
        "interpretation_label": (
            "Greeting-related body movement"
        ),
        "interpretation_description": (
            "Ear flapping occurring together with socially directed "
            "trunk contact during greeting is consistent with part "
            "of a multimodal greeting interaction."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Observed African elephant greeting sequences include "
            "audible body movements and tactile behaviours, and elephants "
            "combine different modalities depending on the recipient."
        ),
        "limitations": (
            "Ear flapping also serves thermoregulation and therefore "
            "should never be interpreted as a social signal in isolation."
        ),
        "source_keys": [
            "eleuteri_2024",
        ],
    },
]
