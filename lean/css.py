from template import Template
from scss import Scss

class ScssTemplate(Template):
   	
   	default_mime_type = 'text/css'

   	@staticmethod
	def is_engine_initialized():
		return 'Scss' in globals()

	def prepare(self):
		self._options['filename'] = self.eval_file
		self._options['line'] = self._line
		self._options['syntax'] = 'scss'

		self.engine = Scss(scss_opts=self._options)

	def evaluate(self,scope, locals, block=None):
		if not hasattr(self,'output') or not self.output:
			self.output = self.engine.compile(self.data)

		return self.output