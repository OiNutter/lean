from template import Template

class JinjaTemplate(Template):

	@staticmethod
	def is_engine_initialized():
		return 'jinja2' in globals()

	def prepare(self):
		return

	def initialize_engine(self):
		global jinja2
		import jinja2

	def evaluate(self,scope, local_vars, block=None):
		if not hasattr(self,'output') or not self.output:
			tmpl = jinja2.Template(self.data)
			import inspect
			if scope and not isinstance(scope,dict):
				scope = dict(inspect.getmembers(scope))
			self.output = tmpl.render(scope)

		return self.output



