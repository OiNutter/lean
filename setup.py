from distutils.core import setup

setup(name='Lean',
      version='0.1',
      url='https://github.com/OiNutter/lean',
      download_url='https://github.com/OiNutter/lean/tarball/master',
      description='Generic interface to multiple Python template engines - Tilt for Python',
      long_description=open('DESCRIPTION','r').read(),
      author='Will McKenzie',
      author_email='will@oinutter.co.uk',
      packages=['lean'],
      package_dir={'lean': 'lean'},
      package_data={},
      license='MIT License',
      classifiers=[
	        'Development Status :: 3 - Alpha',
	        'Intended Audience :: Developers',
	        'License :: OSI Approved :: MIT License',
	        'Programming Language :: Python :: 2',
	        'Programming Language :: Python :: 2.6',
	        'Programming Language :: Python :: 2.7',
    	]
	)