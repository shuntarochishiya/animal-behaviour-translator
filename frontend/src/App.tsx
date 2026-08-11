import { useEffect, useState } from "react";

import {
  getObservationOptions,
  getSpecies,
  interpretObservation,
  type InterpretationResponse,
  type ObservationOptions,
  type Species,
} from "./api";

import "./App.css";


function App() {
  const [species, setSpecies] = useState<Species[]>([]);
  const [selectedSpecies, setSelectedSpecies] = useState("");

  const [options, setOptions] =
    useState<ObservationOptions | null>(null);

  const [selectedSignals, setSelectedSignals] =
    useState<string[]>([]);

  const [selectedContext, setSelectedContext] =
    useState("");

  const [result, setResult] =
    useState<InterpretationResponse | null>(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState("");


  useEffect(() => {
    async function loadSpecies() {
      try {
        const data = await getSpecies();

        setSpecies(data);

        if (data.length > 0) {
          setSelectedSpecies(data[0].slug);
        }
      } catch {
        setError("Could not load species.");
      }
    }

    loadSpecies();
  }, []);


  useEffect(() => {
    if (!selectedSpecies) {
      return;
    }

    async function loadOptions() {
      try {
        setSelectedSignals([]);
        setSelectedContext("");
        setResult(null);
        setError("");

        const data = await getObservationOptions(
          selectedSpecies
        );

        setOptions(data);
      } catch {
        setError(
          "Could not load observation options."
        );
      }
    }

    loadOptions();
  }, [selectedSpecies]);


  function toggleSignal(signal: string) {
    setSelectedSignals((current) => {
      if (current.includes(signal)) {
        return current.filter(
          (item) => item !== signal
        );
      }

      return [...current, signal];
    });
  }


  async function handleInterpret() {
    if (
      !selectedSpecies ||
      selectedSignals.length === 0 ||
      !selectedContext
    ) {
      setError(
        "Select at least one signal and a context."
      );

      return;
    }

    try {
      setLoading(true);
      setError("");

      const response =
        await interpretObservation(
          selectedSpecies,
          selectedSignals,
          selectedContext
        );

      setResult(response);
    } catch {
      setError(
        "Interpretation request failed."
      );
    } finally {
      setLoading(false);
    }
  }


  return (
    <main className="page">
      <section className="container">
        <header className="header">
          <p className="eyebrow">
            Research-based prototype
          </p>

          <h1>
            Animal Behaviour Translator
          </h1>

          <p className="intro">
            Select an animal, observed signals,
            and context. The system compares
            the observation with research-backed
            interpretation rules.
          </p>
        </header>


        <section className="form-card">
          <label className="field">
            <span>
              Species
            </span>

            <select
              value={selectedSpecies}
              onChange={(event) =>
                setSelectedSpecies(
                  event.target.value
                )
              }
            >
              {species.map((item) => (
                <option
                  key={item.slug}
                  value={item.slug}
                >
                  {item.common_name}
                </option>
              ))}
            </select>
          </label>


          <div className="field">
            <span>
              Observed signals
            </span>

            <div className="signal-grid">
              {options?.signals.map(
                (signal) => (
                  <label
                    key={signal.slug}
                    className="signal-card"
                  >
                    <input
                      type="checkbox"
                      checked={
                        selectedSignals.includes(
                          signal.slug
                        )
                      }
                      onChange={() =>
                        toggleSignal(
                          signal.slug
                        )
                      }
                    />

                    <div>
                      <strong>
                        {signal.name}
                      </strong>

                      <small>
                        {signal.category}
                      </small>

                      <p>
                        {signal.description}
                      </p>
                    </div>
                  </label>
                )
              )}
            </div>
          </div>


          <label className="field">
            <span>
              Context
            </span>

            <select
              value={selectedContext}
              onChange={(event) =>
                setSelectedContext(
                  event.target.value
                )
              }
            >
              <option value="">
                Select context
              </option>

              {options?.contexts.map(
                (context) => (
                  <option
                    key={context}
                    value={context}
                  >
                    {context}
                  </option>
                )
              )}
            </select>
          </label>


          <button
            className="interpret-button"
            onClick={handleInterpret}
            disabled={loading}
          >
            {loading
              ? "Interpreting..."
              : "Interpret observation"}
          </button>


          {error && (
            <p className="error">
              {error}
            </p>
          )}
        </section>


        {result && (
          <section className="result-section">
            {result.primary_interpretation ? (
              <>
                <p className="eyebrow">
                  Most likely interpretation
                </p>

                <h2>
                  {
                    result.primary_interpretation
                      .label
                  }
                </h2>

                <p>
                  {
                    result.primary_interpretation
                      .description
                  }
                </p>


                <div className="score-row">
                  <div>
                    <strong>
                      {
                        result.primary_interpretation
                          .system_match_score
                      }
                      /100
                    </strong>

                    <span>
                      System match
                    </span>
                  </div>

                  <div>
                    <strong>
                      {
                        result.primary_interpretation
                          .scientific_evidence
                      }
                    </strong>

                    <span>
                      Scientific evidence
                    </span>
                  </div>
                </div>


                <h3>
                  Evidence basis
                </h3>

                <p>
                  {
                    result.primary_interpretation
                      .evidence_basis
                  }
                </p>


                <h3>
                  Limitations
                </h3>

                <p>
                  {
                    result.primary_interpretation
                      .limitations
                  }
                </p>


                <h3>
                  Scientific sources
                </h3>

                <ul>
                  {
                    result.primary_interpretation
                      .sources.map(
                        (source) => (
                          <li
                            key={source.key}
                          >
                            <a
                              href={
                                source.url
                              }
                              target="_blank"
                              rel="noreferrer"
                            >
                              {
                                source.authors
                              }{" "}
                              (
                              {
                                source.year
                              }
                              ) —{" "}
                              {
                                source.title
                              }
                            </a>
                          </li>
                        )
                      )
                  }
                </ul>


                {result.alternatives.length > 0 && (
                  <section className="alternatives-section">
                    <h3>
                      Alternative interpretations
                    </h3>

                    <p className="alternatives-intro">
                      These rules also match part
                      of the observation, but less
                      closely than the primary
                      interpretation.
                    </p>

                    <div className="alternatives-list">
                      {result.alternatives.map(
                        (alternative) => (
                          <article
                            key={
                              alternative.rule_key
                            }
                            className="alternative-card"
                          >
                            <div className="alternative-header">
                              <h4>
                                {
                                  alternative.label
                                }
                              </h4>

                              <span className="alternative-score">
                                {
                                  alternative
                                    .system_match_score
                                }
                                /100
                              </span>
                            </div>

                            <p>
                              {
                                alternative.description
                              }
                            </p>

                            <div className="alternative-meta">
                              <span>
                                Evidence:{" "}
                                <strong>
                                  {
                                    alternative
                                      .scientific_evidence
                                  }
                                </strong>
                              </span>

                              <span>
                                Context matched:{" "}
                                <strong>
                                  {
                                    alternative
                                      .context_matched
                                      ? "Yes"
                                      : "No"
                                  }
                                </strong>
                              </span>
                            </div>

                            {
                              alternative
                                .missing_supporting_signals
                                .length > 0 && (
                                <p className="missing-signals">
                                  Missing supporting
                                  signals:{" "}
                                  {
                                    alternative
                                      .missing_supporting_signals
                                      .join(", ")
                                  }
                                </p>
                              )
                            }

                            <details>
                              <summary>
                                Evidence and sources
                              </summary>

                              <p>
                                {
                                  alternative
                                    .evidence_basis
                                }
                              </p>

                              <p>
                                <strong>
                                  Limitations:
                                </strong>{" "}
                                {
                                  alternative
                                    .limitations
                                }
                              </p>

                              <ul>
                                {
                                  alternative
                                    .sources.map(
                                      (source) => (
                                        <li
                                          key={
                                            source.key
                                          }
                                        >
                                          <a
                                            href={
                                              source.url
                                            }
                                            target="_blank"
                                            rel="noreferrer"
                                          >
                                            {
                                              source.authors
                                            }{" "}
                                            (
                                            {
                                              source.year
                                            }
                                            ) —{" "}
                                            {
                                              source.title
                                            }
                                          </a>
                                        </li>
                                      )
                                    )
                                }
                              </ul>
                            </details>
                          </article>
                        )
                      )}
                    </div>
                  </section>
                )}
              </>
            ) : (
              <>
                <h2>
                  Insufficient evidence
                </h2>

                <p>
                  No research-backed rule
                  matches this observation
                  closely enough.
                </p>
              </>
            )}


            <p className="disclaimer">
              {result.disclaimer}
            </p>
          </section>
        )}
      </section>
    </main>
  );
}


export default App;
