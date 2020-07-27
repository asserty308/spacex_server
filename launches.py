import http.client
import json

def get_next_launch():
    try:
        conn = http.client.HTTPSConnection('api.spacexdata.com')
        conn.request('GET', '/v3/launches/upcoming')
        res = conn.getresponse()

        data = res.read()
        conn.close()

        launches = json.loads(data.decode('utf-8'))
        next_launch = launches[0]
        
        return next_launch
    except:
        return 0
