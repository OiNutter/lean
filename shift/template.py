import io

class Template(object):

	# Template source; loaded from a file or given directly
	_data

	# The name of the file where the template data was loaded from
	_file

	# The line number in _file where the template data was loaded from
	_line

	# A dict of template engine specific options. This is passed directly
    # to the underlying engine and is not used by the generic template
    # interface.
    _options

    # Used to determine if this class's initialize_engine method has
    # been called yet.
	engine_initialized = False

	def is_engine_initialized(self):
		return engine_initialized

	def __init__(self,file=None,line=1,options={},block=None):
		''' Create a new template with the file, line, and options specified. By
    		default, template data is read from the file. When a block is given,
    		it should read template data and return as a String. When file is nil,
    		a block is required.
    		
    		All arguments are optional.
    	'''
		self._file = os.path.abspath(file) if file else None
		self._line = line
		self._options = options

		if not file and not block:
			raise ValueError('file or block required')

		# call the initialize_engine method if this is the very first time
      	# an instance of this class has been created.
		if not self.is_engine_initialized():
			self.initialize_engine()
			self.engine_initialized = True

		# used to hold compiled template methods
		self.compiled_methods = {}

		self.default_encoding = self._options.pop('default_encoding','UTF-8')

		# load template data and prepare (uses binread to avoid encoding issues)
		self.reader = block || io.open(self._file,'r',encoding = self.default_encoding).read()