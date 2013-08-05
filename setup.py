from distutils.core import setup

setup(name='Smush',
      version='1.0',
      description='Lossless image optimiser script',
      url='https://github.com/thebeansgroup/smush.py',
      platforms='OS Independent',
      keywords="image optimize lossless",
      scripts=['bin/smush_it'],
      packages=['smush', 'smush.optimisers', 'smush.optimisers.formats'],
      include_package_data=True
)