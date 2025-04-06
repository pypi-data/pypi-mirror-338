from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import pathlib


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        # Download spaCy models
        subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_lg"])
        subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_md"])
        subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_sm"])


# Read the README file
this_directory = pathlib.Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read the requirements.txt file
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='ccd_deidentification',
    version='0.2.0',  # Update this to your current version
    packages=find_packages(),
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'ccd-deid=ccd_deidentification.main:main'
        ]
    },
    cmdclass={
        'install': PostInstallCommand,
    },
)
