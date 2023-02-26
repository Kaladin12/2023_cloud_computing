#!/bin/bash

dir="$(pwd)"

function deploy(){
    aws s3 sync . "s3://kaladin.cetystijuana.com" --profile kaladin12
}

if [ $dir == "~/2/website" ];
then 
    deploy
else
    cd ~/2/website;
    deploy
fi