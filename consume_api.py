#  Created by Bogdan Trif on 2021.08.30 , 5:24 PM ; btrif
import requests
import json

response = requests.get(
             "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
             )
print(response)
for question in response.json()['items'] :
    if question['answer_count'] == 0 :
        print( question  )
        print( question['title']  )
        print( question['link']  )
        print()
    else :
        print("skipped")
        print()




