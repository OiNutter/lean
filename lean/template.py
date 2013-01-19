import io
import os
import abc

class Template(object):

	__metaclass__ = abc.ABCMeta

	# Template source; loaded from a file or given directly
	_data = None

	# The name of the file where the template data was loaded from
	_file = None

	# The line number in _file where the template data was loaded from
	_line = 0

	# A dict of template engine specific options. This is passed directly
    # to the underlying engine and is not used by the generic template
    # interface.
	_options = {}

    # Used to determine if this class's initialize_engine method has
    # been called yet.
	engine_initialized = False

	@classmethod
	@abc.abstractmethod
	def is_engine_initialized(cls):
		return cls.engine_initialized
   
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
			self.__class__.engine_initialized = True

		# used to hold compiled template methods
		self.compiled_methods = {}

		self.default_encoding = self._options.pop('default_encoding','UTF-8')

		# load template data and prepare (uses binread to avoid encoding issues)
		self.reader = block if block else lambda t:io.open(self._file,'r',encoding = self.default_encoding).read()
		self.data = self.reader(self)
		return self.prepare()

	def render(self,scope=None,local_vars=None,block=None):
		''' Render the template in the given scope with the locals specified. If a
    		block is given, it is typically available within the template via
    		+yield+.
    	'''
		return self.evaluate(scope or {}, local_vars or {}, block)

	def basename(self, suffix=''):
		''' The basename of the template file.'''
		return os.path.basename(self._file, suffix) if self._file else None

	def name(self):
		''' The template file's basename with all extensions chomped off.'''
   		self.basename().split('.', 2)[0] if self.basename() else None

   	def eval_file(self):
   		'''The filename used in backtraces to describe the template.'''
		return self._file if self._file else '(__TEMPLATE__)'

	def initialize_engine(self):    	
		''' Called once and only once for each template subclass the first time
			the template class is initialized. This should be used to require the
			underlying template library and perform any initial setup.
		'''
		return

	def prepare(self):
		''' Do whatever preparation is necessary to setup the underlying template
    		engine. Called immediately after template data is loaded. Instance
    		variables set in this method are available when #evaluate is called.
    		
    		Subclasses must provide an implementation of this method.
		'''
		raise NotImplementedError

	def evaluate(self,scope,locals,block=None):
		''' Execute the compiled template and return the result string. Template
    		evaluation is guaranteed to be performed in the scope object with the
    		locals specified and with support for yielding to the block.
   			
   			This method is only used by source generating templates. Subclasses that
    		override render() may not support all features.
		'''
		method = self.compiled_method(locals.keys())
		setattr(self,'compiled',method.__get__(self,self.__class__))
		return self.compiled()

	#def precompiled(self,local_vars):
	#	preamble = self.precompiled_preamble(local_vars)
	#	template = self.precompiled_template(local_vars)
	#	magic_comment = self.extract_magic_comment(template)
	#	if magic_comment:
	#		preamble = magic_comment + "\n" + preamble

	#	parts = [
	#			preamble,
	#			template,
	#			self.precompiled_postamble(local_vars)
	#		]

	#	return ['\n'.join(parts),preamble.count('\n')+1]

	#def precompiled_template(self,local_vars):
	#	raise NotImplementedError

	#def precompiled_preamble(self,local_vars):

	#	preamble = []
	#	for key,value in local_vars.iteritems():
	#		preamble.append("%s = locals")


