from os import path
from typing import Dict
import os
from pathlib import Path
from distutils.dir_util import copy_tree
import json


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


def _copy_application_template(template_name: str, destination_path: str) -> None:
    package_path = str(Path(os.path.dirname(os.path.abspath(__file__))).parent)
    source_path = path.join(package_path, f'reports-templates/{template_name}')

    copy_tree(source_path, destination_path)


def _zip_directory(path: str, zip_handler):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_handler.write(os.path.join(root, file))


def _start_server_and_view_report(report_directory: str, mode: str, port: int) -> None:
    """
    Serve the report to the user using a web server.

    :param report_directory: The directory created report is saved
    :param mode: server mode ('server': will open a new tab in your default browser,
    'js': will open a new tab in your browser using a different method, 'jupyter': will open the report application
    in your notebook).
    default: 'server'
    :param port: the server port. default: random between (1024-49151)
    :return: None
    """
    print('''\n\n ### \nServing the report this way, might not work on all machine.
Try different server mode ('server', 'js' or 'jupyter') or save and download the report and open index.html \n###\n\n''')
    print('Clear your browser\'s cache if your report was not updated\n\n')
    import multiprocessing as mp
    import time
    import importlib.util
    spec = importlib.util.spec_from_file_location("app", f'{report_directory}/app.py')
    app = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(app)
    try:
        p = mp.Process(target=app.run_application, args=(port, report_directory))
        p.start()
        time.sleep(1.0)
        url = f'http://127.0.0.1:{port}/'
        if mode == 'server':
            import webbrowser
            webbrowser.open(url)
        elif mode == 'js':
            from IPython.core.display import display
            from IPython.display import Javascript
            display(Javascript('window.open("{url}");'.format(url=url)))
        else:
            from IPython.display import IFrame
            from IPython.core.display import display
            display(IFrame('http://127.0.0.1:5000/', '100%', '800px'))
        p.join()
    except (KeyboardInterrupt, SystemExit):
        print('\n! Received keyboard interrupt, stopping server.\n')
    pass


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

    def _serve_report_using_flask(self, template_name: str, mode: str, port: int) -> None:
        """
        Creates the report directory, copies the web application based on the template name,
        saves the report data and starts the flask server.

        :param template_name: the name of the report's template
        :param mode: the server mode
        :param port: the server port
        :return: None
        """
        report_directory = self._create_report_directory()
        _copy_application_template(template_name, report_directory)
        self._save_report_data(report_directory)
        _start_server_and_view_report(report_directory, mode, port)

    def _save_the_report(self, template_name: str, zip_report: bool) -> None:
        """
        Creates the report directory, copies the web application based on the template name,
        saves the report data.

        :param template_name: the name of the report's template
        :return: None
        """
        report_directory = self._create_report_directory()
        _copy_application_template(template_name, report_directory)
        self._save_report_data(report_directory)

        if zip_report:
            self._zip_report_directory(report_directory)

        print(f'''The report has been saved.
To view the report, go to the report's directory ({report_directory}) and open index.html then upload report_data.json.
To zip the report directory, set zip_report=True when saving.''')

    def _create_report_directory(self) -> str:
        """
        Creates the report directory if it doesn't exist.

        :return: report_directory
        """
        report_folder = self.report_folder_name if self.report_folder_name else self.title
        report_directory = path.join(self.output_directory, report_folder)
        if not os.path.exists(report_directory):
            os.mkdir(report_directory)

        return report_directory

    def _save_report_data(self, report_directory: str) -> None:
        """
        Takes the report_directory and saves the data as json there.

        :param report_directory:
        :return: None
        """
        if self.encryption_secret:
            data = self._encrypt_report_data()
            with open(path.join(report_directory, 'report_data.json'), 'wb') as file:
                file.write(data)
                file.close()
        else:
            data = self.report_data
            with open(path.join(report_directory, 'report_data.json'), 'w') as file_path:
                json.dump(data, file_path)

    def _zip_report_directory(self, report_directory: str) -> None:
        import shutil
        report_folder = self.report_folder_name if self.report_folder_name else self.title
        shutil.make_archive(f'{self.output_directory}/{report_folder}', 'zip', report_directory)

    def _encrypt_report_data(self):
        from Crypto import Random
        from Crypto.Cipher import AES
        import base64
        BLOCK_SIZE = 16

        def pad(data):
            length = 16 - (len(data) % 16)
            return data.decode("utf-8") + chr(length) * length

        def encrypt(message, passphrase):
            IV = Random.new().read(BLOCK_SIZE)
            aes = AES.new(passphrase, AES.MODE_CFB, IV, segment_size=128)
            return base64.b64encode(IV + aes.encrypt(pad(message).encode("utf-8")))

        key = self.encryption_secret.encode('utf-8')
        encoded_data = json.dumps(self.report_data).encode('utf-8')

        encrypted_data = encrypt(encoded_data, key)

        return encrypted_data
