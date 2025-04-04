from setuptools import setup,find_packages
setup (
    name='inf_STT',
    version='0.1',
    author='Ashish Kumar',
    author_email='ar6858439@gmail.com',
    description='Speech to Text Conversion package created by Ashish Kumar',

)
packages = find_packages(),
install_requirements = [
    'selenium',
    'webdriver-manager',
]
