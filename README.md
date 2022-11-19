# SRS:
Develop a RESTful web service to obtain music information.

The following information about the music should be stored in the database:
1. Title
2. Rating (min value - 1, max value - 5)
3. Genres - id, title 
4. Singers - id, name 
5. Similar tracks
6. Album

Create API endpoints to get a list of music and detailed information about a particular track.

The endpoint with collection of tracks should return the following:
1. Title
2. Rating
3. Genres (id, title)
4. Singer
5. Album
Users should be able to order tracks by release date, rating, filter by genres (multiply by ids) and search by title. 
Default ordering by rating (desc).

The endpoint with detailed information should return the following:
1. Title
2. Rating 
3. Genres (id, title)
4. Singers (id, name)
5. Similar tracks (title, singers)
6. Album