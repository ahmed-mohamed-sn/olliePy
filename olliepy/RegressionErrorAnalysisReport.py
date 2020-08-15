from typing import List, Dict, Tuple
from .Report import Report
import pandas as pd
from .utils.TypeChecking import is_instance


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
        a dictionary containing the definition of the error classes that will be created. The key is the error_class name
        and the value is the minimum (inclusive) and maximum (exclusive) which will be used to calculate the error_class
        of the test observations. For example:
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

    def create_report(self) -> None:
        """
        Creates a report using the user defined data and the data calculated based on the error
        :return: None
        """

        self._add_user_defined_data()
        self._add_error_class_to_test_df()
        self._add_datasets()

        if self.categorical_features is not None and len(self.categorical_features) > 0:
            self._add_categorical_count_plot()

        self._add_parallel_coordinates_plot()

    def _add_user_defined_data(self) -> None:
        """
        Adds user defined data to the report
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
        error classes provided by the user
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
        Adds datasets to reports (info, stats, numerical data)
        :return: None
        """

        datasets_dict = {}

        def add_dataset(df: pd.DataFrame, dataset_name: str) -> None:
            """
            Adds a dataset stats and data to the datasets_dict
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

    def _add_categorical_count_plot(self) -> None:
        """
        Add the categorical count plots (stacked bar plot) data to the report
        :return: None
        """

        def add_categorical_count_data(feature_dictionary: Dict, feature_name: str, primary_dataset: str,
                                       secondary_dataset: str) -> None:
            """
            Calculate the value counts for each dataset and for that particular categorical feature.
            Then groups the value_counts() dataframes afterwards it computes the data needed for the stacked bar plot in plotly

            :param feature_dictionary: the feature dictionary that will be added the categorical count plot data
            :param feature_name: the feature name
            :param primary_dataset: the primary dataset name
            :param secondary_dataset: the secondary dataset name
            :return: None
            """
            if primary_dataset == self._training_data_name:
                primary_count_df = self.train_df.loc[:, [feature_name]].value_counts()
            else:
                primary_count_df = self.test_df.loc[
                    self.test_df[self._error_class_col_name] == primary_dataset, [feature_name]].value_counts()

            if secondary_dataset == self._testing_data_name:
                secondary_count_df = self.test_df.loc[:, [feature_name]].value_counts()
            else:
                secondary_count_df = self.test_df.loc[
                    self.test_df[self._error_class_col_name] == secondary_dataset, [feature_name]].value_counts()

            primary_count_df = primary_count_df.reset_index().rename({0: primary_dataset}, axis=1)
            secondary_count_df = secondary_count_df.reset_index().rename({0: secondary_dataset}, axis=1)
            merged_cat_count = primary_count_df.merge(secondary_count_df, on=feature_name, how='outer').fillna(
                0).sort_values(by=feature_name)

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

        from itertools import product
        categorical_count_dict = {}

        for feature in self.categorical_features:
            feature_dict = {}
            for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets,
                                                                        self._secondary_datasets):
                if primary_dataset_name != secondary_dataset_name:
                    add_categorical_count_data(feature_dict, feature, primary_dataset_name, secondary_dataset_name)
                    categorical_count_dict.update({feature: feature_dict})

        self._update_report({'categorical_count_plots': categorical_count_dict})

    def _add_parallel_coordinates_plot(self) -> None:
        """
        Check for suitable features (numerical based on quantiles(default: 0.25, 0.75)
        and categorical based on cosine similarity). Afterwards it adds the needed data for the plotly parallel coordinates plot
        :return: None
        """

        def add_parallel_coordinates(parallel_coordinates_dictionary: Dict, primary_dataset: str,
                                     secondary_dataset: str):
            from sklearn.preprocessing import LabelEncoder

            selected_features = []
            if self.categorical_features is not None and len(self.categorical_features) > 0:
                selected_features.extend(
                    self.categorical_features)  # will be replaced by cosine similarity based selection

            q_threshold_1 = 0.25
            q_threshold_2 = 0.75

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

            if self.numerical_features is not None:
                for numerical_feature in self.numerical_features:
                    primary_q_1 = primary_df.loc[:, numerical_feature].quantile(q_threshold_1)
                    primary_q_2 = primary_df.loc[:, numerical_feature].quantile(q_threshold_2)
                    secondary_q_1 = secondary_df.loc[:, numerical_feature].quantile(q_threshold_1)
                    secondary_q_2 = secondary_df.loc[:, numerical_feature].quantile(q_threshold_2)
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
                        'colors': colors,
                        'dimensions': dimensions
                    }})

        from itertools import product
        parallel_coordinates_dict = {}
        for primary_dataset_name, secondary_dataset_name in product(self._primary_datasets, self._secondary_datasets):
            if primary_dataset_name != secondary_dataset_name:
                add_parallel_coordinates(parallel_coordinates_dict, primary_dataset_name, secondary_dataset_name)

        if len(parallel_coordinates_dict) > 0:
            self._update_report({'parallel_coordinates': parallel_coordinates_dict})
