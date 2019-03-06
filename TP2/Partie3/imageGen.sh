 #!/bin/bash
getFFT() {
	for i in carre cercle 
	do
		pnormalization 0 1 $i.pan $i.pan
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
		pifft $i-re.pan $i-im.pan $i-re.pan $i-im.pan		
		pmodulus damier-$i-re.pan damier-$i-im.pan damier-$i-rec.pan 
		plog damier-$i-rec.pan damier-$i-passe-bas.pan
	done	
}

getFFT
passeBas

for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done