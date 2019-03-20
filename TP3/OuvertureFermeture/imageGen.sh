#!/bin/bash

getHistogram() {
	pnormalization 0 255 cells.pan | pim2uc - - | phistogram - cells-histo.pan
	pplot1d 512 256 1 0 0 cells-histo.pan cells-histo-img.pan
	pnormalization 0 255 cells-histo-img.pan | pim2uc - -  |ppan2png - cells-histo.pan
}

binarize() {
	pbinarization 36 255 cells.pan cells-bin.pan
}

getErosion() {
	for i in 0 1 2 3 4 5 6 7 8 
	do
		for j in 1 2 3
		do
			perosion $i $j cells-bin.pan cells-form$i-taille$j.pan
		done
	done
}

fillUpCell() {
	for i in 0 1 2 3 4 5 6 7 8 
	do
		for j in 1 2 3
		do
			pdilation $i $j cells-form$i-taille$j.pan cells-form$i-taille$j-dil.pan
			pdilation 2 1 cells-form$i-taille$j-dil.pan - | perosion 2 1 - - | pmask cells.pan - cells-form$i-taille$j-rec.pan
		done
	done
}

reconstruct() {
	for i in 4 8
	do
		pdilationreconstruction $i cells-bin.pan cells-form7-taille3-dil.pan cells-$i-rec.pan
	done
}


binarize
getErosion
fillUpCell
reconstruct

for i in *.pan
do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done