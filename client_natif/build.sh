#!/bin/bash

yes|rm -rf ./build
mkdir build
cd build

if [[ $1 = "debug" ]];
then
    echo "DEEEEEEEEEEBBBBBUUUUUUUUUUUUUUUUGGGGGG",
    cmake -DCMAKE_BUILD_TYPE=Debug ..
else
    cmake ..
fi

echo "---- MAKE ----"
make
cd ..
echo "Build over."
if [[ " $@ " =~ " launch " ]];
then
    if [ $1 = "debug" ]
    then
	valgrind ./build/PartyDroneControlPanel
    else
	./build/PartyDroneControlPanel
    fi
fi
