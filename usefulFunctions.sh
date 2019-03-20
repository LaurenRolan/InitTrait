#!/bin/bash
allToPNG() {
	for i in *.pan
	do
	    [ -f "$i" ] || break
	    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
	    mv $i.png ${i%.pan}.png
	done
}

getHistogram() {
	pnormalization 0 255 cells.pan | pim2uc - - | phistogram - cells-histo.pan
	pplot1d 512 256 1 0 0 cells-histo.pan cells-histo-img.pan
	pnormalization 0 255 cells-histo-img.pan | pim2uc - -  |ppan2png - cells-histo.pan
}