import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup


start = timeit.default_timer()

urls = [
    "https://news.naver.com/",
    "https://weather.naver.com/",
    "https://tistory.com",
    "https://velog.io/",
    "https://github.com",
]


async def fetch(url, thread_params):
    print(f"Thread name: {threading.current_thread().getName()}, Start: {url}")
    # block -> non-block
    res = await loop.run_in_executor(thread_params, urlopen, url)

    soup = BeautifulSoup(res.read(), "html.parser")
    title = soup.select_one("title")

    print(f"Thread name: {threading.current_thread().getName()}, Done: {url}")

    return title


async def main():
    # create a thread pool
    excute = ThreadPoolExecutor(max_workers=10)

    # future to gather
    futures = [asyncio.ensure_future(fetch(url, excute)) for url in urls]

    # result -> wait for all complete future tasks
    result = await asyncio.gather(*futures)
    print(f"\nResult: {result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())  # 작업 완료 까지 대기
    duration = timeit.default_timer() - start
    print(f"Run-Time: {duration:.2f}")
