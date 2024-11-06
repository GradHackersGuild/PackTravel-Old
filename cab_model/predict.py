"""
MIT License

Copyright (c) 2022 Makarand Pundlik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

"""Module to contain functionality to predict cab price"""
from datetime import date
import pickle
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

class predict_price():
    """Class to contain functionality to predict cab price"""
    def __init__(self, distance, date_time_str):
        self.distance = distance
        self.date_time_str = date_time_str.split(" ")
        self.date = self.date_time_str[0]
        self.time = self.date_time_str[1]
        self.columns = ['distance', 'LyftCabs', 'UberCabs', 'Black', 'Black SUV', 'Lux', 'Lux Black', 'Lux Black XL', 'Lyft', 'Lyft XL', 'Shared', 'UberPool', 'UberX', 'UberXL', 'WAV', 'EarlyMorning', 'LateNight', 'MorningNoon', 'Night', 'weekend', 'weekday']

    def populateTimePeriod(self, to_pred_data):
        """This method sanitizes the format of time"""
        hour = [int(n) for n in self.time.split(":")][0]
        if 3 <= hour and hour <= 6 :
            to_pred_data['EarlyMorning'] = 1
        elif 6 < hour and hour <= 17 :
            to_pred_data['MorningNoon'] = 1
        elif 17 < hour and hour <= 22 :
            to_pred_data['Night'] = 1
        else :
            to_pred_data['LateNight'] = 1

        date_list = self.date.split("-")
        for i in range(len(date_list)):
            if date_list[i] != "":
                date_list[i] = int(date_list[i])
            else:
                date_list[i] = 0
        d = date(day=date_list[0], month=date_list[1], year=date_list[2]).strftime('%A')

        if d in ["Saturday", "Sunday"] :
            to_pred_data["weekend"] = 1
        else :
            to_pred_data["weekday"] = 1
        to_pred_data["weekend"] = 1

        return to_pred_data

    def dataframeFromDict(self, to_pred):
        """This method converts a dictionary to data frame"""
        new_data = pd.DataFrame(to_pred.items()).transpose()
        cols = new_data.iloc[0]
        new_data = new_data[1:]
        new_data.columns = cols
        return new_data


    def predictCabs(self, to_pred):
        """This method predicts cab price with input data"""
        path_to_model = str(BASE_DIR) + r"/cab_model/model.pkl"
        with open(path_to_model, 'rb') as f:
            lasso_trained_model = pickle.load(f)

        res1 = ""
        res2 = ""
        cabs = {
            "UberCabs" : ['UberPool', 'Black SUV'],
            "LyftCabs" : ['Shared', 'Lux Black XL']
        }
        price_range = []
        for each_cab_comp in cabs.keys():
            to_pred[each_cab_comp] = 1
            
            for eachCabType in cabs[each_cab_comp]:
                to_pred[eachCabType] = 1
                to_pred_df = self.dataframeFromDict(to_pred)
                price = lasso_trained_model.predict(to_pred_df.to_numpy())
                price_range.append(price)
                to_pred[eachCabType] = 0
            #res += f"For {each_cab_comp}, price ranges from ${round(price_range[0][0], 2)} to ${round(price_range[1][0], 2)}\n"
            to_pred[each_cab_comp] = 0
        res1 = "For Uber, price range is from: $"+str(round(price_range[0][0], 2))+" to: $"+str(round(price_range[1][0], 2))
        res2 = "For Lyft, price range is from: $"+str(round(price_range[2][0], 2))+" to: $"+str(round(price_range[3][0], 2))
        return res1, res2

    def createDataForPrice(self):
        """This method creates data to predict cab price"""
        to_pred = {}
        for each in self.columns:
            to_pred[each] = 0
        to_pred["distance"] = self.distance
        to_pred = self.populateTimePeriod(to_pred)
        return to_pred


    def generate_data_return_price(self):
        """This method returns estimate price"""
        data = self.createDataForPrice()
        price_str = self.predictCabs(data)
        return price_str
