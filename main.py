"""Script for Yandex services usage"""

from RandomDataFileCreator import RandomDataFileCreator


def main():
	rand_file_data_creator = RandomDataFileCreator()
	rand_file_data_creator.create_random_data_file('data/services_info', 1000)


if __name__ == "__main__":
	main()
