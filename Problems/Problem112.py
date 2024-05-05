import numpy as np
import sys
sys.path.append(r".\\")

from Services.NumberAnalysis import is_number_bouncy


ratio = 0.0
number_of_bouncies = 0
i = 0
while ratio != 99:
    i += 1
    if is_number_bouncy(i):
        number_of_bouncies += 1
        ratio = np.round(np.floor((number_of_bouncies/i)*100))
    

print(i)