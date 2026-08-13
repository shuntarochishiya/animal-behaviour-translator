# Animal Behaviour Translator

A research-based full-stack prototype that interprets observable animal behaviour using a structured scientific knowledge base.

The application does **not** claim to literally translate animal language or read an animal's thoughts. Instead, it compares user-provided observations with species-specific behavioural rules backed by published research and returns one or more cautious interpretations together with an application-generated match score, limitations, and scientific sources.

---

## Supported Species

The current prototype supports:

- Domestic dog (*Canis lupus familiaris*)
- Domestic cat (*Felis catus*)
- Domestic horse (*Equus caballus*)
- African elephant (*Loxodonta africana*)
- Domestic duck (*Anas platyrhynchos domesticus*)

Each species has its own set of observable signals, interpretation rules, evidence descriptions, limitations, and scientific references.

---

## Main Features

- Species-specific behavioural knowledge base
- Multiple observable signals per request
- Context-aware interpretation
- Primary and alternative interpretations
- Scientific evidence level for each rule
- Application-generated match score
- Explicit limitations and uncertainty
- Scientific references attached to rules
- Aggregated evidence summary
- `insufficient_evidence` response when the knowledge base cannot support an interpretation
- FastAPI REST API
- React + TypeScript frontend
- PostgreSQL database
- Docker Compose for local database setup

---

# Technology Stack

## Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- PostgreSQL
- psycopg
- Uvicorn

## Frontend

- React
- TypeScript
- Vite

## Infrastructure

- Docker
- Docker Compose
- PostgreSQL 17 container

---

# Project Structure

```text
animal-behaviour-translator/
├── app/
│   ├── api/
│   │   ├── interpretation.py
│   │   ├── observation_options.py
│   │   └── species.py
│   │
│   ├── database/
│   │   ├── db.py
│   │   ├── seed.py
│   │   └── seed_data/
│   │       ├── __init__.py
│   │       ├── dog.py
│   │       ├── cat.py
│   │       ├── horse.py
│   │       ├── elephant.py
│   │       └── duck.py
│   │
│   ├── models/
│   │   ├── interpretation_rules.py
│   │   ├── rule_source.py
│   │   ├── signals.py
│   │   ├── source.py
│   │   └── species.py
│   │
│   ├── schemas/
│   │   ├── interpretation.py
│   │   ├── observation_options.py
│   │   └── species.py
│   │
│   ├── services/
│   │   └── interpretation_engine.py
│   │
│   ├── main.py
│   └── settings.py
│
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── App.css
│   │   ├── api.ts
│   │   ├── index.css
│   │   └── main.tsx
│   └── ...
│
├── research/
│   ├── dog.md
│   ├── cat.md
│   ├── horse.md
│   └── elephant.md
│
├── compose.yaml
├── requirements.txt
└── README.md
```

---

# Installation and Startup

## 1. Clone the Repository

```bash
git clone https://github.com/shuntarochishiya/animal-behaviour-translator.git
cd animal-behaviour-translator
```

---

## 2. Start PostgreSQL

The project uses PostgreSQL running in Docker.

Start the database:

```bash
docker compose up -d
```

The current local configuration is:

```text
Host: 127.0.0.1
Host port: 55432
Container port: 5432
Database: animal_translator
User: animal_user
```

The non-default host port `55432` is used to avoid conflicts with PostgreSQL instances already using ports such as `5432` or `5433`.

Check that the container is running:

```bash
docker ps
```

The PostgreSQL container should appear as running.

---

## 3. Create a Python Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\activate
```

Install backend dependencies:

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_URL=postgresql+psycopg://animal_user:animal_password@127.0.0.1:55432/animal_translator
```

The real `.env` file should not be committed to Git.

---

## 5. Seed the Knowledge Base

Run:

```bash
python -m app.database.seed
```

Expected output:

```text
Database seed completed.
```

The seed process creates or updates:

- species
- behavioural signals
- scientific sources
- interpretation rules
- relationships between interpretation rules and sources

The seed process is designed to update existing records rather than blindly create duplicate entries.

---

## 6. Start the Backend

Run:

```bash
uvicorn app.main:app
```

Backend:

```text
http://127.0.0.1:8000
```

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

During development, automatic reload can also be enabled:

```bash
uvicorn app.main:app --reload
```

---

## 7. Start the Frontend

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

The Vite development server normally starts at:

```text
http://localhost:5173
```

The frontend communicates with the backend at:

```text
http://127.0.0.1:8000
```

---

# Example Observation

The interpretation endpoint accepts:

