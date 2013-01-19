import sys
sys.path.insert(0,"../../")

from lean import Lean

details = {
	'title':'Mustache Test',
	'users':[
		{"url":"http://oinutter.co.uk","username":"OiNutter"},
		{"url":"http://autoclubrevolution.com","username":"ACR"},
	]
}
tmpl = Lean.load('test.mustache')
print tmpl.render(details)
