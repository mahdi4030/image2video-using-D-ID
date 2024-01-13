import time
import random
import requests

auth_bearer = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik53ek53TmV1R3ptcFZTQjNVZ0J4ZyJ9.eyJodHRwczovL2QtaWQuY29tL2ZlYXR1cmVzIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9jeF9sb2dpY19pZCI6IiIsImh0dHBzOi8vZC1pZC5jb20vY2hhdF9zdHJpcGVfc3Vic2NyaXB0aW9uX2lkIjoiIiwiaHR0cHM6Ly9kLWlkLmNvbS9zdHJpcGVfY3VzdG9tZXJfaWQiOiIiLCJpc3MiOiJodHRwczovL2F1dGguZC1pZC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMDc0MTM1NDE0MjczNjA3MTIwMTgiLCJhdWQiOlsiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS9hcGkvdjIvIiwiaHR0cHM6Ly9kLWlkLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2OTExNzY5OTEsImV4cCI6MTY5MTI2MzM5MSwiYXpwIjoiR3pyTkkxT3JlOUZNM0VlRFJmM20zejNUU3cwSmxSWXEiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIHJlYWQ6Y3VycmVudF91c2VyIHVwZGF0ZTpjdXJyZW50X3VzZXJfbWV0YWRhdGEgb2ZmbGluZV9hY2Nlc3MifQ.Ysvx24o9el-KAju2VS8iq8EnQdh5CCBoQZOlD-oDp0q_DgrYhHr_uOt_WmxFWBULvhykcXu5_p5cBlfHzykp5H-5l8HNLvf0b4PWo-cSFzAgrgDgmDVpmGFEWEAZaeMO9TikhoRCUFnPDehayYKfBEK8FTX0c36y4DZFrhkGS6X5j3UsZoirhSva7ZDkxI7YliuDF2QZmtTnqDMetKtBw6BdG9-BZ2f5WsaxvcHECBAeNS44qQALVECPn0c-IJf53G8NTgHL1JXiJpVVL4Rl4aRpbkdUkVWIcUKMeUTqNnFDBhkCLF7Kmryedag2GvS3mubYZSkSMLTTJ__Ujl8ijA"

specific_driver_list = [
    "nostalgia/driver-01",
    "stitch/driver-05",
    "stitch/driver-10",
    "classics/driver-rocking-around",
    "subtle/driver-01",
    "fun/driver-02",
    "classics/driver-on-my-way",
    "dance/driver-07",
    "subtle/driver-08",
    "classics/driver-feliz-navidad",
    "classics/driver-hope-you-have-happy-birthday",
    "dance/driver-04",
    "classics/driver-country-fire",
    "fun/driver-10",
    "fun/driver-01",
    "subtle/driver-10",
    "nostalgia/driver-15",
    "classics/driver-queen-of-the-night",
    "dance/driver-11",
    "stitch/driver-31",
    "classics/driver-old-souls",
    "stitch/driver-03",
    "nostalgia/driver-09",
    "classics/driver-its-good-to-be-alive",
    "stitch/driver-07",
    "stitch/driver-13",
    "classics/driver-here-comes-santa-claus",
    "stitch/driver-33",
    "subtle/driver-13",
    "nostalgia/driver-03",
    "dance/driver-03",
    "stitch/driver-04",
    "subtle/driver-12",
    "subtle/driver-11",
    "nostalgia/driver-11",
    "stitch/driver-24",
    "classics/driver-la-cucaracha",
    "fun/driver-04",
    "classics/driver-happy-birthday-to-you",
    "stitch/driver-11",
    "subtle/driver-17",
    "dance/driver-02",
    "dance/driver-01",
    "nostalgia/driver-12",
    "dance/driver-09",
    "stitch/driver-12",
    "nostalgia/driver-04",
    "dance/driver-08",
    "nostalgia/driver-10",
    "stitch/driver-30",
    "nostalgia/driver-02",
    "nostalgia/driver-06",
    "nostalgia/driver-14",
    "stitch/driver-22",
    "stitch/driver-14",
    "subtle/driver-02",
    "classics/driver-la-traviata-female",
    "stitch/driver-15",
    "stitch/driver-08",
    "stitch/driver-18",
    "subtle/driver-04",
    "subtle/driver-09",
    "subtle/driver-03",
    "stitch/driver-17",
    "stitch/driver-21",
    "nostalgia/driver-16",
    "subtle/driver-05",
    "stitch/driver-27",
    "nostalgia/driver-07",
    "stitch/driver-32",
    "stitch/driver-25",
    "subtle/driver-15",
    "stitch/driver-16",
    "stitch/driver-06",
    "dance/driver-10",
    "stitch/driver-23",
    "nostalgia/driver-05",
    "nostalgia/driver-08",
    "dance/driver-06",
    "dance/driver-05",
    "stitch/driver-19",
    "fun/driver-07",
    "subtle/driver-19",
    "classics/driver-amazing",
    "stitch/driver-09",
    "subtle/driver-07",
    "fun/driver-09",
    "subtle/driver-16",
    "classics/driver-rigoletto",
    "stitch/driver-20",
    "fun/driver-06",
    "subtle/driver-18",
    "nostalgia/driver-17",
    "subtle/driver-06",
    "stitch/driver-26",
    "stitch/driver-29",
    "fun/driver-03",
    "fun/driver-08",
    "stitch/driver-02",
    "classics/driver-la-traviata-male",
    "fun/driver-05",
    "subtle/driver-14",
    "stitch/driver-01"
]

files = [
    "face_input_1.png",
    "face_input_2.jpeg"
]

types = [
    "image/png",
    "image/jpeg"
]

def get_specific_animation(id):
    # get animation
    url = "https://api.d-id.com/animations/" + id

    headers = {
        "accept": "application/json",
        "authorization": auth_bearer
    }

    response = requests.get(url, headers=headers)
    return response.json()


for idx, file in enumerate(files, start=0):
    # upload image
    url = "https://api.d-id.com/images"
    files = { "image": ("./images/" + file, open("./images/" + file, "rb"), types[idx]) }
    headers = {
        "accept": "application/json",
        "authorization": auth_bearer
    }

    response = requests.post(url, files=files, headers=headers)
    json = response.json()
    # print(json)

    # create animation
    url = "https://api.d-id.com/animations"
    payload = {
        "source_url": json["url"],
        "driver_url": "bank://" + random.choice(specific_driver_list)
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": auth_bearer
    }

    response = requests.post(url, json=payload, headers=headers)
    json = response.json()
    # print(json)

    anim_result = get_specific_animation(json["id"])
    if not anim_result["result_url"]:
        time.sleep(1)
        anim_result = get_specific_animation(json["id"])
    # print(json)

    r = requests.get(anim_result["result_url"], stream = True) 

    with open("./animations/" + "".join(file.split(".")[:-1]) + ".mp4", 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk)
    
    print(file + " completed")


print("\n--- All done! ---")