#!/bin/bash
allToPNG() {
	for i in *.pan
	do
	    [ -f "$i" ] || break
	    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
	    mv $i.png ${i%.pan}.png
	done
}

pskeletonization 4 outils.pan skeleton4-outils.pan
pskeletonization 8 outils.pan skeleton8-outils.pan

ppostthinning skeleton4-outils.pan post4-outils.pan
ppostthinning skeleton8-outils.pan post8-outils.pan

allToPNG