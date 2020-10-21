import pandas as pd
from .Report import Report
from .utils.TypeChecking import is_instance
from typing import List
import time
import json
from pandas.api.types import is_datetime64_any_dtype as is_datetime


def validate_attributes(dataframes: List[pd.DataFrame],
                        dataframes_names: List[str],
                        numerical_columns: List[str],
                        categorical_columns: List[str],
                        date_columns: List[str]):
    if len(dataframes) == 0:
        raise AttributeError('You need to pass at least one pandas dataframe to create a dashboard.')

    if not is_instance(dataframes, List[pd.DataFrame]):
        raise TypeError('''one or more of the provided data_frames is not valid.
            Please make sure that you are passing a list of pandas dataframes''')

    if not is_instance(dataframes_names, List[str]):
        raise TypeError('''one or more of the provided data_frames_names is not valid.
        Please make sure that you are passing a list of strings for the data frames' names''')

    if len(dataframes) != len(dataframes_names):
        raise AttributeError('You need to have a dataframe name for each dataframe you have in dataframes')

    if len(categorical_columns + numerical_columns) == 0:
        raise AttributeError(
            'You need to pass categorical_columns and/or numerical_columns in order to create a dashboard.')

    for df, df_name in zip(dataframes, dataframes_names):
        df_columns = df.columns.tolist()
        for col in numerical_columns:
            if col not in df_columns:
                raise AttributeError(f'Numerical column: {col} is not found in {df_name} dataframe.')
        for col in categorical_columns:
            if col not in df_columns:
                raise AttributeError(f'Categorical column: {col} is not found in {df_name} dataframe.')
        for col in date_columns:
            if col not in df_columns:
                raise AttributeError(f'Date column: {col} is not found in {df_name} dataframe.')
            if not is_datetime(pd.to_datetime(df[col], infer_datetime_format=True, errors='ignore')):
                raise TypeError(
                    f'''Date column: {col} has one or more rows which are not a valid date format in {df_name} dataframe.
                        You can replace invalid values with None''')


