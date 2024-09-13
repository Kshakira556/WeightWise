# tests/test_smart_scale.py

import asyncio
from app.services.smart_scale_service import SmartScaleService

async def test_smart_scale_service():
    # Replace with your actual Bluetooth device address
    device_address = '00:00:00:00:00:00'
    service = SmartScaleService(device_address)

    # Connect to the smart scale
    assert await service.connect() == True

    # Fetch weight
    weight = await service.fetch_weight()
    print(f"Fetched weight: {weight}")

    # Close the connection
    await service.close_connection()

if __name__ == '__main__':
    asyncio.run(test_smart_scale_service())
