#
# Copyright (c) 2013, GREYC.
# All rights reserved
#
# You may use this file under the terms of the BSD license as follows:
#
# "Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of the GREYC, nor the name of its
#     contributors may be used to endorse or promote products
#     derived from this software without specific prior written
#     permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."#
# 
# For more information, refer to:
# https://clouard.users.greyc.fr/Pandore
#

"""
Python wrapper around Pandore.
"""
__author__ = ("Regis Clouard")

import subprocess

def executepandoreoperator( operator, args ):
    '''
    Executes a Pandore operator with the spezcified list of arguments.
    Returns the status value.
    '''
    commandline = [str(x) for x in (operator,) + args] 
    subprocess.Popen(commandline, stdout=subprocess.PIPE).communicate()[0]
    result = subprocess.Popen("pstatus", stdout=subprocess.PIPE).communicate()[0]
    if result.startswith('SUCCESS'):
        return True
    elif result.startswith('FAILURE'):
        return False
    else:
        try:
            return float(result)
        except ValueError:
            return result

def pvisu( filename ):
    subprocess.call(["pvisu", filename]);

def pabs( *args ):
    return executepandoreoperator('pabs', args)

def padd( *args ):
    return executepandoreoperator('padd', args)

def paddcst( *args ):
    return executepandoreoperator('paddcst', args)

def paddval( *args ):
    return executepandoreoperator('paddval', args)

def pblend( *args ):
    return executepandoreoperator('pblend', args)

def pclipvalues( *args ):
    return executepandoreoperator('pclipvalues', args)

def pconvolution( *args ):
    return executepandoreoperator('pconvolution', args)

def pdif( *args ):
    return executepandoreoperator('pdif', args)

def pdiv( *args ):
    return executepandoreoperator('pdiv', args)

def pdivcst( *args ):
    return executepandoreoperator('pdivcst', args)

def pdivval( *args ):
    return executepandoreoperator('pdivval', args)

def pexp( *args ):
    return executepandoreoperator('pexp', args)

def pintegralimage( *args ):
    return executepandoreoperator('pintegralimage', args)

def plipadd( *args ):
    return executepandoreoperator('plipadd', args)

def plipmultcst( *args ):
    return executepandoreoperator('plipmultcst', args)

def plipsub( *args ):
    return executepandoreoperator('plipsub', args)

def plog( *args ):
    return executepandoreoperator('plog', args)

def pmax( *args ):
    return executepandoreoperator('pmax', args)

def pmean( *args ):
    return executepandoreoperator('pmean', args)

def pmin( *args ):
    return executepandoreoperator('pmin', args)

def pmult( *args ):
    return executepandoreoperator('pmult', args)

def pmultcst( *args ):
    return executepandoreoperator('pmultcst', args)

def pmultval( *args ):
    return executepandoreoperator('pmultval', args)

def pnormalization( *args ):
    return executepandoreoperator('pnormalization', args)

def ppow( *args ):
    return executepandoreoperator('ppow', args)

def pround( *args ):
    return executepandoreoperator('pround', args)

def psetcst( *args ):
    return executepandoreoperator('psetcst', args)

def psqrt( *args ):
    return executepandoreoperator('psqrt', args)

def psquareintegralimage( *args ):
    return executepandoreoperator('psquareintegralimage', args)

def psub( *args ):
    return executepandoreoperator('psub', args)

def psubval( *args ):
    return executepandoreoperator('psubval', args)

def parray2array( *args ):
    return executepandoreoperator('parray2array', args)

def parrayargmax( *args ):
    return executepandoreoperator('parrayargmax', args)

def parraycovarmat( *args ):
    return executepandoreoperator('parraycovarmat', args)

def parrayeuclideannorm( *args ):
    return executepandoreoperator('parrayeuclideannorm', args)

def parraygetvalue( *args ):
    return executepandoreoperator('parraygetvalue', args)

def parraymean( *args ):
    return executepandoreoperator('parraymean', args)

def parraymedian( *args ):
    return executepandoreoperator('parraymedian', args)

def parraymode( *args ):
    return executepandoreoperator('parraymode', args)

def parraynorm( *args ):
    return executepandoreoperator('parraynorm', args)

def parraysize( *args ):
    return executepandoreoperator('parraysize', args)

def parraysmax( *args ):
    return executepandoreoperator('parraysmax', args)

def parraysmean( *args ):
    return executepandoreoperator('parraysmean', args)

def parraysmin( *args ):
    return executepandoreoperator('parraysmin', args)

def parraysnorm( *args ):
    return executepandoreoperator('parraysnorm', args)

def pcorrelationcoefficient( *args ):
    return executepandoreoperator('pcorrelationcoefficient', args)

def pcreatearray( *args ):
    return executepandoreoperator('pcreatearray', args)

def parray2im( *args ):
    return executepandoreoperator('parray2im', args)

