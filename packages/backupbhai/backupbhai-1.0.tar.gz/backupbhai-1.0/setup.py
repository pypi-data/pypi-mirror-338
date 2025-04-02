from setuptools import setup

setup(
    name="backupbhai",
    version="1.0",
    packages=["backupbhai"],
    entry_points={
        "console_scripts": [
            "backupbhai=backupbhai:run",
        ],
    },
)