- species
- one or more observed signals
- behavioural context

Example:

```json
{
  "species": "dog",
  "signals": [
    "growl",
    "stiff-body",
    "tail-tucked"
  ],
  "context": "threat"
}
```

Duck example:

```json
{
  "species": "duck",
  "signals": [
    "tail-wagging"
  ],
  "context": "after-flight"
}
```

Elephant example:

```json
{
  "species": "african-elephant",
  "signals": [
    "trunk-touching",
    "head-raising"
  ],
  "context": "greeting"
}
```

---

# Response Structure

A successful response contains:

```json
{
  "status": "interpreted",
  "species": "dog",
  "observed_signals": [
    "growl",
    "stiff-body"
  ],
  "context": "resource",
  "primary_interpretation": {
    "...": "..."
  },
  "alternatives": [],
  "evidence_summary": {
    "evidence_basis": [],
    "limitations": [],
    "sources": []
  },
  "disclaimer": "..."
}
```

If the knowledge base contains no relevant rule, the API can return:

```json
{
  "status": "insufficient_evidence",
  "species": "dog",
  "observed_signals": [],
  "context": "",
  "primary_interpretation": null,
  "alternatives": [],
  "evidence_summary": null,
  "disclaimer": "..."
}
```

Returning insufficient evidence is intentional.

The application should prefer uncertainty over inventing an unsupported behavioural interpretation.

---

# Knowledge Base Architecture

The runtime knowledge base is stored in PostgreSQL.

The source data used to populate the database is stored in:

```text
app/database/seed_data/
```

Each species module contains three main structures:

```python
SIGNALS = [...]
SOURCES = [...]
RULES = [...]
```

---

## Species

The `species` table stores:

- slug
- common name
- scientific name
- description

Example:

```text
slug: african-elephant
common name: African elephant
scientific name: Loxodonta africana
```

---

## Signals

The `signals` table stores directly observable behaviour.

Examples include:

```text
dog:
growl
play-bow
stiff-body

cat:
slow-blinking
tail-up
hissing

horse:
ears-forward
tail-swishing
pawing

African elephant:
trunk-touching
trumpeting
rumbling

duck:
tail-wagging
head-bobbing
preening
```

A signal contains:

- species
- slug
- name
- category
- behavioural description

Signals describe observations rather than assumed emotions.

For example:

```text
tail-wagging
```

is an observation.

It is not automatically converted into:

```text
happy
```

without behavioural and scientific context.

---

## Scientific Sources

Scientific references are stored in the `sources` table.

Each source contains:

- unique source key
- title
- authors
- publication year
- journal
- DOI
- URL
- source type
- evidence notes

Sources are stored separately because one publication may support multiple behavioural rules.

---

## Interpretation Rules

The `interpretation_rules` table contains the behavioural knowledge used by the interpretation engine.

Each rule contains:

- species
- unique rule key
- primary signal
- context
- supporting signals
- interpretation label
- interpretation description
- evidence level
- evidence basis
- limitations

Conceptual example:

```text
Species:
dog

Primary signal:
growl

Supporting signal:
stiff-body

Context:
resource

Possible interpretation:
competitive or warning-related communication
```

The rule does not state that every dog growl always means aggression.

---

## Rule–Source Relationship

The `rule_source` table connects interpretation rules to scientific publications.

Conceptually:

```text
InterpretationRule
        ↓
RuleSource
        ↓
Source
```

This allows the API to return the scientific references associated with every interpretation.

---

# How the Interpretation Logic Works

The project uses a deterministic rule-based interpretation engine.

There is no language model making behavioural decisions at runtime.

The current process is:

1. Receive species, observed signals and context.
2. Find the requested species in PostgreSQL.
3. Convert selected signals into a normalized set.
4. Load all interpretation rules belonging to that species.
5. Parse the rule's supporting signals.
6. Check whether the primary signal matches.
7. Check whether any supporting signals match.
8. Discard rules for which neither the primary nor any supporting signal is observed.
9. Compare the submitted context with the rule context.
10. Determine matched and missing supporting signals.
11. Calculate the application-generated match score.
12. Load scientific sources associated with the rule.
13. Sort candidate interpretations by match score.
14. Return the highest-ranked interpretation as the primary interpretation.
15. Return the remaining matched rules as alternatives.
16. Aggregate evidence, limitations and unique scientific sources into an evidence summary.

The system therefore uses:

```text
observed behaviour
        +
context
        +
species-specific rules
        +
scientific sources
        ↓
possible interpretation
```

rather than:

```text
one signal = one fixed meaning
```

