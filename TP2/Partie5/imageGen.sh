#!/bin/bash

pbmp2pan timbres.bmp timbres.pan
pbmp2pan motif.bmp motif.pan
pfftcorrelation timbres.pan motif.pan correlation.pan
psetcst 0 correlation.pan zeros.pan
pfftshift correlation.pan zeros.pan correlation.pan zeros.pan 
#psetcst 0 correlation.pan correlation-i.pan
#pfft correlation.pan correlation-i.pan re.pan im.pan
#pfftshift re.pan im.pan re.pan im.pan


for i in *.pan
do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done