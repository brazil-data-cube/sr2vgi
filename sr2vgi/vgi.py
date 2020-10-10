import numpy


def evi(b2, b4, b8):
    """
    Enhanced Vegetation Index (Huete et al., 2002).

    .. math:: EVI = 2.5 * (b8 - b4) / (b8 + 6 * b4 - 7.5 * b2 + 1)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns EVI: Index value

    .. Tip::

        Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., \
        Ferreira, L. G. 2002. Overview of the radiometric and biophysical \
        performance of the MODIS vegetation indices. Remote Sensing of \
        Environment 83(1-2), 195-213. doi:10.1016/S0034-4257(02)00096-2.

    """

    EVI = 2.5 * (b8 - b4) / (b8 + 6 * b4 - 7.5 * b2 + 1)
    return EVI


def ndvi(b4, b8):
    """
    Normalized Difference Vegetation Index (Rouse Jr et al., 1974).

    .. math:: NDVI = (b8 - b4)/(b8 + b4)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns NDVI: Index value

    .. Tip::

        Rouse, J. W., Haas, R. H., Schell, J. A., Deering, D. W. 1974. \
        Monitoring vegetation systems in the great plains with ERTS. \
        In: Proceedings of the Third Earth Resources Technology Satellite-1 \
        Symposium; NASA SP-351 (pp. 309-317).

    """

    NDVI = (b8 - b4)/(b8 + b4)
    return NDVI


def ndwi_gao(b8, b11):
    """
    Normalized Difference Water Index (Gao, 1996).

    .. math:: NDWI = (b8 - b11)/(b8 + b11)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NDWI: Index value

    .. Tip::

        Gao, B. 1996. NDWI - A normalized difference water index for remote \
        sensing of vegetation liquid water from space. Remote Sensing of \
        Environment 58(3), 257-266. doi:10.1016/s0034-4257(96)00067-3.

    """

    NDWI = (b8 - b11)/(b8 + b11)
    return NDWI


def ndwi_mcfeeters(b3, b8):
    """
    Normalized Difference Water Index (McFeeters, 1996).

    .. math:: NDWI = (b3 - b8)/(b3 + b8)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns NDWI: Index value

    .. Tip::

        McFeeters, S. K. 1996. The use of the Normalized Difference Water \
        Index (NDWI) in the delineation of open water features. International \
        Journal of Remote Sensing 17(7), 1425-1432. \
        doi:10.1080/01431169608948714.
    """
    NDWI = (b3 - b8)/(b3 + b8)
    return NDWI


def savi(b4, b8):
    """
    Soil-Adjusted Vegetation Index (Huete, 1988).

    .. math:: SAVI = ((b8 - b4))/((b8 + b4 + 0.5))*1.5

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns SAVI: Index value

    .. Tip::

       Huete, A. 1988. A soil-adjusted vegetation index (SAVI). \
       Remote Sensing of Environment 25(3), 295-309. \
       doi:10.1016/0034-4257(88)90106-x.
    """

    SAVI = ((b8 - b4))/((b8 + b4 + 0.5))*1.5
    return SAVI


def evi2(b2, b4, b8):
    """
    Enhanced Vegetation Index-2 (Jiang et al., 2008).

    .. math:: EVI2 = 2.5 * (b8 - b4) / (b8 + 6 * b4 + 2.4 * b2 + 1)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns EVI2: Index value

    .. Tip::

        Jiang, Z., Huete, A. R., Didan, K., Miura, T. 2008. \
        Development of a two-band enhanced vegetation index without \
        a blue band. Remote sensing of Environment 112(10), 3833-3845. \
        doi:10.1016/j.rse.2008.06.006.
    """

    EVI2 = 2.5 * (b8 - b4) / (b8 + 6 * b4 + 2.4 * b2 + 1)
    return EVI2


def gndvi(b3, b8):
    """
    Green Normalized Difference Vegetation Index \
    (Gitelson, Kaufman, and Merzlyak, 1996).

    .. math:: GNDVI = (b8 - b3) / (b8 + b3)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns GNDVI: Index value

    .. Tip::

        Gitelson, A., Kaufman, Y. J., Merzlyak, M. N. 1996. Use of a green \
        channel in remote sensing of global vegetation from EOS-MODIS. \
        Remote Sensing of Environment 58(3), 289-298. \
        doi:10.1016/s0034-4257(96)00072-7.
    """

    GNDVI = (b8 - b3) / (b8 + b3)
    return GNDVI


def msavi(b5, b8):
    """
    Modified Soil-Adjusted Vegetation Index (Qi et al., 1994).

    .. math:: MSAVI = (2 * b8 + 1 - sqrt((2 * b8 + 1)^2 - 8 * (b8 - b5))) / 2

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MSAVI: Index value

    .. Tip::

       Qi, J., Chehbouni, A., Huete, A. R., Kerr, Y. H., Sorooshian, S. \
       1994. A modified soil adjusted vegetation index. Remote Sensing \
       of Environment 48(2), 119-126. doi:10.1016/0034-4257(94)90134-1.
    """

    MSAVI = (2 * b8 + 1 - numpy.sqrt((2 * b8 + 1)**2 - 8 * (b8 - b5))) / 2
    return MSAVI


def osavi(b4, b8):
    """
    Optimized Soil-Adjusted Vegetation Index \
    (Rondeaux, Steven, and Baret, 1996).

    .. math:: OSAVI = 1.16 * b8 - (b4 / b8) + b4 + 0.16

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns OSAVI: Index value

    .. Tip::

        Rondeaux, G., Steven, M., Baret, F. 1996. \
        Optimization of soil-adjusted vegetation indices. \
        Remote Sensing of Environment 55, 95-107. \
        doi:10.1016/0034-4257(95)00186-7.
    """

    OSAVI = 1.16 * b8 - (b4 / b8) + b4 + 0.16
    return OSAVI


def afri_16(b8a, b11):
    """
    Aerosol Free Vegetation Index 1.6 \
    (Karnieli, Kaufman, Remer, and Wald, 2001).

    .. math:: AFRI_16 = b8a - 0.66 * (b11 / b8a) + 0.66 * b11

    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns AFRI_16: Index value

    .. Tip::

        Karnieli, A., Kaufman, Y. J., Remer, L., Wald, A. 2001. \
        AFRI - aerosol free vegetation index. Remote Sensing of Environment \
        77,10-21. doi:10.1016/S0034-4257(01)00190-0.
    """

    AFRI_16 = b8a - 0.66 * (b11 / b8a) + 0.66 * b11
    return AFRI_16


def ari(b3, b5):
    """
    Anthocyanin Reflectance Index (Gitelson, Chivkunova and Merzlyak, 2009).

    .. math:: ARI = (1/b3) - (1/b5)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns ARI: Index value

    .. Tip::

        Karnieli, A., Kaufman, Y. J., Remer, L., Wald, A. 2001. \
        AFRI - aerosol free vegetation index. Remote Sensing of Environment \
        77,10-21. doi:10.1016/S0034-4257(01)00190-0.
    """

    ARI = (1/b3) - (1/b5)
    return ARI


def avi(b4, b8a):
    """
    Ashburn Vegetation Index (Ashburn, 1978).

    .. math:: AVI = 2 * b8a - b4

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns AVI: Index value

    .. Tip::

        Ashburn, P. 1978. The vegetative index number and crop \
        identification. The LACIE Symposium Proceedings of the \
        Technical Session, 843-855.
    """

    AVI = 2 * b8a - b4
    return AVI


