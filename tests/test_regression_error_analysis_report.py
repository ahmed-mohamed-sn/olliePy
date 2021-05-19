import pytest

from olliepy.RegressionErrorAnalysisReport import RegressionErrorAnalysisReport
import pandas as pd
from .utils import delete_directory

valid_output_directory = './tests/output'


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
                                      train_df=pd.DataFrame({'BMI': [], 'e': []}),
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
                                      test_df=pd.DataFrame({'BMI': [], 'e': []}),
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
    [{'ACCEPTABLE': (0, 1)}],
    [{'ACCEPTABLE': (False, True)}],
    {3: (0.0, 1.0)}
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


@pytest.fixture()
def empty_report():
    return RegressionErrorAnalysisReport(title='Test report title',
                                         output_directory=valid_output_directory,
                                         train_df=pd.DataFrame({'target': [], 'error': []}),
                                         test_df=pd.DataFrame({'target': [], 'error': []}),
                                         target_feature_name='target',
                                         error_column_name='error',
                                         error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                         acceptable_error_class='ACCEPTABLE',
                                         numerical_features=[],
                                         categorical_features=[],
                                         subtitle='Test report subtitle')


@pytest.mark.parametrize("enable_patterns_report", [
    3,
    'test',
    {},
    [1, 2, 3]
])
def test_invalid_enable_patterns_report(enable_patterns_report, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(enable_patterns_report=enable_patterns_report)


@pytest.mark.parametrize("patterns_report_group_by_categorical_features", [
    3,
    {},
    [1, 2, 3],
    False
])
def test_invalid_patterns_report_group_by_categorical_features(patterns_report_group_by_categorical_features,
                                                               empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(
            patterns_report_group_by_categorical_features=patterns_report_group_by_categorical_features)


@pytest.mark.parametrize("patterns_report_group_by_numerical_features", [
    3,
    {},
    [1, 2, 3],
    False
])
def test_invalid_patterns_report_group_by_numerical_features(patterns_report_group_by_numerical_features,
                                                             empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(
            patterns_report_group_by_numerical_features=patterns_report_group_by_numerical_features)


@pytest.mark.parametrize("patterns_report_group_by_categorical_features", [
    'ALL',
    'All',
    'somethingElse'
])
def test_invalid_patterns_report_group_by_categorical_features_string(patterns_report_group_by_categorical_features,
                                                                      empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(
            patterns_report_group_by_categorical_features=patterns_report_group_by_categorical_features)


@pytest.mark.parametrize("patterns_report_group_by_numerical_features", [
    'ALL',
    'All',
    'somethingElse'
])
def test_invalid_patterns_report_group_by_numerical_features_string(patterns_report_group_by_numerical_features,
                                                                    empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(
            patterns_report_group_by_numerical_features=patterns_report_group_by_numerical_features)


@pytest.mark.parametrize("patterns_report_group_by_categorical_features", [
    ['a', 'b'],
    'a'
])
def test_invalid_patterns_report_group_by_categorical_features_list(patterns_report_group_by_categorical_features,
                                                                    empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(
            patterns_report_group_by_categorical_features=patterns_report_group_by_categorical_features)


@pytest.mark.parametrize("patterns_report_group_by_numerical_features", [
    ['a', 'b'],
    'a'
])
def test_invalid_patterns_report_group_by_numerical_features_list(patterns_report_group_by_numerical_features,
                                                                  empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(
            patterns_report_group_by_numerical_features=patterns_report_group_by_numerical_features)


@pytest.mark.parametrize("patterns_report_number_of_bins", [
    13.0,
    'test',
    3.3,
    [2.0, 3.0]
])
def test_invalid_patterns_report_number_of_bins(patterns_report_number_of_bins, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(
            patterns_report_number_of_bins=patterns_report_number_of_bins)


@pytest.mark.parametrize("patterns_report_number_of_bins,patterns_report_group_by_numerical_features", [
    ([1, 2, 3], 'all'),
    ([1, 2, 3, 10], 'all')
])
def test_invalid_patterns_report_number_of_bins_with_patterns_report_group_by_numerical_features(
        patterns_report_number_of_bins, patterns_report_group_by_numerical_features, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(
            patterns_report_group_by_numerical_features=patterns_report_group_by_numerical_features,
            patterns_report_number_of_bins=patterns_report_number_of_bins)


@pytest.mark.parametrize("patterns_report_number_of_bins,patterns_report_group_by_numerical_features", [
    ([1, 2, 3, 10], ['a', 'b', 'c']),
    ([1, 2], ['a', 'b', 'c'])
])
def test_invalid_patterns_report_number_of_bins_with_patterns_report_group_by_numerical_features_length(
        patterns_report_number_of_bins, patterns_report_group_by_numerical_features, empty_report):
    report = RegressionErrorAnalysisReport(title='Test report title',
                                           output_directory=valid_output_directory,
                                           train_df=pd.DataFrame({'target': [], 'error': []}),
                                           test_df=pd.DataFrame({'target': [], 'error': []}),
                                           target_feature_name='target',
                                           error_column_name='error',
                                           error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                           acceptable_error_class='ACCEPTABLE',
                                           numerical_features=['a', 'b', 'c'],
                                           categorical_features=[],
                                           subtitle='Test report subtitle')
    with pytest.raises(AttributeError):
        report.create_report(
            patterns_report_group_by_numerical_features=patterns_report_group_by_numerical_features,
            patterns_report_number_of_bins=patterns_report_number_of_bins)


@pytest.mark.parametrize("enable_parallel_coordinates_plot", [
    3,
    'test',
    {},
    [1, 2, 3]
])
def test_invalid_enable_parallel_coordinates_plot(enable_parallel_coordinates_plot, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(enable_parallel_coordinates_plot=enable_parallel_coordinates_plot)


@pytest.mark.parametrize("cosine_similarity_threshold", [
    3,
    'test',
    {},
    [1, 2, 3]
])
def test_invalid_cosine_similarity_threshold(cosine_similarity_threshold, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(cosine_similarity_threshold=cosine_similarity_threshold)


@pytest.mark.parametrize("cosine_similarity_threshold", [
    3.0,
    -1.0,
    -0.01,
    1.01
])
def test_invalid_cosine_similarity_threshold_value(cosine_similarity_threshold, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(cosine_similarity_threshold=cosine_similarity_threshold)


@pytest.mark.parametrize("parallel_coordinates_q1_threshold", [
    3,
    'test',
    {},
    [1, 2, 3]
])
def test_invalid_parallel_coordinates_q1_threshold(parallel_coordinates_q1_threshold, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(parallel_coordinates_q1_threshold=parallel_coordinates_q1_threshold)


@pytest.mark.parametrize("parallel_coordinates_q2_threshold", [
    3,
    'test',
    {},
    [1, 2, 3]
])
def test_invalid_parallel_coordinates_q2_threshold(parallel_coordinates_q2_threshold, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(parallel_coordinates_q2_threshold=parallel_coordinates_q2_threshold)


@pytest.mark.parametrize("parallel_coordinates_q1_threshold", [
    3.0,
    -1.0,
    -0.01,
    1.01
])
def test_invalid_parallel_coordinates_q1_threshold_value(parallel_coordinates_q1_threshold, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(parallel_coordinates_q1_threshold=parallel_coordinates_q1_threshold)


@pytest.mark.parametrize("parallel_coordinates_q2_threshold", [
    3.0,
    -1.0,
    -0.01,
    1.01
])
def test_invalid_parallel_coordinates_q2_threshold_value(parallel_coordinates_q2_threshold, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(parallel_coordinates_q2_threshold=parallel_coordinates_q2_threshold)


@pytest.mark.parametrize("parallel_coordinates_q1_threshold,parallel_coordinates_q2_threshold", [
    (0.7, 0.3),
    (0.51, 0.49),
    (0.9, 0.1)
])
def test_invalid_parallel_coordinates_q1_threshold_and_parallel_coordinates_q2_threshold(
        parallel_coordinates_q1_threshold,
        parallel_coordinates_q2_threshold, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(parallel_coordinates_q1_threshold=parallel_coordinates_q1_threshold,
                                   parallel_coordinates_q2_threshold=parallel_coordinates_q2_threshold)


@pytest.mark.parametrize("parallel_coordinates_features", [
    3,
    {},
    [1, 2, 3]
])
def test_invalid_parallel_coordinates_features(parallel_coordinates_features, empty_report):
    with pytest.raises(TypeError):
        empty_report.create_report(parallel_coordinates_features=parallel_coordinates_features)


@pytest.mark.parametrize("parallel_coordinates_features", [
    'AUTO',
    'Auto',
    '',
    ['a', 'b', 'c']
])
def test_invalid_parallel_coordinates_features_value(parallel_coordinates_features, empty_report):
    with pytest.raises(AttributeError):
        empty_report.create_report(parallel_coordinates_features=parallel_coordinates_features)


@pytest.mark.parametrize("parallel_coordinates_features", [
    ['a'],
])
def test_invalid_parallel_coordinates_features_number_of_features(parallel_coordinates_features, empty_report):
    report = RegressionErrorAnalysisReport(title='Test report title',
                                           output_directory=valid_output_directory,
                                           train_df=pd.DataFrame({'target': [], 'error': [], 'a': []}),
                                           test_df=pd.DataFrame({'target': [], 'error': [], 'a': []}),
                                           target_feature_name='target',
                                           error_column_name='error',
                                           error_classes={'ACCEPTABLE': (0.0, 1.0)},
                                           acceptable_error_class='ACCEPTABLE',
                                           numerical_features=[],
                                           categorical_features=[],
                                           subtitle='Test report subtitle')
    with pytest.raises(AttributeError):
        report.create_report(parallel_coordinates_features=parallel_coordinates_features)


@pytest.fixture()
def simple_report():
    train_df = pd.DataFrame({'weight': {0: 74.48889704151111,
                                        1: 83.23062945633602,
                                        2: 58.404847212649685,
                                        3: 78.15622647206627,
                                        4: 79.32958733202109,
                                        5: 30.505818004592548,
                                        6: 75.5109602551382,
                                        7: 38.48389654950436,
                                        8: 101.36793814909961,
                                        9: 55.50409954014475},
                             'height': {0: 1.691766915191099,
                                        1: 1.9491826474035565,
                                        2: 1.2852713830834017,
                                        3: 1.3070265980930795,
                                        4: 1.4082847624165382,
                                        5: 2.1092287694563883,
                                        6: 1.2141654096900105,
                                        7: 1.5432515253201904,
                                        8: 1.5778261997325116,
                                        9: 1.5518513879251712},
                             'gender': {0: 'male',
                                        1: 'female',
                                        2: 'male',
                                        3: 'female',
                                        4: 'female',
                                        5: 'female',
                                        6: 'female',
                                        7: 'female',
                                        8: 'male',
                                        9: 'female'},
                             'BMI': {0: 31.231420289851012,
                                     1: 21.90675777726569,
                                     2: 42.42681812245051,
                                     3: 45.75038272162881,
                                     4: 39.99946978863252,
                                     5: 6.8570182001235835,
                                     6: 51.22173452143229,
                                     7: 16.158669891418683,
                                     8: 48.86113291803425,
                                     9: 23.047551994650284},
                             'error': {0: 4.35965045351168,
                                       1: 4.2512455184537075,
                                       2: -2.308950637211275,
                                       3: -1.2665772229146128,
                                       4: 1.2316660337917327,
                                       5: 5.02980912521628,
                                       6: -3.422442273158559,
                                       7: 4.715049764661153,
                                       8: -5.575733463244902,
                                       9: 4.012867455526585}})

    test_df = pd.DataFrame({'weight': {0: 52.25806772623051,
                                       1: 54.69766066240298,
                                       2: 52.06483988871636,
                                       3: 62.91902427740109,
                                       4: 47.7799463904831,
                                       5: 44.30962234747368,
                                       6: 63.99950158640414,
                                       7: 59.54355306685157,
                                       8: 50.84080568723348,
                                       9: 71.18986475553054},
                            'height': {0: 1.739476242029242,
                                       1: 1.7550120224198116,
                                       2: 1.5241736180721417,
                                       3: 1.4803520957617644,
                                       4: 1.656645901891169,
                                       5: 1.493587129704761,
                                       6: 1.6663233819769372,
                                       7: 1.8113877793130846,
                                       8: 1.8625683686536378,
                                       9: 1.6745775829534932},
                            'gender': {0: 'female',
                                       1: 'male',
                                       2: 'male',
                                       3: 'male',
                                       4: 'male',
                                       5: 'male',
                                       6: 'male',
                                       7: 'male',
                                       8: 'male',
                                       9: 'male'},
                            'BMI': {0: 17.270954674667788,
                                    1: 21.310311937234523,
                                    2: 26.894093036181275,
                                    3: 34.45348672331068,
                                    4: 20.891398977668707,
                                    5: 23.835165364395273,
                                    6: 27.65917747850496,
                                    7: 21.776753009598,
                                    8: 17.586087267923713,
                                    9: 30.46413614849721},
                            'error': {0: 7.395859499144738,
                                      1: 6.6498794687474,
                                      2: 2.1178110852914998,
                                      3: 1.352281099323676,
                                      4: 4.626225079884751,
                                      5: 0.64125099459838,
                                      6: 4.765865116297338,
                                      7: 7.822131201189546,
                                      8: 3.996376015557967,
                                      9: 5.1269345948654745}})

    error_classes = {
        'ACCEPTABLE': (-0.5, 1.5),
        'OVER_ESTIMATING': (1.5, 5.0)
    }

    categorical_features = ['gender']
    numerical_features = ['weight', 'height']

    target_feature = 'BMI'

    return RegressionErrorAnalysisReport(title='BMI Regression Report',
                                         output_directory=valid_output_directory,
                                         train_df=train_df,
                                         test_df=test_df,
                                         target_feature_name=target_feature,
                                         error_column_name='error',
                                         error_classes=error_classes,
                                         acceptable_error_class='ACCEPTABLE',
                                         numerical_features=numerical_features,
                                         categorical_features=categorical_features,
                                         report_folder_name='TestFullReport',
                                         subtitle='BMI distribution shift')


def test_create_report_simple(simple_report):
    expected_output = {'title': 'BMI Regression Report',
                       'subtitle': 'BMI distribution shift',
                       'report': {'primaryDatasets': ['Training data', 'ACCEPTABLE'],
                                  'secondaryDatasets': ['Testing data', 'ACCEPTABLE', 'OVER_ESTIMATING'],
                                  'numericalFeatures': ['weight', 'height', 'BMI'], 'categoricalFeatures': ['gender'],
                                  'targetFeature': 'BMI', 'datasets': {'Training data': {
                               'info': {'name': 'Training data', 'numberOfRows': 10, 'minError': -5.575733463244902,
                                        'meanError': 1.102658475463179, 'stdError': 3.941365381389868,
                                        'medianError': 2.622266744659159, 'maxError': 5.02980912521628,
                                        'errors': [4.35965045351168, 4.2512455184537075, -2.308950637211275,
                                                   -1.2665772229146128, 1.2316660337917327, 5.02980912521628,
                                                   -3.422442273158559, 4.715049764661153, -5.575733463244902,
                                                   4.012867455526585], 'stats': {
                                       'weight': {'min': 30.505818004592548, 'mean': 67.49829000130634,
                                                  'std': 21.59766336766331, 'median': 74.99992864832466,
                                                  'max': 101.36793814909961, 'count': 10, 'missingCount': 0},
                                       'height': {'min': 1.2141654096900105, 'mean': 1.5637855598311947,
                                                  'std': 0.28926913773626567, 'median': 1.547551456622681,
                                                  'max': 2.1092287694563883, 'count': 10, 'missingCount': 0},
                                       'BMI': {'min': 6.8570182001235835, 'mean': 32.746095622548765,
                                               'std': 15.186679926045725, 'median': 35.61544503924176,
                                               'max': 51.22173452143229, 'count': 10, 'missingCount': 0},
                                       'gender': {'uniqueCount': 2, 'missingCount': 0}}}, 'data': {
                                   'weight': [74.48889704151111, 83.23062945633602, 58.404847212649685,
                                              78.15622647206627, 79.32958733202109, 30.505818004592548,
                                              75.5109602551382, 38.48389654950436, 101.36793814909961,
                                              55.50409954014475],
                                   'height': [1.691766915191099, 1.9491826474035565, 1.2852713830834017,
                                              1.3070265980930795, 1.4082847624165382, 2.1092287694563883,
                                              1.2141654096900105, 1.5432515253201904, 1.5778261997325116,
                                              1.5518513879251712],
                                   'BMI': [31.231420289851012, 21.90675777726569, 42.42681812245051, 45.75038272162881,
                                           39.99946978863252, 6.8570182001235835, 51.22173452143229, 16.158669891418683,
                                           48.86113291803425, 23.047551994650284]}}, 'Testing data': {
                               'info': {'name': 'Testing data', 'numberOfRows': 10, 'minError': 0.64125099459838,
                                        'meanError': 4.449461415490077, 'stdError': 2.4771220201885265,
                                        'medianError': 4.696045098091044, 'maxError': 7.822131201189546,
                                        'errors': [7.395859499144738, 6.6498794687474, 2.1178110852914998,
                                                   1.352281099323676, 4.626225079884751, 0.64125099459838,
                                                   4.765865116297338, 7.822131201189546, 3.996376015557967,
                                                   5.1269345948654745], 'stats': {
                                       'weight': {'min': 44.30962234747368, 'mean': 55.96028863887274,
                                                  'std': 8.28098920044576, 'median': 53.477864194316744,
                                                  'max': 71.18986475553054, 'count': 10, 'missingCount': 0},
                                       'height': {'min': 1.4803520957617644, 'mean': 1.6664104122776042,
                                                  'std': 0.132314518932591, 'median': 1.670450482465215,
                                                  'max': 1.8625683686536378, 'count': 10, 'missingCount': 0},
                                       'BMI': {'min': 17.270954674667788, 'mean': 24.21415646179821,
                                               'std': 5.584236868127869, 'median': 22.80595918699664,
                                               'max': 34.45348672331068, 'count': 10, 'missingCount': 0},
                                       'gender': {'uniqueCount': 2, 'missingCount': 0}}}, 'data': {
                                   'weight': [52.25806772623051, 54.69766066240298, 52.06483988871636,
                                              62.91902427740109, 47.7799463904831, 44.30962234747368, 63.99950158640414,
                                              59.54355306685157, 50.84080568723348, 71.18986475553054],
                                   'height': [1.739476242029242, 1.7550120224198116, 1.5241736180721417,
                                              1.4803520957617644, 1.656645901891169, 1.493587129704761,
                                              1.6663233819769372, 1.8113877793130846, 1.8625683686536378,
                                              1.6745775829534932],
                                   'BMI': [17.270954674667788, 21.310311937234523, 26.894093036181275,
                                           34.45348672331068, 20.891398977668707, 23.835165364395273, 27.65917747850496,
                                           21.776753009598, 17.586087267923713, 30.46413614849721]}}, 'ACCEPTABLE': {
                               'info': {'name': 'ACCEPTABLE', 'numberOfRows': 2, 'minError': 0.64125099459838,
                                        'meanError': 0.996766046961028, 'stdError': 0.5027742086790379,
                                        'medianError': 0.996766046961028, 'maxError': 1.352281099323676,
                                        'errors': [1.352281099323676, 0.64125099459838], 'stats': {
                                       'weight': {'min': 44.30962234747368, 'mean': 53.614323312437385,
                                                  'std': 13.1588342984777, 'median': 53.614323312437385,
                                                  'max': 62.91902427740109, 'count': 2, 'missingCount': 0},
                                       'height': {'min': 1.4803520957617644, 'mean': 1.4869696127332626,
                                                  'std': 0.00935858225032697, 'median': 1.4869696127332626,
                                                  'max': 1.493587129704761, 'count': 2, 'missingCount': 0},
                                       'BMI': {'min': 23.835165364395273, 'mean': 29.144326043852978,
                                               'std': 7.508287037707042, 'median': 29.144326043852978,
                                               'max': 34.45348672331068, 'count': 2, 'missingCount': 0},
                                       'gender': {'uniqueCount': 1, 'missingCount': 0}}},
                               'data': {'weight': [62.91902427740109, 44.30962234747368],
                                        'height': [1.4803520957617644, 1.493587129704761],
                                        'BMI': [34.45348672331068, 23.835165364395273]}}, 'OVER_ESTIMATING': {
                               'info': {'name': 'OVER_ESTIMATING', 'numberOfRows': 4, 'minError': 2.1178110852914998,
                                        'meanError': 3.876569324257889, 'stdError': 1.2193461286137446,
                                        'medianError': 4.311300547721359, 'maxError': 4.765865116297338,
                                        'errors': [2.1178110852914998, 4.626225079884751, 4.765865116297338,
                                                   3.996376015557967], 'stats': {
                                       'weight': {'min': 47.7799463904831, 'mean': 53.67127338820927,
                                                  'std': 7.117401386805094, 'median': 51.45282278797492,
                                                  'max': 63.99950158640414, 'count': 4, 'missingCount': 0},
                                       'height': {'min': 1.5241736180721417, 'mean': 1.6774278176484714,
                                                  'std': 0.13942628856425054, 'median': 1.6614846419340532,
                                                  'max': 1.8625683686536378, 'count': 4, 'missingCount': 0},
                                       'BMI': {'min': 17.586087267923713, 'mean': 23.257689190069666,
                                               'std': 4.842964994637156, 'median': 23.89274600692499,
                                               'max': 27.65917747850496, 'count': 4, 'missingCount': 0},
                                       'gender': {'uniqueCount': 1, 'missingCount': 0}}}, 'data': {
                                   'weight': [52.06483988871636, 47.7799463904831, 63.99950158640414,
                                              50.84080568723348],
                                   'height': [1.5241736180721417, 1.656645901891169, 1.6663233819769372,
                                              1.8625683686536378],
                                   'BMI': [26.894093036181275, 20.891398977668707, 27.65917747850496,
                                           17.586087267923713]}}}, 'statistical_tests': {'Training data_Testing data': {
                               'weight': {'ks_2samp': {'p_value': 0.05244755244755244, 'p_value_threshold': 0.01},
                                          'wasserstein_distance': 16.157972199205595},
                               'height': {'ks_2samp': {'p_value': 0.41752365281777043, 'p_value_threshold': 0.01},
                                          'wasserstein_distance': 0.17951590622505403},
                               'BMI': {'ks_2samp': {'p_value': 0.16782134274394334, 'p_value_threshold': 0.01},
                                       'wasserstein_distance': 10.900209930960395}, 'gender': {
                                   'cosine_similarity': {'cosine_similarity': 0.49301257198088044,
                                                         'cosine_similarity_threshold': 0.8}}},
                               'Training data_ACCEPTABLE': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.4545454545454545,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 17.80987271703907},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.4545454545454545,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.21814799305073757},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.7575757575757576,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 9.075902297520356},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.39391929857916774,
                                           'cosine_similarity_threshold': 0.8}}},
                               'Training data_OVER_ESTIMATING': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.1878121878121879,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 19.14105225847095},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.49950049950049946,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.18284154704922675},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.1878121878121879,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 11.91970372134013},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.39391929857916774,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_Testing data': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.9393939393939394,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 4.665332291544885},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.18181818181818177,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.17944079954434158},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.7575757575757576,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 4.930169582054765},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.9938837346736189,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_ACCEPTABLE': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'height': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 1.0,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_OVER_ESTIMATING': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.9333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 5.4840422701142515},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.1333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.19045820491520876},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.9333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 5.886636853783314},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 1.0,
                                           'cosine_similarity_threshold': 0.8}}}},
                                  'categorical_count_plots': {'gender': {
                                      'Training data_Testing data': {'title': 'Training data vs Testing data',
                                                                     'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'Testing data', 'color': '#FF938D', 'data': [1, 9]}]},
                                      'Training data_ACCEPTABLE': {'title': 'Training data vs ACCEPTABLE',
                                                                   'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'ACCEPTABLE', 'color': '#FF938D', 'data': [0.0, 2.0]}]},
                                      'Training data_OVER_ESTIMATING': {'title': 'Training data vs OVER_ESTIMATING',
                                                                        'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'OVER_ESTIMATING', 'color': '#FF938D', 'data': [0.0, 4.0]}]},
                                      'ACCEPTABLE_Testing data': {'title': 'ACCEPTABLE vs Testing data',
                                                                  'categories': ['male', 'female'], 'series': [
                                              {'name': 'ACCEPTABLE', 'color': '#8180FF', 'data': [2.0, 0.0]},
                                              {'name': 'Testing data', 'color': '#FF938D', 'data': [9, 1]}]},
                                      'ACCEPTABLE_OVER_ESTIMATING': {'title': 'ACCEPTABLE vs OVER_ESTIMATING',
                                                                     'categories': ['male'], 'series': [
                                              {'name': 'ACCEPTABLE', 'color': '#8180FF', 'data': [2]},
                                              {'name': 'OVER_ESTIMATING', 'color': '#FF938D', 'data': [4]}]}}}}}

    simple_report.create_report(enable_parallel_coordinates_plot=False, enable_patterns_report=False)
    assert expected_output == simple_report.report_data


def test_create_report_with_parallel_coordinates_plot(simple_report):
    expected_output = {'title': 'BMI Regression Report',
                       'subtitle': 'BMI distribution shift',
                       'report': {'primaryDatasets': ['Training data', 'ACCEPTABLE'],
                                  'secondaryDatasets': ['Testing data', 'ACCEPTABLE', 'OVER_ESTIMATING'],
                                  'numericalFeatures': ['weight', 'height', 'BMI'], 'categoricalFeatures': ['gender'],
                                  'targetFeature': 'BMI', 'datasets': {'Training data': {
                               'info': {'name': 'Training data', 'numberOfRows': 10, 'minError': -5.575733463244902,
                                        'meanError': 1.102658475463179, 'stdError': 3.941365381389868,
                                        'medianError': 2.622266744659159, 'maxError': 5.02980912521628,
                                        'errors': [4.35965045351168, 4.2512455184537075, -2.308950637211275,
                                                   -1.2665772229146128, 1.2316660337917327, 5.02980912521628,
                                                   -3.422442273158559, 4.715049764661153, -5.575733463244902,
                                                   4.012867455526585], 'stats': {
                                       'weight': {'min': 30.505818004592548, 'mean': 67.49829000130634,
                                                  'std': 21.59766336766331, 'median': 74.99992864832466,
                                                  'max': 101.36793814909961, 'count': 10, 'missingCount': 0},
                                       'height': {'min': 1.2141654096900105, 'mean': 1.5637855598311947,
                                                  'std': 0.28926913773626567, 'median': 1.547551456622681,
                                                  'max': 2.1092287694563883, 'count': 10, 'missingCount': 0},
                                       'BMI': {'min': 6.8570182001235835, 'mean': 32.746095622548765,
                                               'std': 15.186679926045725, 'median': 35.61544503924176,
                                               'max': 51.22173452143229, 'count': 10, 'missingCount': 0},
                                       'gender': {'uniqueCount': 2, 'missingCount': 0}}}, 'data': {
                                   'weight': [74.48889704151111, 83.23062945633602, 58.404847212649685,
                                              78.15622647206627, 79.32958733202109, 30.505818004592548,
                                              75.5109602551382, 38.48389654950436, 101.36793814909961,
                                              55.50409954014475],
                                   'height': [1.691766915191099, 1.9491826474035565, 1.2852713830834017,
                                              1.3070265980930795, 1.4082847624165382, 2.1092287694563883,
                                              1.2141654096900105, 1.5432515253201904, 1.5778261997325116,
                                              1.5518513879251712],
                                   'BMI': [31.231420289851012, 21.90675777726569, 42.42681812245051, 45.75038272162881,
                                           39.99946978863252, 6.8570182001235835, 51.22173452143229, 16.158669891418683,
                                           48.86113291803425, 23.047551994650284]}}, 'Testing data': {
                               'info': {'name': 'Testing data', 'numberOfRows': 10, 'minError': 0.64125099459838,
                                        'meanError': 4.449461415490077, 'stdError': 2.4771220201885265,
                                        'medianError': 4.696045098091044, 'maxError': 7.822131201189546,
                                        'errors': [7.395859499144738, 6.6498794687474, 2.1178110852914998,
                                                   1.352281099323676, 4.626225079884751, 0.64125099459838,
                                                   4.765865116297338, 7.822131201189546, 3.996376015557967,
                                                   5.1269345948654745], 'stats': {
                                       'weight': {'min': 44.30962234747368, 'mean': 55.96028863887274,
                                                  'std': 8.28098920044576, 'median': 53.477864194316744,
                                                  'max': 71.18986475553054, 'count': 10, 'missingCount': 0},
                                       'height': {'min': 1.4803520957617644, 'mean': 1.6664104122776042,
                                                  'std': 0.132314518932591, 'median': 1.670450482465215,
                                                  'max': 1.8625683686536378, 'count': 10, 'missingCount': 0},
                                       'BMI': {'min': 17.270954674667788, 'mean': 24.21415646179821,
                                               'std': 5.584236868127869, 'median': 22.80595918699664,
                                               'max': 34.45348672331068, 'count': 10, 'missingCount': 0},
                                       'gender': {'uniqueCount': 2, 'missingCount': 0}}}, 'data': {
                                   'weight': [52.25806772623051, 54.69766066240298, 52.06483988871636,
                                              62.91902427740109, 47.7799463904831, 44.30962234747368, 63.99950158640414,
                                              59.54355306685157, 50.84080568723348, 71.18986475553054],
                                   'height': [1.739476242029242, 1.7550120224198116, 1.5241736180721417,
                                              1.4803520957617644, 1.656645901891169, 1.493587129704761,
                                              1.6663233819769372, 1.8113877793130846, 1.8625683686536378,
                                              1.6745775829534932],
                                   'BMI': [17.270954674667788, 21.310311937234523, 26.894093036181275,
                                           34.45348672331068, 20.891398977668707, 23.835165364395273, 27.65917747850496,
                                           21.776753009598, 17.586087267923713, 30.46413614849721]}}, 'ACCEPTABLE': {
                               'info': {'name': 'ACCEPTABLE', 'numberOfRows': 2, 'minError': 0.64125099459838,
                                        'meanError': 0.996766046961028, 'stdError': 0.5027742086790379,
                                        'medianError': 0.996766046961028, 'maxError': 1.352281099323676,
                                        'errors': [1.352281099323676, 0.64125099459838], 'stats': {
                                       'weight': {'min': 44.30962234747368, 'mean': 53.614323312437385,
                                                  'std': 13.1588342984777, 'median': 53.614323312437385,
                                                  'max': 62.91902427740109, 'count': 2, 'missingCount': 0},
                                       'height': {'min': 1.4803520957617644, 'mean': 1.4869696127332626,
                                                  'std': 0.00935858225032697, 'median': 1.4869696127332626,
                                                  'max': 1.493587129704761, 'count': 2, 'missingCount': 0},
                                       'BMI': {'min': 23.835165364395273, 'mean': 29.144326043852978,
                                               'std': 7.508287037707042, 'median': 29.144326043852978,
                                               'max': 34.45348672331068, 'count': 2, 'missingCount': 0},
                                       'gender': {'uniqueCount': 1, 'missingCount': 0}}},
                               'data': {'weight': [62.91902427740109, 44.30962234747368],
                                        'height': [1.4803520957617644, 1.493587129704761],
                                        'BMI': [34.45348672331068, 23.835165364395273]}}, 'OVER_ESTIMATING': {
                               'info': {'name': 'OVER_ESTIMATING', 'numberOfRows': 4, 'minError': 2.1178110852914998,
                                        'meanError': 3.876569324257889, 'stdError': 1.2193461286137446,
                                        'medianError': 4.311300547721359, 'maxError': 4.765865116297338,
                                        'errors': [2.1178110852914998, 4.626225079884751, 4.765865116297338,
                                                   3.996376015557967], 'stats': {
                                       'weight': {'min': 47.7799463904831, 'mean': 53.67127338820927,
                                                  'std': 7.117401386805094, 'median': 51.45282278797492,
                                                  'max': 63.99950158640414, 'count': 4, 'missingCount': 0},
                                       'height': {'min': 1.5241736180721417, 'mean': 1.6774278176484714,
                                                  'std': 0.13942628856425054, 'median': 1.6614846419340532,
                                                  'max': 1.8625683686536378, 'count': 4, 'missingCount': 0},
                                       'BMI': {'min': 17.586087267923713, 'mean': 23.257689190069666,
                                               'std': 4.842964994637156, 'median': 23.89274600692499,
                                               'max': 27.65917747850496, 'count': 4, 'missingCount': 0},
                                       'gender': {'uniqueCount': 1, 'missingCount': 0}}}, 'data': {
                                   'weight': [52.06483988871636, 47.7799463904831, 63.99950158640414,
                                              50.84080568723348],
                                   'height': [1.5241736180721417, 1.656645901891169, 1.6663233819769372,
                                              1.8625683686536378],
                                   'BMI': [26.894093036181275, 20.891398977668707, 27.65917747850496,
                                           17.586087267923713]}}}, 'statistical_tests': {'Training data_Testing data': {
                               'weight': {'ks_2samp': {'p_value': 0.05244755244755244, 'p_value_threshold': 0.01},
                                          'wasserstein_distance': 16.157972199205595},
                               'height': {'ks_2samp': {'p_value': 0.41752365281777043, 'p_value_threshold': 0.01},
                                          'wasserstein_distance': 0.17951590622505403},
                               'BMI': {'ks_2samp': {'p_value': 0.16782134274394334, 'p_value_threshold': 0.01},
                                       'wasserstein_distance': 10.900209930960395}, 'gender': {
                                   'cosine_similarity': {'cosine_similarity': 0.49301257198088044,
                                                         'cosine_similarity_threshold': 0.8}}},
                               'Training data_ACCEPTABLE': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.4545454545454545,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 17.80987271703907},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.4545454545454545,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.21814799305073757},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.7575757575757576,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 9.075902297520356},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.39391929857916774,
                                           'cosine_similarity_threshold': 0.8}}},
                               'Training data_OVER_ESTIMATING': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.1878121878121879,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 19.14105225847095},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.49950049950049946,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.18284154704922675},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.1878121878121879,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 11.91970372134013},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.39391929857916774,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_Testing data': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.9393939393939394,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 4.665332291544885},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.18181818181818177,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.17944079954434158},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.7575757575757576,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 4.930169582054765},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 0.9938837346736189,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_ACCEPTABLE': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'height': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 1.0,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.0},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 1.0,
                                           'cosine_similarity_threshold': 0.8}}},
                               'ACCEPTABLE_OVER_ESTIMATING': {
                                   'weight': {'ks_2samp': {
                                       'p_value': 0.9333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 5.4840422701142515},
                                   'height': {'ks_2samp': {
                                       'p_value': 0.1333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 0.19045820491520876},
                                   'BMI': {'ks_2samp': {
                                       'p_value': 0.9333333333333333,
                                       'p_value_threshold': 0.01},
                                       'wasserstein_distance': 5.886636853783314},
                                   'gender': {
                                       'cosine_similarity': {
                                           'cosine_similarity': 1.0,
                                           'cosine_similarity_threshold': 0.8}}}},
                                  'categorical_count_plots': {'gender': {
                                      'Training data_Testing data': {'title': 'Training data vs Testing data',
                                                                     'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'Testing data', 'color': '#FF938D', 'data': [1, 9]}]},
                                      'Training data_ACCEPTABLE': {'title': 'Training data vs ACCEPTABLE',
                                                                   'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'ACCEPTABLE', 'color': '#FF938D', 'data': [0.0, 2.0]}]},
                                      'Training data_OVER_ESTIMATING': {'title': 'Training data vs OVER_ESTIMATING',
                                                                        'categories': ['female', 'male'], 'series': [
                                              {'name': 'Training data', 'color': '#8180FF', 'data': [7, 3]},
                                              {'name': 'OVER_ESTIMATING', 'color': '#FF938D', 'data': [0.0, 4.0]}]},
                                      'ACCEPTABLE_Testing data': {'title': 'ACCEPTABLE vs Testing data',
                                                                  'categories': ['male', 'female'], 'series': [
                                              {'name': 'ACCEPTABLE', 'color': '#8180FF', 'data': [2.0, 0.0]},
                                              {'name': 'Testing data', 'color': '#FF938D', 'data': [9, 1]}]},
                                      'ACCEPTABLE_OVER_ESTIMATING': {'title': 'ACCEPTABLE vs OVER_ESTIMATING',
                                                                     'categories': ['male'], 'series': [
                                              {'name': 'ACCEPTABLE', 'color': '#8180FF', 'data': [2]},
                                              {'name': 'OVER_ESTIMATING', 'color': '#FF938D', 'data': [4]}]}}},
                                  'parallel_coordinates': {
                                      'Training data_OVER_ESTIMATING': {'primaryDatasetName': 'Training data',
                                                                        'secondaryDatasetName': 'OVER_ESTIMATING',
                                                                        'colors': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                                                                                   1, 1], 'dimensions': [
                                              {'range': [0, 1], 'label': 'gender',
                                               'values': [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1], 'tickvals': [0, 1],
                                               'ticktext': ['female', 'male']},
                                              {'range': [30.505818004592548, 101.36793814909961], 'label': 'weight',
                                               'values': [74.48889704151111, 83.23062945633602, 58.404847212649685,
                                                          78.15622647206627, 79.32958733202109, 30.505818004592548,
                                                          75.5109602551382, 38.48389654950436, 101.36793814909961,
                                                          55.50409954014475, 52.06483988871636, 47.7799463904831,
                                                          63.99950158640414, 50.84080568723348]}]}}}}

    simple_report.create_report(enable_parallel_coordinates_plot=True, enable_patterns_report=False)
    assert expected_output == simple_report.report_data


