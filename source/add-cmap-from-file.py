import os
import sys
import re

from fontTools import ttLib
from fontTools.ttLib.tables import _c_m_a_p

from nototools import font_data

CURR_DIR = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

def addUVS(font, Variants):
    cmap14 = _c_m_a_p.CmapSubtable.newSubtable(14)
    cmap14.cmap = {}
    # cmap14.uvsDict = {uvs: [[ base, variant ]]}
    cmap14.uvsDict = Variants
    cmap14.platformID = 0
    cmap14.platEncID = 5
    cmap14.language = 0xFF  # what fontTools would have used
    font["cmap"].tables.append(cmap14)


def addVariant(selector, base, variant, Variants):
        print( "Line: {}: ({}, {})".format( hex(selector), hex(base), variant ) )
        if selector in Variants:
             Variants[selector].append( [base, variant] )
        else:
             Variants[selector] = [ [base, variant] ]


def readVariantFile( variantPath, Variants ):
    file1 = open( variantPath, 'r')
    Lines = file1.readlines()

    vsPattern = re.compile("^\$(\w{4}) \$(\w{4}|\w{5}) (.*?)$")

    # Strips the newline character
    for line in Lines:
        vs = vsPattern.match( line )
        if( vs ):
            base     = int( vs[1] , 16 ) 
            selector = int( vs[2] , 16 )
            variant  = vs[3] 
            addVariant( selector, base, variant, Variants ) 


def main():
    fontPath = sys.argv[1]
    font = ttLib.TTFont(fontPath)

    if font_data.get_variation_sequence_cmap(font):
        # do not process font if it already has a var selector cmap
        raise ValueError("font %s already has a format 14 cmap" % font_file)

    Variants = dict()
    variantPath = sys.argv[3]
    readVariantFile( variantPath, Variants )

    addUVS( font, Variants )

    font.save( sys.argv[2] )


if __name__ == "__main__":
    main()
