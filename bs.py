import pandas as pd
from instagramy import InstagramUser
import json
import os


def get_instagramy_bios(data):
    bios = []
    for i, name in enumerate(data.name):
        print(i, name)

        try:
            user = InstagramUser(name, sessionid=os.environ.get('SESSION_ID'))
            print(user)
            bio = user.biography
        # except instagramy.core.exceptions.UsernameNotFound:
        except Exception as e:
            print(e)
            bio = ''

        bios.append(bio)

    with open('bios.json', 'w') as f:
        json.dump(bios, f, ensure_ascii=False)


data = pd.read_csv('newBaik.csv')
bios = get_instagramy_bios(data)
