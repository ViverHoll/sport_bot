import asyncio
from asyncio import CancelledError

import nats
from nats.aio.msg import Msg

# обработчик полученных сообщений
async def message_handler(msg: Msg) -> None:
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received message '{data}' from subject '{subject}'")



async def main() -> None:
    nats_connect = await nats.connect("nats://127.0.0.1:4222")
    subject = "my.first.subject"

    # подписываемся на сабджект
    await nats_connect.subscribe(subject, cb=message_handler)
    print(f"Subscribed to subject '{subject}'")

    try:
        await asyncio.Future()
    except CancelledError:
        pass
    finally:
        await nats_connect.close()

if __name__ == "__main__":
    asyncio.run(main())

