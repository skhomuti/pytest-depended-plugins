
pytest_plugins = ["allure_pytest", "first_plugin"]


def pytest_addoption(parser):

    parser.addoption(
        "--third-option",
        action="store_true",
        default=None,
    )
