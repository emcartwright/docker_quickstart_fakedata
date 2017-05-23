#!/bin/bash

#count # of buildings in fake data

num_cols="$(head -1 data.csv | sed 's/[^,]//g' | wc -c)"
echo "$num_cols"

idx=0
echo "Spinning messenger containers..."
#make client containers equal to # of cols in data.csv connected to mynet
#run messenger.py in each respective messenger
# assign "idx" so that each messenger knows which column it should parse
until [ $idx -eq $num_cols ]
do
	echo $idx
	docker run --net mynet -d quick_start  python messenger.py $idx
	let idx++
	

done
