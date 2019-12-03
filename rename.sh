#!/bin/bash

echo "This script will rename all significat project section replacing 'myproject' with given name"
echo
read -p 'New project name: ' NEWNAME

echo "Patching test import"
sed -i '' 's/myproject/'${NEWNAME}'/' tests/test_main.py
echo "Patching setup.cfg"
sed -i '' 's/myproject/'${NEWNAME}'/' setup.cfg
echo "Patching Makefile"
sed -i '' 's/myproject/'${NEWNAME}'/' Makefile
echo "Renaming folder"
mv myproject ${NEWNAME}
echo "DONE, remember to edit setup.cfg and README.md for additional details on your project"