def pgr2im( *args ):
    return executepandoreoperator('pgr2im', args)

def pgr2rg( *args ):
    return executepandoreoperator('pgr2rg', args)

def pim2array( *args ):
    return executepandoreoperator('pim2array', args)

def pim2d23d( *args ):
    return executepandoreoperator('pim2d23d', args)

def pim2rg( *args ):
    return executepandoreoperator('pim2rg', args)

def pim2sf( *args ):
    return executepandoreoperator('pim2sf', args)

def pim2sl( *args ):
    return executepandoreoperator('pim2sl', args)

def pim2uc( *args ):
    return executepandoreoperator('pim2uc', args)

def pim3d22d( *args ):
    return executepandoreoperator('pim3d22d', args)

def pimc2img( *args ):
    return executepandoreoperator('pimc2img', args)

def pimc2imx( *args ):
    return executepandoreoperator('pimc2imx', args)

def pimg2imc( *args ):
    return executepandoreoperator('pimg2imc', args)

def pimg2imx( *args ):
    return executepandoreoperator('pimg2imx', args)

def pimgs2imc( *args ):
    return executepandoreoperator('pimgs2imc', args)

def pimx2imc( *args ):
    return executepandoreoperator('pimx2imc', args)

def pimx2img( *args ):
    return executepandoreoperator('pimx2img', args)

def prg2gr( *args ):
    return executepandoreoperator('prg2gr', args)

def prg2im( *args ):
    return executepandoreoperator('prg2im', args)

def prg2imc( *args ):
    return executepandoreoperator('prg2imc', args)

def pgaussclassification( *args ):
    return executepandoreoperator('pgaussclassification', args)

def pkmeans( *args ):
    return executepandoreoperator('pkmeans', args)

def pknn( *args ):
    return executepandoreoperator('pknn', args)

def pcol2csv( *args ):
    return executepandoreoperator('pcol2csv', args)

def pcol2txt( *args ):
    return executepandoreoperator('pcol2txt', args)

def pcolcatenateitem( *args ):
    return executepandoreoperator('pcolcatenateitem', args)

def pcolgetimages( *args ):
    return executepandoreoperator('pcolgetimages', args)

def pcolgetobject( *args ):
    return executepandoreoperator('pcolgetobject', args)

def pcolgetvalue( *args ):
    return executepandoreoperator('pcolgetvalue', args)

def pcolremoveitem( *args ):
    return executepandoreoperator('pcolremoveitem', args)

def pcolrenameitem( *args ):
    return executepandoreoperator('pcolrenameitem', args)

def pcolsetobject( *args ):
    return executepandoreoperator('pcolsetobject', args)

def pcolsetvalue( *args ):
    return executepandoreoperator('pcolsetvalue', args)

def pnewcollection( *args ):
    return executepandoreoperator('pnewcollection', args)

def pobject2col( *args ):
    return executepandoreoperator('pobject2col', args)

def ptxt2col( *args ):
    return executepandoreoperator('ptxt2col', args)

def pcmyk2rgb( *args ):
    return executepandoreoperator('pcmyk2rgb', args)

def pgray2bw( *args ):
    return executepandoreoperator('pgray2bw', args)

def pgray2falsecolor( *args ):
    return executepandoreoperator('pgray2falsecolor', args)

def phsi2rgb( *args ):
    return executepandoreoperator('phsi2rgb', args)

def phsl2rgb( *args ):
    return executepandoreoperator('phsl2rgb', args)

def plab2lch( *args ):
    return executepandoreoperator('plab2lch', args)

def pluv2lch( *args ):
    return executepandoreoperator('pluv2lch', args)

def prgb2ast( *args ):
    return executepandoreoperator('prgb2ast', args)

def prgb2cmyk( *args ):
    return executepandoreoperator('prgb2cmyk', args)

def prgb2gray( *args ):
    return executepandoreoperator('prgb2gray', args)

def prgb2hsi( *args ):
    return executepandoreoperator('prgb2hsi', args)

def prgb2hsl( *args ):
    return executepandoreoperator('prgb2hsl', args)

def prgb2i1i2i3( *args ):
    return executepandoreoperator('prgb2i1i2i3', args)

def prgb2pca( *args ):
    return executepandoreoperator('prgb2pca', args)

def prgb2rngnbn( *args ):
    return executepandoreoperator('prgb2rngnbn', args)

def prgb2wry( *args ):
    return executepandoreoperator('prgb2wry', args)

def prgb2xyz( *args ):
    return executepandoreoperator('prgb2xyz', args)

def prgb2ycbcr( *args ):
    return executepandoreoperator('prgb2ycbcr', args)

def prgb2ych1ch2( *args ):
    return executepandoreoperator('prgb2ych1ch2', args)

def prgb2yiq( *args ):
    return executepandoreoperator('prgb2yiq', args)

