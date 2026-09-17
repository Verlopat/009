#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."

echo "[1/3] Running ZK proof demo"
cd prover
npm install
node prove.js
cd ..

echo "[2/3] Running CARC simulation"
cd sim
python simulate.py
cd ..

echo "[3/3] Done"
