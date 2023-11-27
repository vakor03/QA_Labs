import re


def parse(text):
    result_list = []

    intervals = re.findall(
        r'\[\s*(\d+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.\d+)\s+MBytes\s+(\d+)\s+Mbits/sec\s+(\d+)\s+(\d+)\s+KBytes',
        text)

    for interval in intervals:
        result_dict = {
            # 'ID': int(interval[0]),  # ID field is commented out as it is not used
            'Interval': interval[1],
            'Transfer': float(interval[2]),
            'Bitrate': float(interval[3]),
            'Retr': float(interval[4]),
            'Cwnd': float(interval[5])
        }

        result_list.append(result_dict)

    return result_list