def bai(b4, b6, b7, b8a, b12):
    """
    Burned Area Index for Sentinel-2 (Filipponi, 2018).

    .. math:: top = (1 - sqrt((b6*b7*b8a) / b4))
    bottom = (((b12 - b8a) / sqrt(b12 + b8a)) + 1)
    BAI = top * bottom

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns BAI: Index value

    .. Tip::

        Filipponi, F. 2018. BAIS2: burned area index for Sentinel-2. \
        in: Multidisciplinary Digital Publishing Institute Proceedings \
        (Vol. 2, No. 7, p. 364). doi:10.3390/ecrs-2-05177.
    """
    top = (1 - numpy.sqrt((b6*b7*b8a) / b4))
    bottom = (((b12 - b8a) / numpy.sqrt(b12 + b8a)) + 1)
    BAI = top * bottom
    return BAI


def cigreen(b3, b8):
    """
    Chlorophyll Index Green (Gitelson et al., 2003a).

    .. math:: CIGREEN = (b8/b3) - 1

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns CIGREEN: Index value

    .. Tip::

        Gitelson, A. A., Gritz, Y., Merzlyak, M. N. 2003a. Relationships \
        between leaf chlorophyll content and spectral reflectance and \
        algorithms for non-destructive chlorophyll assessment in higher plant \
        leaves. Journal of Plant Physiology 160(3), 271-282. \
        doi:10.1078/0176-1617-00887.
    """

    CIGREEN = (b8/b3) - 1
    return CIGREEN


def cire(b5, b7):
    """
    Chlorophyll Index Red-edge (Gitelson et al., 2003a).

    .. math:: CIRE = (b7/b5) - 1

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns cire: Index value

    .. Tip::

        Gitelson, A. A., Gritz, Y., Merzlyak, M. N. 2003a. Relationships \
        between leaf chlorophyll content and spectral reflectance and \
        algorithms for non-destructive chlorophyll assessment in higher plant \
        leaves. Journal of Plant Physiology 160(3), 271-282. \
        doi:10.1078/0176-1617-00887.
    """

    CIRE = (b7/b5) - 1
    return CIRE


def cired_re(b4, b5, b8, a=0.7):
    """
    Red and Red-edge Modified Chlorophyll Index (Xie et al. 2018).

    .. math:: CIREDRE = (b8 / (a * b4 + (1 - a) * b5)) - 1

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param a: parameter.
    :type a: float

    :returns CIREDRE: Index value

    .. Tip::

        Xie, Q., Dash, J., Huang, W., Peng, D., Qin, Q., Mortimer, \
        H., ... Dong, Y. 2018. Vegetation indices combining the red \
        and red-edge spectral information for leaf area index retrieval. \
        IEEE Journal of Selected Topics in Applied Earth Observations \
        and Remote Sensing 11(5), 1482-1493. doi:10.1109/JSTARS.2018.2813281.
    """

    CIREDRE = (b8 / (a * b4 + (1 - a) * b5)) - 1
    return CIREDRE


def cri700(b2, b5):
    """
    Carotenoid Reflectance Index 700 (Gitelson, Merzlyak, and Chivkunova, \
    2001a).

    .. math:: CRI700 = (1/b2) - (1/b5)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns CRI700: Index value

    .. Tip::

        Gitelson, A., Merzlyak, M. N., Chivkunova, O. B. 2001a. \
        Optical properties and nondestructive estimation of anthocyanin \
        content in plant leaves. Photochemistry and Photobiology, 74,38-45. \
         doi:10.1562/0031-8655(2001)074<0038:opaneo>2.0.co;2.
    """

    CRI700 = (1/b2) - (1/b5)
    return CRI700


def cvi(b3, b4, b8):
    """
    Chlorophyll Vegetation Index (Hunt et al., 2011).

    .. math:: CVI = (b8/b3) * (b4/b3)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns CVI: Index value

    .. Tip::

        Hunt, E. R., Daughtry, C. S. T., Eitel, J. U. H., Long, D. S. 2011. \
        Remote sensing leaf chlorophyll content using a visible Band index. \
        Agronomy Journal 103, 1090-1099. doi:10.2134/agronj2010.0395.
    """

    CVI = (b8/b3) * (b4/b3)
    return CVI


def datt1(b4, b5, b8):
    """
    Vegetation Index proposed by Datt 1 (Datt, 1999a).

    .. math:: DATT1 = (b8 - b5) / (b8 - b4)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns DATT1: Index value

    .. Tip::
        Datt, B. 1999a. Remote sensing of water content in Eucalyptus leaves. \
        Australian Journal of Botany 47, 909-923. doi:10.1071/BT98042.
    """

    DATT1 = (b8 - b5) / (b8 - b4)
    return DATT1


def datt3(b3, b5, b8a):
    """
    Vegetation Index proposed by Datt 3 (Datt, 1998).

    .. math:: DATT3 = b8a / (b3 * b5)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns DATT3: Index value

    .. Tip::

       Datt, B. 1998. Remote sensing of chlorophyll a, chlorophyll b, \
       chlorophyll a + b, and total carotenoid content in eucalyptus leaves. \
       Remote Sensing of Environment, 66, 111-121. \
       doi:10.1016/S0034-4257(98)00046-7.
    """

    DATT3 = b8a / (b3 * b5)
    return DATT3


def dnvi(b1, b2):
    """
    Discriminant Normalized Vegetation Index (Manna and Raychawdhuri, 2018).

    .. math:: DNVI = (b1 - b2)^2 / sqrt(b1 + b2)

    :param b1: Coastal.
    :type b1: numpy.ndarray or float
    :param b2: Blue.
    :type b2: numpy.ndarray or float

    :returns DNVI: Index value

    .. Tip::

        Manna, S., Raychaudhuri, B. 2018. Mapping distribution of Sundarban \
        mangroves using Sentinel-2 data and new spectral metric for detecting \
        their health condition. Geocarto International 35(4), 434-452. \
        doi:10.1080/10106049.2018.1520923.
    """

    DNVI = (b1 - b2)**2 / numpy.sqrt(b1 + b2)
    return DNVI


def gari(b2, b3, b4, b8):
    """
    Green Atmospherically Resistant Vegetation Index \
    (Gitelson, Kaufman and Merzlyak, 1996).

    .. math:: GARI = b8 - (b3 - (b2 - b4)) / b8 + (b3 - (b2 - b4))

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns GARI: Index value

    .. Tip::

       Gitelson, A. A., Kaufman, Y. J., & Merzlyak, M. N. (1996). Use of a \
       green channel in remote sensing of global vegetation from EOS-MODIS. \
       Remote Sensing of Environment, 58(3), 289–298. \
       doi:10.1016/s0034-4257(96)00072-7 
    """

    GARI = b8 - (b3 - (b2 - b4)) / b8 + (b3 - (b2 - b4))
    return GARI


def gcvi(b3, b8):
    """
    Green Chlorophyll Vegetation Index (Gitelson et al., 2003b).

    .. math:: GCVI = (b8/b3) - 1

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns GCVI: Index value

    .. Tip::

        Gitelson, A. A., Viña, A., Arkebauer, T. J., Rundquist, D. C., \
        Keydan, G., Leavitt, B. 2003b. Remote estimation of leaf area \
        index and green leaf biomass in maize canopies. Geophysical \
        Research Letters 30(5). doi:10.1029/2002gl016450.
    """

    GCVI = (b8/b3) - 1
    return GCVI


def grvi(b3, b4):
    """
    Green-Red Vegetation Index (Tucker, 1979).

    .. math:: GRVI = (b3 - b4)/(b3 + b4)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float

    :returns GRVI: Index value

    .. Tip::

        Tucker, C.J. 1979. Red and photographic infrared linear combinations \
        for monitoring vegetation. Remote Sensing of Environment 8, 127-150. \
        doi:10.1016/0034-4257(79)90013-0.
    """

    GRVI = (b3 - b4)/(b3 + b4)
    return GRVI


