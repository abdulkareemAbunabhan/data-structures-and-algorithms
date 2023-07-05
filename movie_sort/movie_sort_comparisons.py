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


def get_title_without_pref(title):
    prefs = ['A', 'An', 'The']
    words = title.split()
    if words[0] in prefs:
        return ' '.join(words[1:])
    return title


def sorter_by_title(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if get_title_without_pref(arr[j]['title']) > get_title_without_pref(arr[j + 1]['title']):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def sorter_by_year(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j]['year'] <arr[j + 1]['year']:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(sorter_by_title(movies))
print(sorter_by_year(movies))