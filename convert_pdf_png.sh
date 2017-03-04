#!/bin/bash

convert -density 144 $1 \
   -background white -alpha remove -bordercolor black -border 5 \
   $1.png
 
for file in $1-*.png
do
   convert $file \
      \( +clone -background black -shadow 30x10+15+15 \) \
      +swap -background white -layers merge +repage $file
done
