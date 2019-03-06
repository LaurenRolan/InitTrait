 #!/bin/bash
generate3 () {
	echo $1
	for i in 0 1 2 
	do
   		pimc2img $i $1-barbara.pan $1-barbara-$i.pan
    	pmaximumvalue $1-barbara-$i.pan > toto
    	pstatus
	done
}

pbmp2pan barbara.bmp rgb-barbara.pan
generate3 'rgb'

prgb2hsl rgb-barbara.pan hsl-barbara.pan
generate3 'hsl'

prgb2hsl rgb-barbara.pan xyz-barbara.pan
generate3 'xyz'

prgb2yiq rgb-barbara.pan yiq-barbara.pan
generate3 'yiq'

prgb2yuv rgb-barbara.pan yuv-barbara.pan
generate3 'yuv'

pxyz2lab 6 xyz-barbara.pan lab-barbara.pan
generate3 'lab'

pxyz2luv 6 xyz-barbara.pan luv-barbara.pan
generate3 'luv'

for i in *.pan; do
    [ -f "$i" ] || break
    pnormalization 0 255 $i - | pim2uc - - | ppan2png - $i.png
    mv $i.png ${i%.pan}.png
done