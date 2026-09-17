pragma circom 2.1.6;

template EnergyThreshold() {
    signal input energy_used;
    signal input energy_threshold;
    signal input carbon_intensity;
    signal input carbon_threshold;

    signal output valid_energy;
    signal output valid_carbon;
}

component main = EnergyThreshold();
