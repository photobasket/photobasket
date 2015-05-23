import re

map = {' ' : '_',
       '.' : '_dot_',
       '&' : '_and_',
       '$' : '_dolar_',
       ':' : '_colon_',
       ',' : '_comma_'
       }

_under = re.compile(r'_+')

def parse_for_beautiful_url(text):
	str = ''.join([map.get(ch,ch) for ch in text])
	str = _under.sub('_',str)
	if str[-1:] == '_': return str[0:-1]
	return str

def createAlbumUrl(request, email, albumname):
	return 'http://' + request.get_header('host') + "/albums/" + email + parse_for_beautiful_url(albumname)


