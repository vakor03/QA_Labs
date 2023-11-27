import subprocess
import parser

server_ip = '10.0.3.1'


def client(server_ip):
    try:
        result = subprocess.run(['iperf3', '-c', server_ip], capture_output=True, text=True, check=True)
        return result.stdout, None
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.stderr}"


result, error = client(server_ip)

if error:
    print("Error occurred:")
    print(error)
else:
    result_list = parser.parse(result)
    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)
