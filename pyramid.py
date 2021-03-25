
""" 
command javascript

a=[]
document.addEventListener('mousedown', function(e) {a.push(e.screenX);console.log(a)})


"""

import json
import numpy as np
import pandas as pd

with open("input.json",) as file:
    data = json.load(file)


params={} 
values={}   
result={}  
total=np.zeros(len(data["legend"]))
   
for item in data["points"].keys():                      
    params[item] = {
                    "x0":data["points"][item][0],
                    "calibration": data["points"][item][-1]
                   }
    values[item] = data["points"][item][1:-1] 
 
    multiplicator = 1 if item==list(data["points"].keys())[-1] else -1
    values_in_pixels = np.array(multiplicator * ( params[item]['x0']- np.array(values[item])))
    calibration_factor = (multiplicator*(params[item]['x0']-params[item]['calibration'])) / data['calibration_point']
    result[item] = values_in_pixels/calibration_factor

    total +=result[item] 



pyramid_dataframe  = pd.DataFrame(
index=data["legend"],
data=total,
columns=['total']
)

pyramid_dataframe['total'] = pyramid_dataframe['total']* 100/pyramid_dataframe['total'].sum()
 