def prgb2yuv( *args ):
    return executepandoreoperator('prgb2yuv', args)

def pxyz2lab( *args ):
    return executepandoreoperator('pxyz2lab', args)

def pxyz2luv( *args ):
    return executepandoreoperator('pxyz2luv', args)

def pxyz2rgb( *args ):
    return executepandoreoperator('pxyz2rgb', args)

def pyuv2rgb( *args ):
    return executepandoreoperator('pyuv2rgb', args)

def pbarbremoval( *args ):
    return executepandoreoperator('pbarbremoval', args)

def pblindedgeclosing( *args ):
    return executepandoreoperator('pblindedgeclosing', args)

def pclosedcontourselection( *args ):
    return executepandoreoperator('pclosedcontourselection', args)

def pcontourextensionconic( *args ):
    return executepandoreoperator('pcontourextensionconic', args)

def pcontourextensionrect( *args ):
    return executepandoreoperator('pcontourextensionrect', args)

def pcontourselection( *args ):
    return executepandoreoperator('pcontourselection', args)

def pdistance( *args ):
    return executepandoreoperator('pdistance', args)

def pdistance1( *args ):
    return executepandoreoperator('pdistance1', args)

def pedgeclosing( *args ):
    return executepandoreoperator('pedgeclosing', args)

def pedgedirection( *args ):
    return executepandoreoperator('pedgedirection', args)

def pellipsoidalapproximation( *args ):
    return executepandoreoperator('pellipsoidalapproximation', args)

def phoughlines( *args ):
    return executepandoreoperator('phoughlines', args)

def popencontourselection( *args ):
    return executepandoreoperator('popencontourselection', args)

def ppolygonalapproximation( *args ):
    return executepandoreoperator('ppolygonalapproximation', args)

def ppostthinning( *args ):
    return executepandoreoperator('ppostthinning', args)

def panalyze2pan( *args ):
    return executepandoreoperator('panalyze2pan', args)

def pany2pan( *args ):
    return executepandoreoperator('pany2pan', args)

def pbmp2pan( *args ):
    return executepandoreoperator('pbmp2pan', args)

def pfits2pan( *args ):
    return executepandoreoperator('pfits2pan', args)

def pgif2pan( *args ):
    return executepandoreoperator('pgif2pan', args)

def pjpeg2pan( *args ):
    return executepandoreoperator('pjpeg2pan', args)

def ppan2analyze( *args ):
    return executepandoreoperator('ppan2analyze', args)

def ppan2bmp( *args ):
    return executepandoreoperator('ppan2bmp', args)

def ppan2d23d( *args ):
    return executepandoreoperator('ppan2d23d', args)

def ppan2fits( *args ):
    return executepandoreoperator('ppan2fits', args)

def ppan2gif( *args ):
    return executepandoreoperator('ppan2gif', args)

def ppan2jpeg( *args ):
    return executepandoreoperator('ppan2jpeg', args)

def ppan2pan( *args ):
    return executepandoreoperator('ppan2pan', args)

def ppan2png( *args ):
    return executepandoreoperator('ppan2png', args)

def ppan2ppm( *args ):
    return executepandoreoperator('ppan2ppm', args)

def ppan2ps( *args ):
    return executepandoreoperator('ppan2ps', args)

def ppan2raw( *args ):
    return executepandoreoperator('ppan2raw', args)

def ppan2tiff( *args ):
    return executepandoreoperator('ppan2tiff', args)

def ppan2txt( *args ):
    return executepandoreoperator('ppan2txt', args)

def ppan2vff( *args ):
    return executepandoreoperator('ppan2vff', args)

def ppan3d22d( *args ):
    return executepandoreoperator('ppan3d22d', args)

def pparrec2pan( *args ):
    return executepandoreoperator('pparrec2pan', args)

def ppng2pan( *args ):
    return executepandoreoperator('ppng2pan', args)

def pppm2pan( *args ):
    return executepandoreoperator('pppm2pan', args)

def pras2pan( *args ):
    return executepandoreoperator('pras2pan', args)

def praw2pan( *args ):
    return executepandoreoperator('praw2pan', args)

def ptiff2pan( *args ):
    return executepandoreoperator('ptiff2pan', args)

def ptxt2pan( *args ):
    return executepandoreoperator('ptxt2pan', args)

def pvff2pan( *args ):
    return executepandoreoperator('pvff2pan', args)

def pyuv2pan( *args ):
    return executepandoreoperator('pyuv2pan', args)

def pderiche( *args ):
    return executepandoreoperator('pderiche', args)

def pdivneumann( *args ):
    return executepandoreoperator('pdivneumann', args)

def pgradient( *args ):
    return executepandoreoperator('pgradient', args)

def pgradientthreshold( *args ):
    return executepandoreoperator('pgradientthreshold', args)

def pgradneumann( *args ):
    return executepandoreoperator('pgradneumann', args)

