from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.2'
DESCRIPTION = 'A Discord API Wrapper often used for automation'
LONG_DESCRIPTION = 'Create scripts that interact with Discord API for automation. You do not need to worry about using requests and you can simply interact with Discord API without hastle.'

# Setting up
setup(
    name="disquest",
    version=VERSION,
    author="PlutoGuy",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'requests', 'json', 'emoji'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)