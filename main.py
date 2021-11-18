from hat.drivers import modbus
from hat.drivers import tcp
import asyncio


async def async_main():
    modbus_type = modbus.ModbusType.TCP
    address = tcp.Address('161.53.17.239', 8502)
    master = await modbus.create_tcp_master(modbus_type, address)
    while True:
        data = await master.read(device_id=1,
                                 data_type=modbus.DataType.HOLDING_REGISTER,
                                 start_address=4003, quantity=1)
        print(data)
        await asyncio.sleep(2)


def main():
    asyncio.run(async_main())


main()
