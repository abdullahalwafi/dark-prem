#Compiled By Mr ProAL
#Github : https://github.com/MrproAl-404
import marshal,zlib,base645
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
