from olliepy import __version__, __all__


def test_version():
    assert __version__ == '0.2.7'


def test_modules():
    assert 'RegressionErrorAnalysisReport' in __all__
    assert 'InteractiveDashboard' in __all__
