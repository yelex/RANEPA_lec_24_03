import pandas as pd
from utilities.utils import Singleton

class BaseData(Singleton):
    def __init__(self):
        self.path_to_filled_df = r'~/PycharmProjects/ane_django/parsed_content/filled.csv'
        self.path_to_gks_basket = r'~/Downloads/data.xls'
    
    def get_filled_df(self, path=None):
        if not path:
            path = self.path_to_filled_df
        return pd.read_csv(path, index_col='id').drop(columns='level_0')