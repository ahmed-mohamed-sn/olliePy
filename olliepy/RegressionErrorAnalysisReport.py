from typing import List, Dict, Tuple
from .Report import Report
import pandas as pd
from .utils.TypeChecking import is_instance
from scipy.spatial.distance import cosine
from scipy.stats import ks_2samp, wasserstein_distance
from itertools import product
from sklearn.preprocessing import LabelEncoder
import time

def validate_attributes(train_df, test_df, target_feature_name, error_column_name,
                        error_classes, acceptable_error_class, numerical_features, categorical_features):
    if type(train_df) is not pd.DataFrame:
        raise TypeError(f'provided train_df is not valid. train_df has to be a pandas dataframe')

    if type(test_df) is not pd.DataFrame:
        raise TypeError(f'provided test_df is not valid. test_df has to be a pandas dataframe')

    train_columns = train_df.columns.to_list()
    test_columns = test_df.columns.to_list()

    if type(target_feature_name) is not str:
        raise TypeError(f'''provided target_feature_name is not valid.
                            \ntarget_feature_name ({target_feature_name}) has to be a str''')

    if target_feature_name not in train_columns:
        raise TypeError(f'provided target_feature_name ({target_feature_name}) is not train_df')

    if target_feature_name not in test_columns:
        raise TypeError(f'provided target_feature_name ({target_feature_name}) is not test_df')

    if type(error_column_name) is not str:
        raise TypeError(f'''provided error_column_name is not valid.
                            \ntest_error_column_name ({error_column_name}) has to be a str''')

    if error_column_name not in train_columns:
        raise TypeError(f'provided error_column_name ({error_column_name}) is not train_df')

    if error_column_name not in test_columns:
        raise TypeError(f'provided error_column_name ({error_column_name}) is not test_df')

    if not is_instance(error_classes, Dict[str, Tuple[float, float]]):
        raise TypeError(
            f'provided error_classes is not valid. error_classes has to be a Dict[str, Tuple[float, float]]')

    if acceptable_error_class is not None and type(acceptable_error_class) is not str:
        raise TypeError(f'''provided acceptable_error_class is not valid.
                            \nacceptable_error_class ({acceptable_error_class}) has to be a str or None''')

    if acceptable_error_class is not None and acceptable_error_class not in error_classes:
        raise TypeError(f'''provided acceptable_error_class is not valid.
                            \n{acceptable_error_class} has to be defined in error_classes''')

    if numerical_features is None and categorical_features is None:
        raise AttributeError(f'''both numerical_features and categorical_features are not defined.
                                \nyou need to provide one of them or both in order to proceed.''')

    if numerical_features is not None and not is_instance(numerical_features, List[str]):
        raise TypeError(f'provided numerical_features is not valid. numerical_features has to be a List[str]')

    if categorical_features is not None and not is_instance(categorical_features, List[str]):
        raise TypeError(f'provided categorical_features is not valid. categorical_features has to be a List[str]')


def _cosine_similarity(vector_a, vector_b):
    return 1.0 - cosine(vector_a, vector_b)


