import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '192.168.1.2', 10075)

    print(f'Send: {message!r}')
    writer.write(bytes.fromhex(message))

    data = await reader.read(100)
    #print(f'Received: {data.decode()!r}')

    await writer.drain()

    print(f'Send: {message!r}')
    writer.write(bytes.fromhex(message))

    data = await reader.read(100)
    #print(f'Received: {data.decode()!r}')



asyncio.run(tcp_echo_client('924000F4F87AF73425C89A6DA9DDEBABA83CA6E6B4726DEF512300DEEA43D58F22503FAF9C5296107CA4BEA9578AAE4968062073C624A807AD44D254298D58B63CDA3BE4338C57'))
