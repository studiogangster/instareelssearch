import requests
import traceback


def login():
    url = "https://i.instagram.com/api/v1/accounts/login/"

    payload = "signed_body=SIGNATURE.%7B%22jazoest%22%3A%2222292%22%2C%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2244%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22d20596c5-4720-4e34-a478-76dc8069f0ff%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A4%3A1647081061%3AAU%2FVoc1%2F0yiJY4l5feYAAT82Eu9tP8Lxyu5dQcTjsfZcBsAzv3%2BvfrDpq9yKECs7eNqfdXEu2LUwb%2BukJ9tKUgfyzDaLwIPliDJXHzelvlQOddmUKLzS%2BXa52sBAp1AL40mXAOPksbkgwTJQfVLnwiQz4BUDYRYd8ox5Y2Obw%2FVhxp0mR6fqZ%2BhUi%2BaWt0V%2FzK67aiSeS1I6n6mgbjBUZTF8IpT%2BcaqNAZeZof%2FzpmcjYj7TKqlBoXO%2FTnkJf%2BKL3aMxuvLkRKQLO00hCxj93miufSLpEsAe7vXH%2FLQx9eOT%2BZp%2BvmwR2YnmjtJMSTgLxoov4X0SPGaEwdIWKp4vk5TO2Cr3pmCjeXukebZgS8DqBhFo%2FcOXOCKofBPqVhCDUMIjSgRPKJs%3D%22%2C%22username%22%3A%22ninaaisoft%40gmail.com%22%2C%22adid%22%3A%226b57fe85-7222-49c4-85fe-a77cb116e7a6%22%2C%22guid%22%3A%2244743578-5663-437a-85c2-6803f21f27ab%22%2C%22device_id%22%3A%22android-ad850d8f23d24d8f%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D"
    headers = {
    'X-IG-App-Locale': 'en_GB',
    'X-IG-Device-Locale': 'en_GB',
    'X-IG-Mapped-Locale': 'en_GB',
    'X-Pigeon-Session-Id': 'UFS-35445475-1b61-4775-911a-39e042802044-3',
    'X-Pigeon-Rawclienttime': '1647081061.919',
    'X-IG-Bandwidth-Speed-KBPS': '6270.000',
    'X-IG-Bandwidth-TotalBytes-B': '645829',
    'X-IG-Bandwidth-TotalTime-MS': '103',
    'X-IG-App-Startup-Country': 'IN',
    'X-Bloks-Version-Id': '54a609be99b71e070ffecba098354aa8615da5ac4ebc1e44bb7be28e5b244972',
    'X-IG-WWW-Claim': '0',
    'X-Bloks-Is-Layout-RTL': 'false',
    'X-Bloks-Is-Panorama-Enabled': 'true',
    'X-IG-Device-ID': '44743578-5663-437a-85c2-6803f21f27ab',
    'X-IG-Family-Device-ID': 'd20596c5-4720-4e34-a478-76dc8069f0ff',
    'X-IG-Android-ID': 'android-ad850d8f23d24d8f',
    'X-IG-Timezone-Offset': '19800',
    'X-IG-Nav-Chain': '9cb:self_profile:4,8jo:bottom_sheet_profile:6,AQ1:settings_category_options:7,A37:add_account_bottom_sheet:8,9vd:login_landing:9',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTv10=',
    'X-IG-App-ID': '567067343352427',
    'Priority': 'u=3',
    'User-Agent': 'Instagram 212.0.0.38.119 Android (31/12; 450dpi; 1080x2327; samsung; SM-G985F; y2s; exynos990; en_GB; 329675731)',
    'Accept-Language': 'en-GB, en-US',
    'X-MID': 'YixVagABAAFR6fzjs2rzLKbOlQek',
    'IG-INTENDED-USER-ID': '0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'Connection': 'close',
    'Content-Length': '1038'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    auth = response.headers['ig-set-authorization']

    auth = auth#.split(":")[-1]
    print("auth", auth)
    print(auth)
    return auth


AUTH_TOKEN = login()

# AUTH_TOKEN = "eyJkc191c2VyX2lkIjoiNTEwMTM2NjA3NzMiLCJzZXNzaW9uaWQiOiI1MTAxMzY2MDc3MyUzQW94cjI2anFUZFRBSE1KJTNBMjgiLCJzaG91bGRfdXNlX2hlYWRlcl9vdmVyX2Nvb2tpZXMiOnRydWV9"


Headers = {
    'User-Agent': 'Instagram 212.0.0.38.119 Android (31/12; 450dpi; 1080x2327; samsung; SM-G985F; y2s; exynos990; en_GB; 329675731)',
    'Authorization': '{}'.format(AUTH_TOKEN),
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    # 'Cookie': 'ig_did=04D31262-9480-46E8-BB93-5C86BE752D7B; ig_nrcb=1; mid=YiyqowAEAAHQsJ8ov16Miyc3lIgt'
    }

import requests

# AUTH_TOKEN = "eyJkc191c2VyX2lkIjoiNTIxOTE1MDc3MTAiLCJzZXNzaW9uaWQiOiI1MjE5MTUwNzcxMCUzQW1VUzIzWnRjaFh5QjBuJTNBMiIsInNob3VsZF91c2VfaGVhZGVyX292ZXJfY29va2llcyI6dHJ1ZX0"


def getSongDetails(clusterId, assetId):
    url = "https://i.instagram.com/api/v1/clips/music/"

    payload = "audio_asset_id={}&audio_cluster_id={}".format(assetId,  clusterId)
    headers = Headers
    Headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()


def searchSong(title):

    url = "https://i.instagram.com/api/v1/music/audio_global_search/?search_surface=audio_serp_page&timezone_offset=19800&count=30&query={}".format(title)

    payload={}
    headers = Headers

    response = requests.request("GET", url, headers=headers, data=payload)

    # print("content",  response.text)
    return response.json()


def _searchSong(title):

    url = "https://i.instagram.com/api/v1/music/audio_global_search/?search_surface=audio_serp_page&timezone_offset=19800&count=30&query={}&browse_session_id=26dd094f-ba73-4f38-8211-3f05692fe081".format(title)

    payload={}
    headers = Headers

    response = requests.request("GET", url, headers=headers, data=payload)

    print(Headers, response.json())
    return response.json()


def SearchSong(query):
    res = _searchSong(query)["items"][0]["track"]
    # print(res)
    clusterId, assetId = res["audio_cluster_id"] ,  res["id"] 
    print(clusterId, assetId)
    res = getSongDetails('453007299865290', '453007299865290')#["formatted_media_count"]#["items"][0]#["media"]#["play_count"]
    # res = getSongDetails(clusterId, assetId)#["formatted_media_count"]#["items"][0]#["media"]#["play_count"]
    # print(res)
    return res
    # print(clusterId, assetId)


from flask import Flask , jsonify
app = Flask(__name__)

# login()
# _=SearchSong("do gallan");print(_)

@app.route('/')
def index():
    return jsonify({"status": True, "api_service": "Enabled"})

@app.route('/<query>')
def user(query):
    try:
        print("SearchSong")
        res = SearchSong(query)
        print("SearchSong",  res)
        reel_count = res["formatted_media_count"]
        return jsonify({"status": True, "count_reel": reel_count ,  "details": res  })
    except:
        traceback.print_exc()
        return jsonify({"status": False, "message": "Service is Down!"})
	# return '<h1>Hello, {0}!</h1>'.format(query)

if __name__ == '__main__':
    app.run(debug=False, port=7878, host="0.0.0.0")
