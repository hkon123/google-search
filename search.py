from googleapiclient.discovery import build
import pprint

my_api_key = "AIzaSyBl3Yvf-Fjqe35xpGmsgj3YX0hb7V6QonY"
my_cse_id = "009566027274741518800:pm2zzxr7sye"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(
    'regnskapsfører oslo', my_api_key, my_cse_id, num=10)

results2 = google_search(
    'regnskapsfører oslo', my_api_key, my_cse_id, start = 11, num=10)

for result in results:
    print(result['link'])
    #pprint.pprint(result)
for result in results2:
    print(result['link'])
