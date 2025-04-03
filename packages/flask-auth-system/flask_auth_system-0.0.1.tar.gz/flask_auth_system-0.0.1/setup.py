from setuptools import setup, find_packages

setup(
    name='flask-auth-system',
    version='v0.0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'jwt',
        'email_validator',
        'flask_sqlalchemy',
        'flask_migrate',
        'fernet',
        'python-dotenv',
        'requests',
        'cryptography',]
)