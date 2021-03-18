from setuptools import setup

setup(
    name="third-plugin",
    py_modules=['third_plugin'],
    entry_points={
        'pytest11': [
            'third_plugin = third_plugin',
        ],
    },
    classifiers=["Framework :: Pytest"],
)
