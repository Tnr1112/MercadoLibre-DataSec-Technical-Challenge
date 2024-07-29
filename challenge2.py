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

def getBestInGenre(genre):
	series = getSeries()
	bestSerie = None
	filteredSeries = filterSeriesByGenre(series, genre)
	for filteredSerie in filteredSeries:
		if bestSerie is None or filteredSerie["imdb_rating"] > bestSerie["imdb_rating"]:
			bestSerie = filteredSerie
		elif filteredSerie["imdb_rating"] == bestSerie["imdb_rating"] and filteredSerie['name'] < bestSerie['name']:
			bestSerie = filteredSerie
	return bestSerie

def bestInGenre(genre):
	bestSerie = getBestInGenre(genre)
	return bestSerie["name"] if bestSerie else None