#%% PACKAGES IMPORTATION

import numpy as np
from cryopy.material import plot_single,plot_multiple
import types

#%% MATERIAL DEFINITION
material = 'Copper OFHC'


#%% FUNCTION DEFINITION - PROPERTIES
def molar_mass() -> float:
    """
    Returns the molar mass of XXX.

    Returns:
    --------
    float
        The molar mass in kg/mol.
    """
    return 63.546e-3  # kg/mol


def molar_volume(temperature: float) -> float:
    """
    Computes the molar volume of XXX.

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).

    Returns:
    --------
    float
        The molar volume in cubic meters per mole (m³/mol).

    Raises:
    -------
    ValueError
        If the temperature is out of the valid range for `density()`, 
        or if `density(temperature)` returns zero to prevent division by zero.
    """
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    try:
        rho = density(temperature)
        if rho <= 0:
            raise ValueError(f"Density must be positive, got {rho} kg/m³ at {temperature}K.")
        
        return molar_mass() / rho

    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")


def specific_heat(temperature: float, unit: str) -> float:
    """
    Computes the specific heat of XXX in either 'mol' or 'kg' units.

    Valid temperature range: 3K to 300K.

    Reference:
    https://trc.nist.gov/cryogenics/materials/OFHC%20Copper/OFHC_Copper_rev1.htm

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).
        Must be within the range [4, 300].

    unit : str
        The unit of specific heat, either 'mol' or 'kg'.

    Returns:
    --------
    float
        The specific heat in either [J/(mol·K)] or [J/(kg·K)], depending on the unit.

    Raises:
    -------
    ValueError
        If the temperature is out of range.
        If the unit is not 'mol' or 'kg'.
    TypeError
        If the temperature is not a number.
    """
    # Validate input
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    if not (3 <= temperature <= 300):
        raise ValueError(f"Temperature {temperature}K is out of the valid range [3, 300]K.")
    
    if unit not in {"mol", "kg"}:
        raise ValueError(f"Invalid unit '{unit}'. Expected 'mol' or 'kg'.")

    # Polynomial coefficients for log10(T)
    coefficients = np.array([
        -1.91844, -0.15973, 8.61013, -18.996, 21.9661,
        -12.7328, 3.54322, -0.3797, 0])

    # Compute specific heat using log10(T)
    log_temp = np.log10(temperature)
    specific_heat_value = 10**np.polyval(coefficients[::-1], log_temp)

    if unit == 'kg':
        return specific_heat_value
    else:
        return specific_heat_value/molar_mass()
    


def thermal_conductivity(temperature: float,RRR = 50, source: str = 'MARQUARDT') -> float:
    """
    Computes the thermal conductivity of XXX.

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).

    RRR : int
        The Resistivity Residual Ratio, must be 
        
    source : str, optional (default: 'MARQUARDT')
        The data origin, can be 'MARQUARDT', 'BARUCCI', or 'SAUVAGE'.

    Returns:
    --------
    float
        The thermal conductivity in W/(m·K).

    Raises:
    -------
    ValueError
        If the temperature is out of range for the selected source.
        If the source is not one of the valid options.
    TypeError
        If the temperature is not a number.
    """

    # Validate input type
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    if source == 'MARQUARDT':
        if not (4 <= temperature <= 300):
            raise ValueError(f"Temperature {temperature}K is out of the valid range [4, 300]K for MARQUARDT.")

        # Polynomial coefficients for log10(T)
        coefficients = np.array([0.07918, 1.0967, -0.07277, 0.08084, 0.02803, 
                                 -0.09464, 0.04179, -0.00571])

        log_temp = np.log10(temperature)
        conductivity_log = np.polyval(coefficients[::-1], log_temp)

        return 10 ** conductivity_log  # Convert from log scale

    elif source == 'BARUCCI':
        if not (4.2 <= temperature <= 70):
            raise ValueError(f"Temperature {temperature}K is out of the valid range [4.2, 70]K for BARUCCI.")

        return temperature / (0.445 + 4.9e-7 * temperature ** 3)

    elif source == 'SAUVAGE':
        if not (0.095 <= temperature <= 20):
            raise ValueError(f"Temperature {temperature}K is out of the valid range [0.095, 20]K for SAUVAGE.")

        # Chebyshev polynomial coefficients for ln(T)
        coefficients = np.array([
            2.39703410e-01, 1.88576787e+00, -4.39839595e-01, 9.53687043e-02,
            2.05443158e-03, -2.89908152e-03, -1.33420775e-04, 1.14453429e-04,
            -8.72830666e-06
        ])

        log_temp = np.log(temperature)
        conductivity_ln = np.polynomial.chebyshev.chebval(log_temp, coefficients)

        return np.exp(conductivity_ln)

    else:
        raise ValueError(f"Invalid source '{source}'. Expected 'MARQUARDT', 'BARUCCI', or 'SAUVAGE'.")




