import csv
from pprint import pprint


class Model:
    def __init__(self):
        self._ticket_data = dict()

    def load_ticket_data(self, filepath):
        self._ticket_data['filepath'] = filepath

        with open(self._ticket_data['filepath'], 'r', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')

            # extract the ticket header data
            _, self._ticket_data['order_number'] = next(reader)
            _, self._ticket_data['ship_date'] = next(reader)
            next(reader)  # skip a line
            _, self._ticket_data['customer_name'] = next(reader)

            # the next 4 lines are not needed
            for i in range(4):
                next(reader)

            pprint(self._ticket_data)
            for line in reader:
                print(line)

    @property
    def ticket_data(self):
        return self._ticket_data

    @ticket_data.setter
    def ticket_data(self, data):
        self._ticket_data = data
