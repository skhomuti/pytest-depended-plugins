from setuptools import setup

setup(
    name="second-plugin",
    py_modules=['second_plugin'],
    entry_points={
        'pytest11': [
            'second_plugin = second_plugin',
        ],
    },
    classifiers=["Framework :: Pytest"],
)
