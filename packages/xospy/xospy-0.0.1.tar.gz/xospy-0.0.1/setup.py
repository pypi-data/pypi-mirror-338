from setuptools import setup, find_packages

# get requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='xospy',
    version='0.0.1',
    description='Interact with the xos operating system from python.',
    author='xlate',
    author_email='dyllan@xlate.ai',
    url='https://xlate.ai',
    # packages=find_packages(),
    install_requires=required,
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'License :: OSI Approved :: MIT License',
    #     'Programming Language :: Python :: 3',
    #     'Programming Language :: Python :: 3.6',
    #     'Programming Language :: Python :: 3.7',
    #     'Programming Language :: Python :: 3.8',
    #     'Programming Language :: Python :: 3.9',
    # ],
)