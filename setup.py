from setuptools import setup, find_packages

setup(
    name='process-runner_start',
    version='1.0.1',
    description='A command-line tool to simplify running and compiling projects.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Exator911',
    author_email='matthewbates0727@gmail.com',
    url='https://github.com/Exator921/process-runner',
    packages=find_packages(),
    install_requires=[
        # Add dependencies from requirements.txt here
    ],
    entry_points={
        'console_scripts': [
            'process-runner_start=process_runner_start.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
