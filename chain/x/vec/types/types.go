package types

type MsgSubmitCommitment struct {
	NodeID           string `json:"node_id"`
	EnergyUsed       uint64 `json:"energy_used"`
	CarbonIntensity  uint64 `json:"carbon_intensity"`
	EnergyThreshold  uint64 `json:"energy_threshold"`
	CarbonThreshold  uint64 `json:"carbon_threshold"`
	Proof            string `json:"proof"`
	Attestation      string `json:"attestation"`
}
