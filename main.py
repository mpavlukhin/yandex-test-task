"""Script for Yandex services usage"""

from RandomDataFileCreator import RandomDataFileCreator
from DataHandler import ServicesDataHandler


DATA_FILE = 'data/services_info'


def main():
	rand_file_data_creator = RandomDataFileCreator()
	rand_file_data_creator.create_random_data_file(DATA_FILE, 1000)

	services_data_handler = ServicesDataHandler()
	services_info = services_data_handler.handle_data(DATA_FILE)


if __name__ == "__main__":
	main()
