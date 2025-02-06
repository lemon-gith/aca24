#! /usr/bin/bash

scripts_array=("varyarch-energy-3params" "varycachelinesize" "varycachesize")

for i in 0 1 2
do 
	ssh texel"($i+15)" "cd $TEST_PATH; ./scripts/${scripts_array[$i]} >> ./remote_testing/next-${scripts_array[$i]}.txt; exit;" &
done

echo "greetings, I am returned"
