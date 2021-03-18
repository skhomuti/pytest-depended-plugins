

def pytest_addoption(parser):

    parser.addoption(
        "--second-option",
        action="store_true",
        default=None,
    )
