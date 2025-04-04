from setuptools import setup, find_packages

setup(
    name='panmetrics',
    version='0.1.1',
    description='A library for evaluation metrics.',
    author='Morteza Alizadeh',
    author_email='alizadehmorteza2020@gmail.com',
    # url='https://github.com/yourusername/morteza',
    packages=find_packages(),
    install_requires=['numpy'],
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
