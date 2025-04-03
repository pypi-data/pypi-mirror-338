from setuptools import setup, find_packages

setup(
    name="neri_library",
    version="0.2.4",
    author="Guilherme Neri",
    author_email="gui.neriaz@gmail.com ",
    description="Neri Library",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NeriAzv/Neri-Library",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            *[f"{cmd}=bcpkgfox.cli:main" for cmd in [
                "bcpkgfox",
                "bpckgofx",
                "bcpkffox",
                "bcpkhfox",
                "bcpkfox",
                "pkgfox",
                "bcfox",
                "bcpkg",
                "bpkg",
                "pkg",
                "fox",
                "bc",
            ]],
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        'setuptools',
        'pyperclip',
        'pyinstaller',
        'selenium'
    ],
    extras_require={
        "full": [
            'undetected-chromedriver',
            'webdriver-manager',
            'opencv-python',
            'pygetwindow',
            'pyinstaller',
            'pyscreeze',
            'pyautogui',
            'selenium',
            'requests',
            'pymupdf',
            'Pillow',
            'psutil'
        ],

    },
)
