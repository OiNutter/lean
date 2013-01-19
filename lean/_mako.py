from template import Template

class MakoTemplate(Template):

	@staticmethod
	def is_engine_initialized():
		return 'mako_template' in globals()

	def prepare(self):
		pass

	def initialize_engine(self):
		global mako_template
		from mako import template as mako_template

	def evaluate(self,scope, local_vars, block=None):
		if not hasattr(self,'output') or not self.output:
			import inspect
			if scope and not isinstance(scope,dict):
				scope = dict(inspect.getmembers(scope))

			tmpl = mako_template.Template(self.data)
			self.output = tmpl.render(**scope)

		return self.output