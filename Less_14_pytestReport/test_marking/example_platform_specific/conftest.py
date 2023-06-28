def pytest_configure(config):
    config.addinivalue_line(
        "markers", "darwin: mark test to run only on darwin environment"),
    config.addinivalue_line(
        "markers", "linux: mark test to run only on linux environment"),
    config.addinivalue_line(
        "markers", "win32: mark test to run only on win32 environment")

