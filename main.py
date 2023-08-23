from flask import Flask, render_template
import vimeo, json
app = Flask(__name__)

#API key SYNTAX GOES HERE
client = vimeo.VimeoClient(
	token='TOKEN',
	key='KEY',
	secret='SECRET'
)

def decode_json_reel(client, id):
	about_me = client.get('/me/albums/'+ id +'/videos?per_page=50&sort=manual', params={"fields": "name,link,pictures.sizes.link"})
	assert about_me.status_code == 200 
	data_encoded = json.dumps(about_me.json())
	data_decoded = json.loads(data_encoded)
	video_data = data_decoded["data"]
	return video_data

def get_thumbnails(json_list):
	thumbnail_list =[]
	for i in range(len(json_list)):
		filtered = json_list[i]['pictures']
		more_filter = filtered.get('sizes')
		tn = more_filter[4]['link']
		thumbnail_list.append(tn)
	return thumbnail_list

#Landing page of app, includes video data list & thumbail list
@app.route('/')
def landing():
	#Replace album_id with a public Vimeo album; You can find it in the URL 
	#Example: https://vimeo.com/showcase/7693012
	album_id = '7693012'
	main_result = decode_json_reel(client, album_id)
	reel_thumbnail_list = get_thumbnails(main_result)
	return render_template('index.html', main_result=main_result, reel_thumbnail_list=reel_thumbnail_list)

if __name__ == '__main__':
		app.run(debug=True)
