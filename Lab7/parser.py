import re

"""
Для парсера рекомендую використовувати бібліотеку re. Для свого парсера, я
використовував регулярку, що можна побачити нижче. Таким чином, можна відсіяти всі
непотрібні рядки з виводу
iperf-клієнта, а залишити тільки ті, що стосуються трафіку.
"""
REGEXP = r'\[\s*[0-9]*\]\s*[0-9\.-]*\s*(sec)\s*[0-9\.]*\s*[A-Z]?(Bytes)\s*[0-9\.]*\s*[A-Z]?(bits/sec)\s*[0-9]*\s*[0-9\.]*\s*[A-Z]?(Bytes)'
KEYS = ('Interval', 'Transfer', 'Bitrate', 'Retr', 'Cwnd')


def parse(text):
    result_list = []

    intervals = re.findall(r'\[\s*(\d+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+)\s+MBytes\s+(\d+)\s+Mbits/sec', text)

    for interval in intervals:
        result_dict = {
            # 'ID': int(interval[0]),  # ID field is commented out as it is not used
            'Interval': interval[1],
            'Transfer': float(interval[2]),
            'Bitrate': float(interval[3])
        }

        result_list.append(result_dict)

    return result_list
