from olliepy import __version__, __all__


def test_version():
    assert __version__ == '0.2.6'


def test_modules():
    assert 'RegressionErrorAnalysisReport' in __all__
    assert 'InteractiveDashboard' in __all__
