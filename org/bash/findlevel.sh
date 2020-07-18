#!/bin/bash
imagename=$1

level () {
    echo -n "file:"
    depth=$(grep "template-" $(ls *.org | head -1) | sed -E 's/.*template-([0-9]).org/\1/')

    if [[ $depth != 0 ]]
    then
    #    path=$(printf '../%.0s' {1..$depth})
        for i in `seq $depth`; do echo -n "../";done
    fi

    echo "screenshots/$imagename.png"
}

level
