import csv
import numpy as np
import matplotlib.pyplot as plt
import warnings
from scipy.optimize import curve_fit

#suppress warnings
warnings.filterwarnings('ignore')

# Define the monoexponential function
def monoexp(x, A, tau, C):
    return A * np.exp(-x / tau) + C

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    content_raw = list(reader)


content = list(zip(*content_raw))
content[0] = list(content[0])
content[0] = [float(x)-float(content[0][0]) for x in content[0]]

x_data = content[0]



for i, column in enumerate(content[1:]):

    plt.figure()
    y_data = column

    # Initial guess for the parameters (A, tau, C)
    initial_guess = [1, 1, 1]

    # Perform the curve-fit
    params, params_covariance = curve_fit(monoexp, x_data, y_data, p0=initial_guess)

    y_data = [float(y) for y in y_data]
    y_fit  = [monoexp(x, *params) for x in x_data]

    residuals = [i - j for i,j in zip(y_data, y_fit)]
    std_dev = np.std(residuals)
    err = np.sqrt(np.diag(params_covariance))

    # params[0] = A, params[1] = tau, params[2] = C
    if content[0][-1]/100 < params[1] < content[0][-1]/1.5:
        print(f"{params[1]}")    

        # plt.plot(x_data, y_data, 'ko')
        # plt.plot(x_data, y_fit, 'r-')
        # plt.savefig(f"plt{i+1}.jpg")
        # plt.close


