import parser

class TestSuite():
    def test_iperf3_client_connection(self, client):
        transfer_min_value = 2
        bitrate_min_value = 20

        output, error = client

        if error:
            assert False, f"Error while connecting client: {error}"

        result = parser.parse(output)[0]

        if not result:
            assert False, f"Incorrect client output"

        if result['Transfer'] <= transfer_min_value:
            assert False, f"Transfer too low {result['Transfer']} < {transfer_min_value}"

        if result['Bitrate'] <= bitrate_min_value:
            assert False, f"Bitrate too low {result['Bitrate']} < {bitrate_min_value}"

        assert True
