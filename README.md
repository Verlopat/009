# Verifiable Energy and Carbon Reward Simulation

A prototype project for modeling verifiable energy and carbon-related rewards, with a lightweight chain component, a prover component, a Python simulation, Docker Compose orchestration, and saved CSV/plot artifacts.

> **Status:** Research / proof of concept. The reward model, verification logic, and simulation outputs are experimental and should not be used for financial, environmental-credit, or production blockchain decisions without independent validation.

## Overview

The repository combines three main layers:

| Layer | Location | Role |
| --- | --- | --- |
| Chain | `chain/` | Go-based chain application structure, including application, command, and module directories. |
| Prover | `prover/` | Materials related to producing or handling proof-oriented inputs. |
| Simulation | `sim/` | Python model that produces reward-related data and visualizations. |

Docker Compose and shell scripts support local execution. Saved results include `vec_simulation_results.csv`, a reward-distribution chart, and an energy/carbon/reward scatter plot.

## Repository contents

| File or directory | Purpose |
| --- | --- |
| `chain/` | Go module containing the chain application structure. |
| `prover/` | Proof-related project material. |
| `sim/simulate.py` | Python simulation entry point. |
| `sim/requirements.txt` | Python dependencies for the simulation. |
| `scripts/start.sh` | Helper for starting the local environment. |
| `scripts/simulate.sh` | Helper for running the simulation workflow. |
| `docker-compose.yml` | Local multi-service orchestration configuration. |
| `vec_simulation_results.csv` | Saved simulation output data. |
| `carc_reward_distribution.png` | Distribution visualization for modeled rewards. |
| `energy_carbon_reward_scatter.png` | Scatter plot relating energy, carbon, and reward values. |

## Requirements

- Docker and Docker Compose for the configured local services.
- Go, for working with the code under `chain/`.
- Python 3 and the packages listed in `sim/requirements.txt` for simulations and plots.
- Bash or a compatible shell for repository scripts.

## Quick start

Clone the repository and prepare the Python simulation environment:

```bash
git clone https://github.com/Verlopat/009.git
cd 009

python3 -m venv .venv
source .venv/bin/activate
pip install -r sim/requirements.txt
```

Run the simulation directly from its directory:

```bash
cd sim
python3 simulate.py
```

Or use the repository helper script from the repository root after inspecting it:

```bash
sed -n '1,200p' scripts/simulate.sh
bash scripts/simulate.sh
```

To bring up the local Docker-based environment, first review `docker-compose.yml` and `scripts/start.sh`, then run:

```bash
docker compose up --build
```

Use `docker compose down` when the local environment is no longer needed.

## Simulation outputs

The Python simulation produces or uses a tabular result dataset and visualization artifacts:

| Artifact | Meaning |
| --- | --- |
| `vec_simulation_results.csv` | Row-level or scenario-level simulation results. |
| `carc_reward_distribution.png` | Visualizes the distribution of modeled reward values. |
| `energy_carbon_reward_scatter.png` | Visualizes the modeled relationship among energy, carbon, and reward values. |

The checked-in files are snapshots from a prior run. Recreate them after changing model assumptions, input distributions, code, dependency versions, or random seeds.

## Chain and prover components

`chain/` is organized as a Go module with `app/`, `cmd/`, and `x/` directories, following a common separation of application setup, executable commands, and domain modules. `prover/` holds associated proof-oriented material. Inspect their source and configuration before assuming specific consensus, cryptographic, or verification properties.

## Reproducibility

- Record the Git revision, Python and Go versions, dependency versions, and Docker image digests used for a run.
- Record simulation parameters and random seeds used by `sim/simulate.py`.
- Preserve the command used to create each CSV and plot.
- Use explicit image tags or digests for reproducible Docker runs.

## Limitations

- A simulation demonstrates behavior under its model; it does not validate real-world energy, emissions, or carbon-credit claims.
- Reward calculations depend on inputs, assumptions, and the implemented formula. Audit these before using results for incentives or reporting.
- Charts can show correlation in generated data but do not establish causation, correctness, or fraud resistance.
- Do not store production secrets, credentials, or real participant data in Docker Compose files or committed configuration.

## Suggested improvements

1. Document the exact reward formula, units, data sources, and verification assumptions.
2. Add CLI options or a configuration file for simulation parameters and random seeds.
3. Add data dictionaries for every CSV column and chart axis.
4. Add unit tests for reward calculations, validation logic, and edge cases.
5. Document the chain and prover APIs, build steps, and trust boundaries.
6. Pin Docker images and Python/Go dependencies for reproducible builds.
7. Add CI for simulation tests and artifact generation.
8. Add a license and contribution guidance.

## License

No license file is currently included. Add an explicit license before distributing or accepting external contributions.
