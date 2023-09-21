from city_country import city_

def test_city_country():
    city_country_test = city_('Delhi', "India")
    assert city_country_test == "Delhi, India"
    