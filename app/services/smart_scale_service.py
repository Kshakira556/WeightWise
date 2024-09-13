"""
WeightWise Smart Scale Service

Handle integration with smart scales for automatic weight logging using BLE.
"""

from bleak import BleakClient

class SmartScaleService:
    def __init__(self, device_address):
        self.device_address = device_address
        self.client = None

    async def connect(self):
        """
        Connect to the smart scale via Bluetooth BLE.
        """
        try:
            self.client = BleakClient(self.device_address)
            await self.client.connect()
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            return False

    async def fetch_weight(self):
        """
        Fetch weight data from the smart scale.
        
        :return: Weight as a float if successful, None otherwise.
        """
        if not self.client or not self.client.is_connected:
            print("No active connection.")
            return None
        
        try:
            # Assuming the scale sends data in a specific characteristic
            weight_data = await self.client.read_gatt_char('your-characteristic-uuid')
            weight = float(weight_data.decode('utf-8').strip())
            return weight
        except Exception as e:
            print(f"Failed to fetch weight: {e}")
            return None

    async def close_connection(self):
        """
        Close the Bluetooth connection.
        """
        if self.client and self.client.is_connected:
            try:
                await self.client.disconnect()
            except Exception as e:
                print(f"Failed to close connection: {e}")
