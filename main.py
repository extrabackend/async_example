import asyncio
import time

import httpx


class MyAsyncContextManager:

    async def __aenter__(self):
        client = httpx.AsyncClient()
        resp = await client.get('https://www.example.org/')
        print(resp.status_code)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass


def get_response_status_code(url: str) -> int:
    r = httpx.get(url)

    return r.status_code


async def async_get_response_status_code(number) -> int:
    print(f'task {number} is started')
    client = httpx.AsyncClient()
    resp = await client.get('https://www.example.org/')
    print(f'task {number} is finished')
    return resp.status_code


async def main():
    # create task
    task = asyncio.create_task(async_get_response_status_code(1))
    await task

    # using gather
    statuses = asyncio.gather(
        async_get_response_status_code(1),
        async_get_response_status_code(2),
        async_get_response_status_code(3),
    )

    # async context manager
    async with MyAsyncContextManager() as ctx:
        print(ctx)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()

    print('time:', end_time - start_time)


# 1. CPU bound operations
# 2. IO bound operations
