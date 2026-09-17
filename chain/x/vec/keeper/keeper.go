package keeper

type Commitment struct {
	NodeID           string
	EnergyUsed       uint64
	CarbonIntensity  uint64
	EnergyThreshold  uint64
	CarbonThreshold  uint64
	ProofValid       bool
	AttestationValid bool
}

type Keeper struct {
	store map[string]Commitment
}

func NewKeeper() *Keeper {
	return &Keeper{store: make(map[string]Commitment)}
}

func (k *Keeper) SubmitCommitment(c Commitment) {
	k.store[c.NodeID] = c
}

func (k *Keeper) Reward(nodeID string, base float64) float64 {
	c, ok := k.store[nodeID]
	if !ok {
		return 0
	}
	if !c.ProofValid || !c.AttestationValid {
		return 0
	}

	energyScore := 1.0 - float64(c.EnergyUsed)/float64(max(c.EnergyThreshold, 1))
	carbonScore := 1.0 - float64(c.CarbonIntensity)/float64(max(c.CarbonThreshold, 1))

	if energyScore < 0 {
		energyScore = 0
	}
	if carbonScore < 0 {
		carbonScore = 0
	}

	carc := 0.5 + 0.5*((energyScore+carbonScore)/2.0)
	return base * carc
}

func max(a, b uint64) uint64 {
	if a > b {
		return a
	}
	return b
}
