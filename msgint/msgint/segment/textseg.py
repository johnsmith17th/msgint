from smallseg import SEG
import urllib, json
#from pymmseg import mmseg

small_seg = None
scws_url = 'http://www.ftphp.com/scws/api.php'
mmseg_loaded = False

def feature_smallseg(text):
    global small_seg
    if not small_seg:
        small_seg = SEG()
    ls = small_seg.cut(text)
    ls.reverse()
    return dict([(w, 1) for w in ls])

def seg_smallseg(text):
    global small_seg
    if not small_seg:
        small_seg = SEG()
    ls = small_seg.cut(text)
    ls.reverse()
    return ' '.join(ls)
    
def seg_scws(text):
    global scws_url
    data = { 'data': text, 'respond': 'json', 'charset': 'utf-8', 'ignore': 'yes', 'multi': 3 }
    parm = urllib.urlencode(data)
    post = urllib.urlopen(url = scws_url, data = parm)
    resp = post.read()
    jobj = json.loads(resp)
    ls = [i['word'] for i in jobj['words']]
    return ' '.join(ls)

'''    
def seg_pymmseg(text):
    global mmseg_loaded
    if not mmseg_loaded:
        mmseg.dict_load_defaults()
        mmseg_loaded = True
    seg = mmseg.Algorithm(text)
    ls = [i.text for i in seg]
    return ' '.join(ls)
'''