def plaplacian( *args ):
    return executepandoreoperator('plaplacian', args)

def pnonmaximasuppression( *args ):
    return executepandoreoperator('pnonmaximasuppression', args)

def pprewitt( *args ):
    return executepandoreoperator('pprewitt', args)

def proberts( *args ):
    return executepandoreoperator('proberts', args)

def pshen( *args ):
    return executepandoreoperator('pshen', args)

def psobel( *args ):
    return executepandoreoperator('psobel', args)

def pzerocross( *args ):
    return executepandoreoperator('pzerocross', args)

def pborsotti( *args ):
    return executepandoreoperator('pborsotti', args)

def pinterregioncontrast( *args ):
    return executepandoreoperator('pinterregioncontrast', args)

def pintraregionuniformity( *args ):
    return executepandoreoperator('pintraregionuniformity', args)

def pmse( *args ):
    return executepandoreoperator('pmse', args)

def ppsnr( *args ):
    return executepandoreoperator('ppsnr', args)

def psnr( *args ):
    return executepandoreoperator('psnr', args)

def pvinet( *args ):
    return executepandoreoperator('pvinet', args)

def pzeboudj( *args ):
    return executepandoreoperator('pzeboudj', args)

def padaptivemeanfiltering( *args ):
    return executepandoreoperator('padaptivemeanfiltering', args)

def pdenoisePDE( *args ):
    return executepandoreoperator('pdenoisePDE', args)

def pderichesmoothing( *args ):
    return executepandoreoperator('pderichesmoothing', args)

def pexponentialfiltering( *args ):
    return executepandoreoperator('pexponentialfiltering', args)

def pgaussianfiltering( *args ):
    return executepandoreoperator('pgaussianfiltering', args)

def pmalikperonafiltering( *args ):
    return executepandoreoperator('pmalikperonafiltering', args)

def pmcmfiltering( *args ):
    return executepandoreoperator('pmcmfiltering', args)

def pmeanfiltering( *args ):
    return executepandoreoperator('pmeanfiltering', args)

def pmedianfiltering( *args ):
    return executepandoreoperator('pmedianfiltering', args)

def pnagaofiltering( *args ):
    return executepandoreoperator('pnagaofiltering', args)

def pnonlocalmeanfiltering( *args ):
    return executepandoreoperator('pnonlocalmeanfiltering', args)

def pnonlocalmedianfiltering( *args ):
    return executepandoreoperator('pnonlocalmedianfiltering', args)

def poutrangefiltering( *args ):
    return executepandoreoperator('poutrangefiltering', args)

def ppeergroupfiltering( *args ):
    return executepandoreoperator('ppeergroupfiltering', args)

def psharp( *args ):
    return executepandoreoperator('psharp', args)

def pshensmoothing( *args ):
    return executepandoreoperator('pshensmoothing', args)

def psigmafiltering( *args ):
    return executepandoreoperator('psigmafiltering', args)

def psnnfiltering( *args ):
    return executepandoreoperator('psnnfiltering', args)

def pvariancefiltering( *args ):
    return executepandoreoperator('pvariancefiltering', args)

def pbutterworthfilter( *args ):
    return executepandoreoperator('pbutterworthfilter', args)

def pdwt( *args ):
    return executepandoreoperator('pdwt', args)

def pfft( *args ):
    return executepandoreoperator('pfft', args)

def pfftconvolution( *args ):
    return executepandoreoperator('pfftconvolution', args)

def pfftcorrelation( *args ):
    return executepandoreoperator('pfftcorrelation', args)

def pfftdeconvolution( *args ):
    return executepandoreoperator('pfftdeconvolution', args)

def pfftshift( *args ):
    return executepandoreoperator('pfftshift', args)

def pgaussianfilter( *args ):
    return executepandoreoperator('pgaussianfilter', args)

def pgetsubband( *args ):
    return executepandoreoperator('pgetsubband', args)

def pidwt( *args ):
    return executepandoreoperator('pidwt', args)

def pifft( *args ):
    return executepandoreoperator('pifft', args)

def pmodulus( *args ):
    return executepandoreoperator('pmodulus', args)

def pphase( *args ):
    return executepandoreoperator('pphase', args)

def pqmf( *args ):
    return executepandoreoperator('pqmf', args)

def psetsubband( *args ):
    return executepandoreoperator('psetsubband', args)

def pbetagraph( *args ):
    return executepandoreoperator('pbetagraph', args)

def pdelaunay( *args ):
    return executepandoreoperator('pdelaunay', args)

def pedgecutting( *args ):
    return executepandoreoperator('pedgecutting', args)

def pedgevisu( *args ):
    return executepandoreoperator('pedgevisu', args)

def pgraphneighbours( *args ):
    return executepandoreoperator('pgraphneighbours', args)

def pgraphpruning( *args ):
    return executepandoreoperator('pgraphpruning', args)