---

# Match Score / Confidence

The API exposes:

```text
system_match_score
```

This score is generated by the application.

It is **not**:

- a probability reported by a scientific paper
- a machine-learning confidence value
- a calibrated probability of correctness
- proof of an animal's internal emotional state

The current scoring system is:

| Component | Score |
|---|---:|
| Primary signal matches | +40 |
| Context matches | +30 |
| Supporting signals | up to +20 |
| Signals and context were supplied | +10 |

---

## Supporting Signal Score

If a rule contains supporting signals, the available 20 points are awarded proportionally.

Conceptually:

```text
support score =
20 × matched supporting signals / required supporting signals
```

For example:

```text
required supporting signals: 2
matched supporting signals: 1
```

produces:

```text
10 points
```

If a rule requires no supporting signals, the rule currently receives the full 20 supporting-signal points.

---

## Scientific Evidence Cap

After the match score is calculated, it is capped according to the rule's scientific evidence level.

| Evidence level | Maximum score |
|---|---:|
| strong | 100 |
| moderate | 75 |
| limited | 50 |

These caps are project-defined heuristics.

They are **not numerical values taken from the cited scientific publications**.

---

# Scientific Evidence vs System Match

The project deliberately separates two concepts.

## Scientific Evidence

Examples:

```text
strong
moderate
limited
```

This describes how directly the interpretation rule is supported by the stored research.

## System Match Score

Example:

```text
70 / 100
```

This describes how closely the submitted observation matches the stored rule according to the application's algorithm.

A high match score does not mean that a scientific paper reports a 70%, 80%, or 100% probability.

---

# Evidence Summary

Multiple rules may match the same observation.

For this reason, the API also returns:

```text
evidence_summary
```

The evidence summary contains:

- unique evidence-basis statements
- unique limitations
- unique scientific sources

Conceptually:

```text
selected signals
        ↓
matched rules
        ↓
scientific evidence from those rules
        ↓
aggregated evidence summary
```

This prevents the interface from displaying scientific support only for the highest-ranked interpretation.

The current implementation aggregates evidence from matched interpretation rules.

---

# Scientific Source Policy

Scientific traceability is a core design requirement of this project.

The following rules are used:

1. Behavioural claims should be based on identifiable real publications or established behavioural references.
2. Source metadata is stored in the database.
3. Sources include a usable URL and/or DOI whenever available.
4. AI-generated citations must not be accepted as scientific evidence without verification.
5. Rules and sources are stored separately.
6. Each behavioural rule includes limitations.
7. Behaviour is treated as context-dependent.
8. The application does not claim literal animal-language translation.
9. When evidence is insufficient, the application may return `insufficient_evidence`.

The full machine-readable source metadata is stored in:

```text
app/database/seed_data/dog.py
app/database/seed_data/cat.py
app/database/seed_data/horse.py
app/database/seed_data/elephant.py
app/database/seed_data/duck.py
```

and is copied into PostgreSQL by the seed process.

---

# Key Scientific References

The following publications represent the main scientific basis of the current knowledge base.

The complete source-to-rule relationships are stored in the database.

---

## Dogs

### Siniscalchi et al. — Dog communication

Siniscalchi M., d'Ingeo S., Minunno M., Quaranta A. (2018).

**Communication in Dogs.**

*Animals*, 8(8), 131.

DOI:

```text
10.3390/ani8080131
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC6116041/

---

### Faragó et al. — Dog growls

Faragó T., Takács N., Miklósi Á., Pongrácz P. (2017).

**Dog growls express various contextual and affective content for human listeners.**

*Royal Society Open Science*, 4, 170134.

DOI:

```text
10.1098/rsos.170134
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC5451822/

---

### Byosiere et al. — Play bows

Byosiere S.E. et al. (2016).

**Investigating the Function of Play Bows in Dog and Wolf Puppies.**

*PLoS ONE.*

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC5199004/

---

### Maglieri et al. — Play continuation

Maglieri V. et al. (2022).

**Don't stop me now, I'm having such a good time: Domestic dogs use play bows to maintain social play.**

*Current Zoology.*

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC10039175/

---

### Leonetti et al. — Tail wagging

Leonetti S. et al. (2024).

**Why do dogs wag their tails?**

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC10792393/

---

### Riemer — Fear and aggression

Riemer S. (2021).

**A Review on Mitigating Fear and Aggression in Dogs and Cats in a Veterinary Setting.**

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC7826566/

---

# Cats

### Humphrey et al. — Slow blinking

Humphrey T., Proops L., Forman J., Spooner R., McComb K. (2020).

