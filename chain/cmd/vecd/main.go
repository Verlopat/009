package main

import (
	"fmt"

	"vec/chain/app"
	"vec/chain/x/vec/keeper"
)

func main() {
	a := app.NewApp()
	fmt.Println("starting app:", a.Name)

	k := keeper.NewKeeper()
	k.SubmitCommitment(keeper.Commitment{
		NodeID:           "node-01",
		EnergyUsed:       72,
		CarbonIntensity:  41,
		EnergyThreshold:  100,
		CarbonThreshold:  60,
		ProofValid:       true,
		AttestationValid: true,
	})

	reward := k.Reward("node-01", 100.0)
	fmt.Printf("computed reward for node-01: %.2f\n", reward)
}
