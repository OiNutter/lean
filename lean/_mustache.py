from template import Template

class MustacheTemplate(Template):

	@staticmethod
	def is_engine_initialized():
		return 'pystache' in globals()

	def prepare(self):
		pass

	def initialize_engine(self):
		global pystache
		import pystache

	def evaluate(self,scope, local_vars, block=None):
		if not hasattr(self,'output') or not self.output:
			if scope and not isinstance(scope,dict):
				scope = scope.__dict__
			tmpl_vars = scope or {}
			tmpl_vars.update(local_vars or {})
			print 'rendering mustache'
			self.output = pystache.render(self.data,tmpl_vars)
			print self.output

		return self.output