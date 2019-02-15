"""Script for Yandex services usage"""

from DataHandler import ServicesDataHandler
from EmailHandler import EmailHandler
from RandomDataFileCreator import RandomDataFileCreator

DATA_FILE = 'data/services_info'


def write_to_ineffective_services_owners(services_info, fake_email_sending=False):
	for service in services_info:
		data_str = ''
		is_ineffective = False

		cpu_ratio = service[8]
		if cpu_ratio <= 0.75:
			is_ineffective = True
			cpu_quote = service[2]
			cpu_usage_list = service[4]
			cpu_required_quote = service[6]
			data_str += "Квота на использование CPU: {}, " \
						"фактическое использование во " \
						"времени {}. Рекомендуемая квота " \
						"соcтавляет {}.".format(
				cpu_quote, cpu_usage_list, cpu_required_quote
			)

		memory_ratio = service[9]
		memory_required_quote = service[7]
		if memory_ratio <= 0.75:
			is_ineffective = True
			memory_quote = service[3]
			memory_usage_list = service[5]
			data_str += "\nКвота на использование Memory: {}, " \
			"фактическое использование во " \
			"времени {}. Рекомендуемая квота " \
			"составляет {}.".format(
				memory_quote, memory_usage_list, memory_required_quote
			)

		if is_ineffective:
			service_name = service[0]
			msg = "Добрый день!\n\n" \
				  "Меня зовут Максим. Я являюсь техническим менеджером" \
				  " во внутреннем облаке Яндекса. В мои задачи входит оптимизация " \
				  "процесса использования ресурсов сервисами в этом облаке.\n\n" \
				  "Ваш сервис {} находится в рамках предоставляемых ему квот, " \
				  "однако эти квоты слишком велики (они не используются " \
				  "в полной мере). Такие выводы были сделаны в результате " \
				  "анализа данных о работе сервиса.\n\n" \
				  "Данные следующие:\n{}\n\n" \
				  "Пожалуйста, оптимизируйте использование ресурсов сервиса " \
				  "(например, масштабируйте его), чтобы текущие квоты были " \
				  "сохранены. Произвести оптимизацию можно в течение трех рабочих" \
				  " дней. По истечении трех дней, в случае, если оптимизация " \
				  "не будет произведена, будут назначены новые, рекомендуемые " \
				  "для работы сервиса, квоты (квоты будут ограничены).\n\n" \
				  "Спасибо за внимание и понимание!\n" \
				  "Хорошего дня!\n" \
				  "С уважением, Максим.".format(service_name, data_str)

			email_handler = EmailHandler()

			owners = service[1]

			if not fake_email_sending:
				for owner in owners:
					email_handler.send_email(owner, msg.encode('utf-8'))


def main():
	rand_file_data_creator = RandomDataFileCreator()
	rand_file_data_creator.create_random_data_file(DATA_FILE, 1000)

	services_data_handler = ServicesDataHandler()
	services_info = services_data_handler.handle_service_data(DATA_FILE)

	write_to_ineffective_services_owners(services_info, fake_email_sending=True)


if __name__ == "__main__":
	main()
