import numpy as np
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])
average_temp = np.mean(temperatures)
print(f"The average temperature is {average_temp}")

highest_temp = np.max(temperatures)
print(f"The Maximum temperature is {highest_temp}")

lowest_temp = np.min(temperatures)
print(f"The minimum temperature is {lowest_temp}")

F= temperatures*9/5 +32
print(F)
above_20 = np.where(temperatures>20)[0]
print(f"the temperature above 20 degree celcius are: {above_20}")