class RegressionErrorAnalysisReport(Report):
    """
    RegressionErrorAnalysisReport creates a report that analyzes the error in regression problems.

    Attributes
    ----------
    title : str
        the title of the report
    output_directory : str
        the directory where the report folder will be created
    train_df : pd.DataFrame
        the training pandas dataframe of the regression problem which should include the target feature
    test_df : pd.DataFrame
        the testing pandas dataframe of the regression problem which should include the target feature
        and the error column in order to calculate the error class
    target_feature_name : str
        the name of the regression target feature
    error_column_name : str
        the name of the calculated error column 'Prediction - Target' (see example on github for more information)
    error_classes : Dict[str, Tuple]
        a dictionary containing the definition of the error classes that will be created.
        The key is the error_class name and the value is the minimum (inclusive) and maximum (exclusive)
        which will be used to calculate the error_class of the test observations. For example:
        error_classes = {
        'EXTREME_UNDER_ESTIMATION': (-8.0, -4.0), # return 'EXTREME_UNDER_ESTIMATION' if -8.0 <= error < -4.0
        'HIGH_UNDER_ESTIMATION': (-4.0, -3.0), # return 'HIGH_UNDER_ESTIMATION' if -4.0 <= error < -3.0
        'MEDIUM_UNDER_ESTIMATION': (-3.0, -1.0), # return 'MEDIUM_UNDER_ESTIMATION' if -3.0 <= error < -1.0
        'LOW_UNDER_ESTIMATION': (-1.0, -0.5), # return 'LOW_UNDER_ESTIMATION' if -1.0 <= error < -0.5
        'ACCEPTABLE': (-0.5, 0.5), # return 'ACCEPTABLE' if -0.5 <= error < 0.5
        'OVER_ESTIMATING': (0.5, 3.0) # return 'OVER_ESTIMATING' if -0.5 <= error < 3.0
        }
    acceptable_error_class: str
        the name of the acceptable error class that was defined in error_classes
    numerical_features : List[str] default=None
        a list of the numerical features to be included in the report
    categorical_features : List[str] default=None
        a list of the categorical features to be included in the report
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
    create_report()
        creates the error analysis report

    """

    def __init__(self,
                 title: str,
                 output_directory: str,
                 train_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 target_feature_name: str,
                 error_column_name: str,
                 error_classes: Dict[str, Tuple[float, float]],
                 acceptable_error_class: str,
                 numerical_features: List[str] = None,
                 categorical_features: List[str] = None,
                 subtitle: str = None,
                 report_folder_name: str = None,
                 encryption_secret: str = None,
                 generate_encryption_secret: bool = False):
        super().__init__(title,
                         output_directory,
                         subtitle,
                         report_folder_name,
                         encryption_secret,
                         generate_encryption_secret)

        validate_attributes(train_df,
                            test_df,
                            target_feature_name,
                            error_column_name,
                            error_classes,
                            acceptable_error_class,
                            numerical_features,
                            categorical_features)

        self.train_df = train_df.copy()
        self.test_df = test_df.copy()
        self.target_feature_name = target_feature_name
        self.error_column_name = error_column_name
        self.error_classes = error_classes
        self.acceptable_error_class = acceptable_error_class
        self.numerical_features = numerical_features
        self.categorical_features = categorical_features
        self._training_data_name = 'Training data'
        self._testing_data_name = 'Testing data'
        self._error_class_col_name = 'ERROR_CLASS'
        self._primary_datasets = [self._training_data_name, self.acceptable_error_class]
        self._secondary_datasets = [self._testing_data_name]
        self._secondary_datasets.extend(list(self.error_classes.keys()))
        self._template_name = 'regression-error-analysis-report'
        self._default_numerical_bins_for_grouping = 10

    def create_report(self) -> None:
        """
        Creates a report using the user defined data and the data calculated based on the error.

        :return: None
        """
        tic = time.perf_counter()
        cosine_similarity_threshold: float = 0.8

        self._add_user_defined_data()
        self._add_error_class_to_test_df()
        self._add_datasets()
        self._add_statistical_tests(cosine_similarity_threshold)

        if self.categorical_features is not None and len(self.categorical_features) > 0:
            self._add_categorical_count_plot()

        self._add_parallel_coordinates_plot(cosine_similarity_threshold)
        self._find_and_add_all_secondary_datasets_patterns()
        toc = time.perf_counter()

        print(f"The report was created in {toc - tic:0.4f} seconds")

        if self.encryption_secret:
            print(f'Your encryption secret is {self.encryption_secret}')

    def _add_user_defined_data(self) -> None:
        """
        Adds user defined data to the report.

        :return: None
        """

        self._update_report({'primaryDatasets': self._primary_datasets})

        self._update_report({'secondaryDatasets': self._secondary_datasets})

        if self.numerical_features:
            self.numerical_features.append(self.target_feature_name)
            self._update_report({'numericalFeatures': self.numerical_features})

        if self.categorical_features:
            self._update_report({'categoricalFeatures': self.categorical_features})

        self._update_report({'targetFeature': self.target_feature_name})

    def _add_error_class_to_test_df(self) -> None:
        """
        adds the error class to each observation in the test set (test_df) based on the
        error classes provided by the user.

        :return: None
        """

        def add_error_class(error: float) -> str:
            for error_class, min_max in self.error_classes.items():
                minimum, maximum = min_max

                if minimum <= error < maximum:
                    return error_class

            return 'UNDEFINED_ERROR_CLASS'

        self.test_df[self._error_class_col_name] = self.test_df[self.error_column_name].apply(add_error_class)

    def _add_datasets(self) -> None:
        """
        Adds datasets to reports (info, stats, numerical data).

        :return: None
        """

        datasets_dict = {}

        def add_dataset(df: pd.DataFrame, dataset_name: str) -> None:
            """
            Adds a dataset stats and data to the datasets_dict.

            :param df: pd.DataFrame, the selected dataset dataframe
            :param dataset_name: str, the dataset name
            :return: None
            """
            stats = {}
            data = {}

            if self.numerical_features is not None and len(self.numerical_features) > 0:
                for feature in self.numerical_features:
                    stats[feature] = {
                        'min': df.loc[:, feature].min(),
                        'mean': df.loc[:, feature].mean(),
                        'std': df.loc[:, feature].std(),
                        'median': df.loc[:, feature].median(),
                        'max': df.loc[:, feature].max(),
                        'count': int(df.loc[:, feature].count()),
                        'missingCount': int(df.loc[:, feature].isna().sum()),
                    }
                    data[feature] = df.loc[:, feature].values.tolist()

            if self.categorical_features is not None and len(self.categorical_features) > 0:
                for feature in self.categorical_features:
                    stats[feature] = {
                        'uniqueCount': int(df.loc[:, feature].nunique()),
                        'missingCount': int(df.loc[:, feature].isna().sum())
                    }

            dataset_dict = {dataset_name: {
                'info': {
                    'name': dataset_name,
                    'numberOfRows': df.shape[0],
                    'minError': df.loc[:, self.error_column_name].min(),
                    'meanError': df.loc[:, self.error_column_name].mean(),
                    'stdError': df.loc[:, self.error_column_name].std(),
                    'medianError': df.loc[:, self.error_column_name].median(),
                    'maxError': df.loc[:, self.error_column_name].max(),
                    'errors': df.loc[:, self.error_column_name].tolist(),
                    'stats': stats
                },
                'data': data
            }}

            datasets_dict.update(dataset_dict)

        add_dataset(self.train_df, self._training_data_name)
        add_dataset(self.test_df, self._testing_data_name)

        for error_class_name in self.error_classes.keys():
            selected_df = self.test_df.loc[self.test_df[self._error_class_col_name] == error_class_name, :]
            add_dataset(selected_df, error_class_name)

        self._update_report({'datasets': datasets_dict})

    def _count_categories_and_merge_count_dataframes(self, feature_name: str, primary_dataset: str,
                                                     secondary_dataset: str,
                                                     normalize=False) -> pd.DataFrame:
        """
        It counts the different categories (of the provided feature) for the primary and secondary dataset then merge
        the count dataframes into a single dataframe that contains all the categories.
        It also fills missing values with 0.

        :param feature_name: the feature name
        :param primary_dataset: the primary dataset name
        :param secondary_dataset: the secondary dataset name
        :param normalize: whether to normalizr the categorical count, default:False
        :return: the merged dataframe
        """
        if primary_dataset == self._training_data_name:
            primary_count_df = self.train_df.loc[:, feature_name].value_counts(normalize=normalize)
        else:
            primary_count_df = self.test_df.loc[
                self.test_df[self._error_class_col_name] == primary_dataset, feature_name].value_counts(
                normalize=normalize)
        if secondary_dataset == self._testing_data_name:
            secondary_count_df = self.test_df.loc[:, feature_name].value_counts(normalize=normalize)
        else:
            secondary_count_df = self.test_df.loc[
                self.test_df[self._error_class_col_name] == secondary_dataset, feature_name].value_counts(
                normalize=normalize)

        primary_count_df = primary_count_df.reset_index()\
            .rename({feature_name: primary_dataset, 'index': feature_name}, axis=1)
        secondary_count_df = secondary_count_df.reset_index()\
            .rename({feature_name: secondary_dataset, 'index': feature_name}, axis=1)
        merged_cat_count = primary_count_df.merge(secondary_count_df, on=feature_name, how='outer').fillna(
            0).sort_values(by=primary_dataset, ascending=False)

        return merged_cat_count

    def _add_categorical_count_plot(self) -> None:
        """
        Add the categorical count plots (stacked bar plot) data to the report
        :return: None
        """

        def add_categorical_count_data(feature_dictionary: Dict, feature_name: str, primary_dataset: str,
                                       secondary_dataset: str) -> None:
            """
            Calculate the value counts for each dataset and for that particular categorical feature.
            Then groups the value_counts() dataframes afterwards it computes the data needed for the stacked bar plot
            in plotly.

            :param feature_dictionary: the feature dictionary that will be added the categorical count plot data
            :param feature_name: the feature name
            :param primary_dataset: the primary dataset name
            :param secondary_dataset: the secondary dataset name
            :return: None
            """
            merged_cat_count = self._count_categories_and_merge_count_dataframes(feature_name,
                                                                                 primary_dataset,
                                                                                 secondary_dataset,
                                                                                 normalize=False)

            key = f'{primary_dataset}_{secondary_dataset}'
            title = f'{primary_dataset} vs {secondary_dataset}'
            categories = merged_cat_count.loc[:, feature_name].tolist()
            primary_data = merged_cat_count.loc[:, primary_dataset].tolist()
            secondary_data = merged_cat_count.loc[:, secondary_dataset].tolist()
            feature_dictionary.update({key: {
                'title': title,
                'categories': categories,
                'series': [
                    {
                        'name': primary_dataset,
                        'color': '#8180FF',
                        'data': primary_data
                    },
                    {
                        'name': secondary_dataset,
                        'color': '#FF938D',
                        'data': secondary_data
                    }
                ]
            }})

        categorical_count_dict = {}
        for feature in self.categorical_features:
            feature_dict = {}
            for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets,
                                                                        self._secondary_datasets):
                if primary_dataset_name != secondary_dataset_name:
                    add_categorical_count_data(feature_dict, feature, primary_dataset_name, secondary_dataset_name)
                    categorical_count_dict.update({feature: feature_dict})

        self._update_report({'categorical_count_plots': categorical_count_dict})

    def _get_primary_secondary_datasets(self, primary_dataset: str, secondary_dataset: str) -> Tuple[
        pd.DataFrame, pd.DataFrame]:
        """
        Finds the correct primary and secondary datasets and return them.

        :param primary_dataset: the name of the primary dataset
        :param secondary_dataset: the name of the secondary dataset
        :return: primary_df, secondary_df
        """
        if primary_dataset == self._training_data_name:
            primary_df = self.train_df.copy()
            primary_df.loc[:, self._error_class_col_name] = self._training_data_name
        else:
            primary_df = self.test_df.loc[self.test_df[self._error_class_col_name] == primary_dataset, :].copy()

        if secondary_dataset == self._testing_data_name:
            secondary_df = self.test_df.copy()
            secondary_df.loc[:, self._error_class_col_name] = self._testing_data_name
        else:
            secondary_df = self.test_df.loc[self.test_df[self._error_class_col_name] == secondary_dataset, :].copy()
        return primary_df, secondary_df

    def _add_parallel_coordinates_plot(self, cosine_similarity_threshold) -> None:
        """
        Check for suitable features (numerical based on quantiles(default: 0.25, 0.75)
        and categorical based on cosine similarity).
        Afterwards it adds the needed data for the plotly parallel coordinates plot.

        :param cosine_similarity_threshold: the cosine similarity threshold for the categorical features
        :return: None
        """

        def add_parallel_coordinates(parallel_coordinates_dictionary: Dict, primary_dataset: str,
                                     secondary_dataset: str) -> None:
            """
            Decides which features will be added to the parallel coordinates plot based on predefined thresholds.
            Then prepares the data that is expected by the plotly parallel coordinates plot.

            :param parallel_coordinates_dictionary: the parallel coordinates data dictionary
            :param primary_dataset: the name of the primary dataset
            :param secondary_dataset: the name of the secondary dataset
            :return: None
            """
            selected_features = []

            first_quantile_threshold = 0.25
            second_quantile_threshold = 0.75

            primary_df, secondary_df = self._get_primary_secondary_datasets(primary_dataset, secondary_dataset)

            if self.categorical_features is not None:
                for categorical_feature in self.categorical_features:
                    merged_cat_count = self._count_categories_and_merge_count_dataframes(categorical_feature,
                                                                                         primary_dataset,
                                                                                         secondary_dataset,
                                                                                         normalize=True)
                    primary_vector = merged_cat_count.loc[:, primary_dataset].tolist()
                    secondary_vector = merged_cat_count.loc[:, secondary_dataset].tolist()
                    cosine_similarity = _cosine_similarity(primary_vector, secondary_vector)

                    if cosine_similarity < cosine_similarity_threshold:
                        selected_features.append(categorical_feature)

            if self.numerical_features is not None:
                for numerical_feature in self.numerical_features:
                    primary_q_1 = primary_df.loc[:, numerical_feature].quantile(first_quantile_threshold)
                    primary_q_2 = primary_df.loc[:, numerical_feature].quantile(second_quantile_threshold)
                    secondary_q_1 = secondary_df.loc[:, numerical_feature].quantile(first_quantile_threshold)
                    secondary_q_2 = secondary_df.loc[:, numerical_feature].quantile(second_quantile_threshold)
                    if primary_q_1 >= secondary_q_2 or secondary_q_1 >= primary_q_2:
                        selected_features.append(numerical_feature)

            if len(selected_features) > 0:
                key = f'{primary_dataset}_{secondary_dataset}'
                combined_df = pd.concat([primary_df, secondary_df], axis=0).copy()
                colors = combined_df.loc[:, self._error_class_col_name].apply(
                    lambda error_class: 0 if error_class == primary_dataset else 1).tolist()
                dimensions = []
                for feature in selected_features:
                    if self.numerical_features is not None and feature in self.numerical_features:
                        feature_min = combined_df.loc[:, feature].min()
                        feature_max = combined_df.loc[:, feature].max()
                        dimensions.append({
                            'range': [feature_min, feature_max],
                            'label': feature,
                            'values': combined_df.loc[:, feature].tolist()
                        })
                    elif self.categorical_features is not None and feature in self.categorical_features:
                        label_encoder = LabelEncoder()
                        values = label_encoder.fit_transform(combined_df.loc[:, feature])
                        values_range = [int(values.min()), int(values.max())]
                        tick_values = label_encoder.transform(label_encoder.classes_).tolist()
                        tick_text = label_encoder.classes_.tolist()
                        dimensions.append({
                            'range': values_range,
                            'label': feature,
                            'values': values.tolist(),
                            'tickvals': tick_values,
                            'ticktext': tick_text
                        })

                if len(dimensions) > 1:
                    parallel_coordinates_dictionary.update({key: {
                        'primaryDatasetName': primary_dataset,
                        'secondaryDatasetName': secondary_dataset,
                        'colors': colors,
                        'dimensions': dimensions
                    }})

        parallel_coordinates_dict = {}
        for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets, self._secondary_datasets):
            if primary_dataset_name != secondary_dataset_name:
                add_parallel_coordinates(parallel_coordinates_dict, primary_dataset_name, secondary_dataset_name)

        if len(parallel_coordinates_dict) > 0:
            self._update_report({'parallel_coordinates': parallel_coordinates_dict})

    def _add_statistical_tests(self, cosine_similarity_threshold) -> None:
        """
        Calculates and adds statistical tests to the report data.

        :param cosine_similarity_threshold: the cosine similarity threshold for the categorical features
        :return: None
        """

        def add_statistical_test(statistical_tests_dictionary: Dict, primary_dataset: str,
                                 secondary_dataset: str) -> None:
            """
            Calculates statistical tests (ks_2samp) and metrics (wasserstein distance, cosine similarity)
            then adds the results to the dictionary.

            :param statistical_tests_dictionary: the statistical tests data dictionary
            :param primary_dataset: the name of the primary data set
            :param secondary_dataset: the name of the secondary data set
            :return: None
            """

            primary_df, secondary_df = self._get_primary_secondary_datasets(primary_dataset, secondary_dataset)
            key = f'{primary_dataset}_{secondary_dataset}'
            tests_dictionary = {key: {}}
            p_value_threshold = 0.01

            if self.numerical_features is not None:
                for numerical_feature in self.numerical_features:
                    primary_values = primary_df.loc[:, numerical_feature].values
                    secondary_values = secondary_df.loc[:, numerical_feature].values
                    p_value = ks_2samp(primary_values, secondary_values)[1]
                    wasser_distance = wasserstein_distance(secondary_values, primary_values)
                    tests_dictionary[key].update({
                        numerical_feature: {
                            'ks_2samp': {
                                'p_value': p_value,
                                'p_value_threshold': p_value_threshold
                            },
                            'wasserstein_distance': wasser_distance
                        }
                    })

            if self.categorical_features is not None:
                for categorical_feature in self.categorical_features:
                    if primary_dataset != secondary_dataset:
                        merged_cat_count = self._count_categories_and_merge_count_dataframes(categorical_feature,
                                                                                             primary_dataset,
                                                                                             secondary_dataset,
                                                                                             normalize=True)
                        primary_vector = merged_cat_count.loc[:, primary_dataset].tolist()
                        secondary_vector = merged_cat_count.loc[:, secondary_dataset].tolist()
                        cosine_similarity = _cosine_similarity(primary_vector, secondary_vector)
                    else:
                        cosine_similarity = 1.0

                    tests_dictionary[key].update({
                        categorical_feature: {
                            'cosine_similarity': {
                                'cosine_similarity': cosine_similarity,
                                'cosine_similarity_threshold': cosine_similarity_threshold
                            }
                        }
                    })

            statistical_tests_dictionary.update(tests_dictionary)

        statistical_tests_dict = {}
        for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets, self._secondary_datasets):
            add_statistical_test(statistical_tests_dict, primary_dataset_name, secondary_dataset_name)

        self._update_report({'statistical_tests': statistical_tests_dict})

    def serve_report_from_local_server(self, mode: str = 'server', port: int = None) -> None:
        """
        Serve the report to the user using a web server.
        modes:
        1- 'server': will open a new tab in the default browser using webbrowser package
        2- 'js': will open a new tab in the default browser using IPython
        3- 'jupyter': will open the report in a jupyter notebook

        :param mode: server mode ('server': will open a new tab in your default browser,
        'js': will open a new tab in your browser using a different method, 'jupyter': will open the report application
        in your notebook).
        default: 'server'
        :param port: the server port. default: None. a random port will be generated between (1024-49151)
        :return: None
        """
        if not port:
            import random
            port = random.randint(1024, 49151)
        super()._serve_report_using_flask(self._template_name, mode, port)

    def save_report(self, zip_report: bool = False) -> None:
        """
        Creates the report directory, copies the web application based on the template name,
        saves the report data.

        :param zip_report: enable it in order to zip the directory for downloading. default: False
        :return: None
        """

        super()._save_the_report(self._template_name, zip_report)

    def _find_and_add_all_secondary_datasets_patterns(self) -> None:
        """
        Find all groups in secondary datasets and check if they exist in the primary datasets.
        Output the groups, error and target distributions and the distance between the distributions.

        :return: None
        """

        def query_datasets_for_count_error_target(primary_df, secondary_df, features_values):
            query_list = []
            for feature, feature_value in features_values:
                query_list.append(f'{feature} == "{feature_value}"')

            query = ' and '.join(query_list)
            filtered_primary_dataset = primary_df.query(query)
            filtered_secondary_dataset = secondary_df.query(query)

            output = {
                'primaryCount': filtered_primary_dataset.shape[0],
                'secondaryCount': filtered_secondary_dataset.shape[0],
                'secondaryErrorMean': filtered_secondary_dataset.loc[:, self.error_column_name].mean(),
                'secondaryErrorStd': filtered_secondary_dataset.loc[:, self.error_column_name].std(),
                'secondaryTargetMean': filtered_secondary_dataset.loc[:, self.target_feature_name].mean(),
                'secondaryTargetStd': filtered_secondary_dataset.loc[:, self.target_feature_name].std(),
                'primaryTargetValues': filtered_primary_dataset.loc[:, self.target_feature_name].tolist(),
                'secondaryTargetValues': filtered_secondary_dataset.loc[:, self.target_feature_name].tolist(),
                'primaryErrorValues': filtered_primary_dataset.loc[:, self.error_column_name].tolist(),
                'secondaryErrorValues': filtered_secondary_dataset.loc[:, self.error_column_name].tolist(),
                'primaryErrorMean': filtered_primary_dataset.loc[:, self.error_column_name].mean(),
                'primaryErrorStd': filtered_primary_dataset.loc[:, self.error_column_name].std(),
                'primaryTargetMean': filtered_primary_dataset.loc[:, self.target_feature_name].mean(),
                'primaryTargetStd': filtered_primary_dataset.loc[:, self.target_feature_name].std()
            }

            for dataset in ['primary', 'secondary']:
                if dataset == 'primary':
                    df = filtered_primary_dataset
                else:
                    df = filtered_secondary_dataset

                if output[f'{dataset}Count'] == 1:
                    output.update({
                        f'{dataset}ErrorMean': df.loc[:, self.error_column_name].values[0],
                        f'{dataset}ErrorStd': None,
                        f'{dataset}TargetMean': df.loc[:, self.target_feature_name].values[0],
                        f'{dataset}TargetStd': None,
                    })
                elif output[f'{dataset}Count'] == 0:
                    output.update({
                        f'{dataset}ErrorMean': None,
                        f'{dataset}ErrorStd': None,
                        f'{dataset}TargetMean': None,
                        f'{dataset}TargetStd': None,
                    })

            if output['primaryCount'] > 0 and output['secondaryCount'] > 0:
                output['errorWassersteinDistance'] = wasserstein_distance(
                    filtered_secondary_dataset.loc[:, self.error_column_name],
                    filtered_primary_dataset.loc[:, self.error_column_name])

                output['targetWassersteinDistance'] = wasserstein_distance(
                    filtered_secondary_dataset.loc[:, self.target_feature_name],
                    filtered_primary_dataset.loc[:, self.target_feature_name])
            else:
                output['errorWassersteinDistance'] = None
                output['targetWassersteinDistance'] = None

            return output

        def add_patterns(grouped_patterns_dictionary: Dict, primary_dataset: str,
                         secondary_dataset: str) -> None:
            """
            Group by all features in secondary_dataset and try to find these patterns in primary dataset.

            :param grouped_patterns_dictionary: the patterns data dictionary
            :param primary_dataset: the name of the primary data set
            :param secondary_dataset: the name of the secondary data set
            :return: None
            """

            primary_df, secondary_df = self._get_primary_secondary_datasets(primary_dataset, secondary_dataset)
            key = f'{primary_dataset}_{secondary_dataset}'
            patterns_dictionary = {}

            group_by_features = self.categorical_features[:]

            numerical_features = list(filter(lambda f_name: f_name != self.target_feature_name,
                                             self.numerical_features))

            for numerical_feature in numerical_features:
                binning_features_name = f'{numerical_feature}_BIN'

                secondary_df.loc[:, binning_features_name], bins = pd.cut(secondary_df.loc[:, numerical_feature],
                                                                          retbins=True, include_lowest=True,
                                                                          bins=self._default_numerical_bins_for_grouping)
                primary_df.loc[:, binning_features_name] = pd.cut(primary_df.loc[:, numerical_feature], bins=bins)

                primary_df = primary_df.dropna()
                primary_df.loc[:, binning_features_name] = primary_df.loc[:, binning_features_name].astype(str)
                secondary_df.loc[:, binning_features_name] = secondary_df.loc[:, binning_features_name].astype(str)
                group_by_features.append(binning_features_name)

            primary_df = primary_df.drop(numerical_features, axis=1)
            secondary_df = secondary_df.drop(numerical_features, axis=1)

            secondary_groupby_all_df = secondary_df.groupby(by=group_by_features).mean()
            secondary_all_groups = secondary_groupby_all_df.index.tolist()

            patterns_list = []
            for index, group in enumerate(secondary_all_groups):
                group_dict = {'name': f'Group {index}', 'features': {}}

                features_values = []
                for feature_index,  feature in enumerate(group_by_features):
                    group_dict['features'][feature] = group[feature_index]
                    features_values.append((feature, group[feature_index]))

                count_error_target_dict = query_datasets_for_count_error_target(primary_df,
                                                                                secondary_df,
                                                                                features_values)
                group_dict.update(count_error_target_dict)
                patterns_list.append(group_dict)

            patterns_dictionary[key] = patterns_list
            grouped_patterns_dictionary.update(patterns_dictionary)

        grouped_patterns_dict = {}
        for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets, self._secondary_datasets):
            add_patterns(grouped_patterns_dict, primary_dataset_name, secondary_dataset_name)

        self._update_report({'grouped_patterns': grouped_patterns_dict})
