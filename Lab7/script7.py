import paramiko

server_ip = '10.0.2.15'
password = 'Golden2003+'
username = 'vakor'


def server():
    """
    In this fixture, establish a connection to the server using ssh. Use the paramiko
    library for this purpose. After the connection, start the iperf server. After iperf
    has finished, close the ssh connection.
    :return: Error message from the server if any
    """
    # Connect to the server via SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, password=password)

    # Start iperf server
    start_server_command = "iperf -s"
    _, stdout, stderr = ssh.exec_command(start_server_command)

    # Wait for the server to finish (you can customize this based on iperf behavior)
    # Here, we wait for 5 seconds, adjust as needed
    ssh.exec_command("sleep 5")

    # Close the SSH connection
    ssh.close()

    # If there is an error, return the error message
    error_message = stderr.read().decode("utf-8")
    if error_message:
        print(f"Error starting iperf server: {error_message}")

    # Return any error message (empty if successful)
    return error_message


result = server()
print(result)
