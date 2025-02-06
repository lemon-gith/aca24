#!/bin/bash

path=$DIR_PATH

cd $path
#fpalu would preferably be set to 0
export SSFLAGS="-lsq:size 16 -bpred bimod -ruu:size 32 -res:fpalu 1 -res:ialu 2 -res:imult 2"
echo -n "$SSFLAGS">"$path/optimal_config_data.txt"
./run-wattch 2>&1 | tee>"$path/optimal_config.log"
cat "$path/remote_testing/inorder.log" | ./scripts/tabulate>>"$path/optimal_config_data.txt"

