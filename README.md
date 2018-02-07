# Example project demonstrating MP3 Firefox bug

MP3 file created with ffmpeg:

`ffmpeg -f lavfi -i sine=f=220:b=4:d=500 -c:a libmp3lame output.mp3`
