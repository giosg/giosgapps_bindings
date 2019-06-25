from distutils.core import setup
setup(
  name = 'giosgapps-bindings',         
  packages = ['giosgapps-bindings'],   
  version = '0.0.1',      
  license = 'MIT',        
  description = 'Module for Giosg Apps development',   
  author = 'Giosg',                  
  author_email = 'surface@giosg.com',      
  url = 'https://github.com/giosg/giosgapps-bindings',   
  download_url = '',    
  keywords = ['AUTH', 'GIOSG'],   
  install_requires=['jwt','requests'],  
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',   
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)