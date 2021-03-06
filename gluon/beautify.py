import cgi
from tag import TAGGER, UL, LI, TABLE, TBODY, TR, TH, TD, DIV, XML

def beautify(obj):
    if isinstance(obj, TAGGER):
        return obj
    elif isinstance(obj, list):
        return UL(*[LI(beautify(item)) for item in  obj])
    elif isinstance(obj, dict):
        return TABLE(TBODY(*[TR(TH(XML(key)),TD(beautify(value))) for key, value in obj.iteritems()]))
    else:
        return XML(obj)

def 
print beautify({'a':[1,2,DIV('3')]})    
    
