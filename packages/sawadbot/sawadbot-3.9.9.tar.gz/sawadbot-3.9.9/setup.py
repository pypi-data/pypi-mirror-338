from setuptools import setup, find_packages

setup(
    name="sawadbot",
    version="3.9.9",
    author="B_Q_5",
    description="Tele : @B_Q_5",
    packages=find_packages(),
    install_requires=[
        'pyTelegramBotAPI>=4.12.0',
        'psutil>=5.9.0',
        'colorama>=0.4.6'
    ],
)