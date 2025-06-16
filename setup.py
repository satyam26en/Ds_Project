from setuptools import setup, find_packages

# Simple hardcoded requirements (cleaner approach)
requirements = [
    'pandas',
    'numpy', 
    'scikit-learn',
    'matplotlib',
    'seaborn',
    'jupyter'
]

setup(
    name='mlproject',
    version='0.0.1',
    author='Satyam Kumar',
    author_email='Satyamkumar26en@gmail.com',
    description='A simple machine learning project template',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    python_requires='>=3.6',
)