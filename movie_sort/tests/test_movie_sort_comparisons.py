import pytest
from movie_sort_comparisons import sorter_by_year,sorter_by_title
movies = [
    {
        'title': 'The Secret of Mountain',
        'year': 2005,
        'genres': ['Adventure', 'Family']
    },
    {
        'title': 'Journey to the Stars',
        'year': 2012,
        'genres': ['Sci-Fi', 'Action']
    },
    {
        'title': 'In the Shadows',
        'year': 2018,
        'genres': ['Thriller', 'Mystery']
    },
    {
        'title': 'The Midnight Heist',
        'year': 2016,
        'genres': ['Crime', 'Thriller']
    },
    {
        'title': 'Echoes of Eternity',
        'year': 2020,
        'genres': ['Drama', 'Mystery']
    },
    {
        'title': 'The Forgotten Journey',
        'year': 2013,
        'genres': ['Adventure', 'Fantasy']
    },
    {
        'title': 'Fading Shadows',
        'year': 2019,
        'genres': ['Horror', 'Suspense']
    },
]


# Assert that the titles are sorted in the correct order
def test_sorter_by_title():
    sorted_by_title = sorter_by_title(movies)

    assert [movie['title'] for movie in sorted_by_title] == [
        'Echoes of Eternity',
        'Fading Shadows',
        'The Forgotten Journey',
        'In the Shadows',
        'Journey to the Stars',
        'The Midnight Heist',
        'The Secret of Mountain'
    ]


# test that the years are sorted in the correct order
def test_sorter_by_year():
    sorted_by_year = sorter_by_year(movies)

    assert [movie['year'] for movie in sorted_by_year] == [2020, 2019, 2018, 2016, 2013, 2012, 2005]