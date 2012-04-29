from template import Template
import coffeescript

class CoffeeScriptTemplate(Template):

	default_mime_type = 'application/javascript'

	default_bare = False

	@staticmethod
	def is_engine_initialized():
		return 'coffeescript' in globals()

	def prepare(self):
		if not self._options.has_key('bare') and not self._options.has_key('no_wrap'):
			self._options['bare'] = self.default_bare

	def evaluate(self,scope, locals, block=None):
		if not hasattr(self,'output') or not self.output:
			self.output = coffeescript.compile(self.data, self._options)

		return self.output



