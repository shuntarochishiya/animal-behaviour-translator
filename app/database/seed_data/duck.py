SIGNALS = [
    {
        "slug": "quacking",
        "name": "Quacking / contact vocalization",
        "category": "vocalization",
        "description": (
            "A quack-like or contact vocalization produced by a duck. "
            "Mallard vocal behaviour varies with context, including "
            "parent-young communication and other social situations."
        ),
    },
    {
        "slug": "alarm-call",
        "name": "Alarm call",
        "category": "vocalization",
        "description": (
            "A threat-related maternal vocalization. Experimental work "
            "with mallard ducklings has shown that species-typical maternal "
            "alarm calls can inhibit vocal and locomotor behaviour."
        ),
    },
    {
        "slug": "freezing",
        "name": "Freezing",
        "category": "posture",
        "description": (
            "A marked reduction or cessation of locomotor and vocal "
            "activity. In mallard ducklings this response has been "
            "experimentally studied following maternal alarm calls."
        ),
    },
    {
        "slug": "head-bobbing",
        "name": "Repeated head movement / bobbing",
        "category": "display",
        "description": (
            "Repeated or stereotyped movement of the head during a social "
            "interaction. Mallard courtship includes several characteristic "
            "head movements and postural display sequences."
        ),
    },
    {
        "slug": "tail-wagging",
        "name": "Rapid tail wagging",
        "category": "movement",
        "description": (
            "Rapid side-to-side movement of the tail. Tail wagging has "
            "been documented in mallards after flight and also occurs "
            "within some behavioural display sequences."
        ),
    },
    {
        "slug": "preening",
        "name": "Preening",
        "category": "maintenance",
        "description": (
            "Feather-maintenance behaviour involving manipulation and "
            "cleaning of the plumage with the bill. Wet preening is an "
            "important water-related maintenance behaviour in ducks."
        ),
    },
    {
        "slug": "wing-flapping",
        "name": "Wing flapping",
        "category": "movement",
        "description": (
            "Repeated movement or extension of the wings. Wing movements "
            "may occur during maintenance, locomotor or social activity, "
            "so surrounding context is required for interpretation."
        ),
    },
]


SOURCES = [
    {
        "key": "miller_gottlieb_1978",
        "title": (
            "Maternal vocalizations of mallard ducks "
            "(Anas platyrhynchos)"
        ),
        "authors": (
            "Miller D.B., Gottlieb G."
        ),
        "year": 1978,
        "journal": "Animal Behaviour",
        "doi": "10.1016/0003-3472(78)90108-2",
        "url": (
            "https://www.sciencedirect.com/science/article/"
            "pii/0003347278901082"
        ),
        "source_type": "observational",
        "evidence_notes": (
            "Field recordings and analysis of species-typical maternal "
            "vocalizations produced by mallard hens during incubation, "
            "brooding and nest-exodus contexts."
        ),
    },
    {
        "key": "finley_1983",
        "title": (
            "A new look at the features of mallard courtship displays"
        ),
        "authors": (
            "Finley J., Ireton D., Schleidt W.M., Thompson T.A."
        ),
        "year": 1983,
        "journal": "Animal Behaviour",
        "doi": "10.1016/S0003-3472(83)80053-0",
        "url": (
            "https://www.sciencedirect.com/science/article/"
            "pii/S0003347283800530"
        ),
        "source_type": "observational",
        "evidence_notes": (
            "Single-frame analysis of stereotyped mallard courtship "
            "displays, including head-flick, head-shake, grunt-whistle, "
            "down-up, head-up-tail-up, bill-dip and nod-swimming."
        ),
    },
    {
        "key": "miller_blaich_1986",
        "title": (
            "Alarm call responsivity of mallard ducklings: "
            "III. Acoustic features affecting behavioral inhibition"
        ),
        "authors": (
            "Miller D.B., Blaich C.F."
        ),
        "year": 1986,
        "journal": "Developmental Psychobiology",
        "doi": "10.1002/dev.420190402",
        "url": (
            "https://pubmed.ncbi.nlm.nih.gov/3732620/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Experimental study showing vocal and locomotor inhibition "
            "in domestic mallard ducklings exposed to maternal alarm "
            "calls, with particular sensitivity to call repetition rate."
        ),
    },
    {
        "key": "hailman_baylis_1991",
        "title": (
            "Post-flight Tail-wagging in the Mallard"
        ),
        "authors": (
            "Hailman J.P., Baylis J.R."
        ),
        "year": 1991,
        "journal": "Journal of Field Ornithology",
        "doi": None,
        "url": (
            "https://digitalcommons.usf.edu/jfo/vol62/iss2/13/"
        ),
        "source_type": "observational",
        "evidence_notes": (
            "Field observations and an experiment examining tail-wagging "
            "after flight in mallards. The authors discuss a possible "
            "maintenance function related to resetting feathers disrupted "
            "by strenuous activity."
        ),
    },
    {
        "key": "mi_2020",
        "title": (
            "Lack of access to an open water source for bathing inhibited "
            "the development of the preen gland and preening behavior "
            "in Sanshui White ducks"
        ),
        "authors": (
            "Mi J., Wang H., Chen X., Hartcher K., Wang Y., "
            "Wu Y., Liao X."
        ),
        "year": 2020,
        "journal": "Poultry Science",
        "doi": "10.1016/j.psj.2020.08.018",
        "url": (
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC7647854/"
        ),
        "source_type": "experimental",
        "evidence_notes": (
            "Experimental study showing that access to an open water "
            "source affected preen-gland development and the occurrence "
            "of wet preening behaviour in ducks."
        ),
    },
]