def pgraphvisu( *args ):
    return executepandoreoperator('pgraphvisu', args)

def pleafcutting( *args ):
    return executepandoreoperator('pleafcutting', args)

def pmst( *args ):
    return executepandoreoperator('pmst', args)

def pnodedisc( *args ):
    return executepandoreoperator('pnodedisc', args)

def pnodevisu( *args ):
    return executepandoreoperator('pnodevisu', args)

def psig( *args ):
    return executepandoreoperator('psig', args)

def pcontrast1value( *args ):
    return executepandoreoperator('pcontrast1value', args)

def pcontrastvalue( *args ):
    return executepandoreoperator('pcontrastvalue', args)

def penergyvalue( *args ):
    return executepandoreoperator('penergyvalue', args)

def pentropyvalue( *args ):
    return executepandoreoperator('pentropyvalue', args)

def phistogram( *args ):
    return executepandoreoperator('phistogram', args)

def plocalextrema( *args ):
    return executepandoreoperator('plocalextrema', args)

def plocalmaxima( *args ):
    return executepandoreoperator('plocalmaxima', args)

def plocalminima( *args ):
    return executepandoreoperator('plocalminima', args)

def pmaximumvalue( *args ):
    return executepandoreoperator('pmaximumvalue', args)

def pmeanvalue( *args ):
    return executepandoreoperator('pmeanvalue', args)

def pmedianvalue( *args ):
    return executepandoreoperator('pmedianvalue', args)

def pminimumvalue( *args ):
    return executepandoreoperator('pminimumvalue', args)

def pmodevalue( *args ):
    return executepandoreoperator('pmodevalue', args)

def psumvalue( *args ):
    return executepandoreoperator('psumvalue', args)

def pvalueclassnumber( *args ):
    return executepandoreoperator('pvalueclassnumber', args)

def pvaluenumber( *args ):
    return executepandoreoperator('pvaluenumber', args)

def pvaluerank( *args ):
    return executepandoreoperator('pvaluerank', args)

def pvariancevalue( *args ):
    return executepandoreoperator('pvariancevalue', args)

def pproperty( *args ):
    return executepandoreoperator('pproperty', args)

def psetstatus( *args ):
    return executepandoreoperator('psetstatus', args)

def pstatus( *args ):
    return executepandoreoperator('pstatus', args)

def plinearinterpolation( *args ):
    return executepandoreoperator('plinearinterpolation', args)

def pand( *args ):
    return executepandoreoperator('pand', args)

def pinverse( *args ):
    return executepandoreoperator('pinverse', args)

def pmask( *args ):
    return executepandoreoperator('pmask', args)

def pnot( *args ):
    return executepandoreoperator('pnot', args)

def por( *args ):
    return executepandoreoperator('por', args)

def pxor( *args ):
    return executepandoreoperator('pxor', args)

def pextremumsharpening( *args ):
    return executepandoreoperator('pextremumsharpening', args)

def phistogramequalization( *args ):
    return executepandoreoperator('phistogramequalization', args)

def phistogramspecification( *args ):
    return executepandoreoperator('phistogramspecification', args)

def plineartransform( *args ):
    return executepandoreoperator('plineartransform', args)

def plogtransform( *args ):
    return executepandoreoperator('plogtransform', args)

def ppowerlawtransform( *args ):
    return executepandoreoperator('ppowerlawtransform', args)

def prds( *args ):
    return executepandoreoperator('prds', args)

def pstereogram( *args ):
    return executepandoreoperator('pstereogram', args)

def psubsampling( *args ):
    return executepandoreoperator('psubsampling', args)

def pareaclosing( *args ):
    return executepandoreoperator('pareaclosing', args)

def pareaopening( *args ):
    return executepandoreoperator('pareaopening', args)

def pdilatation( *args ):
    return executepandoreoperator('pdilatation', args)

def pdilatationreconstruction( *args ):
    return executepandoreoperator('pdilatationreconstruction', args)

def pdilation( *args ):
    return executepandoreoperator('pdilation', args)

def pdilationreconstruction( *args ):
    return executepandoreoperator('pdilationreconstruction', args)

def perosion( *args ):
    return executepandoreoperator('perosion', args)

def perosionreconstruction( *args ):
    return executepandoreoperator('perosionreconstruction', args)

def pgeodesicdilatation( *args ):
    return executepandoreoperator('pgeodesicdilatation', args)

def pgeodesicdilation( *args ):
    return executepandoreoperator('pgeodesicdilation', args)

def pgeodesicerosion( *args ):
    return executepandoreoperator('pgeodesicerosion', args)

def phitormiss( *args ):
    return executepandoreoperator('phitormiss', args)

def phomotopicskeletonization( *args ):
    return executepandoreoperator('phomotopicskeletonization', args)

def plineardilatation( *args ):
    return executepandoreoperator('plineardilatation', args)