def test_create_report_with_patterns_report():
    import json
    with open('tests/data/report_with_patterns_report_output.json') as json_file:
        expected_output = json.load(json_file)

    train_df = pd.read_csv('tests/data/train_data.csv')
    test_df = pd.read_csv('tests/data/test_data.csv')

    error_classes = {
        'HIGH_UNDER_ESTIMATION': (-8.0, -3.0),
        'LOW_UNDER_ESTIMATION': (-3.0, -0.5),
        'ACCEPTABLE': (-0.5, 0.5),
        'OVER_ESTIMATING': (0.5, 3.0)
    }

    categorical_features = ['gender']
    numerical_features = ['weight', 'height']

    target_feature = 'BMI'

    full_report = RegressionErrorAnalysisReport(title='BMI Regression Report',
                                                output_directory=valid_output_directory,
                                                train_df=train_df,
                                                test_df=test_df,
                                                target_feature_name=target_feature,
                                                error_column_name='error',
                                                error_classes=error_classes,
                                                acceptable_error_class='ACCEPTABLE',
                                                numerical_features=numerical_features,
                                                categorical_features=categorical_features,
                                                subtitle='BMI distribution shift')

    full_report.create_report(enable_parallel_coordinates_plot=False, enable_patterns_report=True)

    assert expected_output == full_report.report_data