def ireci(b4, b5, b6, b7):
    """
    Inverted Red-edge Chlorophyll Index (Frampton et al., 2013).

    .. math:: IRECI = (b7 - b4) / (b5 / b6)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns IRECI: Index value

    .. Tip::

        Frampton, W.J., Dash, J., Watmough, G., Milton, E.J. 2013. \
        Evaluating the capabilities of Sentinel-2 for quantitative \
        estimation of biophysical variables in vegetation. ISPRS Journal \
        of Photogrammetry and Remote Sensing 82, 83-92. \
        doi:10.1016/j.isprsjprs.2013.04.007.
    """

    IRECI = (b7 - b4) / (b5 / b6)
    return IRECI


def lanthoc(b3, b5, b7):
    """
    Leaf Anthocyanid Content (Wulf and Stuhler, 2015).

    .. math:: LAnthoC = b7/(b3 - b5)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns LAnthoC: Index value

    .. Tip::

        Wulf, H.; Stuhler, S. 2015. Sentinel-2: Land Cover, \
        Preliminary User Feedback on Sentinel-2A Data. \
        in: Proceedings of the Sentinel-2A Expert Users \
        Technical Meeting, Frascati, Italy, 29-30 September 2015.
    """

    LAnthoC = b7/(b3 - b5)
    return LAnthoC


def lcaroc(b2, b5, b7):
    """
    Leaf Carotenoid Content (Wulf and Stuhler, 2015).

    .. math:: LCaroC = b7/(b2 - b5)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns LCaroC: Index value

    .. Tip::

        Wulf, H.; Stuhler, S. 2015. Sentinel-2: Land Cover, \
        Preliminary User Feedback on Sentinel-2A Data. \
        in: Proceedings of the Sentinel-2A Expert Users \
        Technical Meeting, Frascati, Italy, 29-30 September 2015.
    """

    LCaroC = b7/(b2 - b5)
    return LCaroC


def lchloc(b5, b7):
    """
    Leaf Chlorophyll Content (Wulf and Stuhler, 2015).

    .. math:: LChloC = b7/b5

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns LChloC: Index value

    .. Tip::

        Wulf, H.; Stuhler, S. 2015. Sentinel-2: Land Cover, \
        Preliminary User Feedback on Sentinel-2A Data. \
        in: Proceedings of the Sentinel-2A Expert Users \
        Technical Meeting, Frascati, Italy, 29-30 September 2015.
    """

    LChloC = b7/b5
    return LChloC


def lswi(b8, b11):
    """
    Land Surface Water Index (Xiao et al., 2002).

    .. math:: LSWI = (b8 - b11)/(b8 + b11)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns LSWI: Index value

    .. Tip::

    """

    LSWI = (b8 - b11)/(b8 + b11)
    return LSWI


def maccioni(b4, b5, b7):
    """
    Vegetation Index proposed by Maccioni (Maccioni, Agati, and \
    Mazzinghi, 2001).

    .. math:: Maccioni = (b7 - b5)/(b7 - b4)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns Maccioni: Index value

    .. Tip::

        Maccioni, A., Agati, G., Mazzinghi, P. 2001. New vegetation indices \
        for remote measurement of chlorophylls based on leaf directional \
        reflectance spectra. Journal of Photochemistry and Photobiology \
        B: Biology 61(1-2), 52-61. doi:10.1016/S1011-1344(01)00145-2.
    """

    Maccioni = (b7 - b5)/(b7 - b4)
    return Maccioni


def mcari(b3, b4, b5):
    """
    Modified Chlorophyll Absorption in Reflectance Index \
    (Daughtry et al. 2000).

    .. math:: MCARI = ((b5 - b4) - 0.2 * (b5 - b3)) * (b5 / b4)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns MCARI: Index value

    .. Tip::

        Daughtry, C. S. T., Walthall, C. L., Kim, M. S., De Colstoun, E. B., \
        McMurtrey Iii, J. E. 2000. Estimating corn leaf chlorophyll \
        concentration from leaf and canopy reflectance. Remote Sensing of \
        Environment 74(2), 229-239. doi:10.1016/S0034-4257(00)00113-9.
    """
    MCARI = ((b5 - b4) - 0.2 * (b5 - b3)) * (b5 / b4)
    return MCARI


def mirbi(b11, b12):
    """
    Mid Infrared Burned Index (Trigg and Flasse, 2001).

    .. math:: MIRBI = 10 * b12 - 9.8 * b11 + 2

    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns MIRBI: Index value

    .. Tip::

        Trigg, S., Flasse, S. 2001. An evaluation of different bi-spectral \
        spaces for discriminating burned shrub-savannah. International \
        Journal of Remote Sensing 22(13), 2641-2647. \
        doi:10.1080/01431160110053185.
    """

    MIRBI = 10 * b12 - 9.8 * b11 + 2
    return MIRBI


def mndbi(b8, b12):
    """
    Modified Normalized Difference Built-up Index \
    (Shingare, Hemane, and Dandekar, 2014).

    .. math:: MNDBI = (b12 - b8)/(b12 + b8)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns MNDBI: Index value

    .. Tip::

        Shingare, P.P., Hemane, P.M., Dandekar, D.S., 2014. Fusion \
        classification of multispectral and panchromatic image using \
        improved decision tree algorithm. in: International Conference \
        on Signal Propagation and Computer Technology (ICSPCT) 2014, \
        pp. 598-603. doi:10.1109/ICSPCT.2014.6884944.
    """

    MNDBI = (b12 - b8)/(b12 + b8)
    return MNDBI


def mndvi(b2, b4, b8):
    """
    Modified Normalized Difference Vegetation Index \
    (Main et al., 2011).

    .. math:: MNDVI = (b8 - b4) / (b8 + b4 - 2 * b2)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MNDVI: Index value

    .. Tip::

       Main, R., Cho, M. A., Mathieu, R., O’kennedy, M. M., Ramoelo, A., \
        Koch, S. 2011. An investigation into robust spectral indices for \
        leaf chlorophyll estimation. ISPRS Journal of Photogrammetry and \
        Remote Sensing 66, 751-761. doi:10.1016/j.isprsjprs.2011.08.001.
    """

    MNDVI = (b8 - b4) / (b8 + b4 - 2 * b2)
    return MNDVI


def mndwi(b3, b11):
    """
    Modified Normalized Difference Water Index (Xu, 2006).

    .. math:: MNDWI = (b3 - b11) / (b3 + b11)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns MNDWI: Index value

    .. Tip::

        Xu, H. (2006). Modification of normalised difference water index \
        (NDWI) to enhance open water features in remotely sensed imagery. \
        International Journal of Remote Sensing 27(14), 3025-3033. \
        doi:10.1080/01431160600589179.
    """

    MNDWI = (b3 - b11) / (b3 + b11)
    return MNDWI


def mnsi(b3, b4, b6, b8):
    """
    Misra Non-such Index (Misra, Wheeler, and Oliver, 1977).

    .. math:: MNSI = 0.404 * b3 + 0.039 * b4 - 0.505 * b6 + 0.762 * b8

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MNSI: Index value

    .. Tip::

        Misra, P. N., Wheeler, S. G., Oliver, R. E. 1977. Kauth-Thomas \
        brightness and greenness axes. in: Contract NASA 9-14350, 23-46.
    """

    MNSI = 0.404 * b3 + 0.039 * b4 - 0.505 * b6 + 0.762 * b8
    return MNSI


def msi(b8a, b11):
    """
    Moisture Stress Index (Rock, Williams, and Vogelmann, 1985).

    .. math:: MSI = b11 / b8a

    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns MSI: Index value

    .. Tip::

        Rock, B.N., Williams, D.L., Vogelmann, J.E. 1985. Field and airborne \
        spectral characterization of suspected acid deposition damage in red \
        spruce (picea rubens) from vermont. in: Proceedings of the 11th \
        International Symposium—Machine Processing of Remotely Sensed Data, \
        West Lafayette, IN, USA, 25-27 June 1985; pp. 71-81.
    """

    MSI = b11 / b8a
    return MSI


