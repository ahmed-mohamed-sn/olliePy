from typing import List, Dict, Tuple
from .Report import Report
import pandas as pd


# def check_attributes_type():

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
    test_error_column_name : str
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
        'PERFECT': (-0.5, 0.5), # return 'PERFECT' if -0.5 <= error < 0.5
        'OVER_ESTIMATING': (0.5, 3.0) # return 'OVER_ESTIMATING' if -0.5 <= error < 3.0
        }
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
    get_encryption_secret()
        Returns the encryption_secret

    """

    def __init__(self,
                 title: str,
                 output_directory: str,
                 train_df: pd.DataFrame,
                 test_df: pd.DataFrame,
                 target_feature_name: str,
                 test_error_column_name: str,
                 error_classes: Dict[str, Tuple],
                 numerical_features: List[str],
                 categorical_features: List[str],
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

        # check_attributes_type(train_df,
        #                       test_df,
        #                       target_feature_name,
        #                       test_error_column_name,
        #                       error_classes,
        #                       numerical_features,
        #                       categorical_features)
        self.train_df = train_df
        self.test_df = test_df
        self.target_feature_name = target_feature_name
        self.target_predictions = test_error_column_name
        self.error_classes = error_classes
        self.numerical_features = numerical_features
        self.categorical_features = categorical_features
