#!/bin/bash
erosion() {
	for i in 0 1 2
	do
		perosion $i 1 outils.pan erosion-$i.pan
	done
	perosion 2 1 erosion-2.pan erosion-2-double.pan
	perosion 2 2 outils.pan erosion-lambda.pan
}

dilatation() {
	for i in 0 1 2
	do
		pdilatation $i 1 outils.pan dilatation-$i.pan
	done
	pdilatation 2 1 dilatation-2.pan dilatation-2-double.pan
	pdilatation 2 2 outils.pan dilatation-lambda.pan
}

erosion
dilatation

for i in *.pan
do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done