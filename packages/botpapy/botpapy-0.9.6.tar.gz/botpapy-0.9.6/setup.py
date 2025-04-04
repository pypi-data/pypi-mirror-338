from setuptools import setup, find_packages

setup(
    name='botpapy',
    version='0.9.6',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv_python',
        'Pillow',
        'pywin32'
    ],
    author="Alpel",
    author_email="Alpel@gmx.net",
    description="Python Library to automate tasks with template matching in (non-visible) windows",
    long_description=open("botpapy/README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Alpel99/botpapy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    # entry_points={
    #     'console_scripts': [
    #         'crangeTest = botpapy:crangeTest',
    #         'checkWindowNames = botpapy:checkWindowNames'
    #     ]
    # }
)