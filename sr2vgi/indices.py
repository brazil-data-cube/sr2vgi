def ndvi_re(redge1, nir):
    # Normalized Difference Vegetation Index 690-710 - ok
    ndvi_re = (nir - redge1) / (nir + redge1)
    return ndvi_re


def cii_re(redge1, nir):
    # Chlorophyll IndexRedEdge - ok
    cii_re = nir / redge1 - 1.0
    return cii_re


def gcvi(bnir, green):
    # Chlorophyll Green - ok
    gcvi = (bnir / green) - 1.0  #
    return gcvi


def msr(nir, red, coastal):
    # Modified Simple Ratio - ok
    # msr = (nir - coastal) / (red - coastal)
    msr = ((nir / red) - 1) / ((nir / red) * 0.5 + 1)
    return msr


def msr_re(nir, red):
    import numpy
    # Modified Simple Ratio 670,800 - ok
    msr_re = ((nir / red) - 1.0) / numpy.sqrt((nir / red) + 1.0)
    return msr_re


def msr_ren(nir, redge1):
    import numpy
    # Modified Simple Ratio 670,800 - ok
    msr_ren = ((nir / redge1) - 1.0) / numpy.sqrt((nir / redge1) + 1.0)
    return msr_ren


def ci_re(redge3, redge1):
    import numpy
    # Chlorophyll Red-Edge - ok
    ci_re = numpy.power((redge3 / redge1), (-1.0))
    return ci_re


def rervi(nir, redge1):
    # red-edge vegentation index - ok
    rervi = nir / redge1
    return rervi


def ireci(red, redge1, redge2, redge3):
    # Inverted Red-Edge Chlorophyll Index (IRECI) - ok
    ireci = (redge3 - red) / (redge1 / redge2)  # IRECI
    return ireci


def IRECI2(red, redge1, redge2, nir):
    # Inverted Red-Edge Chlorophyll Index (IRECI) - ok
    IRECI2 = (nir - red) / (redge1 / redge2)
    return IRECI2


def NDre1m(coastal, redge1, redge2):
    # Normalized Difference NIR/SWIR Normalized Burn Ratio
    # Normalized Difference red - edge 1 modified - ok
    NDre1m = (redge2 - redge1) / (redge2 + redge1 - 2 * coastal)  #
    return NDre1m


def NDre2m(coastal, redge1, redge3):
    # Normalized Difference red - edge 2 modified - ok
    NDre2m = (redge3 - redge1) / (redge3 + redge1 - 2 * coastal)
    return NDre2m


def SRre1(coastal, redge1, redge2):
    # Simple Ratio Red edge1 - ok
    SRre1 = (redge2 - coastal) / (redge1 - coastal)  #
    return SRre1


def SRre2(coastal, redge1, redge3):
    # Simple Ratio Red edge2 - ok
    SRre2 = (redge3 - coastal) / (redge1 - coastal)  #
    return SRre2


def MSRren(bnir, redge1):
    import numpy
    # Modified Simple Ratio red - edge narrow
    # msren = (( bnir / redge1 ) - 1)  / (numpy.power( ((1 / 2) + 1),2)) #
    MSRren = ((bnir / redge1) - 1) / (( (bnir / redge1) + 1) **2  )
    return MSRren


def NDSWIR2(nir, swir2):
    # Normalized Difference NIR/SWIR Normalized Burn Ratio 2 - ok
    NDSWIR2 = (nir - swir2) / (nir + swir2)
    return NDSWIR2


def MNDWI(green, swir1):
    # modified normalized difference water index - ok
    MNDWI = (green - swir1) / (green + swir1)  #
    return MNDWI

def REIP1(redge3, redge2, redge1, red):
    # Red-Edge Inflection Point 1 - ok
    REIP1 = 700.0 + 40.0 * ((((red + redge3) / 2.0) - redge1) / (redge2 - redge1))
    return REIP1


def REIP2(redge3, redge2, redge1, red):
    # Red-Edge Inflection Point 2 - ok
    REIP2 = 702.0 + 40.0 * ((((red + redge3) / 2.0) - redge1) / (redge2 - redge1))
    return REIP2


def REIP3(redge3, redge2, redge1, red):
    # Red-Edge Inflection Point 3 - ok
    REIP3 = 705.0 + 35.0 * ((((red + redge3) / 2.0) - redge1) / (redge2 - redge1))
    return REIP3


def ndvi_re2(redge2, red):
    # Normalized Difference Vegetation proposta Michel - ok
    ndvi_re2 = (redge2 - red) / (redge2 + red)
    return ndvi_re2


def ndvi_resw(redge2, swir2):
    # Normalized Difference Vegetation Red-edge Swir2 - ok
    ndvi_resw = (redge2 - swir2) / (redge2 + swir2)
    return ndvi_resw


def psri(red, redge2, green):
    # Plant Senescent Reflection Index - ok
    psri = (red - green) / redge2
    return psri


def mtci(red, redge2, redge1):
    # MERIS Terrestrial Chlorophyll Index - ok
    mtci = (redge2 - redge1) / (redge1 + red)
    return mtci


