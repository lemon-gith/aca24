#!/usr/bin/bash

scripts_array=("varyarch-energy-3params" "varycachelinesize" "varycachesize")
arr_last_idx=$((${#scripts_array[@]} - 1))

# use indices to be able to iterate through destinations, too
for i in $(seq 0 $arr_last_idx)
do 
	script=${scripts_array[$i]}
	ssh texel$(($i+5)) "cd $DIR_PATH; ./scripts/$script >> ./remote_testing/next-$script.txt; exit;" &
done

echo "greetings, I am returned"
