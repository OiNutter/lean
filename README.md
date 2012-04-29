Shift
=======

Shift is intended to provide a consistent interface to various python templating languages. Code wise it is a port of [Tilt](https://github.com/rtomayko/tilt) for Ruby.

At the moment it just has support for CoffeeScript and Scss as those are what I need but I will be adding support for as many other python templating languages as I can. I will also be trying to add support for the compiled template functionality that Tilt has, just as soon as I can understand how it works and how to do it in Python.

If you want to get involved and help add support for other templating languages then please, get stuck in!

Basic Usage
-----------

```python
from shift import Shift

tmpl = Shift.load('blah.coffee')
tmpl.render()

```

License
-------

Copyright 2012 Will McKenzie

Shift is licensed under the MIT License, please see the LICENSE file
for more details.
