import subprocess
import re

server_ip = '10.0.3.1'


def client(server_ip):
    try:
        result = subprocess.run(['iperf', '-c', server_ip], capture_output=True, text=True, check=True)
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.stderr}"


def parse(text):
    result_list = []

    # Use regular expressions to find intervals in the iperf output
    intervals = re.findall(r'\[\s*(\d+)\]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.\d+)\s+GBytes\s+(\d+\.\d+)\s+Gbits/sec',
                           text)

    for interval in intervals:
        result_dict = {
            # 'ID': int(interval[0]),  # ID field is commented out as it is not used
            'Interval': interval[1],
            'Transfer': float(interval[2]),
            'Bitrate': float(interval[3])
        }

        result_list.append(result_dict)

    return result_list


result, error = client(server_ip)

# Check if there was an error during the iperf operation
if error:
    # Print an error message if an error occurred
    print("Error occurred:")
    print(error)
else:
    # Parse the iperf output and print values that meet certain criteria
    result_list = parse(result)
    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)
