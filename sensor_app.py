import device_model
import select
import sys
import socket
import asyncio

# This method will be called when sensor data is updated
def updateData (deviceModel):
    # Directly print out the device data dictionary
    print (deviceModel.deviceData)
    # Uncomment appropriately for printing individual sensor data items
    # Timestamp:
    # print(deviceModel.get("time"))
    # Acceleration:
    # print(deviceModel.get("AccX"))
    # print(deviceModel.get("AccY"))
    # print(deviceModel.get("AccZ"))
    # Angular velocity:
    # print(deviceModel.get("AsX"))
    # print(deviceModel.get("AsY"))
    # print(deviceModel.get("AsZ"))
    # Angle:
    # print(deviceModel.get("AngleX"))
    # print(deviceModel.get("AngleY"))
    # print(deviceModel.get("AngleZ"))
    # Magnetic field:
    # print(deviceModel.get("HX"))
    # print(deviceModel.get("HY"))
    # print(deviceModel.get("HZ"))

# Check for user input from stdin
async def requested_end_of_bt_data ():
    result = select.select ([sys.stdin], [], [], 0)
    if result[0]:
        return True
    return False

# Poll for receiving sensor data
async def receive_sensor_data (sock):
    result = select.select ([sock], [], [])
    if result:
        res = sock.recv (1024)
        device.onDataReceived (None, res)

# Main event loop: read sensor data and check for user input
async def app_loop(sock):
    exit_loop = False
    while not exit_loop:
        read_stdin_task = asyncio.create_task (requested_end_of_bt_data())
        read_sensor_task = asyncio.create_task (receive_sensor_data(sock))
        await read_sensor_task
        exit_loop = await read_stdin_task


if __name__ == '__main__':
    # Create device
    device = device_model.DeviceModel (updateData)
    # If device is ready, open socket and start event loop
    if device.isReady:
        socket = asyncio.run (device.openDevice())
        asyncio.run (app_loop(socket))
