import fs from "fs";

const input = JSON.parse(fs.readFileSync("./input/sample.json", "utf8"));

function teeMeasure(i) {
  return {
    node_id: "node-01",
    energy_used: i.energy_used,
    carbon_intensity: i.carbon_intensity,
    attestation: "TEE_MEASUREMENT_OK"
  };
}

function zkProve(i) {
  const energyOk = i.energy_used <= i.energy_threshold;
  const carbonOk = i.carbon_intensity <= i.carbon_threshold;
  return {
    proof: "ZK_PROOF_PLACEHOLDER",
    publicSignals: {
      energy_threshold: i.energy_threshold,
      carbon_threshold: i.carbon_threshold,
      valid_energy: energyOk ? 1 : 0,
      valid_carbon: carbonOk ? 1 : 0
    }
  };
}

const attested = teeMeasure(input);
const proof = zkProve(input);

const output = {
  ...attested,
  ...proof
};

fs.writeFileSync("./proof-output.json", JSON.stringify(output, null, 2));
console.log(JSON.stringify(output, null, 2));