def plineardilation( *args ):
    return executepandoreoperator('plineardilation', args)

def plinearerosion( *args ):
    return executepandoreoperator('plinearerosion', args)

def pnonlocaldilation( *args ):
    return executepandoreoperator('pnonlocaldilation', args)

def pnonlocalerosion( *args ):
    return executepandoreoperator('pnonlocalerosion', args)

def psedesign( *args ):
    return executepandoreoperator('psedesign', args)

def psedilatation( *args ):
    return executepandoreoperator('psedilatation', args)

def psedilation( *args ):
    return executepandoreoperator('psedilation', args)

def pseerosion( *args ):
    return executepandoreoperator('pseerosion', args)

def pskeletonization( *args ):
    return executepandoreoperator('pskeletonization', args)

def pwatershed( *args ):
    return executepandoreoperator('pwatershed', args)

def pblockmatching( *args ):
    return executepandoreoperator('pblockmatching', args)

def pplotquiver( *args ):
    return executepandoreoperator('pplotquiver', args)

def pregistrationPDE( *args ):
    return executepandoreoperator('pregistrationPDE', args)

def pharris( *args ):
    return executepandoreoperator('pharris', args)

def psusan( *args ):
    return executepandoreoperator('psusan', args)

def pgetquadrangle( *args ):
    return executepandoreoperator('pgetquadrangle', args)

def pquadrangle2rectangle( *args ):
    return executepandoreoperator('pquadrangle2rectangle', args)

def pskewanglecorrection( *args ):
    return executepandoreoperator('pskewanglecorrection', args)

def pareaselection( *args ):
    return executepandoreoperator('pareaselection', args)

def pboundary( *args ):
    return executepandoreoperator('pboundary', args)

def pboundaryregularization( *args ):
    return executepandoreoperator('pboundaryregularization', args)

def pboundingbox( *args ):
    return executepandoreoperator('pboundingbox', args)

def pcenterofmass( *args ):
    return executepandoreoperator('pcenterofmass', args)

def pcompactnessselection( *args ):
    return executepandoreoperator('pcompactnessselection', args)

def pconvexhull( *args ):
    return executepandoreoperator('pconvexhull', args)

def pconvexityselection( *args ):
    return executepandoreoperator('pconvexityselection', args)

def pdensityselection( *args ):
    return executepandoreoperator('pdensityselection', args)

def peccentricityselection( *args ):
    return executepandoreoperator('peccentricityselection', args)

def pelongationselection( *args ):
    return executepandoreoperator('pelongationselection', args)

def penergyselection( *args ):
    return executepandoreoperator('penergyselection', args)

def peulernumberselection( *args ):
    return executepandoreoperator('peulernumberselection', args)

def pfillhole( *args ):
    return executepandoreoperator('pfillhole', args)

def pholeselection( *args ):
    return executepandoreoperator('pholeselection', args)

def pinnerselection( *args ):
    return executepandoreoperator('pinnerselection', args)

def plabelmasking( *args ):
    return executepandoreoperator('plabelmasking', args)

def plabelselection( *args ):
    return executepandoreoperator('plabelselection', args)

def plabelsselection( *args ):
    return executepandoreoperator('plabelsselection', args)

def pmaximumselection( *args ):
    return executepandoreoperator('pmaximumselection', args)

def pmeanselection( *args ):
    return executepandoreoperator('pmeanselection', args)

def pminimumselection( *args ):
    return executepandoreoperator('pminimumselection', args)

def porientationselection( *args ):
    return executepandoreoperator('porientationselection', args)

def poutborderselection( *args ):
    return executepandoreoperator('poutborderselection', args)

def pperimeterselection( *args ):
    return executepandoreoperator('pperimeterselection', args)

def prectangularityselection( *args ):
    return executepandoreoperator('prectangularityselection', args)

def prelabelingfromarray( *args ):
    return executepandoreoperator('prelabelingfromarray', args)

def prelabelingwithgraph( *args ):
    return executepandoreoperator('prelabelingwithgraph', args)

def psizeselection( *args ):
    return executepandoreoperator('psizeselection', args)

def psphericityselection( *args ):
    return executepandoreoperator('psphericityselection', args)

def pvarianceselection( *args ):
    return executepandoreoperator('pvarianceselection', args)

def pvolumeselection( *args ):
    return executepandoreoperator('pvolumeselection', args)

def pareadisorderfactor( *args ):
    return executepandoreoperator('pareadisorderfactor', args)

def pregionarea( *args ):
    return executepandoreoperator('pregionarea', args)

def pregioncompactness( *args ):
    return executepandoreoperator('pregioncompactness', args)

def pregionconvexity( *args ):
    return executepandoreoperator('pregionconvexity', args)

def pregiondensity( *args ):
    return executepandoreoperator('pregiondensity', args)

def pregiondepth( *args ):
    return executepandoreoperator('pregiondepth', args)

