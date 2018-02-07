# Example project demonstrating MP3 Firefox bug


## Testing the project:

1. Setup server

```
# clone it
$ git clone https://github.com/OskarPersson/firefox-mp3-bug
$ cd firefox-mp3-bug

# install django
$ pip install django

# create (sqlite) database
$ python manage.py migrate

# start server
$ python manage.py runserver
```

2. Go to localhost:8000 in Firefox and let it play for a few seconds
3. Reload page
4. Clear cache
5. Go back to page


MP3 file created with ffmpeg:

`ffmpeg -f lavfi -i sine=f=220:b=4:d=5000 -c:a libmp3lame output.mp3`
