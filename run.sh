#!/bin/bash
set -e
MPSPDZ=~/MP-SPDZ
PROJECT="/mnt/d/work/Distributed Rollup/my-mpc-project"

echo "=== Generating input shares ==="
cd "$PROJECT"
python3 gen_inputs.py
cp Player-Data/Input-P*-0 "$MPSPDZ/Player-Data/"

echo "=== Compiling MPC program ==="
cp "$PROJECT/mpc_programs/secret_sort.mpc" "$MPSPDZ/Programs/Source/"
cd "$MPSPDZ"
./compile.py -R 64 secret_sort

echo "=== Running 3-party MPC ==="
Scripts/ring.sh secret_sort
