from typing import List, Dict, Final, Optional
from concurrent.futures import ProcessPoolExecutor, as_completed
from concurrent.futures import Future
import urllib.request


URLS: Final[List[str]] = [
    "https://www.naver.com/",
    "https://www.github.com/",
    "https://www.google.com/",
    "https://www.udemy.com/",
    "https://www.coursera.org/",
]


def load_url(url: str, timeout: int) -> str:
    """url html source parsing"""
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def main():
    with ProcessPoolExecutor(max_workers=5) as excute:
        # future load(not run)
        # example: <Future at 0x7f9f602e4490 state=running>: 'https://www.naver.com/'
        future_to_url: Dict[Future, str] = {
            excute.submit(load_url, url, 2): url for url in URLS
        }

        # print(future_to_url)
        for future in as_completed(future_to_url):
            url: Optional[str] = future_to_url.get(future)

            try:
                data: str = future.result()
            except Exception as e:
                print(f"{url} generated an exception: {e}")
            else:
                print(f"{url} page is {len(data)} bytes")


if __name__ == "__main__":
    main()
