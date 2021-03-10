import argparse

if __name__ == '__main__':
    # initialize
    parser = argparse.ArgumentParser(description='Say a Greeting.')
    # first argument in command line
    parser.add_argument('name', type=str)
    # adding optional argument
    parser.add_argument('--city', type=str, default='San Francisco',
                        help='where this person from?')
    # collect arguments 
    args = parser.parse_args()
    name = args.name
    city = args.city
    print(f'hello, {name} from {city}')
