from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='pdfword2md',
    version='0.2.0',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'pdfword2md=converter:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A tool to convert between PDF, DOCX and Markdown formats',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pdfword2md',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    setup_requires=['wheel'],
)