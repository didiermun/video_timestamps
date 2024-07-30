from setuptools import setup, find_packages

setup(
    name='video_timestamps',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'moviepy',
    ],
    entry_points={
        'console_scripts': [
            'add-timestamp=video_timestamps.add_timestamp:main',
        ],
    },
)
