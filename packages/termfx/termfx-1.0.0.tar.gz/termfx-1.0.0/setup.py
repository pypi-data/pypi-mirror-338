from setuptools import setup, find_packages

setup(
    name='termfx',
    version='1.0.0',
    description='Powerful and beautiful terminal output/input utilities for Python CLI tools.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='MyArchiveProject',
    url='https://github.com/MyArchiveProjects/termfx',
    project_urls={
        "Source": "https://github.com/MyArchiveProjects/termfx",
        "Issues": "https://github.com/MyArchiveProjects/termfx/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    keywords='terminal cli print input formatting color styled centered progress bar ascii',
    python_requires='>=3.7',
)
