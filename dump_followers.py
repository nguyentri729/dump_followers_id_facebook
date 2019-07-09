import requests, json
access_token = 'access token here'
stop = False
url = 'https://graph.facebook.com/me/subscribers?method=get&limit=100&access_token='+access_token;
f = open("list_uid.txt","w+")
while stop == False:
	r = requests.get(url);
	try:
		result = json.loads(r.text)
		for fl in result['data']:
			f.write(fl['id']+'\n')
			print(fl['id']+'\n')
		if result['paging']['next'] != '':
			#code
			print(result['paging']['next'])
			url = result['paging']['next']
		else:
			stop = True
	except Exception as e:
		stop = True
	
