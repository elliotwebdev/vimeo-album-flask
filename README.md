# vimeo-album-flask
Retrieve public Vimeo album data using Flask! This application uses the Python web framework to communicate with Vimeo's REST API.

![preview](https://i.imgur.com/y5ieqAZ.png)

## Getting Started
Follow these steps in the source code before starting development server.

### API Keys Registration
You must first register app on Vimeo following this guide [HERE](https://developer.vimeo.com/api/guides/start)
* Insert Vimeo API keys by inputting key syntax in main.py here:

```
client = vimeo.VimeoClient(
	#API key SYNTAX GOES HERE
)
```

### Getting album data
You can specify a certain video album(showcase) using the album ID in a get request or as an argument below:

```
@app.route('/')
def landing():
	#Replace album_id with a public Vimeo album; You can find it in the URL 
	#Example: https://vimeo.com/showcase/7693012
	album_id = '7693012'
```

### Start development server
In terminal, enter the following:
* export FLASK_APP=main
* flask run
* Enter the given URL in the browser

View a live version of this application at https://derekhenriquez-editor.com
