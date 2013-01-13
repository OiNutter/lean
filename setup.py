from distutils.core import setup
import pandoc

pandoc.core.PANDOC_PATH = "pandoc"

doc = pandoc.Document()
doc.markdown = open('README.md','r').read()

setup(name='Lean',
      version='0.2',
      url='https://github.com/OiNutter/lean',
      download_url='https://github.com/OiNutter/lean/tarball/master',
      description='Generic interface to multiple Python template engines - Tilt for Python',
      long_description=doc.rst,
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