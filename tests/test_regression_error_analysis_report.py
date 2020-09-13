import pytest

from olliepy.RegressionErrorAnalysisReport import RegressionErrorAnalysisReport
import pandas as pd

valid_output_directory = './tests/output'


def delete_directory(directory):
    import shutil
    shutil.rmtree(directory)


@pytest.mark.parametrize("title", [
    None,
    20,
    False
])
def test_invalid_title(title):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title=title,
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      report_folder_name='TestRegressionErrorAnalysisReport')


@pytest.mark.parametrize("subtitle", [
    20,
    False
])
def test_invalid_subtitle(subtitle):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle=subtitle,
                                      report_folder_name='TestRegressionErrorAnalysisReport')


@pytest.mark.parametrize("output_directory", [
    'fake_output',
    './fake_output'
])
def test_invalid_output_directory(output_directory):
    with pytest.raises(NotADirectoryError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      report_folder_name='TestRegressionErrorAnalysisReport')


def test_none_output_directory():
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=None,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      report_folder_name='TestRegressionErrorAnalysisReport')


@pytest.mark.parametrize("report_folder_name", [
    3,
    False
])
def test_invalid_report_folder_name(report_folder_name):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      report_folder_name=report_folder_name)


@pytest.mark.parametrize("encryption_secret", [
    3,
    False
])
def test_invalid_encryption_secret_type(encryption_secret):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      encryption_secret=encryption_secret)


@pytest.mark.parametrize("encryption_secret", [
    '123456789',
    'iusadiudhadiahdiadhadihadihdasdsaddasdasd',
    ''
])
def test_invalid_encryption_secret_value(encryption_secret):
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      encryption_secret=encryption_secret)


@pytest.mark.parametrize("generate_encryption_secret", [
    3,
    'False'
])
def test_invalid_generate_encryption_secret_type(generate_encryption_secret):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle',
                                      generate_encryption_secret=generate_encryption_secret)


def test_valid_generate_encryption_secret_type():
    report = RegressionErrorAnalysisReport(title='Test report title',
                                           output_directory=valid_output_directory,
                                           train_df=pd.DataFrame({'target': [], 'error': []}),
                                           test_df=pd.DataFrame({'target': [], 'error': []}),
                                           target_feature_name='target',
                                           error_column_name='error',
                                           error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                           acceptable_error_class='ACCEPTABLE',
                                           numerical_features=[],
                                           categorical_features=[],
                                           subtitle='Test report subtitle',
                                           generate_encryption_secret=True)

    assert len(report.encryption_secret) == 16
    assert type(report.encryption_secret) is str


@pytest.mark.parametrize("train_df", [
    3,
    'False'
])
def test_invalid_train_df(train_df):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=train_df,
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("test_df", [
    3,
    'False'
])
def test_invalid_test_df(test_df):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=test_df,
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("target_feature_name", [
    3,
    False
])
def test_invalid_target_feature_name(target_feature_name):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name=target_feature_name,
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


def test_target_feature_name_not_in_train_df():
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'BMI': [], 'error': []}),
                                      target_feature_name='BMI',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


def test_target_feature_name_not_in_test_df():
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'BMI': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='BMI',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("error_column_name", [
    3,
    False
])
def test_invalid_error_column_name(error_column_name):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name=error_column_name,
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


def test_error_column_name_not_in_train_df():
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'e': []}),
                                      test_df=pd.DataFrame({'BMI': [], 'error': []}),
                                      target_feature_name='BMI',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


def test_error_column_name_not_in_test_df():
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'BMI': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'e': []}),
                                      target_feature_name='BMI',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("error_classes", [
    3,
    False,
    ({'ACCEPTABLE': (0, 1)}),
    ({'ACCEPTABLE': (False, True)}),
    ({3: (0.0, 1.0)})
])
def test_invalid_error_classes(error_classes):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes=error_classes,
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("acceptable_error_class", [
    3,
    False,
    {}
])
def test_invalid_acceptable_error_class(acceptable_error_class):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class=acceptable_error_class,
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("acceptable_error_class", [
    'A',
    'acceptable',
    'Acceptable'
])
def test_acceptable_error_class_not_in_error_classes(acceptable_error_class):
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class=acceptable_error_class,
                                      numerical_features=[],
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


def test_both_numerical_and_categorical_features_are_none():
    with pytest.raises(AttributeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=None,
                                      categorical_features=None,
                                      subtitle='Test report subtitle')

@pytest.mark.parametrize("numerical_features", [
    3,
    False,
    {},
    [1, 2, 3]
])
def test_invalid_numerical_features(numerical_features):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=numerical_features,
                                      categorical_features=[],
                                      subtitle='Test report subtitle')


@pytest.mark.parametrize("categorical_features", [
    3,
    False,
    {},
    [1, 2, 3]
])
def test_invalid_categorical_features(categorical_features):
    with pytest.raises(TypeError):
        RegressionErrorAnalysisReport(title='Test report title',
                                      output_directory=valid_output_directory,
                                      train_df=pd.DataFrame({'target': [], 'error': []}),
                                      test_df=pd.DataFrame({'target': [], 'error': []}),
                                      target_feature_name='target',
                                      error_column_name='error',
                                      error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                      acceptable_error_class='ACCEPTABLE',
                                      numerical_features=[],
                                      categorical_features=categorical_features,
                                      subtitle='Test report subtitle')