def msr2(b4, b5, b8):
    """
    Modified Simple Ratio (Chen, 1996).

    .. math:: MSR = ((b8 / b4) - 1) / \\sqrt((b8 / b5) + 1)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MSR: Index value

    .. Tip::

        Chen, J. 1996. Evaluation of vegetation indices and modified simple \
        ratio for boreal applications. Canadian Jurnal of Remote Sensing 22, \
        229-242. doi:10.1080/07038992.1996.10855178.
    """

    MSR = ((b8 / b4) - 1) / numpy.sqrt((b8 / b5) + 1)
    return MSR


def msrredre(b4, b5, b8, a=0.4):
    """
    Red and Red-edge MSR Index (Xie et al. 2018).
    Usually, a is between 0 and 1

    .. math:: top = (b8 / (a * b4 + (1 - a) * b5)) - 1
    bottom = \\sqrt(b8 * (a * b4 + (1 - a) * b5) + 1)

    MSRREDRE = top / bottom

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MSRREDRE: Index value

    .. Tip::

        Xie, Q., Dash, J., Huang, W., Peng, D., Qin, Q., Mortimer, \
        H., ... Dong, Y. 2018. Vegetation indices combining the red \
        and red-edge spectral information for leaf area index retrieval. \
        IEEE Journal of Selected Topics in Applied Earth Observations \
        and Remote Sensing 11(5), 1482-1493. doi:10.1109/JSTARS.2018.2813281.
    """

    top = (b8 / (a * b4 + (1 - a) * b5)) - 1
    bottom = numpy.sqrt(b8 * (a * b4 + (1 - a) * b5) + 1)

    MSRREDRE = top / bottom
    return MSRREDRE


def msrre(b5, b8):
    """
    Modified Simple Ratio Red-edge (Wu et al., 2008).

    .. math:: top = (b8 / b5) - 1
    bottom = \\sqrt((b8 / b5) + 1)

    MSRRE = top / bottom

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns MSRRE: Index value

    .. Tip::

        Wu, C., Niu, Z., Tang, Q., Huang, W. 2008. Estimating chlorophyll \
        content from hyperspectral vegetation indices: Modeling and \
        validation. Agricultural and Forest Meteorology 148(8-9), 1230-1241. \
        doi:10.1016/j.agrformet.2008.03.005.
    """
    top = (b8 / b5) - 1
    bottom = numpy.sqrt( (b8 / b5) + 1)

    MSRRE = top / bottom
    return MSRRE


def MSRREn(b5, b8a):
    """
    Modified Simple Ratio Red-edge normalized (Wu et al., 2008).

    .. math:: top = (b8a / b5) - 1
    bottom = \\sqrt((b8a / b5) + 1)

    MSRREn = top / bottom

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns MSRREn: Index value

    .. Tip::

        Wu, C., Niu, Z., Tang, Q., Huang, W. 2008. Estimating chlorophyll \
        content from hyperspectral vegetation indices: Modeling and \
        validation. Agricultural and Forest Meteorology 148(8-9), 1230-1241. \
        doi:10.1016/j.agrformet.2008.03.005.
    """

    top = (b8a / b5) - 1
    bottom = numpy.sqrt((b8a / b5) + 1)

    MSRREn = top / bottom
    return MSRREn


def mtci(b4, b5, b6):
    """
    MERIS Terrestrial Chlorophyll Index (Dash and Curran, 2004).

    .. math:: MTCI = (b6 - b5)/(b5 + b4)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns MTCI: Index value

    .. Tip::

        Dash, J., Curran, P.J., 2004. The MERIS terrestrial chlorophyll \
        index. International Journal of Remote Sensing 25, 5403-5413. \
        doi:10.1080/0143116042000274015.
    """

    MTCI = (b6 - b5)/(b5 + b4)
    return MTCI


def nbr(b8, b12):
    """
    Normalized Burn Ratio \
    (García and Caselles, 1991. Named by Key and Benson, 1999).

    .. math:: NBR = (b8 - b12) / (b8 + b12)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NBR: Index value

    .. Tip::

        García, M. J. L., Caselles, V. 1991. Mapping burns and natural \
        reforestation using thematic Mapper data. Geocarto International \
        6(1), 31-37. doi:10.1080/10106049109354290.

        Key, C.H., Benson, N., 1999. The Normalized Burn Ratio (NBR): A \
        Landsat TM Radiometric Measure of Burn Severity. United States \
        Geological Survey, Northern Rocky Mountain Science Center.
    """

    NBR = (b8 - b12) / (b8 + b12)
    return NBR


def nbr2(b11, b12):
    """
    Normalized Burn Ratio-2 (García and Caselles, 1991).

    .. math:: NBR2 = (b11 - b12) / (b11 + b12)

    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NBR2: Index value

    .. Tip::

        García, M. J. L., Caselles, V. 1991. Mapping burns and natural \
        reforestation using thematic Mapper data. Geocarto International \
        6(1), 31-37. doi:10.1080/10106049109354290.
    """

    NBR2 = (b11 - b12) / (b11 + b12)
    return NBR2


def nbai(b6, b11):
    """
    Normalized Difference Bareness Index (Zhao and Chen, 2005).

    .. math:: NDBaI = (b6 - b11) / (b6 + b11)

    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NDBaI: Index value

    .. Tip::

        Zhao, H., Chen, X., 2005. Use of normalized difference bareness \
        index in quickly mapping bare areas from TM/ETM+. in: Proceedings \
        of the 2005 IEEE International Geoscience and Remote Sensing \
        Symposium 3, pp. 1666. doi:10.1109/IGARSS.2005.1526319.
    """

    NDBaI = (b6 - b11) / (b6 + b11)
    return NDBaI


def ndbi(b8, b11):
    """
    Normalized Difference Built-up Index (Zha, Gao, and Ni, 2003).

    .. math:: NDBI = (b11 - b8) / (b11 + b8)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NDBI: Index value

    .. Tip::

        Zha, Y.; Gao, J.; Ni, S. 2003. Use of normalized difference \
        built-up index in automatically mapping urban areas from TM \
        imagery. International Journal of Remote Sensing 24, 583-594. \
        doi:10.1080/01431160304987.
    """

    NDBI = (b11 - b8) / (b11 + b8)
    return NDBI


def ndii(b8, b11):
    """
    Normalized Difference Infrared Index \
    (Hardisky, Klemas and Smart, 1983).

    .. math:: NDII = (b8 - b11) / (b8 + b11)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NDII: Index value

    .. Tip::

        Hardisky, M.A., Klemas, V. and Smart, R.M. 1983. \
        The Influence of Soil Salinity, Growth Form, and \
        Leaf Moisture on the Spectral Radiance of Spartina \
        alterniflora Canopies. Photogrammetric Engineering \
        and Remote Sensing 49, 77-83.
    """

    NDII = (b8 - b11) / (b8 + b11)
    return NDII


def ndmi(b8, b11):
    """
    Normalized Difference Moisture Index \
    (Gerard et al., 2003).

    .. math:: NDMI = (b8 - b11) / (b8 + b11)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NDMI: Index value

    .. Tip::

        Gerard, F., Plummer, S., Wadsworth, R., Sanfeliu, \
        A. F., Iliffe, L., Balzter, H., & Wyatt, B. 2003. \
        Forest fire scar detection in the boreal forest with \
        multitemporal SPOT-VEGETATION data. IEEE Transactions \
        on Geoscience and Remote Sensing 41(11), 2575-2585. \
        doi:10.1109/tgrs.2003.819190.
    """

    NDMI = (b8 - b11) / (b8 + b11)
    return NDMI


def ndre1(b5, b6):
    """
    Normalized Difference Red-edge 1 \
    (Gitelson and Merzlyak, 1994).

    .. math:: NDRE1 = (b6 - b5)/(b6 + b5)

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns NDRE1: Index value

    .. Tip::

       Gitelson, A., Merzlyak, M. N. 1994. Spectral reflectance changes \
       associated with autumn senescence of Aesculus hippocastanum L. and \
       Acer platanoides L. leaves. Spectral features and relation to \
       chlorophyll estimation. Journal of Plant Physiology 143(3), 286-292. \
       doi:10.1016/S0176-1617(11)81633-0.
    """

    NDRE1 = (b6 - b5)/(b6 + b5)
    return NDRE1


