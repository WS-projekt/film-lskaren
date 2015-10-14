import urllib2
import urllib
import json

def init():
	'''
		Initiate the program
	'''
	# Get search string from user
	search_string = get_movie_title()
	# Fetches and prints the title of the movies in the result
	fetch_movies(search_string)

def get_movie_title():
	'''
		Get serach string from user
	'''
	return raw_input("Movie title to search for: ")
	
def fetch_movies(movie_title):
	'''
		Fetches movies from omdb-API, and prints the results (movie titles)
	'''
	# Parametes for the API-request
	parameters = {'s' : movie_title, 'r' : 'json'}
	# Fetches the result from the API
	response = urllib2.urlopen('http://www.omdbapi.com/?' + urllib.urlencode(parameters))
	# Parse the result as JSON
	movies = json.loads(response.read())
	
	# Do we get any results
	if 'Search' not in movies:
		print '\nNo search results'
		return
		
	# Loop through every movie
	print '\nMovies\n======'
	for movie in movies['Search']:
		# Prints the movie in the console/terminal
		print "Movie: " + movie['Title']
	
init()