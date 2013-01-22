from template import Template

class ScssTemplate(Template):
   	
   	default_mime_type = 'text/css'

   	@staticmethod
	def is_engine_initialized():
		return 'Scss' in globals()

	def initialize_engine(self):
		global Scss
		from scss import Scss

	def prepare(self):
		self.engine = Scss(scss_opts=self.sass_options())

	def sass_options(self):
		options = self._options
		options.update({
			'filename': self.eval_file(),
			'line': self._line,
			'syntax':'scss'
		})
		return options

	def evaluate(self,scope, locals, block=None):
		if not hasattr(self,'output') or not self.output:
			self.output = self.engine.compile(self.data)

		return self.output