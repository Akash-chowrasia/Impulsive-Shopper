def number_parser(data):
    num = data.split("Price:")[-1]
    number = num.split("Rs.")[-1]
    return int(number)

def list_finder(list_element):
    price_list = []
    for price in list_element:
        data = price.text
        price_list.append(number_parser(data))
    return price_list