**The role of cat eye narrowing movements in cat-human communication.**

*Scientific Reports.*

DOI:

```text
10.1038/s41598-020-73426-0
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC7536207/

---

### Deputte et al. — Visual signals

Deputte B.L. et al. (2021).

**Heads and Tails: An Analysis of Visual Signals in Cats, Felis catus.**

*Animals*, 11(9), 2752.

DOI:

```text
10.3390/ani11092752
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC8469685/

---

### Rodan et al. — Feline behaviour and handling

Rodan I. et al. (2011).

**AAFP and ISFM Feline-Friendly Handling Guidelines.**

*Journal of Feline Medicine and Surgery*, 13, 364–375.

DOI:

```text
10.1016/j.jfms.2011.03.012
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC11107994/

---

### Tavernier et al. — Vocal communication

Tavernier C., Ahmed S., Houpt K.A., Yeon S.C. (2020).

**Feline vocal communication.**

*Journal of Veterinary Science*, 21, e18.

DOI:

```text
10.4142/jvs.2020.21.e18
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC7000907/

---

# Horses

### McDonnell — Equine ethogram

McDonnell S.M. (2003).

**The Equid Ethogram: A Practical Field Guide to Horse Behavior.**

Eclipse Press.

URL:

https://books.google.com/books/about/The_Equid_Ethogram.html?id=-Mvm9NjH0WUC

---

### Wathan et al. — Equine facial actions

Wathan J., Burrows A.M., Waller B.M., McComb K. (2015).

**EquiFACS: The Equine Facial Action Coding System.**

*PLoS ONE*, 10(8), e0131738.

DOI:

```text
10.1371/journal.pone.0131738
```

URL:

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0131738

---

### Proops et al. — Human communication cues

Proops L., Rayner J., Taylor A.M., McComb K. (2013).

**The Responses of Young Domestic Horses to Human-Given Cues.**

*PLoS ONE.*

DOI:

```text
10.1371/journal.pone.0067000
```

URL:

https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0067000

---

# African Elephants

### Allen et al. — Trunk-mediated greeting

Allen C.R.B. et al. (2021).

**Function of Trunk-Mediated "Greeting" Behaviours between Male African Elephants: Insights from Choice of Partners.**

*Animals.*

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC8467434/

---

### Eleuteri et al. — Multimodal greeting

Eleuteri V. et al. (2024).

**Multimodal communication and audience directedness in the greeting behaviour of African savannah elephants.**

*Communications Biology.*

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC11082179/

---

### Fuchs et al. — Trumpeting

Fuchs E. et al. (2021).

**Acoustic structure and information content of trumpets in African savanna elephants.**

*Scientific Reports.*

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC8610244/

---

### King et al. — Alarm communication

King L.E., Soltis J., Douglas-Hamilton I., Savage A., Vollrath F. (2010).

**Bee Threat Elicits Alarm Call in African Elephants.**

*PLoS ONE*, 5, e10346.

DOI:

```text
10.1371/journal.pone.0010346
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC2859947/

---

# Ducks

### Miller & Gottlieb — Maternal vocalizations

Miller D.B., Gottlieb G. (1978).

**Maternal vocalizations of mallard ducks (Anas platyrhynchos).**

*Animal Behaviour*, 26, 1178–1194.

DOI:

```text
10.1016/0003-3472(78)90108-2
```

URL:

https://www.sciencedirect.com/science/article/pii/0003347278901082

---

### Finley et al. — Courtship displays

Finley J., Ireton D., Schleidt W.M., Thompson T.A. (1983).

**A new look at the features of mallard courtship displays.**

*Animal Behaviour*, 31(2), 348–354.

DOI:

```text
10.1016/S0003-3472(83)80053-0
```

URL:

https://www.sciencedirect.com/science/article/pii/S0003347283800530

---

### Miller & Blaich — Alarm response

Miller D.B., Blaich C.F. (1986).

**Alarm call responsivity of mallard ducklings: III. Acoustic features affecting behavioral inhibition.**

*Developmental Psychobiology*, 19.

DOI:

```text
10.1002/dev.420190402
```

URL:

https://pubmed.ncbi.nlm.nih.gov/3732620/

---

### Hailman & Baylis — Tail wagging

Hailman J.P., Baylis J.R. (1991).

**Post-flight Tail-wagging in the Mallard.**

*Journal of Field Ornithology*, 62(2), 226–229.

URL:

https://digitalcommons.usf.edu/jfo/vol62/iss2/13/

This source is used cautiously.

The project does **not** interpret duck tail wagging as "happiness". The stored rule concerns documented post-flight tail movement and its possible maintenance-related function.

---

### Mi et al. — Preening

Mi J. et al. (2020).

**Lack of access to an open water source for bathing inhibited the development of the preen gland and preening behavior in Sanshui White ducks.**

*Poultry Science.*

DOI:

```text
10.1016/j.psj.2020.08.018
```

URL:

https://pmc.ncbi.nlm.nih.gov/articles/PMC7647854/

---

# Use of AI

AI tools were used during development as a programming, debugging, research-assistance and documentation tool.

AI was used for:

- discussing the software architecture
- drafting initial code
- refactoring Python and TypeScript code
- debugging backend and frontend errors
- helping design the database structure
- helping structure interpretation rules
- helping locate candidate scientific publications
- preparing documentation

Scientific references were not intended to be accepted purely because an AI model produced them.

Candidate sources should be checked against:

- the journal publisher
- DOI records
- PubMed
- PubMed Central
- other authoritative bibliographic databases

before being included in the final knowledge base.

---

## AI Is Not Used During Runtime Interpretation

The interpretation engine itself does not call a language model.

The runtime pipeline is:

```text
User observation
        ↓