def ndre2(b5, b7):
    """
    Normalized Difference Red-edge 2 (Barnes et al., 2000).

    .. math:: NDRE2 = (b7 - b5)/(b7 + b5)

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns NDRE2: Index value

    .. Tip::

       Barnes, E., Clarke, T., Richards, S., Colaizzi, P., Haberland, J., \
       Kostrzewski, M., et al. (2000). Coincident detection of crop water \
       stress, nitrogen status and canopy density using ground based \
       multispectral data. in: P. C. Robert, R. H. Rust, & W. E. Larson \
       (Eds.), Proceedings of the 5th International Conference on Precision \
       Agriculture, 16-19 July 2000. Bloomington, USA.
    """

    NDRE2 = (b7 - b5)/(b7 + b5)
    return NDRE2


def ndredgeswir(b6, b12):
    """
    Normalized Difference Red-edge and SWIR2 (Radoux et al., 2016).

    .. math:: NDREDGESWIR = (b6 - b12)/(b6 + b12)

    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NDREDGESWIR: Index value

    .. Tip::

       Radoux, J., Chomé, G., Jacques, D. C., Waldner, F., Bellemans, \
       N., Matton, N., ... Defourny, P. 2016. Sentinel-2’s potential for \
       sub-pixel landscape feature detection. Remote Sensing 8(6), 488. \
       doi:10.3390/rs8060488.
    """

    NDREDGESWIR = (b6 - b12)/(b6 + b12)
    return NDREDGESWIR


def ndre1m(b1, b5, b6):
    """
    Normalized Difference Red-edge 1 modified (Sims and Gamon, 2002).

    .. math:: NDRE1M = (b6 - b5)vi700 / (b6 + b5 - 2 * b1)

    :param b1: Coastal.
    :type b1: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns NDRE1M: Index value

    .. Tip::

       Sims, D.A., Gamon, J.A., 2002. Relationships between leaf pigment \
       content and spectral reflectance across a wide range of species, \
       leaf structures and developmental stages. Remote Sensing of \
       Environment 81, 337-354. doi:10.1016/S0034-4257(02)00010-X.
    """

    NDRE1M = (b6 - b5) / (b6 + b5 - 2 * b1)
    return NDRE1M


def ndre2m(b1, b5, b7):
    """
    Normalized Difference Red-edge 2 modified (Sims and Gamon, 2002).

    .. math:: NDRE2M = (b7 - b5) / (b7 + b5 - 2 * b1)

    :param b1: Coastal.
    :type b1: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns NDRE2M: Index value

    .. Tip::

       Sims, D.A., Gamon, J.A., 2002. Relationships between leaf pigment \
       content and spectral reflectance across a wide range of species, \
       leaf structures and developmental stages. Remote Sensing of \
       Environment 81, 337-354. doi:10.1016/S0034-4257(02)00010-X.
    """

    NDRE2M = (b7 - b5) / (b7 + b5 - 2 * b1)
    return NDRE2M


def ndswir(b8, b12):
    """
    Normalized Difference SWIR (Gerard et al., 2003).

    .. math:: NDSWIR = (b8 - b12) / (b8 + b12)

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NDSWIR: Index value

    .. Tip::

       Gerard, F., Plummer, S., Wadsworth, R., Sanfeliu, A. F., Iliffe, \
       L., Balzter, H., & Wyatt, B. 2003. Forest fire scar detection in \
       the boreal forest with multitemporal SPOT-VEGETATION data. IEEE \
       Transactions on Geoscience and Remote Sensing 41(11), 2575-2585. \
       doi:10.1109/tgrs.2003.819190.
    """

    NDSWIR = (b8 - b12) / (b8 + b12)
    return NDSWIR


def ndti(b11, b12):
    """
    Normalized Difference Tillage Index (Van Deventer et al., 1997).

    .. math:: NDTI = (b11 - b12) / (b11 + b12)

    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NDTI: Index value

    .. Tip::

       Van Deventer, A. P., Ward, A. D., Gowda, P. H., Lyon, J. G. 1997. \
       Using thematic mapper data to identify contrasting soil plains and \
       tillage practices. Photogrammetric Engineering and Remote Sensing \
       63, 87-93.
    """

    NDTI = (b11 - b12) / (b11 + b12)
    return MDTI


def ndvire(b5, b8):
    """
    Normalized Difference Vegetation Index Red-edge \
    (Gitelson and Merzlyak, 1994).

    .. math:: NDVIRE = (b8 - b5) / (b8 + b5)

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns NDVIRE: Index value

    .. Tip::

       Gitelson, A., Merzlyak, M. N. 1994. Spectral reflectance changes \
       associated with autumn senescence of Aesculus hippocastanum L. and \
       Acer platanoides L. leaves. Spectral features and relation to \
       chlorophyll estimation. Journal of Plant Physiology 143(3), 286-292. \
       doi:10.1016/S0176-1617(11)81633-0.
    """

    NDVIRE = (b8 - b5) / (b8 + b5)
    return NDVIRE


def ndvire1n(b5, b8a):
    """
    Normalized Difference Vegetation Index red-edge 1 narrow \
    (Fernández-Manso, Fernández-Manso and Quintano, 2016).

    .. math:: NDVIRE1n = (b8a - b5) / (b8a + b5)

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns NDVIRE1n: Index value

    .. Tip::

       Fernández-Manso, A., Fernández-Manso, O., Quintano, C. 2016. \
       SENTINEL-2A red-edge spectral indices suitability for discriminating \
       burn severity. International Journal Of Applied Earth Observation and \
       Geoinformation 50, 170-175. doi:10.1016/j.jag.2016.03.005.
    """

    NDVIRE1n = (b8a - b5) / (b8a + b5)
    return NDVIRE1n


def ndvire2(b6, b8):
    """
    Normalized Difference Vegetation Index red-edge 2 narrow \
    (Fernández-Manso, Fernández-Manso and Quintano, 2016).

    .. math:: NDVIRE2 = (b8 - b6) / (b8 + b6)

    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns NDVIRE2: Index value

    .. Tip::

       Fernández-Manso, A., Fernández-Manso, O., Quintano, C. 2016. \
       SENTINEL-2A red-edge spectral indices suitability for discriminating \
       burn severity. International Journal Of Applied Earth Observation and \
       Geoinformation 50, 170-175. doi:10.1016/j.jag.2016.03.005.
    """

    NDVIRE2 = (b8 - b6) / (b8 + b6)
    return NDVIRE2


def ndvire2n(b6, b8a):
    """
    Normalized Difference Vegetation Index Red-edge 2 narrow \
    (Fernández-Manso, Fernández-Manso and Quintano, 2016).

    .. math:: NDVIRE2n = (b8a - b6) / (b8a + b6)

    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns NDVIRE2n: Index value

    .. Tip::

       Fernández-Manso, A., Fernández-Manso, O., Quintano, C. 2016. \
       SENTINEL-2A red-edge spectral indices suitability for discriminating \
       burn severity. International Journal Of Applied Earth Observation and \
       Geoinformation 50, 170-175. doi:10.1016/j.jag.2016.03.005.
    """
    #
    NDVIRE2n = (b8a - b6) / (b8a + b6)
    return NDVIRE2n


def ndvire3(b7, b8):
    """
    Normalized Difference Vegetation Index Red-edge 3 \
    (Gitelson and Merzlyak, 1994).

    .. math:: NDVIRE3 = (b8 - b7) / (b8 + b7)

    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns NDVIRE3: Index value

    .. Tip::

       Gitelson, A., Merzlyak, M. N. 1994. Spectral reflectance changes \
       associated with autumn senescence of Aesculus hippocastanum L. and \
       Acer platanoides L. leaves. Spectral features and relation to \
       chlorophyll estimation. Journal of Plant Physiology 143(3), 286-292. \
       doi:10.1016/S0176-1617(11)81633-0.
    """

    NDVIRE3 = (b8 - b7) / (b8 + b7)
    return NDVIRE3


