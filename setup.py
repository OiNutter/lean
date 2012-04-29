from distutils.core import setup

setup(name='shift',
	  version='0.1',
	  description='ADD DESCRIPTION HERE',
	  author='Will McKenzie',
	  author_email='will@oinutter.co.uk',
	  packages=['shift'],
	  package_dir={'shift': '<skeleton_project'},
      package_data={},
      requires:['coffeescript','pyScss']
	  )
