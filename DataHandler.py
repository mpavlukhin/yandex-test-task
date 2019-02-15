class ServicesDataHandler(object):
    """
    Yandex services usage data handler

    It helps to find ineffective services quotes usage.

    """
    def __init__(self):
        pass

    def handle_service_data(self, filename):
        services_info_list = []

        with open(filename, 'r') as infile:
            for line in infile:
                clean_line = line.strip('\n')
                service_info_str = clean_line.split(sep=';')
                services_info = self._parse_data(service_info_str)
                services_info_list.append(services_info)

        return services_info_list

    def _parse_data(self, service_info):
        service_name = service_info[0]
        owners = service_info[1].split(sep=',')
        cpu_limit = int(service_info[2])
        memory_limit = int(service_info[3])

        cpu_usage_list = service_info[4].split(sep=',')
        cpu_usage_list = list(map(int, cpu_usage_list))
        memory_usage_list = service_info[5].split(sep=',')
        memory_usage_list = list(map(int, memory_usage_list))

        required_cpu_quote = self._calc_quantile(cpu_usage_list)
        required_memory_quote = self._calc_quantile(memory_usage_list)

        cpu_ratio = required_cpu_quote / cpu_limit
        memory_ratio = required_memory_quote / memory_limit

        return (
            service_name, owners, cpu_limit, memory_limit, cpu_usage_list,
            memory_usage_list, required_cpu_quote, required_memory_quote,
            cpu_ratio, memory_ratio
        )

    def _calc_quantile(self, dist_list, perc=0.9):
        dist_list_len = len(dist_list)
        sorted_dist_list = sorted(dist_list)

        el_to_ch = round(dist_list_len * perc) - 1

        return sorted_dist_list[el_to_ch]
