from functions.func import cm_to_inch, \
                           inch_to_cm, \
                           km_to_miles, \
                           miles_to_km, \
                           pound_to_kg, \
                           kg_to_pound, \
                           oz_to_gr, \
                           gr_to_oz, \
                           gallon_to_liter, \
                           liter_to_gallon, \
                           pint_to_liter, \
                           liter_to_pint


while True:
    print(
    """
    Сделайте выбор для конвертации
    1<->2: см <-> дюймы; 3<->4: км <-> мили; 5<->6: футы <-> кг, 7<->8: унции <-> граммы;
    9<->10: галлоны <-> литры; 11<->12: амер.пинты <-> литры; 0 - выход.
    """
        )
    try:
        select = int(input('Please enter number convertation from 0 to 12: '))
    except ValueError:
        print("Incorrect input. Try again.")
    finally:
        print(45 * '#')
    if select == 0:
        break
    elif 0 < select < 13:
        try:
            x = float(input("Enter value of the seleted quantity: "))
        except ValueError:
            print('You input is no digit!!!! Try again')
        finally:
            print(45 * '#')
        converter_dict = {
            1: cm_to_inch,
            2: inch_to_cm,
            3: km_to_miles,
            4: miles_to_km,
            5: pound_to_kg,
            6: kg_to_pound,
            7: oz_to_gr,
            8: gr_to_oz,
            9: gallon_to_liter,
            10: liter_to_gallon,
            11: pint_to_liter,
            12: liter_to_pint,
        }
        result = converter_dict[select](x)
        print(f'value of the convertible quantity: {result}')
    else:
        print("Incorrect input!")
        print("Please select number 0-12")
        continue
