import pytest
from olliepy.InteractiveDashboard import InteractiveDashboard
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
        InteractiveDashboard(title=title,
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['TestDF'],
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("output_directory", [
    'fake_output',
    './fake_output'
])
def test_invalid_output_directory(output_directory):
    with pytest.raises(NotADirectoryError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['TestDF'],
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("dataframes", [
    [{'A': ['1', '2', '3']}],
    ['a', 'b'],
    False,
    3
])
def test_invalid_dataframes(dataframes):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=dataframes,
                             dataframes_names=['TestDF'],
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("dataframes_names", [
    [{'A': ['1', '2', '3']}],
    [pd.DataFrame()],
    False,
    3,
    'test'
])
def test_invalid_dataframes_names(dataframes_names):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=dataframes_names,
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("numerical_columns", [
    [1, 2, 3],
    [1, 'test', 3],
    'test',
    3
])
def test_invalid_numerical_columns_type(numerical_columns):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['test'],
                             numerical_columns=numerical_columns,
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("categorical_columns", [
    [1, 2, 3],
    [1, 'test', 3],
    'test',
    3
])
def test_invalid_categorical_columns_type(categorical_columns):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['test'],
                             numerical_columns=[],
                             categorical_columns=categorical_columns,
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("date_columns", [
    [1, 2, 3],
    [1, 'test', 3],
    'test',
    3
])
def test_invalid_date_columns_type(date_columns):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['test'],
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=date_columns,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("dataframes, dataframes_names", [
    ([pd.DataFrame()], []),
    ([], ['test'])
])
def test_invalid_data_attributes_length(dataframes, dataframes_names):
    with pytest.raises(AttributeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=dataframes,
                             dataframes_names=dataframes_names,
                             numerical_columns=[],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("numerical_columns, categorical_columns", [
    ([], [])
])
def test_invalid_data_columns_length(numerical_columns, categorical_columns):
    with pytest.raises(AttributeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame()],
                             dataframes_names=['test'],
                             numerical_columns=numerical_columns,
                             categorical_columns=categorical_columns,
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("dataframes, numerical_columns, categorical_columns, date_columns", [
    ([pd.DataFrame({'X': [1, 2, 3]})], ['B'], [], []),
    ([pd.DataFrame({'X': [1, 2, 3]})], [], ['C'], []),
    ([pd.DataFrame({'X': [1, 2, 3], 'N': [1, 2, 3]})], ['N'], [], ['D'])
])
def test_columns_not_found(dataframes, numerical_columns, categorical_columns, date_columns):
    with pytest.raises(AttributeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=dataframes,
                             dataframes_names=['test'],
                             numerical_columns=numerical_columns,
                             categorical_columns=categorical_columns,
                             date_columns=date_columns,
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("dataframes", [
    [pd.DataFrame({'test_date': ['10-10-9999'], 'X': [1]})],
    [pd.DataFrame({'test_date': ['9999-10-10'], 'X': [1]})],
    [pd.DataFrame({'test_date': ['00-01-2020'], 'X': [1]})],
    [pd.DataFrame({'test_date': ['1-01-0000'], 'X': [1]})],
    [pd.DataFrame({'test_date': ['1-01-1000'], 'X': [1]})],
    [pd.DataFrame({'test_date': ['not a date'], 'X': [1]})]
])
def test_invalid_date_format(dataframes):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=dataframes,
                             dataframes_names=['test'],
                             numerical_columns=['X'],
                             categorical_columns=[],
                             date_columns=['test_date'],
                             dashboard_folder_name=None,
                             encryption_secret=None,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("encryption_secret", [
    '123456789',
    'iusadiudhadiahdiadhadihadihdasdsaddasdasd',
    ''
])
def test_invalid_encryption_secret(encryption_secret):
    with pytest.raises(AttributeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame({'X': [1]})],
                             dataframes_names=['TestDF'],
                             numerical_columns=['X'],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             encryption_secret=encryption_secret,
                             generate_encryption_secret=False)


@pytest.mark.parametrize("generate_encryption_secret", [
    3,
    'False'
])
def test_invalid_generate_encryption_secret(generate_encryption_secret):
    with pytest.raises(TypeError):
        InteractiveDashboard(title='Test dashboard title',
                             output_directory=valid_output_directory,
                             dataframes=[pd.DataFrame({'X': [1]})],
                             dataframes_names=['TestDF'],
                             numerical_columns=['X'],
                             categorical_columns=[],
                             date_columns=None,
                             dashboard_folder_name=None,
                             generate_encryption_secret=generate_encryption_secret)


@pytest.fixture()
def simple_dashboard():
    df = pd.DataFrame({'X': [1], 'B': ['Category_1'], 'C': ['2020-10-24']})

    return InteractiveDashboard(title='Test dashboard title',
                                output_directory=valid_output_directory,
                                dataframes=[df],
                                dataframes_names=['test'],
                                numerical_columns=['X'],
                                categorical_columns=['B'],
                                date_columns=['C'],
                                dashboard_folder_name='TestDashboard',
                                encryption_secret=None,
                                generate_encryption_secret=False)


def test_create_dashboard(simple_dashboard):
    expected_output = {'title': 'Test dashboard title',
                       'datasets': ['test'],
                       'numericalColumns': ['generated_id', 'X'],
                       'categoricalColumns': ['B'],
                       'dateColumns': ['C'],
                       'test': [{'X': 1, 'B': 'Category_1', 'C': 1603497600000, 'generated_id': 0}],
                       'numberDisplays': [],
                       'charts': []}

    simple_dashboard.create_dashboard()

    assert expected_output == simple_dashboard.report_data


@pytest.fixture()
def complex_dashboard():
    df = pd.DataFrame({'A': [1, 2,
                             2, 3,
                             4, 5],
                       'B': ['Category_1', 'Category_1',
                             'Category_2', 'Category_3',
                             'Category_3', 'Category_3'],
                       'C': ['Category_1', 'Category_1',
                             'Category_2', 'Category_2',
                             'Category_2', 'Category_2'],
                       'D': ['Category_1', 'Category_1',
                             'Category_2', 'Category_2',
                             'Category_2', 'Category_2'],
                       'E': ['Category_1', 'Category_1',
                             'Category_2', 'Category_2',
                             'Category_2', 'Category_2'],
                       'F': ['2020-10-24', '2020-10-23',
                             '2020-10-23', '2020-10-22',
                             '2020-10-22', '2020-10-21'],
                       'G': [1, 2,
                             2, 3,
                             4, 5],
                       'H': [1, 2,
                             2, 3,
                             4, 5],
                       'I': [1, 2,
                             2, 3,
                             4, 5]})

    return InteractiveDashboard(title='Test dashboard title',
                                output_directory='.',
                                dataframes=[df],
                                dataframes_names=['test'],
                                numerical_columns=['A', 'G', 'H', 'I'],
                                categorical_columns=['B', 'C', 'D', 'E'],
                                date_columns=['F'],
                                dashboard_folder_name='TestDashboard',
                                encryption_secret=None,
                                generate_encryption_secret=False)


def test_create_dashboard_autogenerate_charts(complex_dashboard):
    expected_output = {'title': 'Test dashboard title',
                       'datasets': ['test'],
                       'numericalColumns': ['generated_id', 'A', 'G', 'H', 'I'],
                       'categoricalColumns': ['B', 'C', 'D', 'E'],
                       'dateColumns': ['F'],
                       'test': [{'A': 1,
                                 'B': 'Category_1',
                                 'C': 'Category_1',
                                 'D': 'Category_1',
                                 'E': 'Category_1',
                                 'F': 1603497600000,
                                 'G': 1,
                                 'H': 1,
                                 'I': 1,
                                 'generated_id': 0},
                                {'A': 2,
                                 'B': 'Category_1',
                                 'C': 'Category_1',
                                 'D': 'Category_1',
                                 'E': 'Category_1',
                                 'F': 1603411200000,
                                 'G': 2,
                                 'H': 2,
                                 'I': 2,
                                 'generated_id': 1},
                                {'A': 2,
                                 'B': 'Category_2',
                                 'C': 'Category_2',
                                 'D': 'Category_2',
                                 'E': 'Category_2',
                                 'F': 1603411200000,
                                 'G': 2,
                                 'H': 2,
                                 'I': 2,
                                 'generated_id': 2},
                                {'A': 3,
                                 'B': 'Category_3',
                                 'C': 'Category_2',
                                 'D': 'Category_2',
                                 'E': 'Category_2',
                                 'F': 1603324800000,
                                 'G': 3,
                                 'H': 3,
                                 'I': 3,
                                 'generated_id': 3},
                                {'A': 4,
                                 'B': 'Category_3',
                                 'C': 'Category_2',
                                 'D': 'Category_2',
                                 'E': 'Category_2',
                                 'F': 1603324800000,
                                 'G': 4,
                                 'H': 4,
                                 'I': 4,
                                 'generated_id': 4},
                                {'A': 5,
                                 'B': 'Category_3',
                                 'C': 'Category_2',
                                 'D': 'Category_2',
                                 'E': 'Category_2',
                                 'F': 1603238400000,
                                 'G': 5,
                                 'H': 5,
                                 'I': 5,
                                 'generated_id': 5}],
                       'numberDisplays': [{'agg': 'count',
                                           'column': 'generated_id',
                                           'title': 'Number of observations',
                                           'type': 'number-display',
                                           'w': 12,
                                           'h': 1,
                                           'maxH': 2,
                                           'i': 0,
                                           'id': 'number_of_observations_number_display',
                                           'x': 0,
                                           'y': 0,
                                           'static': False}],
                       'charts': [{'dimension': 'B',
                                   'agg': 'count',
                                   'column': 'generated_id',
                                   'title': 'B count',
                                   'type': 'row-chart',
                                   'cap': 10,
                                   'w': 4,
                                   'h': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'i': 0,
                                   'id': 'chart_0',
                                   'x': 0,
                                   'y': 0,
                                   'static': False},
                                  {'id': 'chart_1',
                                   'title': 'C',
                                   'type': 'pie-chart',
                                   'dimension': 'C',
                                   'x': 4,
                                   'y': 0,
                                   'w': 4,
                                   'h': 2,
                                   'i': 1,
                                   'minW': 2,
                                   'minH': 2,
                                   'static': False},
                                  {'id': 'chart_2',
                                   'title': 'D',
                                   'type': 'pie-chart',
                                   'dimension': 'D',
                                   'x': 8,
                                   'y': 0,
                                   'w': 4,
                                   'h': 2,
                                   'i': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'static': False},
                                  {'id': 'chart_3',
                                   'title': 'E',
                                   'type': 'pie-chart',
                                   'dimension': 'E',
                                   'x': 0,
                                   'y': 2,
                                   'w': 4,
                                   'h': 2,
                                   'i': 3,
                                   'minW': 2,
                                   'minH': 2,
                                   'static': False},
                                  {'dimension': 'A',
                                   'title': 'A histogram',
                                   'xAxisLabel': 'A',
                                   'yAxisLabel': 'Frequency',
                                   'binWidth': 0.04,
                                   'type': 'histogram-chart',
                                   'w': 4,
                                   'h': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'i': 4,
                                   'id': 'chart_4',
                                   'x': 4,
                                   'y': 2,
                                   'static': False},
                                  {'dimension': 'G',
                                   'title': 'G histogram',
                                   'xAxisLabel': 'G',
                                   'yAxisLabel': 'Frequency',
                                   'binWidth': 0.04,
                                   'type': 'histogram-chart',
                                   'w': 4,
                                   'h': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'i': 5,
                                   'id': 'chart_5',
                                   'x': 8,
                                   'y': 2,
                                   'static': False},
                                  {'dimension': 'H',
                                   'title': 'H histogram',
                                   'xAxisLabel': 'H',
                                   'yAxisLabel': 'Frequency',
                                   'binWidth': 0.04,
                                   'type': 'histogram-chart',
                                   'w': 4,
                                   'h': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'i': 6,
                                   'id': 'chart_6',
                                   'x': 0,
                                   'y': 4,
                                   'static': False},
                                  {'dimension': 'I',
                                   'title': 'I histogram',
                                   'xAxisLabel': 'I',
                                   'yAxisLabel': 'Frequency',
                                   'binWidth': 0.04,
                                   'type': 'histogram-chart',
                                   'w': 4,
                                   'h': 2,
                                   'minW': 2,
                                   'minH': 2,
                                   'i': 7,
                                   'id': 'chart_7',
                                   'x': 4,
                                   'y': 4,
                                   'static': False}]}

    complex_dashboard.create_dashboard(auto_generate_distribution_plots=True)

    assert expected_output == complex_dashboard.report_data


def test_save_dashboard(simple_dashboard):
    import os
    simple_dashboard.create_dashboard()

    dashboard_path = f'{valid_output_directory}/{simple_dashboard.report_folder_name}'
    if os.path.exists(dashboard_path):
        delete_directory(dashboard_path)
        os.remove(f'{dashboard_path}.zip')

    simple_dashboard.save_dashboard(zip_dashboard=False)
    assert os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}/report_data.json')
    assert not os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}.zip')

    simple_dashboard.save_dashboard(zip_dashboard=True)
    assert os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}/report_data.json')
    assert os.path.exists(f'{valid_output_directory}/{simple_dashboard.report_folder_name}.zip')


def test_serve_dashboard(simple_dashboard, mocker):
    simple_dashboard.create_dashboard()
    mocked_serve = mocker.patch('olliepy.Report.Report._serve_report_using_flask')

    def randint(a, b):
        return 33

    mocker.patch('random.randint', randint)

    simple_dashboard.serve_dashboard_from_local_server(port=8080)
    mocked_serve.assert_called_with(simple_dashboard._template_name, 'server', 8080, False)

    simple_dashboard.serve_dashboard_from_local_server()
    mocked_serve.assert_called_with(simple_dashboard._template_name, 'server', 33, False)
