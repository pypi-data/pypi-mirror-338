"""
This file contains the reasoning behind the sizing method when the field is limited by injection (i.e. cooling)
and there is a non-constant ground temperature. This is based on the assumption that the difference between the
maximum peak temperature in injection and the average, undistrubed ground temperature scales like 1/borehole length.

This can be understood since the main contributor to the peak temperature is the peak load, which, in the sizing,
is expressed as a load per meter (W/m), so it scales like 1/borehole length.
"""

from GHEtool import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def validate():
    ground_data = GroundFluxTemperature(3, 10)
    fluid_data = FluidData(0.2, 0.568, 998, 4180, 1e-3)
    pipe_data = DoubleUTube(1, 0.015, 0.02, 0.4, 0.05)
    borefield = Borefield()
    borefield.create_rectangular_borefield(5, 4, 6, 6, 110, 4, 0.075)
    borefield.set_ground_parameters(ground_data)
    borefield.set_fluid_parameters(fluid_data)
    borefield.set_pipe_parameters(pipe_data)
    borefield.calculation_setup(use_constant_Rb=False)
    borefield.set_max_avg_fluid_temperature(17)
    borefield.set_min_avg_fluid_temperature(3)
    hourly_load = HourlyGeothermalLoad()
    hourly_load.load_hourly_profile(FOLDER.joinpath("test\methods\hourly_data\\auditorium.csv"), header=True,
                                    separator=";",
                                    col_injection=0, col_extraction=1)
    borefield.load = hourly_load

    # initiate lists
    Tg_list = []
    max_Tf_list = []
    length_list = range(20, 450, 20)

    for length in length_list:
        print(f'The current borehole length is {length} m.')
        borefield.calculate_temperatures(length)
        Tg_list.append(
            borefield.ground_data.calculate_Tg(length + borefield.D, borefield.D))  # assume vertical boreholes
        max_Tf_list.append(np.max(borefield.results.peak_injection))

    def f(x, a, b):
        return a / x + b

    # determine temperature difference between peak cooling temperature and ground temperature
    diff = np.array(max_Tf_list) - np.array(Tg_list)

    # fit to curve
    popt, pcov = curve_fit(f, length_list, diff)
    print(popt, pcov)

    plt.figure()
    plt.plot(length_list, Tg_list, label='Ground')
    plt.plot(length_list, max_Tf_list, label='Fluid')
    plt.hlines(borefield.Tf_max, 0, length_list[-1], label='Maximum temperature limit')
    plt.xlabel('Borehole length [m]')
    plt.ylabel('Temperature [deg C]')
    plt.legend()
    # plt.show()

    plt.figure()
    plt.plot(length_list, diff, label='Actual calculated difference')
    plt.plot(length_list, f(np.array(length_list), *popt), label='Fitted difference')
    plt.xlabel('Borehole length [m]')
    plt.ylabel('Temperature difference [deg C]')
    plt.title(
        'Temperature difference between maximum peak cooling fluid\ntemperature and undistrubed ground temperature')
    plt.legend()
    plt.show()


if __name__ == "__main__":  # pragma: no cover
    validate()
