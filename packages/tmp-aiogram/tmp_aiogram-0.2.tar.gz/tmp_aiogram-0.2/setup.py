from setuptools import setup, find_packages

setup(
    name="tmp-aiogram",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        'aiogram==2.2',
        'requests',
        'click',
        'autoenv-tool>=0.6',
        
    ],
    entry_points={
        'console_scripts': [
            'tmp=tmp_aiogram.cli:create',  # To'g'ri yo'lni tekshirish zarur
        ],
    },
    url="https://github.com/Husanjonazamov/tmp-aiogram",
    author="Husanjon Azamov",
    author_email="azamovhusanboy@gmail.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
