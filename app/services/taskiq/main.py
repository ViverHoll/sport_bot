import asyncio

from taskiq import InMemoryBroker, TaskiqScheduler
from taskiq.schedule_sources import LabelScheduleSource

broker = InMemoryBroker()

scheduler = TaskiqScheduler(
    broker=broker,
    sources=[
        LabelScheduleSource(broker),
    ],
)


@broker.task(schedule=[
    {
        "cron": "* * * * *",
        "args": [10, 15],
    },
])
async def update_balance(
        balance: int,
        plus: int,
) -> int:
    """Update balance."""
    await asyncio.sleep(2)
    return balance + plus


async def main() -> None:
    await broker.startup()

    task = await update_balance.kiq(10, 15)

    result = await task.wait_result(timeout=3)
    print(f"Task execution took: {result.execution_time} seconds.")
    if not result.is_err:
        print(f"Returned value: {result.return_value}")
    else:
        print("Error found while executing task.")
    await broker.shutdown()


if __name__ == "__main__":
    asyncio.run(main())
