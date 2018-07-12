from pygal_maps_world.i18n import COUNTRIES


# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """returns pygal 2-symbols code from passed country name """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # if string isn't found returns None
        else:
            continue

# print(get_country_code('Andorra'))
# print(get_country_code('Zimbabwe'))