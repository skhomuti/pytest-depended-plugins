

def pytest_addoption(parser):

    parser.addoption(
        "--first-option",
        action="store_true",
        default=None,
    )
