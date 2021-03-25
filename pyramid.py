
import json
import numpy as np
import pandas as pd


#get the data
with open("input.json",) as file:
    data = json.load(file)


params={} 
values={}   
result={}  

total=np.zeros(len(data["legend"]))
   
for item in data["points"].keys():  

    #get the static parameters                    
    params[item] = {
                    "x0":data["points"][item][0],
                    "calibration": data["points"][item][-1]
                   }
    
    #remove static parameters
    values[item] = data["points"][item][1:-1] 
    
    #changes the operation if it refers to left or right
    multiplicator = 1 if item==list(data["points"].keys())[-1] else -1
    
    #number of pixels in the bar
    values_in_pixels = np.array(multiplicator * ( params[item]['x0']- np.array(values[item])))
    
    #calibration factor 
    calibration_factor = (multiplicator*(params[item]['x0']-params[item]['calibration'])) / data['calibration_point']
    
    #make the transformation from pixels to percent
    result[item] = values_in_pixels/calibration_factor

    #get total values
    total +=result[item] 


#create the dataframe
pyramid_dataframe  = pd.DataFrame(
index=data["legend"],
data=total,
columns=['total']
)

#treat rounding problems
pyramid_dataframe['total'] = pyramid_dataframe['total']* 100/pyramid_dataframe['total'].sum()
 