def test_create_report_with_patterns_report_custom():
    import json
    with open('tests/data/report_with_patterns_report_output.json') as json_file:
        expected_output = json.load(json_file)

    train_df = pd.read_csv('tests/data/train_data.csv')
    test_df = pd.read_csv('tests/data/test_data.csv')

    error_classes = {
        'HIGH_UNDER_ESTIMATION': (-8.0, -3.0),
        'LOW_UNDER_ESTIMATION': (-3.0, -0.5),
        'ACCEPTABLE': (-0.5, 0.5),
        'OVER_ESTIMATING': (0.5, 3.0)
    }

    categorical_features = ['gender']
    numerical_features = ['weight', 'height']

    target_feature = 'BMI'

    full_report = RegressionErrorAnalysisReport(title='BMI Regression Report',
                                                output_directory=valid_output_directory,
                                                train_df=train_df,
                                                test_df=test_df,
                                                target_feature_name=target_feature,
                                                error_column_name='error',
                                                error_classes=error_classes,
                                                acceptable_error_class='ACCEPTABLE',
                                                numerical_features=numerical_features,
                                                categorical_features=categorical_features,
                                                subtitle='BMI distribution shift')

    full_report.create_report(enable_parallel_coordinates_plot=False,
                              enable_patterns_report=True,
                              patterns_report_group_by_categorical_features=categorical_features,
                              patterns_report_group_by_numerical_features=numerical_features,
                              patterns_report_number_of_bins=[10, 10])

    assert expected_output == full_report.report_data