def pregioneccentricity( *args ):
    return executepandoreoperator('pregioneccentricity', args)

def pregionelongation( *args ):
    return executepandoreoperator('pregionelongation', args)

def pregionenergy( *args ):
    return executepandoreoperator('pregionenergy', args)

def pregioneulernumber( *args ):
    return executepandoreoperator('pregioneulernumber', args)

def pregionheight( *args ):
    return executepandoreoperator('pregionheight', args)

def pregionmaximum( *args ):
    return executepandoreoperator('pregionmaximum', args)

def pregionmean( *args ):
    return executepandoreoperator('pregionmean', args)

def pregionminimum( *args ):
    return executepandoreoperator('pregionminimum', args)

def pregionorientation( *args ):
    return executepandoreoperator('pregionorientation', args)

def pregionperimeter( *args ):
    return executepandoreoperator('pregionperimeter', args)

def pregionrectangularity( *args ):
    return executepandoreoperator('pregionrectangularity', args)

def pregionsphericity( *args ):
    return executepandoreoperator('pregionsphericity', args)

def pregionvariance( *args ):
    return executepandoreoperator('pregionvariance', args)

def pregionvolume( *args ):
    return executepandoreoperator('pregionvolume', args)

def pregionwidth( *args ):
    return executepandoreoperator('pregionwidth', args)

def pboundarylabeling( *args ):
    return executepandoreoperator('pboundarylabeling', args)

def pboundarymerging( *args ):
    return executepandoreoperator('pboundarymerging', args)

def pcolorquantization( *args ):
    return executepandoreoperator('pcolorquantization', args)

def pcontrast1quadtree( *args ):
    return executepandoreoperator('pcontrast1quadtree', args)

def pcontrastaggregation( *args ):
    return executepandoreoperator('pcontrastaggregation', args)

def pcontrastmerging( *args ):
    return executepandoreoperator('pcontrastmerging', args)

def pcontrastquadtree( *args ):
    return executepandoreoperator('pcontrastquadtree', args)

def pedgebasedragpruning( *args ):
    return executepandoreoperator('pedgebasedragpruning', args)

def pentropymerging( *args ):
    return executepandoreoperator('pentropymerging', args)

def pentropyquadtree( *args ):
    return executepandoreoperator('pentropyquadtree', args)

def pgaussaggregation( *args ):
    return executepandoreoperator('pgaussaggregation', args)

def phistomerging( *args ):
    return executepandoreoperator('phistomerging', args)

def pinnermerging( *args ):
    return executepandoreoperator('pinnermerging', args)

def pinnermostmerging( *args ):
    return executepandoreoperator('pinnermostmerging', args)

def plabeling( *args ):
    return executepandoreoperator('plabeling', args)

def plabelmerging( *args ):
    return executepandoreoperator('plabelmerging', args)

def pmeanaggregation( *args ):
    return executepandoreoperator('pmeanaggregation', args)

def pmeanmerging( *args ):
    return executepandoreoperator('pmeanmerging', args)

def pmeanshiftsegmentation( *args ):
    return executepandoreoperator('pmeanshiftsegmentation', args)

def pmumfordshahmerging( *args ):
    return executepandoreoperator('pmumfordshahmerging', args)

def pseedplacement( *args ):
    return executepandoreoperator('pseedplacement', args)

def psuperpixelsegmentation( *args ):
    return executepandoreoperator('psuperpixelsegmentation', args)

def puniformitymerging( *args ):
    return executepandoreoperator('puniformitymerging', args)

def puniformityquadtree( *args ):
    return executepandoreoperator('puniformityquadtree', args)

def pvarianceaggregation( *args ):
    return executepandoreoperator('pvarianceaggregation', args)

def pvariancemerging( *args ):
    return executepandoreoperator('pvariancemerging', args)

def pvariancequadtree( *args ):
    return executepandoreoperator('pvariancequadtree', args)

def pvoronoi( *args ):
    return executepandoreoperator('pvoronoi', args)

def plegendrepolynomialfitting( *args ):
    return executepandoreoperator('plegendrepolynomialfitting', args)

def plinearregression( *args ):
    return executepandoreoperator('plinearregression', args)

def ppolynomialfitting( *args ):
    return executepandoreoperator('ppolynomialfitting', args)

def pcrosscorrelation( *args ):
    return executepandoreoperator('pcrosscorrelation', args)

def padaptivemeanbinarization( *args ):
    return executepandoreoperator('padaptivemeanbinarization', args)

def pbinarization( *args ):
    return executepandoreoperator('pbinarization', args)

def pchanda( *args ):
    return executepandoreoperator('pchanda', args)

def pcontrastbinarization( *args ):
    return executepandoreoperator('pcontrastbinarization', args)

def pcontrastthresholding( *args ):
    return executepandoreoperator('pcontrastthresholding', args)

