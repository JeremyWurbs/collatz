import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    reqs = []
    for line in f:
        line = line.strip()
        reqs.append(line.split('==')[0])

setuptools.setup(
     name='collatz',
     version='1.0.0',
     description="Package for computing the Collatz Conjecture and related graphs",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/jeremywurbs/collatz",
     packages=setuptools.find_packages(),
     install_requires=reqs,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache License Version 2.0",
         "Operating System :: OS Independent",
         "Topic :: Scientific/Engineering :: Mathematics",
     ],
 )
