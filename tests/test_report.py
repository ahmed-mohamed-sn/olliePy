import pytest

from olliepy.Report import Report

valid_output_directory = './tests/output'


def delete_directory(directory):
    import shutil
    shutil.rmtree(directory)


@pytest.mark.parametrize("title", [
    (None),
    (20),
    (False)
])
def test_invalid_title(title):
    with pytest.raises(TypeError):
        Report(title=title,
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               report_folder_name='TestReport')


@pytest.mark.parametrize("subtitle", [
    (20),
    (False)
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
    (3),
    (False)
])
def test_invalid_report_folder_name(report_folder_name):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               report_folder_name=report_folder_name)


@pytest.mark.parametrize("encryption_secret", [
    (3),
    (False)
])
def test_invalid_encryption_secret_type(encryption_secret):
    with pytest.raises(TypeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               encryption_secret=encryption_secret)


@pytest.mark.parametrize("encryption_secret", [
    ('123456789'),
    ('iusadiudhadiahdiadhadihadihdasdsaddasdasd'),
    ('')
])
def test_invalid_encryption_secret_value(encryption_secret):
    with pytest.raises(AttributeError):
        Report(title='Test report title',
               output_directory=valid_output_directory,
               subtitle='Test report subtitle',
               encryption_secret=encryption_secret)


@pytest.mark.parametrize("generate_encryption_secret", [
    (3),
    ('False')
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

    if os.path.exists(f'{valid_output_directory}/{report.report_folder_name}'):
        delete_directory(f'{valid_output_directory}/{report.report_folder_name}')
        os.remove(f'{valid_output_directory}/{report.report_folder_name}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=False)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert not os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')

    report._save_the_report('regression-error-analysis-report', zip_report=True)
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}/report_data.json')
    assert os.path.exists(f'{valid_output_directory}/{report.report_folder_name}.zip')
