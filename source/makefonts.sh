#!/bin/bash

for font in  *.ufo ; do
  fontmake -u $font --overlaps-backend pathops -o ttf
done
