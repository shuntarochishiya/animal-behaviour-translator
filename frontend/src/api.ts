const API_BASE_URL = "http://127.0.0.1:8000";

export interface Species {
  id: number;
  slug: string;
  common_name: string;
  scientific_name: string;
  description: string;
}

export interface SignalOption {
  slug: string;
  name: string;
  category: string;
  description: string;
}

export interface ObservationOptions {
  species: string;
  signals: SignalOption[];
  contexts: string[];
}

export interface Source {
  key: string;
  title: string;
  authors: string;
  year: number;
  journal: string | null;
  doi: string | null;
  url: string;
}

export interface InterpretationAlternative {
  rule_key: string;
  label: string;
  description: string;
  system_match_score: number;
  scientific_evidence: string;
  evidence_basis: string;
  context_matched: boolean;
  matched_supporting_signals: string[];
  missing_supporting_signals: string[];
  limitations: string;
  sources: Source[];
}

export interface InterpretationResponse {
  status: string;
  species: string;
  observed_signals: string[];
  context: string;
  primary_interpretation: InterpretationAlternative | null;
  alternatives: InterpretationAlternative[];
  disclaimer: string;
}

export async function getSpecies(): Promise<Species[]> {
  const response = await fetch(`${API_BASE_URL}/species`);

  if (!response.ok) {
    throw new Error("Failed to load species");
  }

  return response.json();
}

export async function getObservationOptions(
  speciesSlug: string
): Promise<ObservationOptions> {
  const response = await fetch(
    `${API_BASE_URL}/observation-options/${speciesSlug}`
  );

  if (!response.ok) {
    throw new Error("Failed to load observation options");
  }

  return response.json();
}

export async function interpretObservation(
  species: string,
  signals: string[],
  context: string
): Promise<InterpretationResponse> {
  const response = await fetch(`${API_BASE_URL}/interpret`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      species,
      signals,
      context,
    }),
  });

  if (!response.ok) {
    throw new Error("Failed to interpret observation");
  }

  return response.json();
}
