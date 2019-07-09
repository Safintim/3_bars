import json


def load_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: bar['properties']['Attributes']['SeatsCount'])


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda bar: (abs(bar['geometry']['coordinates'][0]-longitude),
                                      abs(bar['geometry']['coordinates'][1]-latitude)))


def main():
    bars = load_data('bars.json')['features']
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    print('Самый большой бар: {}'.format(biggest_bar['properties']['Attributes']['Name']))
    print('Самый маленький бар: {}'.format(smallest_bar['properties']['Attributes']['Name']))

    try:
        longitude = float(input('Введите долготу: '))
        latitude = float(input('Введите широту: '))
        closest_bar = get_closest_bar(bars, longitude, latitude)
        print('Ближайший бар: {}'.format(closest_bar['properties']['Attributes']['Name']))
    except ValueError:
        print('Координаты состоят только из чисел')
        exit()


if __name__ == '__main__':
    main()
