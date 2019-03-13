#!/bin/bash
# Partie Dirac
pshapedesign 256 256 0 0 0 0 empty.pan
psetpixel 128 128 0 255 empty.pan dirac.pan
pmeanfiltering 1 dirac.pan convolute.pan

psetcst 0 convolute.pan convolute-i.pan
pfft convolute.pan convolute-i.pan convolute-re.pan convolute-im.pan
pfftshift convolute-re.pan convolute-im.pan convolute-re.pan convolute-im.pan
pmodulus convolute-re.pan convolute-im.pan final.pan

#Partie Lena
paddnoise 1 10 10 lena.pan bruite.pan
pmeanfiltering 1 bruite.pan convolute.pan

psetcst 0 convolute.pan convolute-i.pan
pfft convolute.pan convolute-i.pan convolute-re.pan convolute-im.pan
pfftshift convolute-re.pan convolute-im.pan convolute-re.pan convolute-im.pan
pmodulus convolute-re.pan convolute-im.pan final.pan


for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done