RULES = [
    {
        "key": "duck_parent_young_vocalization",
        "primary_signal_slug": "quacking",
        "context_slug": "parent-young",
        "supporting_signals": "",
        "interpretation_label": (
            "Possible parent-young contact communication"
        ),
        "interpretation_description": (
            "A vocalization produced by an adult female in a parent-young "
            "context is consistent with social communication between "
            "the hen and ducklings."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Field research on mallards documented species-typical "
            "maternal vocalizations during incubation, brooding and "
            "nest-exodus interactions with young."
        ),
        "limitations": (
            "A generic quack cannot be classified as a maternal contact "
            "call from sound description alone. Acoustic characteristics, "
            "sex, age and behavioural context are required."
        ),
        "source_keys": [
            "miller_gottlieb_1978",
        ],
    },
    {
        "key": "duck_alarm_freezing",
        "primary_signal_slug": "freezing",
        "context_slug": "threat",
        "supporting_signals": (
            "alarm-call"
        ),
        "interpretation_label": (
            "Threat-related behavioral inhibition"
        ),
        "interpretation_description": (
            "Freezing or cessation of activity in the presence of an "
            "alarm call is consistent with a threat-related inhibitory "
            "response in mallard ducklings."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Controlled experiments found that mallard ducklings inhibit "
            "both vocal and locomotor behaviour in response to the "
            "species-typical maternal alarm call."
        ),
        "limitations": (
            "The experimental evidence concerns young mallard/Pekin "
            "ducklings responding to maternal alarm calls. Freezing in "
            "an adult duck or in another context cannot automatically "
            "be assigned the same cause."
        ),
        "source_keys": [
            "miller_blaich_1986",
        ],
    },
    {
        "key": "duck_courtship_head_display",
        "primary_signal_slug": "head-bobbing",
        "context_slug": "courtship",
        "supporting_signals": "",
        "interpretation_label": (
            "Possible courtship display"
        ),
        "interpretation_description": (
            "Repeated stereotyped head movements during a courtship "
            "interaction are consistent with the visual display "
            "repertoire of mallards."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Detailed analysis of mallard courtship identified multiple "
            "stereotyped displays involving characteristic movements "
            "and positions of the head and bill."
        ),
        "limitations": (
            "The informal description 'head bobbing' can cover several "
            "different movements. A particular display cannot be "
            "identified reliably without more detailed information "
            "about posture and movement sequence."
        ),
        "source_keys": [
            "finley_1983",
        ],
    },
    {
        "key": "duck_tail_wagging_post_flight",
        "primary_signal_slug": "tail-wagging",
        "context_slug": "after-flight",
        "supporting_signals": "",
        "interpretation_label": (
            "Post-flight maintenance-related movement"
        ),
        "interpretation_description": (
            "Rapid tail wagging immediately after flight is consistent "
            "with a documented post-flight behavioural sequence in "
            "mallards and may contribute to restoring feather position "
            "after strenuous activity."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Field observations found a high occurrence of tail-wagging "
            "after takeoff and landing. An experiment showed that the "
            "behaviour also occurred after flights ending on land, "
            "arguing against a purely water-removal explanation."
        ),
        "limitations": (
            "Tail wagging is not evidence that a duck is happy. "
            "The study concerns post-flight tail wagging and does not "
            "establish a universal emotional meaning for the movement."
        ),
        "source_keys": [
            "hailman_baylis_1991",
        ],
    },
    {
        "key": "duck_tail_wagging_display",
        "primary_signal_slug": "tail-wagging",
        "context_slug": "courtship",
        "supporting_signals": (
            "head-bobbing"
        ),
        "interpretation_label": (
            "Possible component of a courtship display sequence"
        ),
        "interpretation_description": (
            "Tail movement occurring together with stereotyped head "
            "movements during courtship may form part of a broader "
            "mallard display sequence."
        ),
        "evidence_level": "moderate",
        "evidence_basis": (
            "Mallard courtship displays contain coordinated movements "
            "of the head and tail, while tail-wagging has also been "
            "documented around behavioural display sequences."
        ),
        "limitations": (
            "Tail wagging is not specific to courtship. It is also "
            "documented after flight, so courtship should only be "
            "considered when the surrounding social behaviour supports it."
        ),
        "source_keys": [
            "finley_1983",
            "hailman_baylis_1991",
        ],
    },
    {
        "key": "duck_preening_maintenance",
        "primary_signal_slug": "preening",
        "context_slug": "after-bathing",
        "supporting_signals": "",
        "interpretation_label": (
            "Feather maintenance behaviour"
        ),
        "interpretation_description": (
            "Preening following access to water is consistent with normal "
            "feather-maintenance behaviour in ducks."
        ),
        "evidence_level": "strong",
        "evidence_basis": (
            "Experimental research found substantially more wet preening "
            "in ducks given access to an open water pool and linked water "
            "access with development and function of the preen gland."
        ),
        "limitations": (
            "Preening is a maintenance behaviour and should not be treated "
            "as direct evidence of happiness or another specific emotion. "
            "Its frequency can also be affected by housing and water access."
        ),
        "source_keys": [
            "mi_2020",
        ],
    },
]
