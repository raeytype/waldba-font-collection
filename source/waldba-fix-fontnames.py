#!/usr/local/opt/python@3.11/bin/python3.11
#
# This script remvoes the duplicate name entries in Mac Roman encoding,
# which appear to override the Unicode encoded names on OSX
#
import sys
from fontTools import ttLib


if __name__ == "__main__":
        font_path = sys.argv[1]

        font = ttLib.TTFont(font_path)
	# Name ID, Platform ID, Platform Encoding ID, Language ID
	# Platform ID = (Apple)
	# Platform Encoding ID = 0 (Mac Roman)
	# Language ID = 0 (English?)
	# 
        # Name ID: 
	#   1 = Font Family Name
	#   2 = Font Subfamily Name
	#   4 = Full Font Name
	#   5 = Version String
	#   6 = PostScript Name

        font["name"].removeNames(1, 1, 0, 0)
        font["name"].removeNames(2, 1, 0, 0)
        font["name"].removeNames(4, 1, 0, 0)
        font["name"].removeNames(5, 1, 0, 0)
        font["name"].removeNames(6, 1, 0, 0)
        namerecord_list = font["name"].names

        # list updated name record array contents
        # for record in namerecord_list:
        #     print( record.nameID , ": ", record.string )

        font.save( sys.argv[2] )