def ndvire3n(b7, b8a):
    """
    Normalized Difference Vegetation Index Red-edge 3 narrow \
    (Fernández-Manso, Fernández-Manso and Quintano, 2016).

    .. math:: NDVIRE3n = (b8a - b7)/(b8a + b7)

    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns NDVIRE3n: Index value

    .. Tip::

       Fernández-Manso, A., Fernández-Manso, O., Quintano, C. 2016. \
       SENTINEL-2A red-edge spectral indices suitability for discriminating \
       burn severity. International Journal Of Applied Earth Observation and \
       Geoinformation 50, 170-175. doi:10.1016/j.jag.2016.03.005.
    """

    NDVIRE3n = (b8a - b7)/(b8a + b7)
    return NDVIRE3n


def ndvi705(b5, b6):
    """
    Red-edge Normalized Difference Vegetation Index \
    (Gitelson and Merzlyak, 1994).

    .. math:: NDVI705 = (b6 - b5)/(b6 + b5)

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns NDVI705: Index value

    .. Tip::

       Gitelson, A., Merzlyak, M. N. 1994. Spectral reflectance changes \
       associated with autumn senescence of Aesculus hippocastanum L. and \
       Acer platanoides L. leaves. Spectral features and relation to \
       chlorophyll estimation. Journal of Plant Physiology 143(3), 286-292. \
       doi:10.1016/S0176-1617(11)81633-0.
    """

    NDVI705 = (b6 - b5)/(b6 + b5)
    return NDVI705


def ngrdi(b3, b5):
    """
    Normalized Green Red Difference Index (Zarco-Tejada et al., 2001).

    .. math:: NGRDI = (b3 - b5)/(b3 + b5)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns NGRDI: Index value

    .. Tip::

       Zarco-Tejada, P. J., Miller, J. R., Noland, T. L., Mohammed, \
       G. H., Sampson, P. H. 2001. Scaling-up and model inversion methods \
       with narrowband optical indices for chlorophyll content estimation in \
       closed forest canopies with hyperspectral data. IEEE Transactions on \
       Geoscience and Remote Sensing 39, 1491-1507. doi:10.1109/36.934080.
    """

    NGRDI = (b3 - b5)/(b3 + b5)
    return NGRDI


def nhi(b3, b11):
    """
    Normalized Humidity Index (Lacaux et al., 2007).

    .. math:: NHI = (b11 - b3)/(b11 + b3)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns NHI: Index value

    .. Tip::

       Zarco-Tejada, P. J., Miller, J. R., Noland, T. L., Mohammed, \
       G. H., Sampson, P. H. 2001. Scaling-up and model inversion methods \
       with narrowband optical indices for chlorophyll content estimation in \
       closed forest canopies with hyperspectral data. IEEE Transactions on \
       Geoscience and Remote Sensing 39, 1491-1507. doi:10.1109/36.934080.
    """

    NHI = (b11 - b3)/(b11 + b3)
    return NHI


def nmdi(b8, b11, b12):
    """
    Normalized Multi-band Drought Index (Wang and Qu, 2007).

    .. math:: NMDI = (b8 - (b11 - b12)) / (b8 + (b11 - b12))

    :param b8: NIR.
    :type b8: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns NMDI: Index value

    .. Tip::

       Wang, L., Qu, J. J. 2007. NMDI: A normalized multi‐band drought index \
       for monitoring soil and vegetation moisture with satellite remote \
       sensing. Geophysical Research Letters 34(20). doi:10.1029/2007GL031021.
    """

    NMDI = (b8 - (b11 - b12)) / (b8 + (b11 - b12))
    return NMDI


def ppr(b2, b3):
    """
    Plant Pigment Ratio (Metternicht, 2003).

    .. math:: PPR = (b3 - b2)/(b3 + b2)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b3: Green.
    :type b3: numpy.ndarray or float

    :returns PPR: Index value

    .. Tip::

       Metternicht, G. 2003. Vegetation indices derived from high-resolution \
       airborne videography for precision crop management. International \
       Journal of Remote Sensing 24(14), 2855-2877. \
       doi:10.1080/01431160210163074
    """

    PPR = (b3 - b2)/(b3 + b2)
    return PPR


def psri(b3, b4, b6):
    """
    Plant Senescence Reflectance Index (Merzlyak et al., 1999).

    .. math:: PSRI = (b4 - b3)/b6

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns PSRI: Index value

    .. Tip::

       Merzlyak, M.N.; Gitelson, A.A.; Chivkunova, O.B.; Rakitin, V.Y. 1999. \
       Non-destructive optical detection of pigment changes during leaf \
       senescence and fruit ripening. Physiologia Plantarum 106, 135-141. \
       doi:10.1034/j.1399-3054.1999.106119.x.
    """

    PSRI = (b4 - b3)/b6
    return PSRI


def pvr(b3, b4):
    """
    Photosyntetic Vigour Ratio (Metternicht, 2003).

    .. math:: PVR = (b3 - b4)/(b3 + b4)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float

    :returns PVR: Index value

    .. Tip::

       Metternicht, G. 2003. Vegetation indices derived from high-resolution \
       airborne videography for precision crop management. International \
       Journal of Remote Sensing 24(14), 2855-2877. \
       doi:10.1080/01431160210163074
    """

    PVR = (b3 - b4)/(b3 + b4)
    return PVR


def rbndvi(b2, b4, b8):
    """
    Red-Blue NDVI (Wang et al., 2007).

    .. math:: RBNDVI = (b8 - (b4 + b2))/(b8 + (b4 + b2))

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns RBNDVI: Index value

    .. Tip::

       Wang, F. M., Huang, J. F., Tang, Y. L., Wang, X. Z. 2007. New \
       vegetation index and its application in estimating leaf area index \
       of rice. Rice Science 14(3), 195-203. \
       doi:10.1016/S1672-6308(07)60027-4.
    """

    RBNDVI = (b8 - (b4 + b2))/(b8 + (b4 + b2))
    return RBNDVI


def redswir1(b4, b11):
    """
    Red and SWIR bands difference (Jacques et al., 2014).

    .. math:: RedSWIR1 = b4 - b11

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns RedSWIR1: Index value

    .. Tip::

       Jacques D.C. et al., 2014. Monitoring dry vegetation masses in \
       semi-arid areas with MODIS SWIR bands. Remote Sensing of Environment \
       153, 40-49. doi:10.1016/j.rse.2014.07.027.
    """

    RedSWIR1 = b4 - b11
    return RedSWIR1


def reip(b4, b5, b6, b7):
    """
    Red-edge Inflection Point (Herrmann et al. 2011).

    .. math:: REIP = 700 + 40 * ((((b4 + b7) / 2) - b5) / (b6 - b5))

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns REIP: Index value

    .. Tip::

       Herrmann, I., Pimstein, A., Karnieli, A., Cohen, Y., Alchanatis, V., \
       Bonfil, D. J. 2011. LAI assessment of wheat and potato crops by VENμS \
       and Sentinel-2 bands. Remote Sensing of Environment 115, 2141-2151. \
       doi:10.1016/j.rse.2011.04.018.
    """

    REIP = 700 + 40 * ((((b4 + b7) / 2) - b5) / (b6 - b5))
    return REIP


def rervi(b5, b8):
    """
    Red-edge Ratio Vegetation Index (Cao et al., 2013).

    .. math:: RERVI = b8/b5

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns RERVI: Index value

    .. Tip::

       Cao, Q.; Miao, Y.; Wang, H.; Huang, S.; Cheng, S.; Khosla, R.; \
       Jiang, R. 2013. Non-destructive estimation of rice plant nitrogen \
       status with Crop Circle multispectral active canopy sensor. Field \
       Crops Research 154, 133-144. doi:10.1016/j.fcr.2013.08.005.
    """

    RERVI = b8/b5
    return RERVI


