import pandas as pd
import numpy as np 
from warnings import simplefilter

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
data: pd.DataFrame = pd.read_excel('Sunnova_Production_2023.xlsx', sheet_name=1)
monthly_expected_prodcution: pd.DataFrame = pd.read_excel('Sunnova_Production_2023.xlsx', sheet_name=2)
data = data.drop_duplicates(subset='Meter Serial Number', keep=False)
data.loc[data["System Size (kW)"] < 2.0, "System Size (kW)"] = 2.0

data_date_range: pd.DatetimeIndex = pd.date_range(start='2016-01-01', end='2016-12-31')
daily_production_dataframe: pd.DataFrame = data[data_date_range]
data[daily_production_dataframe < 0.0] = 0.0

daily_production_dataframe = data[data_date_range]
for x in range(1, 12):
    monthly_production: pd.DataFrame = daily_production_dataframe[data_date_range[data_date_range.month == x]]
    average_daily_production: float = (monthly_expected_prodcution.iloc[(x - 1), 1] / len(monthly_production.columns))
    data[data_date_range[data_date_range.month == x]] = monthly_production.fillna(average_daily_production)

for x in data.index.tolist():
    for y in range(1, 13):
        column_name: str = 'Month_' + str(y) + '_total'
        month_sum: float = data[data_date_range[data_date_range.month == y]].loc[x].sum()
        data.loc[x, column_name] = month_sum

with pd.ExcelWriter('Sunnova_Programming_Test_Edson_Gamma.xlsx', datetime_format="YYYY-MM-DD HH:MM:SS", date_format="YYYY-MM-DD HH:MM:SS") as writer:
    data.to_excel(writer, sheet_name='Data')
    monthly_expected_prodcution.to_excel(writer, sheet_name='Monthly Expected Production')
