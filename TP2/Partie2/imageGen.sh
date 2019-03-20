 #!/bin/bash
removeFiles() {
	for i in ref target res
	do
		rm $i-re.pan
		rm $i-im.pan	
	done
	rm mod.pan
	rm res-nim.pan
	rm ref-i.pan
	rm target-i.pan
}

getPANandFFT() {
	for i in ref target
	do
		ptiff2pan $i.tif $i.pan
		psetcst 0 $i.pan $i-i.pan
   		pfft $i.pan $i-i.pan $i-re.pan $i-im.pan
   		pfftshift $i-re.pan $i-im.pan $i-re.pan $i-im.pan
	done
}

getPANandFFT

echo "Got PAN and FFT"

pmult ref-re.pan target-re.pan res-re.pan
pmult ref-im.pan target-im.pan res-im.pan
padd res-re.pan res-im.pan res-re.pan

pmult ref-re.pan target-im.pan res-im.pan
pmult ref-im.pan target-re.pan res-nim.pan
psub res-im.pan res-nim.pan res-im.pan

echo "Multiplication ended"

pmodulus ref-re.pan ref-im.pan mod.pan
pmult mod.pan mod.pan mod.pan

echo "Modulus ended"

pdiv res-re.pan mod.pan res-re.pan
pdiv res-im.pan mod.pan res-im.pan

echo "Division ended"

pifft res-re.pan res-im.pan res-re.pan res-im.pan
pfftshift res-re.pan res-im.pan res-re.pan res-im.pan
pmodulus res-re.pan res-im.pan res.pan
pbinarization  0.14 0.16 res.pan res.pan

removeFiles

echo "Files removed"



for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done
