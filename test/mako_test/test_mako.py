import sys
sys.path.insert(0,"../../")

from lean import Lean

details = {
	'title':'Mako Test',
	'users':[
		{"url":"http://oinutter.co.uk","username":"OiNutter"},
		{"url":"http://autoclubrevolution.com","username":"ACR"},
	]
}
tmpl = Lean.load('test.mako')
print tmpl.render(details)
