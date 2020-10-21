from olliepy import __version__, __all__


def test_version():
    assert __version__ == '0.1.24'


def test_modules():
    assert 'RegressionErrorAnalysisReport' in __all__