def linear_thermal_expansion(temperature: float) -> float:
    """
    Computes the linear thermal expansion of XXX.

    Valid temperature range: 4K to 300K.

    Reference:
    https://trc.nist.gov/cryogenics/materials/304LStainless/304LStainless_rev.htm

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).
        Must be within the range [4, 300].

    Returns:
    --------
    float
        The linear thermal expansion (unitless).

    Raises:
    -------
    ValueError
        If the temperature is out of range.
    TypeError
        If the temperature is not a number.
    """
    # Validate input
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    if not (4 <= temperature <= 300):
        raise ValueError(f"Temperature {temperature}K is out of the valid range [4, 300]K.")

    # Polynomial coefficients for temperature^i
    coefficients = np.array([-4.1277e2, -3.0389e-1, 8.7696e-3, -9.9821e-6, 0])

    # Compute linear thermal expansion using Horner's method for efficiency
    expansion = np.polyval(coefficients[::-1], temperature)

    return expansion * 1e-5


def young_modulus(temperature: float) -> float:
    """
    Computes the Young's modulus of XXX.

    Valid temperature range: 0K to 295K.

    Reference:
    https://trc.nist.gov/cryogenics/materials/5083%20Aluminum/5083Aluminum_rev.htm

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).
        Must be within the range [0, 295].

    Returns:
    --------
    float
        The Young's modulus in Pascals (Pa).

    Raises:
    -------
    ValueError
        If the temperature is out of range.
    TypeError
        If the temperature is not a number.
    """
    # Validate input type
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    # Validate temperature range
    if not (0 <= temperature <= 295):
        raise ValueError(f"Temperature {temperature}K is out of the valid range [0, 295]K.")

    # Polynomial coefficients for Young's modulus calculation
    coefficients = np.array([7.771221e1, 1.030646e-2, -2.924100e-4, 
                             8.993600e-7, -1.070900e-9])

    # Compute Young's modulus using polynomial expansion
    result = np.polyval(coefficients[::-1], temperature)

    return result * 1e9  # Convert to Pascals (Pa)


def density(temperature: float) -> float:
    """
    Computes the density of XXX as a function of temperature.

    The density is calculated using the inverse cubic relation with the linear thermal expansion.

    Parameters:
    -----------
    temperature : float
        The temperature of the material in Kelvin (K).

    Returns:
    --------
    float
        The density in kg/m³.

    Raises:
    -------
    ValueError
        If the temperature is out of the valid range for `linear_thermal_expansion()`.
    TypeError
        If the temperature is not a number.
    """
    # Validate input type
    if not isinstance(temperature, (int, float)):
        raise TypeError(f"Temperature must be a number, got {type(temperature).__name__}")

    # Try to calculate the expansion coefficient
    try:
        expansion_coefficient = (linear_thermal_expansion(temperature) + 1) ** 3
    except ValueError as e:
        raise ValueError(f"Failed to calculate expansion coefficient for temperature {temperature}K. {e}")

    # Reference density at 293K in kg/m³
    density_293K = 2701

    # Calculate and return the density
    return density_293K / expansion_coefficient  # Inverse relation due to expansion


    
#%% FUNCTION DEFINITION - PLOTS

