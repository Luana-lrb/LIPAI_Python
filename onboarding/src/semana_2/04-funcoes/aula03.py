""" Aula 3 """

def world_cup_titles(country, *args):
    print('Country: ', country)
    for title in args:
        print('year: ', title)
        
world_cup_titles("Brasil", 1958, 1962, 1970, 1994, 2002)


def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount
    return value

preco = calculate_price(100, tax_percentage=10, discount=5)
print(preco)  

preco2 = calculate_price(100, tax_percentage=15)
print(preco2)  