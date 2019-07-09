import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def get_biggest_bar(bars):
    biggest_bar = max(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return biggest_bar['properties']['Attributes']['Name']


def get_smallest_bar(bars):
    smallest_bar = min(bars['features'], key=lambda bar: bar['properties']['Attributes']['SeatsCount'])
    return smallest_bar['properties']['Attributes']['Name']


def get_closest_bar(bars, longitude, latitude):
    nearest_bar = min(bars['features'], key=lambda bar: (abs(bar['geometry']['coordinates'][0]-longitude),
                                                         abs(bar['geometry']['coordinates'][1]-latitude)))
    return nearest_bar['properties']['Attributes']['Name']


def main():
    bars = load_data('bars.json')
    print('Самый большой бар: {}'.format(get_biggest_bar(bars)))
    print('Самый маленький бар: {}'.format(get_smallest_bar(bars)))

    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
        print('Ближайший бар: {}'.format(get_closest_bar(bars, longitude, latitude)))
    except ValueError:
        print('Координаты состоят только из чисел')
        exit()


if __name__ == '__main__':
    main()