def mcari(red, green, redge1):
    # Modified Chlorophyll Absorption Ratio Index - ok
    mcari = ((redge1 - red) - 0.2 * (redge1 - green)) * (redge1 / red)
    return mcari


def mcari2(red, green, redge3):
    import numpy
    # Modified Chlorophyll Absorption in Reflectance Index 2 - ok
    mcari2 = 1.5 * (2.5 * (redge3 - red) - 1.3 * (redge3 - green)) / numpy.power(
        (2 * redge3 + 1) ** 2 - (6 * redge3 - 5 * numpy.power(red, 2) - 0.5), 2)
    return mcari2


def ndii(bnir, swir1):
    # Normalized difference infrared index - ok
    ndii = (bnir - swir1) / (bnir + swir1)
    return ndii


def nbr2(bnir, swir2):
    # Normalized difference NIR/SWIR normalized burn ratio - ok
    nbr2 = (bnir - swir2) / (bnir + swir2)
    return nbr2


def nmdi(bnir, swir1, swir2):
    # Normalized Multi-band Drought Index
    nmdi = bnir - (swir1 - swir2) / (bnir + (swir1 - swir2))
    return nmdi


def rededge_peak(bnir, redge1, redge2, redge3, red):
    # Red-edge Peak Area - ok
    rededge_peak = red + redge1 + redge2 + redge3 + bnir
    return rededge_peak


def rtvicore(bnir, redge1, green):
    # Red-edge Triangular Vegetation Index - ok
    rtvicore = 100 * (bnir - redge1) - 10 * (bnir - green)
    return rtvicore


def cl_indexgreen(nir, green):
    # Chlorophyll index green - ok
    cl_indexgreen = nir / green - 1.0
    return cl_indexgreen


def cl_green(green, redge3):
    import numpy
    # Chlorophyll index green (extraido do IDB) - ok
    cl_green = numpy.power((redge3 / green), (-1.0))
    return cl_green


def CARI2(red, green, redge1):
    import numpy
    # Nome: Chlorophyll Absorption Reflectance Index - ok
    a = 0.567
    CARI2 = (abs(((redge1 - green) / 150.0 * red + red + green - (a * green))) / numpy.power(
        (numpy.power(a, 2.0) + 1.0), 0.5)) * (redge1 / red)
    return CARI2


def cl_indexgreensen(nir, green, redge1):
    # Chlorophyll index green (extraido do IDB) - ok
    cl_indexgreensen = (redge1 / green) - 1
    return cl_indexgreensen


def cl_indexgreen1(nir, green, redge1):
    # Chlorophyll index green 1 (extraido do IDB) - ok
    cl_indexgreen1 = nir / green - redge1
    return cl_indexgreen1


def cl_indexgreen2(nir, green, redge2):
    # Chlorophyll index green 2 (extraido do IDB) - ok
    cl_indexgreen2 = nir / green - redge2
    return cl_indexgreen2


def cl_indexgreen3(nir, green, redge3):
    # Chlorophyll index green 3 (extraido do IDB) - ok
    cl_indexgreen3 = nir / green - redge3
    return cl_indexgreen3


def gemi(red, nir):
    import numpy
    # Global Environment Monitoring Index - ok
    gemi = ((2.0 * ((nir ** 2.0) - (red ** 2.0)) + 1.5 * nir + 0.5 * red) / (nir + red + 0.5) * (
                1.0 - 0.25 * (2.0 * ((nir ** 2.0) - (red ** 2.0)) + 1.5 * nir + 0.5 * red) / (nir + red + 0.5)) - (
                        red - 0.125) / (1.0 - red))
    gemi[gemi > 1.5] = numpy.nan
    return gemi


def pvi(nir):
    import numpy
    # Perpendicular Vegetation Index - ok
    pvi = (1.0 / numpy.sqrt(numpy.power(0.149, 2.0) + 1.0)) * (nir - 0.374 - 0.735)
    return pvi


def redgei2(redge1, red):
    # Red-edge index 2 (SentinelHub) - ok
    redgei2 = (redge1 - red) / (redge1 + red)
    return redgei2


def redgei1(redge1, red):
    # Red-edge index 1 (SentinelHub) - ok
    redgei1 = (redge1 / red)
    return redgei1


def RBNDVI(nir, red, blue):
    # Red–blue normalized difference vegetation index - ok
    RBNDVI = (nir - (red + blue)) / (nir + (red + blue))
    return RBNDVI


def PVR(green, red):
    # Photosynthetic Vigor Ratio - ok
    PVR = (green - red) / (green + red)
    return PVR


def gndvi(nir, green):
    # Green Normalized Difference Vegetation Index - ok
    gndvi = (nir - green) / (nir + green)
    return gndvi


def ndwi1(swir1, nir):
    # Normalized Difference Water Index (NDWI GAO) - ok
    ndwi1 = (nir - swir1) / (nir + swir1)
    return ndwi1


def ndwi2(green, nir):
    # Normalized Difference Water Index (NDWI MCFEETERS) - ok
    ndwi2 = (green - nir) / (green + nir)
    return ndwi2


