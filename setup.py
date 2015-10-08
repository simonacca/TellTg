from setuptools import find_packages, setup

setup(
    name='Tell Telegram',
    version='1.0.1',
    url='https://github.com/simonacca/TellTelegram',
    author='Simone Accascina',
    author_email='simon@accascina.me',
    description='A command line utility to send Telegram messages via a bot.',
    keywords='telegram bot command line sender',
    license='MIT',
    packages=find_packages(),
    scripts=['telltg/telltg'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
