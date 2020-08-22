#!/bin/bash
cat rosdef_bashrc > ~/.bashrc
mkdir src
catkin_make
cd devel
realpath setup.bash|xargs echo "source">>~/.bashrc
source ~/.bashrc

echo
echo
echo
echo "cd into src and create your ros package using the command catkin_create_pkg <pkg name> <dependencies>"
