from stocks.models import Company
import csv


def run():
    path = 'scripts/nasdaq-listed.csv'
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            _, created = Company.objects.get_or_create(
                symbol=row[0],
                name=row[1],
                market=row[3])


if __name__ == "__main__":
    run()
