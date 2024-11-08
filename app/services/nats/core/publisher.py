import asyncio

import nats

async def main() -> None:
    nats_connect = await nats.connect("nats://127.0.0.1:4222")

    message = "Я отправил сообщение с помощью NATS и с помощью python"

    subject = "my.first.subject"

    for _ in range(10):
        await nats_connect.publish(subject, message.encode())
    print(f"Message {message} published to subject {subject}")
    await nats_connect.close()


if __name__ == "__main__":
    asyncio.run(main())

