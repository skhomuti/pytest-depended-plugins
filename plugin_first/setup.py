from setuptools import setup

setup(
    name="first-plugin",
    py_modules=['first_plugin'],
    entry_points={
        'pytest11': [
            'first_plugin = first_plugin',
        ],
    },
    classifiers=["Framework :: Pytest"],
)
