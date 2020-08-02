import requests

superhero_list = ['Hulk','Captain America', 'Thanos']
superhero_intelligence = {}
syper_dict = {}
count = 0

for hero in superhero_list:
    response = requests.get(f'https://www.superheroapi.com/api.php/2619421814940190/search/{hero}')
    #print(response.json())
    intelligence = int(response.json()['results'][0]['powerstats']['intelligence'])
    superhero_intelligence[hero] = intelligence
#print(superhero_intelligence)
print(f'Самый умный супер герой - {max(superhero_intelligence)} с интеллектом {max(superhero_intelligence.values())}')


