#!/bin/bash

echo "This script will rename all significat project section replacing 'myproject' with given name"
echo
read -p 'New project name: ' NEWNAME


for i in $(grep -Rl ${NEWNAME} myproject | grep -v "__pycache__")
do
    echo "Patching [${i}]"
    sed -i '' 's/myproject/'${NEWNAME}'/' ${i}
done;

echo "Patching setup.cfg"
sed -i '' 's/myproject/'${NEWNAME}'/' setup.cfg

echo "Patching Makefile"
sed -i '' 's/myproject/'${NEWNAME}'/' Makefile

echo "Renaming folder"
mv myproject ${NEWNAME}

echo "DONE, remember to edit setup.cfg and README.md for additional details on your project"
