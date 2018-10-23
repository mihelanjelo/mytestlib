from setuptools import setup, find_packages

setup(name='mytestlib',
      version='0.3',
      url='https://github.com/mihelanjelo/mytestlib.git',
      license='MIT',
      author='Mimsa',
      author_email='mixanrattle@gmail.com',
      description='My test lib',
      packages=find_packages(exclude=['venv', '.idea', '__pycache__']),
      long_description=open('README.md').read(),
      zip_safe=False)