def nhi(swir1, green):
    # Normalized Humidity Index - ok
    nhi = (swir1 - green) / (swir1 + green)
    return nhi


def ndbi(swir1, nir):
    # Normalized Difference Built-up Index - ok
    ndbi = (swir1 - nir) / (swir1 + nir)
    return ndbi


def tcari1(redge1, red, green):
    # Transformed Chlorophyll Absorption in Reflectance Index
    tcari1 = 3 * ((redge1 - red) - 0.2 * (redge1 - green) * (redge1 / red))
    return tcari1


def tcari2(redge2, red, green):
    # Transformed Chlorophyll Absorption in Reflectance Index - proposição redge1 por redge2 - ok
    tcari2 = 3 * ((redge2 - red) - 0.2 * (redge2 - green) * (redge2 / red))
    return tcari2


def tvi(green, red, redge2):
    # Triangular Vegetation Index - ok
    tvi = 0.5 * (120 * (redge2 - green) - 200 * (red - green))
    return tvi


def mtvi1(nir, green, red):
    # Modified Triangle Vegetation Index - ok
    mtvi1 = 1.2 * (1.2 * (nir - green) - 2.5 * (red - green))
    return mtvi1


def mtvi2(nir, redge3, green, red):
    import numpy
    # Modified Triangle Vegetation Index
    # Fórmula original: 1.5 * ( 1.2 * (nir - green) - 2.5 * (red - green) ) / numpy.power( ((2 * nir + 1 )**2 - (6 * nir - 5 * numpy.power(red, 0.5 ))), - 0.5 )
    mtvi2 = (1.5 * (1.2 * (nir - green) - 2.5 * (red - green))) / numpy.sqrt(
        (2 * nir + 1) ** 2 - (6 * nir - 5 * numpy.sqrt(red)) - 0.5)
    return mtvi2


def rsr(nir, redge3, red, swir1):
    import numpy
    # swir index Reduced Simple Ratio
    # Fórmula original: (redge3/red) * ( (numpy.max(swir1) - swir1) / (numpy.max(swir1) - numpy.min(swir1)))
    rsr = (nir / red) * ((numpy.max(swir1) - swir1) / (numpy.max(swir1) - numpy.min(swir1)))
    return rsr


def vi700(redge1, red):
    # Vegetation index 700
    vi700 = (redge1 - red) / (redge1 + red)
    return vi700


def PVR_2(green, red):
    # Photosynthetic vigor ratio 2 - ok
    PVR_2 = (green - red) / (green + red)
    return PVR_2


def ngrdi(green, redge1):
    # Normalized green red difference index - ok
    ngrdi = (green - redge1) / (green + redge1)
    return ngrdi


def ngrdi2(green, red):
    # Normalized Green-Red Difference Index - ok
    ngrdi2 = (green - red) / (green + red)
    return ngrdi2


def ari(green, redge1):
    # Anthocyanin reflectance index
    ari = (1 / green) - (1 / redge1)
    return ari


def savi(nir, red):
    # Soil-Adjusted Vegetation Index
    savi = ((nir - red)) / ((nir + red + 0.5)) * 1.5
    return savi


def CARI(red, green, redge1):
    import numpy
    # Chlorophyll absorption ratio index
    #CARI = (redge1 / red) * (numpy.sqrt(numpy.power( ( ((redge1 - green) / 150.0) * 670.0 + red + (green - (( (redge1 - green) / 150.0) * 550.0))), 2.0)) ) / (numpy.power( (( (redge1 - green) / numpy.power(150.0, 2.0)) + 1.0), 0.5))
    a = (redge1 - green) / 150.0
    b = green*550*a
    CARI = (redge1 * numpy.sqrt(( a * red + red + b)**2) / red) * (a**2 + 1)

    return CARI


def NDTI(swir1,swir2):
    # Normalized Difference Tillage Index - ok
    NDTI = ((swir1 - swir2)) / ((swir1 + swir2))
    return NDTI

def NDrededgeSWIR(redge2,swir2):
    # Normalized Difference Red-edge and SWIR - ok
    NDrededgeSWIR = (redge2 - swir2) / (redge2 + swir2)
    return NDrededgeSWIR


def S2REP(red,redge1,redge2,redge3):
    # S2 Red-edge Position - ok
    S2REP = 705 + 35 * ((((redge3 + red / 2) - redge1) / redge2 - redge1))
    return S2REP


def CRI700(blue, redge1):
    # Carotenoid reflectance index 700 - ok
    CRI700 = (1 / blue) - (1 / redge1)
    return CRI700


def AFRI(nir,swir1):
    # Aerosol Free Vegetation Index - ok
    AFRI = (nir - (0.66 * swir1)) / (nir + (0.66 * swir1))
    return AFRI


def SIPI(nir,green,red):
    # Structure intensive pigment index - ok
    SIPI = (nir - green) / (nir - red)
    return SIPI


def AVI(nir,red):
    # Ashburn Vegetation Index
    avi = 2 * nir - red
    return avi
def NDre1(redge1,redge2):
    NDre1 = (redge2 - redge1) / (redge2 + redge1)
    return NDre1