def REPA(b4, b5, b6, b7, b8a):
    """
    Red-edge Peak Area (Radoux et al. 2016).

    .. math:: REPA = b4 + b5 + b6 + b7 + b8a

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns REPA: Index value

    .. Tip::

       Radoux, J., Chomé, G., Jacques, D. C., Waldner, F., Bellemans, \
       N., Matton, N., ... Defourny, P. 2016. Sentinel-2’s potential for \
       sub-pixel landscape feature detection. Remote Sensing 8(6), 488. \
       doi:10.3390/rs8060488.
    """

    REPA = b4 + b5 + b6 + b7 + b8a
    return REPA


def rtvicore(b3, b5, b8):
    """
    Red-edge Triangular Vegetation Index (Chen et al., 2010).

    .. math:: RTVIcore = 100 * (b8 - b5) - 10 * (b8 - b3)

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns RTVIcore: Index value

    .. Tip::

       Chen, P. F., Nicolas, T., Wang, J. H., Philippe, V., Huang, W. J., Li, \
       B. G. 2010. New index for crop canopy fresh biomass estimation. \
       Spectroscopy and Spectral Analysis 30(2), 512-517. \
       10.3964/j.issn.1000-0593(2010)02-0512-06.
    """

    RTVIcore = 100 * (b8 - b5) - 10 * (b8 - b3)
    return RTVIcore


def savirre(b4, b5, b8, a=0.4, L=0.5):
    """
    Soil-Adjusted Vegetation Index with red and red-edge \
    (Vincent, Kumar, and Upadhyay, 2020).

    .. math:: top = (1 + L) * (b8 - (a * b4 + (1 - a) * b5))
    bottom = b5 + L + (a * b4 + (1 - a) * b5)

    SAVIRRE = top / bottom

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns SAVIRRE: Index value

    .. Tip::
        L is a variable. Its values range within -1 to 1, depending on the \
        amount of green vegetation present in the area. To run the remote \
        sensing analysis of areas with high green vegetation, L is set to \
        zero (in which case SAVI index data will be equal to NDVI); whereas \
        low green vegetation regions require L=1.
        The value of L varies by the amount or cover of green vegetation: in \
        very high vegetation regions, L=0; and in areas with no green \
        vegetation, L=1. Generally, an L=0.5 works well in most situations \
        and is the default value used.

    .. Tip::

       Vincent, A., Kumar, A., Upadhyay, P. 2020. Effect of Red-Edge \
       Region in Fuzzy Classification: A Case Study of Sunflower Crop. \
       Journal of the Indian Society of Remote Sensing 1-13. \
       doi:10.1007/s12524-020-01109-4.

    """

    top = (1 + L) * (b8 - (a * b4 + (1 - a) * b5))
    bottom = b5 + L + (a * b4 + (1 - a) * b5)

    SAVIRRE = top / bottom
    return SAVIRRE


def sipi(b3, b4, b8):
    """
    Structure Intensive Pigment Index \
    (Peñuelas, Baret and Filella, 1995).

    .. math:: SIPI = b3/b8 - b4

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns SIPI: Index value

    .. Tip::

       Peñuelas, J., Baret, F., Filella, I. 1995. Semi-empirical \
       indices to assess carotenoids/chlorophyll-a ratio from leaf \
       spectral reflectance. Photosynthetica 31, 221-230.
    """

    SIPI = b3/b8 - b4
    return SIPI


def siwsi(b8a, b11):
    """
    Shortwave Infrared Water Stress Index \
    (Fensholt and Sandholt, 2003).

    .. math:: SIWSI = (b8a - b11)/(b8a + b11)

    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns SIWSI: Index value

    .. Tip::

       Fensholt, R., Sandholt, I. 2003. Derivation of a shortwave \
       infrared water stress index from MODIS near- and shortwave \
       infrared data in a semiarid environment. Remote Sensing of \
       Environment 87, 111-121. doi:10.1016/j.rse.2003.07.002.
    """

    SIWSI = (b8a - b11)/(b8a + b11)
    return SIWSI


def sri(b4, b8):
    """
    Simple Ratio Index (Jordan, 1969).

    .. math:: SRI = b8/b4

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8: NIR.
    :type b8: numpy.ndarray or float

    :returns SRI: Index value

    .. Tip::

       Jordan, C.F. 1969. Derivation of leaf-area index from quality \
       of light on the forest floor. Ecology 50, 663-666. \
       doi:10.2307/1936256.
    """

    SRI = b8/b4
    return SRI


def srnirnarrowgreen(b3, b8a):
    """
    Simple Ratio NIR narrow and Green \
    (le Maire, François, and Dufrêne, 2004).

    .. math:: SRNIRnarrowGreen = b8a/b3

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns SRNIRnarrowGreen: Index value

    .. Tip::

       le Maire, G.; François, C.; Dufrêne, E. 2004. Towards universal \
       broad leaf chlorophyll indices using PROSPECT simulated database \
       and hyperspectral reflectance measurements. Remote Sensing of \
       Environment 89, 1-28. doi:10.1016/j.rse.2003.09.004.
    """

    SRNIRnarrowGreen = b8a/b3
    return SRNIRnarrowGreen


def snrirnarrowred(b4, b8a):
    """
    Simple Ratio NIR narrow and Red (Blackburn, 1998).

    .. math:: SRNIRnarrowRed = b8a/b4

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns SRNIRnarrowRed: Index value

    .. Tip::

       Blackburn, G.A. 1998. Quantifying chlorophylls and caroteniods \
       at leaf and canopy scales. Remote Sensing of Environment 66, 273-285. \
       doi:10.1016/S0034-4257(98)00059-5.
    """

    SRNIRnarrowRed = b8a/b4
    return SRNIRnarrowRed


def srnirnarrowre1(b5, b8a):
    """
    Simple NIR and Red-edge 1 Ratio (Datt, 1999b).

    .. math:: SRNIRnarrowRE1 = b8a/b5

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns SRNIRnarrowRE1: Index value

    .. Tip::

       Datt, B. 1999b. Visible/near infrared reflectance and chlorophyll \
       content in Eucalyptus leaves. International Journal of Remote Sensing \
       20, 2741-2759. doi:10.1080/014311699211778.
    """

    SRNIRnarrowRE1 = b8a/b5
    return SRNIRnarrowRE1


def srnirnarrowre2(b6, b8a):
    """
    Simple NIR and Red-edge 2 Ratio (Datt, 1999b).

    .. math:: SRNIRnarrowRE2 = b8a/b6

    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns SRNIRnarrowRE2: Index value

    .. Tip::

       Datt, B. 1999b. Visible/near infrared reflectance and chlorophyll \
       content in Eucalyptus leaves. International Journal of Remote Sensing \
       20, 2741-2759. doi:10.1080/014311699211778.
    """

    SRNIRnarrowRE2 = b8a/b6
    return SRNIRnarrowRE2


def srnirnarrowre3(b7, b8a):
    """
    Simple NIR and Red-edge 3 Ratio (Datt, 1999b).

    .. math:: SRNIRnarrowRE3 = b8a/b7

    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float
    :param b8a: NIR narrow.
    :type b8a: numpy.ndarray or float

    :returns SRNIRnarrowRE3: Index value

    .. Tip::

       Datt, B. 1999b. Visible/near infrared reflectance and chlorophyll \
       content in Eucalyptus leaves. International Journal of Remote Sensing \
       20, 2741-2759. doi:10.1080/014311699211778.
    """

    SRNIRnarrowRE3 = b8a/b7
    return SRNIRnarrowRE3


