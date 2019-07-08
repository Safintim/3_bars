import json


def load_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


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
    print(f'Самый большой бар: {get_biggest_bar(bars)}')
    print(f'Самый маленький бар: {get_smallest_bar(bars)}')

    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
    except ValueError:
        print('Координаты состоят только из чисел')
        exit()
    print(f'Ближайший бар: {get_closest_bar(bars, longitude, latitude)}')


if __name__ == '__main__':
    main()
