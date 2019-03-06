#!/bin/bash
set -x
pnormalization 0 255 cercle.pan | pim2uc - - | phistogram - cercle-histo.pan
pplot1d 512 256 1 0 0 cercle-histo.pan cercle-histo-img.pan
pnormalization 0 255 cercle-histo-img.pan | pim2uc - - | ppan2png - cercle-histo.png
for i in 1 2 3 4
do
	paddnoise $i 10 15 cercle.pan cercle-$i.pan

	pnormalization 0 255 cercle-$i.pan | pim2uc - - | ppan2png - cercle-$i.png

	pnormalization 0 255 cercle-$i.pan | pim2uc - - | phistogram - cercle-$i-histo.pan
	pplot1d 512 256 1 0 0 cercle-$i-histo.pan cercle-$i-histo-img.pan
	pnormalization 0 255 cercle-$i-histo-img.pan | pim2uc - - | ppan2png - cercle-$i-histo.png
done
