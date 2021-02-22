#!/bin/bash

echo "This script will rename all significat project section replacing 'myproject' with given name"
echo
read -p 'New project name (avoid spaces or special chars): ' NEWNAME


for i in $(grep -Rl myproject myproject | grep -v "__pycache__")
do
    echo "Patching code [${i}]"
    sed -i '' 's/myproject/'${NEWNAME}'/g' ${i}
done;

for i in $(grep -Rl myproject tests | grep -v "__pycache__")
do
    echo "Patching test [${i}]"
    sed -i '' 's/myproject/'${NEWNAME}'/g' ${i}
done;

echo "Patching setup.cfg"
sed -i '' 's/myproject/'${NEWNAME}'/g' setup.cfg

echo "Patching Makefile"
sed -i '' 's/myproject/'${NEWNAME}'/g' Makefile

echo "Renaming folder"
mv myproject ${NEWNAME}

echo "DONE, remember to edit setup.cfg and README.md for additional details on your project"
