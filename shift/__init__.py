import os
import re

class Shift(object):

  preferred_mappings = {}
  template_mappings = {}

  @staticmethod
  def register(template_class,*extensions):
		''' Register a template for a given extension or range of extensions '''
		for ext in extensions:
			ext = normalize(ext)
			if not Shift.template_mappings.has_key(ext):
				Shift.template_mappings[ext] = []

			Shift.template_mappings[ext].insert(0,template_class)
			Shift.template_mappings[ext] = unique(Shift.template_mappings[ext])

  @staticmethod
  def prefer(template_class,*extensions):
    ''' Makes a template class preferred for the given file extensions. If you
        don't provide any extensions, it will be preferred for all its already
        registered extensions:
      
        # Prefer Markdown for its registered file extensions:
        Shift.prefer(MarkdownTemplate)
        
        # Prefer Markdown only for the .md elxtensions:
        Shift.prefer(MarkdownTemplate, '.md')
    '''

    if len(extensions):
      for (ext,klasses) in Shift.template_mappings.items():
        if klasses.count(template_class):
          Shift.preferred_mappings[ext] = template_class
    else:
      for ext in extensions:
        ext = normalize(ext)
        Shift.register(template_class,ext)
        Shift.preferred_mappings[ext] = template_class

  @staticmethod
  def is_registered(ext):
    ''' Returns true when a template exists on an exact match of the provided file extension '''
    return Shift.template_mappings.has_key(ext.lower()) and len(Shift.template_mappings[ext])

  @staticmethod
  def load(file,line=None,options={},block=None):
    ''' Create a new template for the given file using the file's extension
        to determine the the template mapping.
    '''

    template_class = Shift.get_template(file)
    if template_class:
      return template_class(file,line,options,block)
    else:
      raise LookupError('No template engine registered for ' + os.path.basename(file))

  @staticmethod
  def get_template(file):
    ''' Lookup a template class for the given filename or file
        extension. Return nil when no implementation is found.
    '''

    pattern = str(file).lower()
    while len(pattern) and not Shift.is_registered(pattern):
      pattern = os.path.basename(pattern)
      pattern = re.sub(r'^[^.]*\.?','',pattern)

  	# Try to find a preferred engine.
    preferred_klass = Shift.preferred_mappings[pattern] if Shift.preferred_mappings.has_key(pattern) else None

    if preferred_klass:
  		return preferred_klass

  	# Fall back to the general list of mappings
    klasses = Shift.template_mappings[pattern]

  	# Try to find an engine which is already loaded
    template = None
    for klass in klasses:
  		if hasattr(klass,'is_engine_initialized') and callable(klass.is_engine_initialized):
  			if klass.is_engine_initialized():
  				template = klass
  				break

 		if template:
 			return template

 		# Try each of the classes until one succeeds. If all of them fails,
   	# we'll raise the error of the first class.
    first_failure = None

    for klass in klasses:
      try:
        return klass
      except Exception, e:
        if not first_failure:
          first_failure = e

   	if first_failure:
   		raise Exception(first_failure)

class Cache(object):
  ''' Extremely simple template cache implementation. Calling applications
      create a Tilt::Cache instance and use #fetch with any set of hashable
      arguments (such as those to Tilt.new):
      cache = shift.Cache()
      cache.fetch([path, line, options],Shift.new(path, line, options))
      
      Subsequent invocations return the already loaded template object.
  '''

  def __init__(self):
    self.cache = {}

  def fetch(self,key,result):
    if not self.cache.has_key(key) or not self.cache[key]:
  		self.cache[key] = result

    return self.cache[key]

  def clear(self):
		self.cache = {}

# Util Methods
def normalize(ext):
	''' Normalise file extensions'''
	return re.sub(r'^\.','',str(ext).lower())

def unique(seq):
	''' Removes duplicate elements from a List'''
   	seen = set()
 	seen_add = seen.add
   	return [ x for x in seq if x not in seen and not seen_add(x)]


##############################
## Template Implementations ##
##############################

from coffee import CoffeeScriptTemplate
Shift.register(CoffeeScriptTemplate,'coffee')

#from css import ScssTemplate
#Shift.register(ScssTemplate,'scss')

#from markdown import MarkdownTemplate
#Shift.register(MarkdownTemplate,'markdown','mkd','md')