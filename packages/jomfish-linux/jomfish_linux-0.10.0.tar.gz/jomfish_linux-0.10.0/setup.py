from setuptools import setup, find_packages

setup(
    name='jomfish-linux',
    version='0.10.0',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'jomfish': ['bin/jomfish'],  
    },
    entry_points={
        'console_scripts': [
            'jomfish=jomfish.main:main',
        ],
    },
    install_requires=[
    ],
    description='Jomfish - A high-performance chess engine',
    author='Jimmy Luong',
    author_email='nguyenhungjimmy.luong@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)