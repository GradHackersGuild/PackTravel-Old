import pandas as pd
import numpy as np
from sklearn.linear_model import LassoCV
import warnings
import pickle
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
warnings.filterwarnings('ignore')

filepath = os.path.join(BASE_DIR, 'data')
df_cabs = pd.read_csv(filepath+r"/cab_rides.csv")
df_cabs['time_stamp'] = df_cabs['time_stamp'].astype(str).str[:-3].astype(np.int64)
df_cabs.dropna(inplace=True)

cab_company = pd.get_dummies(df_cabs.cab_type)
cab_company.columns = ['LyftCabs', 'UberCabs']
df_cabs = pd.concat([df_cabs, cab_company], axis=1)

cab_type = pd.get_dummies(df_cabs.name)
df_cabs = pd.concat([df_cabs, cab_type], axis=1)

df_cabs['time_stamp'] = pd.to_datetime(df_cabs['time_stamp'], unit='s')
df_cabs['timePeriodCategory'] = df_cabs.time_stamp.apply(lambda date: "EarlyMorning" if 3 <= date.hour <= 6 else "MorningNoon" if 6 < date.hour <= 17 else "Night" if 17 < date.hour <= 22 else "LateNight")
time_period = pd.get_dummies(df_cabs.timePeriodCategory)
df_cabs = pd.concat([df_cabs, time_period], axis=1)

df_cabs['weekend'] = df_cabs['time_stamp'].dt.day_name().isin(['Saturday', 'Sunday']).astype(int)
df_cabs['weekday'] = df_cabs.weekend.astype(bool).apply(lambda x: 0 if x == 1 else 1)

df_cabs.drop(['destination', 'surge_multiplier', 'source', 'id', 'time_stamp', 'cab_type', 'product_id', 'timePeriodCategory', 'name'], axis=1, inplace=True)

X = df_cabs.loc[:, df_cabs.columns != 'price']
y = pd.DataFrame(df_cabs['price'])

def lassoRegCV(x_train, y_train):
    """
    Lasso regression model to predict cab prices.
    Other models such as Linear Reg., Lasso Reg., KNN Reg. and Random forest Reg. explored and tested as well. 
    Performed different hyperparameter tuning for the models as well and data transformation such as normalizing data. 
    Selected Lasso regression as final model based on testing error rates.
    """
    model_lassocv_ret = LassoCV(alphas=None, cv=10, max_iter=100000)
    model_lassocv_ret.fit(x_train, y_train)
    return model_lassocv_ret

save_model_path = str(BASE_DIR) + "/cab_model/model.pkl"
model_lassocv = lassoRegCV(X.to_numpy(), y.to_numpy())
with open(save_model_path, "wb") as f:
    pickle.dump(model_lassocv, f)
