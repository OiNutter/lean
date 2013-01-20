from template import Template
import re

class StringTemplate(Template):

	def prepare(self):
		self.code = "'{data}'".format(data='\n'.join(self.data.splitlines()))

	def precompiled_template(self,local_vars):
		return self.code

	def precompiled(self,local_vars):
		source, offset = super(StringTemplate,self).precompiled(local_vars)
		return (source,offset+1)