def test_create_report_with_patterns_report_categorical_only():
    import json
    with open('tests/data/report_with_patterns_report_categorical_output.json') as json_file:
        expected_output = json.load(json_file)

    train_df = pd.read_csv('tests/data/train_data.csv')
    test_df = pd.read_csv('tests/data/test_data.csv')

    error_classes = {
        'HIGH_UNDER_ESTIMATION': (-8.0, -3.0),
        'LOW_UNDER_ESTIMATION': (-3.0, -0.5),
        'ACCEPTABLE': (-0.5, 0.5),
        'OVER_ESTIMATING': (0.5, 3.0)
    }

    categorical_features = ['gender']
    numerical_features = ['weight', 'height']

    target_feature = 'BMI'

    full_report = RegressionErrorAnalysisReport(title='BMI Regression Report',
                                                output_directory=valid_output_directory,
                                                train_df=train_df,
                                                test_df=test_df,
                                                target_feature_name=target_feature,
                                                error_column_name='error',
                                                error_classes=error_classes,
                                                acceptable_error_class='ACCEPTABLE',
                                                numerical_features=numerical_features,
                                                categorical_features=categorical_features,
                                                subtitle='BMI distribution shift')

    full_report.create_report(enable_parallel_coordinates_plot=False,
                              enable_patterns_report=True,
                              patterns_report_group_by_categorical_features=categorical_features,
                              patterns_report_group_by_numerical_features=[])

    assert expected_output == full_report.report_data


def test_save_report(simple_report):
    import os
    simple_report.create_report(enable_parallel_coordinates_plot=True, enable_patterns_report=False)

    report_path = f'{valid_output_directory}/{simple_report.report_folder_name}'
    if os.path.exists(report_path):
        delete_directory(report_path)
        os.remove(f'{report_path}.zip')

    simple_report.save_report(zip_report=False)
    assert os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}/report_data.json')
    assert not os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}.zip')

    simple_report.save_report(zip_report=True)
    assert os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}/report_data.json')
    assert os.path.exists(f'{valid_output_directory}/{simple_report.report_folder_name}.zip')


def test_serve_report(simple_report, mocker):
    simple_report.create_report(enable_parallel_coordinates_plot=True, enable_patterns_report=False)
    mocked_serve = mocker.patch('olliepy.Report.Report._serve_report_using_flask')

    def randint(a, b):
        return 33

    mocker.patch('random.randint', randint)

    simple_report.serve_report_from_local_server(port=8080)
    mocked_serve.assert_called_with(simple_report._template_name, 'server', 8080)

    simple_report.serve_report_from_local_server()
    mocked_serve.assert_called_with(simple_report._template_name, 'server', 33)
