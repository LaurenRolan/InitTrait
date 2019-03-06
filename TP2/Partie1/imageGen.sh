 #!/bin/bash
rotate() {
	for i in carre cercle rectangle 
	do
		protation 1 25 normal-$i.pan rotation-$i.pan		
	done
}

translate() {
	for i in carre cercle rectangle 
	do
		ptranslation 1 25 normal-$i.pan translation-$i.pan		
	done
}

rotateAndTranslate() {
	for i in carre cercle rectangle 
	do
		ptranslation 1 25 rotation-$i.pan transRot-$i.pan		
	done
}

getFFT () {
	for i in carre cercle rectangle 
	do
		psetcst 0 $1-$i.pan $1-$i-i.pan
   		pfft $1-$i.pan $1-$i-i.pan $1-$i-re.pan $1-$i-im.pan
   		pfftshift $1-$i-re.pan $1-$i-im.pan $1-$i-re.pan $1-$i-im.pan
	done
}

reconstruct() {
	for i in carre cercle rectangle 
	do
		pmodulus $1-$i-re.pan $1-$i-im.pan $1-$i-rec.pan 
		plog $1-$i-rec.pan $1-$i-rec.pan
	done
}

rotate
translate
rotateAndTranslate
getFFT 'normal'
getFFT 'rotation'
getFFT 'translation'
getFFT 'transRot'

reconstruct 'normal'
reconstruct 'rotation'
reconstruct 'translation'
reconstruct 'transRot'

for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done