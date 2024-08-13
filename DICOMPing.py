import argparse
import pydicom
from pynetdicom import AE

def dicom_ping(ae_title, host, port, calling_ae_title):
    """Function to perform a DICOM Ping"""
    ae = AE(ae_title=calling_ae_title)
    ae.add_requested_context('1.2.840.10008.1.1')
    ae.acse_timeout = 5
    ae.dimse_timeout = 5
    ae.network_timeout = 5
    assoc = ae.associate(host, port, ae_title=ae_title)
    if assoc.is_established:
        status = assoc.send_c_echo()
        if status:
            print("DICOM Ping successful!")
            return True
        else:
            print("DICOM Ping failed")
            return False
    else:
        print("Association failed to establish")
        return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="DICOM Ping using Python and PyDicom")
    parser.add_argument("target_ae_title", help="Target AE Title")
    parser.add_argument("target_host", help="Target host IP address")
    parser.add_argument("target_port", type=int, help="Target host port")
    parser.add_argument("calling_ae_title", help="Calling AE Title")
    args = parser.parse_args()

    result = dicom_ping(args.target_ae_title, args.target_host, args.target_port, args.calling_ae_title)
    if result:
        print("DICOM Ping was successful!")
    else:
        print("DICOM Ping failed")