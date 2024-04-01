import asyncio
import aiohttp
import json


async def make_post_request(url, payload, headers):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, params=payload, headers=headers) as response:
            return await response.json()


async def main():
    url = 'http://0.0.0.0:8000/complete'
    payload = {'prompt': 'What is future of programming',
               'provider': 'anthropic',
               'max_tokens': 50,
               'temperature': 0.5,
               'top_p': 0.5,
               'stream': 'False'}
    headers = {'Content-Type': 'application/json'}

    tasks = []
    for _ in range(1):
        task = asyncio.create_task(make_post_request(url, payload, headers))
        tasks.append(task)

    payload = {'prompt': 'What is future of programming',
               'provider': 'anthropic',
               'max_tokens': 50,
               'temperature': 0.5,
               'top_p': 0.5,
               'stream': 'True'}

    for _ in range(1):
        task = asyncio.create_task(make_post_request(url, payload, headers))
        tasks.append(task)

    payload = {'prompt': 'What is future of programming',
               'provider': 'together',
               'max_tokens': 50,
               'temperature': 0.5,
               'top_p': 0.5,
               'stream': 'True'}

    for _ in range(1):
        task = asyncio.create_task(make_post_request(url, payload, headers))
        tasks.append(task)

    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response)


if __name__ == "__main__":
    asyncio.run(main())