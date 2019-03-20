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

dilatation() {
	pdilation 1 1 tools.pan tools-1.pan
}

recVis() {
	pskeletonization 8 tools-1.pan skeleton8-tools-1.pan
	ppostthinning skeleton8-tools-1.pan post8-tools-1.pan

	pbarbremoval -1 5 post8-tools-1.pan tools-nobarb.pan

	pclosedcontourselection 2 10 tools-nobarb.pan tools-loop.pan

	pdilationreconstruction 8 tools-loop.pan tools.pan tools-mask.pan

	pxor tools.pan tools-mask.pan tools-xor.pan
}

recClous() {

	pdilation 2 1 tools-xor.pan tools-no-vis.pan

	pskeletonization 4 tools-no-vis.pan skeleton-tools.pan
	ppostthinning skeleton-tools.pan post-tools.pan

	pbarbremoval -1 5 post-tools.pan tools-nobarb-c.pan

	plabeling 8 tools-nobarb-c.pan labels.pan

	pregionconvexity convexity labels.pan convexities.pan
	pcol2csv convexities.pan convexities.csv

	#Enlever labels relatives aux regions trop petites
	pconvexityselection 2 0.2 labels.pan relations.pan

	prg2im relations.pan - | pim2uc - haute-convex.pan

	pdilationreconstruction 8 haute-convex.pan tools.pan tools-clous-mask.pan

	pxor tools-xor.pan tools-clous-mask.pan tools-only.pan
}

dilatation
recVis
recClous
allToPNG