def plot_molar_volume(grid: bool = True, xscale: str = 'linear', yscale: str = 'linear') -> None:
    """
    Plots the molar volume of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x = np.arange(4,300,0.1)
    ARRAY_y = [molar_volume(temperature) for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Molar volume [m$^{3}$.mol$^{-1}$]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Molar volume of {material} against the temperature')
    
def plot_thermal_conductivity(grid: bool = True, xscale: str = 'log', yscale: str = 'log') -> None:
    
    """
    Plots the thermal conductivity of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x_1 = np.arange(4,300,0.1)
    ARRAY_y_1 = [thermal_conductivity(temperature,'MARQUARDT') for temperature in ARRAY_x_1]
    
    ARRAY_x_2 = np.arange(4.2,70,0.1)
    ARRAY_y_2 = [thermal_conductivity(temperature,'BARUCCI') for temperature in ARRAY_x_2]
    
    ARRAY_x_3 = np.arange(0.095,20,0.01)
    ARRAY_y_3 = [thermal_conductivity(temperature,'SAUVAGE') for temperature in ARRAY_x_3]
    
    plot_multiple(ARRAY_ARRAY_x = [ARRAY_x_1,ARRAY_x_2,ARRAY_x_3],
         ARRAY_ARRAY_y = [ARRAY_y_1,ARRAY_y_2,ARRAY_y_3],
         ARRAY_label=['Marquardt et al.','Barucci et al.','Sauvage et al.'],
         xlabel = 'Temperature [K]',
         ylabel = r'Thermal conductivity [W.m$^{-1}$.K$^{-1}$]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Thermal conductivity of {material} against the temperature')


def plot_specific_heat(grid: bool = True, xscale: str = 'linear', yscale: str = 'linear') -> None:
    """
    Plots the specific heat of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x = np.arange(4,300,0.1)
    ARRAY_y = [specific_heat(temperature,'kg') for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Specific heat [J.kg$^{-1}$.K$^{-1}$]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Specific heat of {material} against the temperature')
    
    ARRAY_y = [specific_heat(temperature,'mol') for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Specific heat [J.mol$^{-1}$.K$^{-1}$]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Specific heat of {material} against the temperature')
    

def plot_linear_thermal_expansion(grid: bool = True, xscale: str = 'linear', yscale: str = 'linear') -> None:
    
    """
    Plots the linear thermal expansion of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x = np.arange(4,300,0.1)
    ARRAY_y = [linear_thermal_expansion(temperature) for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Linear thermal expansion [1]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Linear thermal expansion of {material} against the temperature')
    
    


def plot_young_modulus(grid: bool = True, xscale: str = 'linear', yscale: str = 'linear') -> None:
    """
    Plots the Young modulus of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x= np.arange(0,295,0.1)
    ARRAY_y = [young_modulus(temperature) for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Young modulus [Pa]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Young modulus of {material} against the temperature')


def plot_density(grid: bool = True, xscale: str = 'linear', yscale: str = 'linear') -> None:
    """
    Plots the density of XXX as a function of temperature.

    Parameters:
    -----------
    grid : bool, optional
        Whether to display a grid on the plot (default is True).

    xscale : str, optional
        Scale type for the x-axis ('linear' or 'log', default is 'linear').

    yscale : str, optional
        Scale type for the y-axis ('linear' or 'log', default is 'linear').

    Returns:
    --------
    None
        Displays the  plot.
    """
    
    ARRAY_x= np.arange(4,300,0.1)
    ARRAY_y = [density(temperature) for temperature in ARRAY_x]
    
    plot_single(ARRAY_x = ARRAY_x,
         ARRAY_y = ARRAY_y,
         xlabel = 'Temperature [K]',
         ylabel = r'Density [kg.m$^{-3}$]',
         grid = grid,
         xscale = xscale,
         yscale = yscale,
         title = f'Density of {material} against the temperature')




def plot_all():
    """ 
    Plots all the properties of XXX.
    
    """ 
    ARRAY_list_functions_plot = [function for function in ARRAY_list_functions if function.startswith('plot')]
    ARRAY_list_functions_plot.remove('plot_all')
    
    for function in ARRAY_list_functions_plot:
        globals()[function]()
    
    
#%% DOCTRING REDEFINITION

ARRAY_list_functions = [
    name for name, obj in globals().items()
    if isinstance(obj, types.FunctionType) and obj.__module__ == "__main__"
]

for function in ARRAY_list_functions:
    globals()[function].__doc__ = globals()[function].__doc__.replace("XXX", f'{material}')
    
