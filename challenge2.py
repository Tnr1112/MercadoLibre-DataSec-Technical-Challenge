import requests


def getSeries():
	baseUrl = "https://jsonmock.hackerrank.com/api/tvseries"
	page = 1
	series = []

	while True:
		response = requests.get(baseUrl, params={"page": page})
		data = response.json()

		if page > data["total_pages"]:
			break

		series += data["data"]

		page += 1

	return series

def filterSeriesByGenre(series, genre):
	return list(filter(lambda x: genre in x["genre"], series))

def bestInGenre(genre):
	series = getSeries()
	filteredSeries = filterSeriesByGenre(series, genre)
	return max(filteredSeries, key=lambda x: (x["imdb_rating"], len(x["name"])))