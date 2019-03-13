 #!/bin/bash
getFFT() {
	for i in carre cercle 
	do
		pnormalization 0 1 $i.pan $i.pan
		psetcst 0 $i.pan $i-i.pan
	 	pfft $i.pan $i-i.pan $i-re.pan $i-im.pan
 		pfftshift $i-re.pan $i-im.pan $i-re.pan $i-im.pan

 		pinverse  $i.pan $i-inv.pan
		pnormalization 0 1 $i-inv.pan $i-inv.pan
		psetcst 0 $i-inv.pan $i-i-inv.pan
	 	pfft $i-inv.pan $i-i-inv.pan $i-re-inv.pan $i-im-inv.pan
 		pfftshift $i-re-inv.pan $i-im-inv.pan $i-re-inv.pan $i-im-inv.pan

	done
	pbmp2pan damier.bmp damier.pan
	paddnoise 1 5 5 damier.pan damier-noise.pan
	psetcst 0 damier-noise.pan damier-i.pan
 	pfft damier-noise.pan damier-i.pan damier-re.pan damier-im.pan
 	pfftshift damier-re.pan damier-im.pan damier-re.pan damier-im.pan
}

passeBas() {
	for i in carre cercle 
	do		
		pmult damier-re.pan $i.pan damier-$i-re.pan
		pmult damier-im.pan $i.pan damier-$i-im.pan
		pfftshift damier-$i-re.pan damier-$i-im.pan damier-$i-re.pan damier-$i-im.pan
		pifft damier-$i-re.pan damier-$i-im.pan damier-$i-passe-bas.pan damier-$i-im.pan
	done	
}

passeHaut() {
	for i in carre cercle 
	do		
		pmult damier-re.pan $i-inv.pan damier-$i-re-inv.pan
		pmult damier-im.pan $i-inv.pan damier-$i-im-inv.pan
		pfftshift damier-$i-re-inv.pan damier-$i-im-inv.pan damier-$i-re-inv.pan damier-$i-im-inv.pan
		pifft damier-$i-re-inv.pan damier-$i-im-inv.pan damier-$i-passe-haut.pan $i-im-inv.pan		
	done	
}

removeImages() {
	for i in carre cercle 
	do		
		rm *-re.pan *-im.pan
		rm *-re-inv.pan *-im-inv.pan
	done	
}


getFFT
passeBas
passeHaut
removeImages

for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done