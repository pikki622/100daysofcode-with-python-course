from typing import List

import requests
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_keyword(keyword: str) -> List[Movie]:
    url = f'https://movieservice.talkpython.fm/api/search/{keyword}'
    return __get_results(url)


def find_movie_by_director(director_name: str) -> List[Movie]:
    url = f'https://movieservice.talkpython.fm/api/director/{director_name}'
    return __get_results(url)


def find_movie_by_imdb_code(imdb_code: str) -> List[Movie]:
    url = f'https://movieservice.talkpython.fm/api/movie/{imdb_code}'
    resp = requests.get(url)
    resp.raise_for_status()
    result = resp.json()
    return [Movie(**result)] if result.get('imdb_code') else []


def __get_results(url):
    resp = requests.get(url)
    resp.raise_for_status()
    results = resp.json()
    return [Movie(**r) for r in results.get('hits')]
