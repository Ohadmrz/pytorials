import csv
import datetime


def apple_stock_sum(stock_file_path: str, out_file_path: str):

    average_dict: dict[datetime.datetime, dict] = {}

    with open(stock_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            year = datetime.datetime.strptime(row['Date'], '%d-%m-%Y').year

            if year not in average_dict:
                average_dict[year] = {
                    'prices': {
                        'sum': 0, 'cnt':0, 'avg': 0, 'min': None, 'max': 0
                    },
                    'volumes': {
                        'sum': 0, 'cnt':0, 'avg': 0, 'min': None, 'max': 0
                    }
                }
            low_price = float(row['Low'])
            high_price = float(row['High'])
            volume = int(row['Volume'])

            average_dict[year]['prices']['sum'] += low_price + high_price / 2
            average_dict[year]['prices']['cnt'] += 1

            average_dict[year]['volumes']['sum'] += int(row['Volume'])
            average_dict[year]['volumes']['cnt'] += 1

            # update min and max values
            if average_dict[year]['prices']['min'] is None or average_dict[year]['prices']['min'] > low_price:
                average_dict[year]['prices']['min'] = low_price

            if average_dict[year]['prices']['max'] < high_price:
                average_dict[year]['prices']['max'] = high_price

            if average_dict[year]['volumes']['min'] is None or average_dict[year]['volumes']['min'] > volume:
                average_dict[year]['volumes']['min'] = volume

            if average_dict[year]['volumes']['max'] < volume:
                average_dict[year]['volumes']['max'] = volume

    with open(out_file_path, 'w', newline='') as csvfile:
        fieldnames = ['Year',  'Avg Price', 'Min Price', 'Max Price', 'Avg Volume', 'Min Volume', 'Max Volume']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for year, data in average_dict.items():
            writer.writerow({
                'Year': year,
                'Avg Price': data['prices']['sum'] / data['prices']['cnt'],
                'Min Price': data['prices']['min'],
                'Max Price': data['prices']['max'],
                'Avg Volume': data['volumes']['sum'] / data['volumes']['cnt'],
                'Min Volume': data['volumes']['min'],
                'Max Volume': data['volumes']['max'],
            })


if __name__ == '__main__':
    apple_stock_sum('data/AAPL.csv', 'out_aapl.csv')