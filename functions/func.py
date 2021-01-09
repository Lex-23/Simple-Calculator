"""Functions for simple calc"""


def cm_to_inch(x: int) -> str:
    """
    функция конвертирует сантиметры в дюймы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * .394
    return f'{round(y, 3)} inch'


def inch_to_cm(x: int) -> str:
    """
    функция конвертирует дюймы в сантиметры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 2.54
    return f'{round(y, 3)} cm'


def km_to_miles(x: int) -> str:
    """
    функция конвертирует килоиетры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * .621
    return f'{round(y, 3)} miles'


def miles_to_km(x: int) -> str:
    """
    функция конвертирует километры в мили (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 1.609
    return f'{round(y, 3)} km'


def pound_to_kg(x: int) -> str:
    """
    функция конвертирует фунты в килограммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * .454
    return f'{round(y, 3)} kg'


def kg_to_pound(x: int) -> str:
    """
    функция конвертирует килограммы в фунты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 2.205
    return f'{round(y, 3)} pound'


def oz_to_gr(x: int) -> str:
    """
    функция конвертирует унции в граммы (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 28.35
    return f'{round(y, 3)} gr'


def gr_to_oz(x: int) -> str:
    """
    функция конвертирует граммы в унции (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 0.0353
    return f'{round(y, 3)} oz'


def gallon_to_liter(x: int) -> str:
    """
    функция конвертирует галлоны в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    '"""
    y = x * 4.546
    return f'{round(y, 3)} l'


def liter_to_gallon(x: int) -> str:

    """
    функция конвертирует литры в галлоны (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 0.264
    return f'{round(y, 3)} gal'


def pint_to_liter(x: int) -> str:

    """
    функция конвертирует амер пинты в литры (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * .473
    return f'{round(y, 3)} l'


def liter_to_pint(x: int) -> str:
    """
    функция конвертирует литры в амер пинты (с округлением до пяти знаков после запятой)
    :param x: int
    :return y: float
    """

    y = x * 2.113
    return f'{round(y, 3)} pnt'