class InteractiveDashboard(Report):
    """
    InteractiveDashboard creates an interactive dashboard that can be used for EDA or error analysis.

    Attributes
    ----------
    title : str
        the title of the report
    output_directory : str
        the directory where the dashboard folder will be created
    dataframes : List[pd.DataFrame]
    dataframes_names : List[str]
    numerical_columns : List[str] default=None
        a list of the numerical columns to be included in the dashboard
    categorical_columns : List[str] default=None
        a list of the categorical columns to be included in the dashboard
    date_columns : List[str] default=None
        a list of the date columns to be included in the dashboard
    report_folder_name : str default=None
        the name of the folder that will contain all the generated report files.
        If not set, the title of the report will be used.
    encryption_secret : str default=None
        the 16 characters secret that will be used to encrypt the generated report data.
        If it is not set, the generated data won't be encrypted.
    generate_encryption_secret : bool default=False
        the encryption_secret will be generated and its value returned as output.
        you can also view encryption_secret to get the generated secret.

    Methods
    -------
    create_dashboard()
        creates the dashboard
    serve_dashboard_from_local_server()
        serves the dashboard using a flask server
    save_dashboard()
        saves the dashboard to be used without a flask server.
    """

    def __init__(self,
                 title: str,
                 output_directory: str,
                 dataframes: List[pd.DataFrame],
                 dataframes_names: List[str],
                 numerical_columns: List[str] = None,
                 categorical_columns: List[str] = None,
                 date_columns: List[str] = None,
                 dashboard_folder_name: str = None,
                 encryption_secret: str = None,
                 generate_encryption_secret: bool = False):
        super().__init__(title,
                         output_directory,
                         '',
                         dashboard_folder_name,
                         encryption_secret,
                         generate_encryption_secret)

        validate_attributes(dataframes,
                            dataframes_names,
                            numerical_columns,
                            categorical_columns,
                            date_columns)

        self.dataframes = [df.copy() for df in dataframes]
        self.dataframes_names = dataframes_names[:]
        self.numerical_columns = numerical_columns[:]
        self.categorical_columns = categorical_columns[:]
        self.date_columns = date_columns[:]
        self._template_name = 'interactive-dashboard'
        self._generated_id_column = 'generated_id'

    def create_dashboard(self, auto_generate_distribution_plots: bool = False) -> None:
        """
        Creates a dashboard using the user defined data.

        :param auto_generate_distribution_plots: generate distribution plots and add them to the dashboard. default: False
        """

        # validate_create_dashboard_attributes(auto_generate_distribution_plots)

        # delete default report location created by parent class
        if 'report' in self.report_data:
            del self.report_data['report']

        tic = time.perf_counter()

        for df in self.dataframes:
            df[self._generated_id_column] = df.index
            for date_column in self.date_columns:
                df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True)

        self.numerical_columns = [self._generated_id_column] + self.numerical_columns
        self.report_data['datasets'] = self.dataframes_names
        self.report_data['numericalColumns'] = self.numerical_columns if self.numerical_columns else []
        self.report_data['categoricalColumns'] = self.categorical_columns if self.categorical_columns else []
        self.report_data['dateColumns'] = self.date_columns if self.date_columns else []

        for df, df_name in zip(self.dataframes, self.dataframes_names):
            self.report_data[df_name] = json.loads(df.to_json(orient='records'))

        if not auto_generate_distribution_plots:
            self.report_data['numberDisplays'] = []
            self.report_data['charts'] = []
        else:
            self.report_data['numberDisplays'] = self._generate_number_displays()
            self.report_data['charts'] = self._generate_charts()

        toc = time.perf_counter()

        print(f"The dashboard was created in {toc - tic:0.4f} seconds")

        if self.encryption_secret:
            print(f'Your encryption secret is {self.encryption_secret}')

    def _generate_number_displays(self) -> List[dict]:
        """
        generate number displays for the auto generate functionality
        :return: List[dict] the generated number displays
        """

        return [
            {
                'agg': 'count',
                'column': self._generated_id_column,
                'title': 'Number of observations',
                'type': 'number-display',
                'w': 12,
                'h': 1,
                'maxH': 2,
                'i': 0,
                'id': 'number_of_observations_number_display',
                'x': 0,
                'y': 0,
                'static':  False
            }
        ]

    def _generate_charts(self) -> List[dict]:
        """
        generate histograms for the auto generate functionality
        :return: List[dict] the generated charts
        """
        charts = []
        x = 0
        y = 0
        w = 4
        h = 2
        i = 0
        max_width = 12

        df = self.dataframes[0]

        for col in self.categorical_columns:
            n_unique = df[col].nunique()
            if n_unique > 2:
                charts.append({
                    'dimension': col,
                    'agg': 'count',
                    'column': self._generated_id_column,
                    'title': f'{col} count',
                    'type': 'row-chart',
                    'cap': 10,
                    'w': w,
                    'h': h,
                    'minW': 2,
                    'minH': 2,
                    'i': i,
                    'id': f'chart_{i}',
                    'x': x,
                    'y': y,
                    'static':  False
                })
            else:
                charts.append({
                    'id': f'chart_{i}',
                    'title': f'{col}',
                    'type': 'pie-chart',
                    'dimension': col,
                    'x': x,
                    'y': y,
                    'w': w,
                    'h': h,
                    'i': i,
                    'minW': 2,
                    'minH': 2,
                    'static': False
                })

            i += 1
            x += w
            if (x + w) > max_width:
                x = 0
                y += h

        for col in self.numerical_columns:
            if col != self._generated_id_column:
                bin_width = (df[col].max() - df[col].min())/100
                charts.append({
                    'dimension': col,
                    'title': f'{col} histogram',
                    'xAxisLabel': col,
                    'yAxisLabel': 'Frequency',
                    'binWidth': bin_width,
                    'type': 'histogram-chart',
                    'w': w,
                    'h': h,
                    'minW': 2,
                    'minH': 2,
                    'i': i,
                    'id': f'chart_{i}',
                    'x': x,
                    'y': y,
                    'static':  False
                })

                i += 1
                x += w
                if (x + w) > max_width:
                    x = 0
                    y += h

        return charts

    def serve_dashboard_from_local_server(self, mode: str = 'server', port: int = None) -> None:
        """
        Serve the dashboard to the user using a web server.
        Available modes:
                - 'server': will open a new tab in the default browser using webbrowser package
                - 'js': will open a new tab in the default browser using IPython
                - 'jupyter': will open the dashboard in a jupyter notebook

        :param mode: the selected web server mode. default: 'server'
        :param port: the server port. default: None. a random port will be generated between (1024-49151)
        :return: None
        """
        if not port:
            import random
            port = random.randint(1024, 49151)
        super()._serve_report_using_flask(self._template_name, mode, port)

    def save_dashboard(self, zip_dashboard: bool = False) -> None:
        """
        Creates the dashboard directory, copies the web application based on the template name,
        saves the dashboard data.

        :param zip_dashboard: enable it in order to zip the directory for downloading. default: False
        :return: None
        """

        super()._save_the_report(self._template_name, zip_dashboard)
