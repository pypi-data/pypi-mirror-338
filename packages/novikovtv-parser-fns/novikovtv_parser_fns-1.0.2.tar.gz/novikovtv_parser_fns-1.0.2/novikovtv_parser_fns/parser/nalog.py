import asyncio
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup, Tag

from novikovtv_parser_fns.parser.captcha.solver import CaptchaSolver
from novikovtv_parser_fns.parser.config import get_parse_config
from novikovtv_parser_fns.parser.constants import RPS, SEARCH_PAGE_RANGE
from novikovtv_parser_fns.parser.exceptions import SearchBadParsing, SearchIDCaptchaError, SearchIDInvalidError
from novikovtv_parser_fns.parser.models.search import SearchRequest, SearchResult


class NalogParserApi(object):
    API_FNS_CAPTCHA_URL = "https://pb.nalog.ru/captcha-dialog.html"
    MAX_CAPTCHA_REQUEST_ATTEMPTS = 10

    def __init__(self):
        self.semaphore = asyncio.Semaphore(RPS)
        self.max_attempts = self.__class__.MAX_CAPTCHA_REQUEST_ATTEMPTS
        self.captcha_url = self.__class__.API_FNS_CAPTCHA_URL

    async def _solve_captcha(self, *args, **kwargs) -> str:
        attempt = 0
        while attempt < self.max_attempts:
            attempt += 1
            print("attempt: ", attempt)
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(self.captcha_url) as resp:
                        html_text = await resp.text()

                        soup = BeautifulSoup(html_text, 'html.parser')
                        captcha: Tag = soup.find('img')
                        if captcha is None:
                            print("captcha not found")
                            return

                        captcha_token: str = captcha['src'].split('&')[0].replace('/static/captcha.bin?a=', '')

                async with aiohttp.ClientSession() as session:
                    async with session.get("https://pb.nalog.ru" + captcha['src']) as resp:
                        captcha_img = await resp.read()
                        captcha_solver = CaptchaSolver(captcha_img)
                        captcha_recognition = captcha_solver.solve()

                print(captcha_recognition, captcha_token)
                if not captcha_token or not captcha_recognition:
                    continue

                async with aiohttp.ClientSession() as session:
                    async with session.post("https://pb.nalog.ru/captcha-proc.json", params={
                        'captcha': captcha_recognition,
                        "captchaToken": captcha_token,
                    }) as resp:
                        print(await resp.json())
                        if not resp.ok:
                            continue
                        captcha_text = await resp.text()
                        captcha_text = captcha_text.replace('\"', '')

                search_id = await self._get_search_id(*args, **kwargs, captcha=captcha_text)
                return search_id
            except Exception as e:
                print("NalogParserApi._solve_captcha", e)
                continue

    async def _try_get_search_id_through_captcha(self, *args, **kwargs) -> Optional[str]:
        try:
            search_id: Optional[str] = await self._get_search_id(*args, **kwargs)
            return search_id
        except SearchIDCaptchaError as e:
            return await self._solve_captcha(*args, **kwargs)

    async def _get_search_id(self, query: str, *, captcha: str = "", page: int = 1) -> Optional[str]:
        params = get_parse_config(query=query, page=page, captcha=captcha)
        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.post('https://pb.nalog.ru/search-proc.json', params=params) as resp:
                    search: SearchRequest = SearchRequest(**await resp.json())
                    if search.ERROR is not None:
                        raise SearchIDCaptchaError(search)

                    return search.id


class NalogParser(NalogParserApi):
    MAX_ITERATIONS = 10
    API_FNS_URL = "https://pb.nalog.ru/search-proc.json"

    def __init__(self):
        super().__init__()
        self.api_url = self.__class__.API_FNS_URL
        self.max_iterations = self.__class__.MAX_ITERATIONS
        self.results: list[SearchResult] = []

    async def search(self, query: str) -> list[SearchResult]:
        task_ids: list = [asyncio.create_task(self._try_get_search_id_through_captcha(query, page=page)) for page in
                          SEARCH_PAGE_RANGE]
        search_id_list_plain: list[Optional[str]] = await asyncio.gather(*task_ids)
        search_id_list = [_search_id for _search_id in search_id_list_plain if id]
        if not search_id_list:
            raise SearchIDInvalidError()

        task: list = [asyncio.create_task(self.__try_search(_search_id)) for _search_id in search_id_list]
        results: list[Optional[SearchResult]] = await asyncio.gather(*task)

        self.results: list[SearchResult] = [res_ for res_ in results if res_ is not None]
        return self.results

    async def __try_search(self, search_id: str) -> Optional[SearchResult]:
        try:
            res: SearchResult = await self.__search(search_id)
            if not res:
                print(f"No results for {search_id}")
            return res
        except Exception as e:
            print("NalogParser.__try_search", e)

    async def __search(self, search_id: str) -> Optional[SearchResult]:
        params = {
            "id": search_id,
            "method": "get-response",
        }

        async with self.semaphore:
            async with aiohttp.ClientSession() as session:
                iterations: int = 0
                while iterations < self.max_iterations:
                    iterations += 1
                    try:
                        async with session.get(self.api_url,
                                               params=params,
                                               headers={"Content-Type": "application/json"}) as resp:
                            search_res_plain = await resp.json()
                            if search_res_plain:
                                break
                    except Exception as e:
                        print("NalogParser.__search", e)
                        continue

                if iterations == self.max_iterations:
                    raise SearchBadParsing()

                search_res: SearchResult = SearchResult(**search_res_plain)
                return search_res


async def main():
    parser = NalogParser()
    res: list[SearchResult] = await parser.search("Тест")



if __name__ == '__main__':
    asyncio.run(main())
