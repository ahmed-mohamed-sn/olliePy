from os import path
from typing import Dict


def validate_attributes(title, output_directory, subtitle, report_folder_name, encryption_secret,
                        generate_encryption_secret):
    if type(title) is not str:
        raise TypeError(f'provided title is not valid. title has to be a str')
    if type(output_directory) is not str:
        raise TypeError(f'provided output_directory is not valid. output_directory has to be a str')
    if not path.exists(output_directory):
        raise NotADirectoryError(f'provided output_directory is not valid. output_directory does not exist')
    if subtitle is not None and type(subtitle) is not str:
        raise TypeError(f'provided subtitle is not valid. subtitle has to be a str')
    if report_folder_name is not None and type(report_folder_name) is not str:
        raise TypeError(f'provided report_folder_name is not valid. report_folder_name has to be a str')
    if encryption_secret is not None and type(encryption_secret) is not str:
        raise TypeError(f'provided encryption_secret is not valid. encryption_secret has to be a str')
    if encryption_secret is not None and len(encryption_secret) != 16:
        raise TypeError(f'provided encryption_secret is not valid. encryption_secret has to be 16 characters')
    if type(generate_encryption_secret) is not bool:
        raise TypeError(f'provided generate_encryption_secret is not valid. encryption_secret has to be a bool')


def _generate_encryption_secret():
    import string
    import random
    length = 16
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class Report:
    """
    Report is the parent class of all the reports. It contains all the method for generating the reports
    and common attributes that all reports share.

    Attributes
    ----------
    title : str
        the title of the report
    output_directory : str
        the directory where the report folder will be created
    subtitle : str default=None
        an optional subtitle to describe your report
    report_folder_name : str default=None
        the name of the folder that will contain all the generated report files.
        If not set, the title of the report will be used.
    encryption_secret : str default=None
        the secret that will be used to encrypt the generated report data.
        If it is not set, the generated data won't be encrypted.
    generate_encryption_secret : bool default=False
        the encryption_secret will be generated and its value returned as output.
        you can also view encryption_secret to get the generated secret.

    Methods
    -------
    _update_report()
        updates the report dictionary inside the report_data dictionary

    """

    def __init__(self,
                 title: str,
                 output_directory: str,
                 subtitle: str = None,
                 report_folder_name: str = None,
                 encryption_secret: str = None,
                 generate_encryption_secret: bool = False) -> None:
        super().__init__()

        validate_attributes(title,
                            output_directory,
                            subtitle,
                            report_folder_name,
                            encryption_secret,
                            generate_encryption_secret)

        self.title = title
        self.output_directory = output_directory
        self.subtitle = subtitle
        self.report_folder_name = report_folder_name
        self.encryption_secret = encryption_secret
        self.generate_encryption_secret = generate_encryption_secret

        if self.encryption_secret is None and self.generate_encryption_secret:
            self.encryption_secret = _generate_encryption_secret()

        self.report_data = {'title': title}

        if subtitle:
            self.report_data['subtitle'] = subtitle

        self.report_data['report'] = {}

    def _update_report(self, data: Dict) -> None:
        """
        Updates the report dictionary in report_data
        :param data: Dict, the data dictionary that will be added to the report dictionary in report_data
        :return: None
        """
        self.report_data['report'].update(data)
