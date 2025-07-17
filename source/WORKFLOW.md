# Create a COLR font with UVS (CMAP 14 Table)

The `.gyphs` format is color-preserving, unfortunately `fontmake` does not
yet support (easily) color output to OpenType fonts.  Unfortunately, the Glyphs
format appears to drop some info. So do this:


1. Open the .glyphs file in FontLab Studio
2. Under File > Font Info > Names
   a) Fix the "Full name", change "Reg" to "Regular"
   b) Fix the "Postscript name", the string before "-Regular" will be missing.
3. Under File > Font Info > Creator
   a) Add "RYT" to the "Vendor" field 
4. Export font form FontLab Studio to "OpenType COLR"
5. Execute in Python 3: `waldba-fix-fontnames.py`
6. Execute in Python 3: `add-cmap-from-file.py`

For example:
```
waldba-fix-fontnames.py  &lt;TTF in file&gt; &lt;TTF out file&gt;
add-cmap-from-file.py &lt;TTF in file&gt; &lt;TTF out file&gt; &lt;UVS mapping file&gt;

waldba-fix-fontnames.py /path/to/WaldbaFantuwua-Regular-COLR.ttf  /tmp/WaldbaFantuwua-NameFix.ttf Waldba.uvs
add-cmap-from-file.py /tmp/WaldbaFantuwua-NameFix.ttf  WaldbaFantuwua-COLR-UVS.ttf Waldba.uvs
```
The `.uvs` file follows the format used by HighLogic's FontCreator tool.
