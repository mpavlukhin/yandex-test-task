import random
import requests


class RandomDataFileCreator(object):
	"""Random data file creator for Yandex services usage"""
	def __init__(self):
		word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
		response = requests.get(word_site)

		words = response.text.splitlines()
		random.shuffle(words)
		self.words = words

		self.emails = ['pavlukhinma@yandex.ru', 'maxtarenvk@yandex.ru', 'pavlukhinm@gmail.com', 'mpavlukhin@yahoo.com']

	def create_random_data_file(self, filename='services_info', number_of_lines=1000):
		self._fill_file_with_rand_data(filename, number_of_lines)

	def _fill_file_with_rand_data(self, filename, number_of_lines):
		with open(filename, 'w') as outfile:
			for i in range(number_of_lines):
				outfile.write('{};{};{};{};{};{}\n'.format(*self._get_rand_line(i)))

	def _get_rand_line(self, service_id):
		service_name = self.words[service_id]
		owners = ','.join(random.sample(self.emails, 2))
		cpu_limit = random.randint(10, 101)
		memory_limit = random.randint(10, 101)

		cpu_usage_list = [random.randint(10, cpu_limit + 1) for _ in range(5, 11)]
		cpu_usage = ','.join(map(str, cpu_usage_list))

		memory_usage_list = [random.randint(10, memory_limit + 1) for _ in range(5, 11)]
		memory_usage = ','.join(map(str, memory_usage_list))

		return service_name, owners, cpu_limit, memory_limit, cpu_usage, memory_usage
