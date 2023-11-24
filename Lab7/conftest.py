import paramiko
import subprocess
import pytest

server_ip = '10.0.2.15'
password = 'Golden2003+'
username = 'vakor'


@pytest.fixture(scope='function')
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
        pytest.fail(f"Error starting iperf server: {error_message}")

    # Add a finalizer to close the server when the test is finished
    def close_server():
        ssh.connect(server_ip, username=username, password=password)
        ssh.exec_command("killall iperf")
        ssh.close()

    # request.addfinalizer(close_server)

    # Return any error message (empty if successful)
    return error_message


@pytest.fixture(scope='function')
def client(server):
    """
    In this fixture, use the subprocess library to connect to our iperf server. After
    executing the command, return the output and error.
    :param server: Call the server fixture
    :return: Return the output and error of the iperf client for further analysis of
    the result. Regarding the error, simply check for a specific error (e.g., failed
    connection to the server). And in the output, analyze some specific values using
    parsing.
    """
    # Execute the iperf client command
    client_command = f"iperf -c {server_ip}"
    process = subprocess.Popen(client_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Wait for the process to finish and get the output and error
    output, error = process.communicate()

    # Check for a specific error (customize based on iperf client behavior)
    if "connection failed" in error.decode("utf-8").lower():
        pytest.fail("Failed to connect to the iperf server")

    # You can add more parsing of specific values from the output if needed

    # Return the output and error for further analysis
    return output.decode("utf-8"), error.decode("utf-8")