React frontend
        ↓
FastAPI
        ↓
PostgreSQL knowledge base
        ↓
Deterministic rule matching
        ↓
Ranked interpretations
        ↓
Evidence + limitations + sources
```

An AI model therefore does not generate a new behavioural meaning for every user request.

The possible interpretations come from predefined, inspectable rules stored in the knowledge base.

---

# Design Principles

## 1. Observable Facts First

The user enters things that can actually be observed.

Examples:

```text
growl
slow blink
tail swishing
trunk touching
tail wagging
```

The system keeps observation separate from interpretation.

---

## 2. No Literal Animal-Language Claims

The system avoids outputs such as:

```text
The dog is saying:
"Leave me alone."
```

Instead it produces cautious behavioural interpretations such as:

```text
Competitive or warning-related communication
may be consistent with the observed behaviour.
```

---

## 3. Context Matters

The same signal can occur in different situations.

For example, dog growling may occur during:

- play
- resource guarding
- conflict

Therefore the system evaluates combinations of:

```text
species
+
signal
+
supporting signals
+
context
```

rather than treating one behaviour as one fixed word.

---

## 4. Alternative Interpretations Are Preserved

Several rules may match the same observation.

The highest-scoring candidate is returned as:

```text
primary_interpretation
```

Other candidates are returned as:

```text
alternatives
```

This prevents the application from pretending that ambiguous behaviour always has one certain explanation.

---

## 5. Uncertainty Is a Valid Result

The application can return:

```text
insufficient_evidence
```

when the knowledge base cannot support an interpretation.

This is preferable to fabricating an answer.

---

# Current Limitations

This project is a prototype.

Current limitations include:

- a limited number of interpretation rules
- a limited number of scientific sources per species
- not every observable signal currently has an independent interpretation rule
- the system relies on manually entered observations
- no automatic video analysis is currently implemented
- no automatic audio classification is currently implemented
- individual animal history is not modelled
- breed, age and individual variation are only partially represented
- environmental details are simplified into contexts
- the scoring system is a project heuristic rather than a scientifically calibrated probability
- the evidence summary currently aggregates evidence from matched rules rather than independently validating every selected signal

The application should not be used as a veterinary diagnostic system.

---

# Possible Future Improvements

Potential future work includes:

- adding more peer-reviewed sources
- adding more rules for existing species
- adding new species
- normalized signal-level scientific evidence
- automated tests for interpretation rules
- Alembic database migrations
- video behaviour recognition
- audio feature extraction
- computer vision
- automatic observable-signal detection
- optional machine-learning perception models
- clearer "why this rule matched" explanations
- improved scoring/calibration
- observation history
- more advanced frontend visualizations

If ML or AI-based perception is added later, it should remain separate from the scientific rule database.

For example:

```text
video
 ↓
computer vision detects posture
 ↓
observable signal
 ↓
scientific rule engine
 ↓
interpretation
```

This preserves traceability.

---

# Disclaimer

This project is an educational and research prototype.

Its results are possible interpretations based on selected behavioural literature and deterministic matching rules.

They are not:

- literal translations of animal language
- veterinary diagnoses
- guaranteed descriptions of emotional state
- predictions of future behaviour

Animal behaviour depends on context, individual experience, environment, age, health, social relationships and many other factors.

The complete behavioural situation should always be considered.
