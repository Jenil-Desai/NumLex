def c_to_f(celsius: float) -> float:
    fahrenheit = ((celsius * 1.8) + 32)
    return round(fahrenheit,2)

def f_to_c(fahrenheit: float) -> float:
    celsius = ((fahrenheit - 32) / 1.8)
    return round(celsius,2)

def c_to_k(celsius: float) -> float:
    kelvin = (celsius + 273.15)
    return round(kelvin,2)

def k_to_c(kelvin: float) -> float:
    celsius = (kelvin - 273.15)
    return round(celsius,2)

def f_to_k(fahrenheit: float) -> float:
    kelvin = ((fahrenheit - 32) * (5/9) + 273.15)
    return round(kelvin,2)

def k_to_f(kelvin: float) -> float:
    fahrenheit = ((kelvin - 273.15) * (9/5) + 32)
    return round(fahrenheit,2)