def pcorrelationbinarization( *args ):
    return executepandoreoperator('pcorrelationbinarization', args)

def pderavi( *args ):
    return executepandoreoperator('pderavi', args)

def pentropybinarization( *args ):
    return executepandoreoperator('pentropybinarization', args)

def pentropythresholding( *args ):
    return executepandoreoperator('pentropythresholding', args)

def pfisher( *args ):
    return executepandoreoperator('pfisher', args)

def pfuzzyclustering( *args ):
    return executepandoreoperator('pfuzzyclustering', args)

def phistothresholding( *args ):
    return executepandoreoperator('phistothresholding', args)

def pmassbinarization( *args ):
    return executepandoreoperator('pmassbinarization', args)

def pniblackbinarization( *args ):
    return executepandoreoperator('pniblackbinarization', args)

def pthresholding( *args ):
    return executepandoreoperator('pthresholding', args)

def pvariancebinarization( *args ):
    return executepandoreoperator('pvariancebinarization', args)

def pweszka( *args ):
    return executepandoreoperator('pweszka', args)

def paddborder( *args ):
    return executepandoreoperator('paddborder', args)

def pbellrescale( *args ):
    return executepandoreoperator('pbellrescale', args)

def pbicubicrescale( *args ):
    return executepandoreoperator('pbicubicrescale', args)

def pextrude1d22d( *args ):
    return executepandoreoperator('pextrude1d22d', args)

def pflip( *args ):
    return executepandoreoperator('pflip', args)

def phermiterescale( *args ):
    return executepandoreoperator('phermiterescale', args)

def planczosrescale( *args ):
    return executepandoreoperator('planczosrescale', args)

def plinearrescale( *args ):
    return executepandoreoperator('plinearrescale', args)

def pmaxprojection( *args ):
    return executepandoreoperator('pmaxprojection', args)

def pmeanprojection( *args ):
    return executepandoreoperator('pmeanprojection', args)

def pmitchellrescale( *args ):
    return executepandoreoperator('pmitchellrescale', args)

def prescale( *args ):
    return executepandoreoperator('prescale', args)

def presize( *args ):
    return executepandoreoperator('presize', args)

def protation( *args ):
    return executepandoreoperator('protation', args)

def pscrolling( *args ):
    return executepandoreoperator('pscrolling', args)

def ptranslation( *args ):
    return executepandoreoperator('ptranslation', args)

def ptransposition( *args ):
    return executepandoreoperator('ptransposition', args)

def paddnoise( *args ):
    return executepandoreoperator('paddnoise', args)

def paddslice( *args ):
    return executepandoreoperator('paddslice', args)

def pcliparea( *args ):
    return executepandoreoperator('pcliparea', args)

def pcopyborder( *args ):
    return executepandoreoperator('pcopyborder', args)

def pdepth2graylevel( *args ):
    return executepandoreoperator('pdepth2graylevel', args)

def pextractregion( *args ):
    return executepandoreoperator('pextractregion', args)

def pextractsubimage( *args ):
    return executepandoreoperator('pextractsubimage', args)

def pgetband( *args ):
    return executepandoreoperator('pgetband', args)

def pgetslice( *args ):
    return executepandoreoperator('pgetslice', args)

def pgetwindowaroundpoints( *args ):
    return executepandoreoperator('pgetwindowaroundpoints', args)

def pgraylevel2depth( *args ):
    return executepandoreoperator('pgraylevel2depth', args)

def pinsertregion( *args ):
    return executepandoreoperator('pinsertregion', args)

def pinsertsubimage( *args ):
    return executepandoreoperator('pinsertsubimage', args)

def pmergeimages( *args ):
    return executepandoreoperator('pmergeimages', args)

def pnewimage( *args ):
    return executepandoreoperator('pnewimage', args)

def ppixelvalue( *args ):
    return executepandoreoperator('ppixelvalue', args)

def premoveslice( *args ):
    return executepandoreoperator('premoveslice', args)

def psetband( *args ):
    return executepandoreoperator('psetband', args)

def psetborder( *args ):
    return executepandoreoperator('psetborder', args)

def psetpixel( *args ):
    return executepandoreoperator('psetpixel', args)

def psetslice( *args ):
    return executepandoreoperator('psetslice', args)

def pshapedesign( *args ):
    return executepandoreoperator('pshapedesign', args)

def psplitimage( *args ):
    return executepandoreoperator('psplitimage', args)

def pcolorcube( *args ):
    return executepandoreoperator('pcolorcube', args)

def pcolorize( *args ):
    return executepandoreoperator('pcolorize', args)

def pcontentsdisplay( *args ):
    return executepandoreoperator('pcontentsdisplay', args)

def pplot1d( *args ):
    return executepandoreoperator('pplot1d', args)

def psuperimposition( *args ):
    return executepandoreoperator('psuperimposition', args)
