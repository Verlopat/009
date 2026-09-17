import random
import pandas as pd
import matplotlib.pyplot as plt

random.seed(42)

NODES = 200
BASE_REWARD = 100.0

def carc_reward(energy_used, energy_threshold, carbon_intensity, carbon_threshold):
    energy_score = max(0.0, 1.0 - energy_used / max(energy_threshold, 1))
    carbon_score = max(0.0, 1.0 - carbon_intensity / max(carbon_threshold, 1))
    sustainability_score = (energy_score + carbon_score) / 2.0
    return BASE_REWARD * (0.5 + 0.5 * sustainability_score)

rows = []
for i in range(NODES):
    node_id = f"node-{i+1:03d}"
    energy_threshold = random.randint(80, 120)
    carbon_threshold = random.randint(40, 70)

    honest = random.random() > 0.25  # 25% dishonest
    efficient = random.random() > 0.45  # 45% inefficient

    if efficient:
        energy_used = random.randint(40, int(energy_threshold * 0.75))
        carbon_intensity = random.randint(15, int(carbon_threshold * 0.75))
    else:
        energy_used = random.randint(energy_threshold, int(energy_threshold * 1.6))
        carbon_intensity = random.randint(carbon_threshold, int(carbon_threshold * 1.6))

    claimed_energy = energy_used
    claimed_carbon = carbon_intensity

    if not honest:
        claimed_energy = max(1, energy_used - random.randint(20, 50))
        claimed_carbon = max(1, carbon_intensity - random.randint(15, 35))

    proof_valid = claimed_energy <= energy_threshold and claimed_carbon <= carbon_threshold
    tee_detects_mismatch = (claimed_energy != energy_used) or (claimed_carbon != carbon_intensity)
    attestation_valid = not tee_detects_mismatch

    reward_without_vec = BASE_REWARD if claimed_energy <= energy_threshold else BASE_REWARD * 0.5
    reward_with_vec = carc_reward(energy_used, energy_threshold, carbon_intensity, carbon_threshold) if (proof_valid and attestation_valid) else 0

    rows.append({
        "node_id": node_id,
        "energy_used": energy_used,
        "carbon_intensity": carbon_intensity,
        "energy_threshold": energy_threshold,
        "carbon_threshold": carbon_threshold,
        "claimed_energy": claimed_energy,
        "claimed_carbon": claimed_carbon,
        "honest": honest,
        "efficient": efficient,
        "proof_valid": proof_valid,
        "attestation_valid": attestation_valid,
        "reward_without_vec": reward_without_vec,
        "reward_with_vec": reward_with_vec
    })

df = pd.DataFrame(rows)

avg_carbon_all = df["carbon_intensity"].mean()
avg_carbon_rewarded = df[df["reward_with_vec"] > 0]["carbon_intensity"].mean()
reduction_pct = 100 * (avg_carbon_all - avg_carbon_rewarded) / avg_carbon_all if avg_carbon_all > 0 else 0

print("Total nodes:", len(df))
print("Rewarded under VEC:", int((df['reward_with_vec'] > 0).sum()))
print("Average carbon intensity (all nodes):", round(avg_carbon_all, 2))
print("Average carbon intensity (rewarded nodes):", round(avg_carbon_rewarded, 2))
print("Carbon intensity reduction:", round(reduction_pct, 2), "%")

df.to_csv("vec_simulation_results.csv", index=False)

plt.figure(figsize=(10, 6))
plt.hist(df["reward_with_vec"], bins=20)
plt.title("Reward Distribution Under CARC")
plt.xlabel("Reward")
plt.ylabel("Number of Nodes")
plt.tight_layout()
plt.savefig("carc_reward_distribution.png", dpi=200)

plt.figure(figsize=(10, 6))
plt.scatter(df["energy_used"], df["carbon_intensity"], c=df["reward_with_vec"], cmap="viridis")
plt.title("Energy vs Carbon Intensity Colored by VEC Reward")
plt.xlabel("Energy Used")
plt.ylabel("Carbon Intensity")
plt.tight_layout()
plt.savefig("energy_carbon_reward_scatter.png", dpi=200)
