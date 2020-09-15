import pytest

from olliepy.Report import Report

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
        Report(title=title,
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               report_folder_name='TestReport')


@pytest.mark.parametrize("subtitle", [
    20,
    False
])
def test_invalid_subtitle(subtitle):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle=subtitle,
               report_folder_name='TestReport')


@pytest.mark.parametrize("output_directory", [
    ('fake_output'),
    ('./fake_output')
])
def test_invalid_output_directory(output_directory):
    with pytest.raises(NotADirectoryError):
        Report(title='Test report title',
               output_directory=output_directory,
               subtitle='Test report subtitle',
               report_folder_name='TestReport')


def test_none_output_directory():
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=None,
               subtitle='Test report subtitle',
               report_folder_name='TestReport')


@pytest.mark.parametrize("report_folder_name", [
    3,
    False
])
def test_invalid_report_folder_name(report_folder_name):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               report_folder_name=report_folder_name)


@pytest.mark.parametrize("encryption_secret", [
    3,
    False
])
def test_invalid_encryption_secret_type(encryption_secret):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               encryption_secret=encryption_secret)


@pytest.mark.parametrize("encryption_secret", [
    '123456789',
    'iusadiudhadiahdiadhadihadihdasdsaddasdasd',
    ''
])
def test_invalid_encryption_secret_value(encryption_secret):
    with pytest.raises(AttributeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               encryption_secret=encryption_secret)


@pytest.mark.parametrize("generate_encryption_secret", [
    3,
    'False'
])
def test_invalid_generate_encryption_secret_type(generate_encryption_secret):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               generate_encryption_secret=generate_encryption_secret)


def test_valid_generate_encryption_secret_type():
    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    generate_encryption_secret=True)

    assert len(report.encryption_secret) == 16
    assert type(report.encryption_secret) is str


@pytest.mark.parametrize("title,output_directory,subtitle,report_folder_name,encryption_secret", [
    ('title_1', valid_output_directory, None, None, None),
    ('title_2', valid_output_directory, 'subtitle_2', 'report_folder', None),
    ('title_3', valid_output_directory, 'subtitle_3', 'report_folder', '1234567891012345'),
])
def test_valid_report(title,
                      output_directory,
                      subtitle,
                      report_folder_name,
                      encryption_secret):
    report = Report(title=title,
                    output_directory=output_directory,
                    subtitle=subtitle,
                    report_folder_name=report_folder_name,
                    encryption_secret=encryption_secret)

    assert report.title == title
    assert report.output_directory == output_directory
    assert report.subtitle == subtitle
    assert report.report_folder_name == report_folder_name
    assert report.encryption_secret == encryption_secret


def test_update_report():
    test_report_dict = {'test_report': {'a': 1, 'b': 2}}
    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    report_folder_name='TestReport')
    report._update_report(test_report_dict)

    assert test_report_dict == report.report_data['report']


def test_save_report():
    import os

    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    report_folder_name='TestReport')

    report_path = f'{valid_output_directory}/{report.report_folder_name}'
    if os.path.exists(report_path):
        delete_directory(report_path)
        os.remove(f'{report_path}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=False)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert not os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=True)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')


def test_encrypted_save_report():
    import os

    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    report_folder_name='EncryptedTestReport',
                    generate_encryption_secret=True)

    report_path = f'{valid_output_directory}/{report.report_folder_name}'
    if os.path.exists(report_path):
        delete_directory(report_path)
        os.remove(f'{report_path}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=False)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert not os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=True)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')


def test_serve_report(mocker):
    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    report_folder_name='EncryptedTestReport',
                    generate_encryption_secret=True)

    mocked_create_report_directory = mocker.patch('olliepy.Report.Report._create_report_directory')
    mocked_save_report_data = mocker.patch('olliepy.Report.Report._save_report_data')
    mocked_copy_application_template = mocker.patch('olliepy.Report._copy_application_template')
    mocked_start_server_and_view_report = mocker.patch('olliepy.Report._start_server_and_view_report')

    report._serve_report_using_flask('regression-error-analysis-report', mode='serve', port=8080)
    mocked_create_report_directory.assert_called_once()
    mocked_copy_application_template.assert_called_once()
    mocked_save_report_data.assert_called_once()
    mocked_start_server_and_view_report.assert_called_once()

def test_serve_report_using_different_modes(mocker):
    report = Report(title='Test report title',
                    output_directory=valid_output_directory,
                    subtitle='Test report subtitle',
                    report_folder_name='EncryptedTestReport',
                    generate_encryption_secret=True)

    mocked_create_report_directory = mocker.patch('olliepy.Report.Report._create_report_directory')
    mocked_save_report_data = mocker.patch('olliepy.Report.Report._save_report_data')
    mocked_copy_application_template = mocker.patch('olliepy.Report._copy_application_template')
    mocked_spec_from_file_location = mocker.patch('importlib.util.spec_from_file_location')
    mocked_module_from_spec = mocker.patch('importlib.util.module_from_spec')
    mocked_webbrowser_open = mocker.patch('webbrowser.open')
    mocked_ipython_display = mocker.patch('IPython.core.display.display')
    mocked_ipython_IFrame = mocker.patch('IPython.display.IFrame')

    report._serve_report_using_flask('regression-error-analysis-report', mode='server', port=8080)
    mocked_create_report_directory.assert_called_once()
    mocked_copy_application_template.assert_called_once()
    mocked_save_report_data.assert_called_once()
    mocked_spec_from_file_location.assert_called_once()
    mocked_module_from_spec.assert_called_once()
    mocked_webbrowser_open.assert_called_once()

    report._serve_report_using_flask('regression-error-analysis-report', mode='js', port=8080)
    mocked_ipython_display.assert_called_once()

    report._serve_report_using_flask('regression-error-analysis-report', mode='jupyter', port=8080)
    mocked_ipython_IFrame.assert_called_once()