def srre1(b1, b5, b6):
    """
    Surface Reflectance Red-edge 1 (Sims and Gamon, 2002).

    .. math:: SRRE1 = (b6 - b1)/(b5 - b1)

    :param b1: Coastal.
    :type b1: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns SRRE1: Index value

    .. Tip::

       Sims, D.A., Gamon, J.A., 2002. Relationships between leaf pigment \
       content and spectral reflectance across a wide range of species, \
       leaf structures and developmental stages. Remote Sensing of \
       Environment 81, 337-354. doi:10.1016/S0034-4257(02)00010-X.
    """

    SRRE1 = (b6 - b1)/(b5 - b1)
    return SRRE1


def srre2(b1, b5, b7):
    """
    Surface Reflectance Red-edge 2 (Sims and Gamon, 2002).

    .. math:: SRRE2 = (b7 - b1)/(b5 - b1)

    :param b1: Coastal.
    :type b1: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns SRRE2: Index value

    .. Tip::

       Sims, D.A., Gamon, J.A., 2002. Relationships between leaf pigment \
       content and spectral reflectance across a wide range of species, \
       leaf structures and developmental stages. Remote Sensing of \
       Environment 81, 337-354. doi:10.1016/S0034-4257(02)00010-X.
    """

    SRRE2 = (b7 - b1)/(b5 - b1)
    return SRRE2


def sti(b11, b12):
    """
    Soil Tillage Index (Van Deventer, 1997).

    .. math:: STI = b11/b12

    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float
    :param b12: SWIR 2.
    :type b12: numpy.ndarray or float

    :returns STI: Index value

    .. Tip::

       Van Deventer, A. P., Ward, A. D., Gowda, P. H., Lyon, J. G. 1997. \
       Using thematic mapper data to identify contrasting soil plains and \
       tillage practices. Photogrammetric Engineering and Remote Sensing \
       63, 87-93.
    """

    STI = b11/b12
    return STI


def s2rep(b4, b5, b6, b7):
    """
    Sentinel-2 Red-edge Position (Frampton et al., 2013).

    .. math:: S2REP = 700 + 35*((((b7 - b4/2) - b5)/b6-b5))

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns S2REP: Index value

    .. Tip::

        Frampton, W.J., Dash, J., Watmough, G., Milton, E.J. 2013. \
        Evaluating the capabilities of Sentinel-2 for quantitative \
        estimation of biophysical variables in vegetation. ISPRS Journal \
        of Photogrammetry and Remote Sensing 82, 83-92. \
        doi:10.1016/j.isprsjprs.2013.04.007.
    """

    S2REP = 700 + 35*((((b7 - b4/2) - b5)/b6-b5))
    return S2REP


def tcari(b3, b4, b5):
    """
    Transformed Chlorophyll Absorption in \
    Reflectance Index (Daughtry et al., 2000).

    .. math:: TCARI = 3 * ((b5 - b4) - 0.2 * (b5 - b3) * (b5/4))

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns TCARI: Index value

    .. Tip::

        Daughtry, C. S. T., Walthall, C. L., Kim, M. S., De Colstoun, E. B., \
        McMurtrey Iii, J. E. 2000. Estimating corn leaf chlorophyll \
        concentration from leaf and canopy reflectance. Remote Sensing of \
        Environment 74(2), 229-239. doi:10.1016/S0034-4257(00)00113-9.
    """

    TCARI = 3 * ((b5 - b4) - 0.2 * (b5 - b3) * (b5/4))
    return TCARI


def tvi(b3, b4, b6):
    """
    Transformed Vegetation Index (Broge and Leblanc, 2001).

    .. math:: TVI = 0.5 * (120 * (b6 - b3) - 200 * (b4 - b3))

    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b6: Red-edge 2.
    :type b6: numpy.ndarray or float

    :returns TVI: Index value

    .. Tip::

        Broge, N.H., Leblanc, E., 2001. Comparing prediction power and \
        stability ofbroadband and hyperspectral vegetation indices for \
        estimation of green leaf area index and canopy chlorophyll density. \
        Remote Sensing of Environment 76, 156-172. \
        doi:10.1016/S0034-4257(00)00197-8.
    """

    TVI = 0.5 * (120 * (b6 - b3) - 200 * (b4 - b3))
    return TVI


def varigreen(b2, b3, b4):
    """
    Visible Atmospherically Resistant Index Green \
    (Gitelson et al. 2001a).

    .. math:: VARIGREEN = (b3 - b4)/(b3 + b4 - b2)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b3: Green.
    :type b3: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float

    :returns VARIGREEN: Index value

    .. Tip::

        Gitelson, A., Merzlyak, M. N., Chivkunova, O. B. 2001a. \
        Optical properties and nondestructive estimation of anthocyanin \
        content in plant leaves. Photochemistry and Photobiology, 74,38-45. \
        doi:10.1562/0031-8655(2001)074<0038:opaneo>2.0.co;2.
    """

    VARIGREEN = (b3 - b4)/(b3 + b4 - b2)
    return VARIGREEN


def vi700(b4, b5):
    """
    Vegetation Index 700 (Gitelson et al., 2002).

    .. math:: VI700 = (b5 - b4)/(b5 + b4)

    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float

    :returns VI700: Index value

    .. Tip::

        Gitelson, A. A., Kaufman, Y. J., Stark, R., Rundquist, D. 2002. \
        Novel algorithms for remote estimation of vegetation fraction. \
        Remote sensing of Environment 80(1), 76-87. \
        doi:10.1016/S0034-4257(01)00289-9.
    """

    VI700 = (b5 - b4)/(b5 + b4)
    return VI700


def vsdi(b2, b4, b11):
    """
    Visible and Shortwave Infrared Drought Index \
    (Zhang et al., 2013).

    .. math:: VSDI = 1 - ((b11 - b2) + (b4 - b2))

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float
    :param b11: SWIR 1.
    :type b11: numpy.ndarray or float

    :returns VSDI: Index value

    .. Tip::

        Zhang, N., Hong, Y., Qin, Q., Liu, L. 2013. VSDI: a visible and \
        shortwave infrared drought index for monitoring soil and vegetation \
        moisture based on optical remote sensing. International Journal of \
        Remote Sensing 34(13), 4585-4609. doi:10.1080/01431161.2013.779046.
    """

    VSDI = 1 - ((b11 - b2) + (b4 - b2))
    return VSDI


def wbi(b2, b4):
    """
    Water Body Index (Domenech and Mallet, 2014).

    .. math:: WBI = (b2 - b4) / (b2 + b4)

    :param b2: Blue.
    :type b2: numpy.ndarray or float
    :param b4: Red.
    :type b4: numpy.ndarray or float

    :returns WBI: Index value

    .. Tip::

        Domenech, E., Mallet, C. 2014. Change Detection in High \
        resolution land use/land cover geodatabases (at object level). \
        EuroSDR official publication, 64.
    """

    WBI = (b2 - b4) / (b2 + b4)
    return WBI


def wdrvire(b5, b7, alpha=0.01):
    """
    Wide Dynamic Range Vegetation Index Red-edge (Peng and Gitelson, 2011).

    .. math:: t1 = (alpha * b7 - b5) / (alpha * b7 + b5)
    WDRVIRE = t1 + ((1 - alpha) / (1 + alpha))

    :param b5: Red-edge 1.
    :type b5: numpy.ndarray or float
    :param b7: Red-edge 3.
    :type b7: numpy.ndarray or float

    :returns WDRVIRE: Index value

    .. Tip::

        Peng, Y., Gitelson, A. A. 2011. Application of chlorophyll-related \
        vegetation indices for remote estimation of maize productivity. \
        Agricultural and Forest Meteorology 151(9), 1267-1276. \
        doi:10.1016/j.agrformet.2011.05.005.
    """

    t1 = (alpha * b7 - b5) / (alpha * b7 + b5)
    WDRVIRE = t1 + ((1 - alpha) / (1 + alpha))
    return WDRVIRE
