from os import listdir
import random
import json

dir_path = "C:\\Users\\ahmed\\Desktop\\certificates"
based_github_link_certificates = "https://ahmedcoolprojects.github.io/portfolio/certificates/"
certificate_object = {
    "title": "",
    "sources": ["GDG MENA"],
    "image": "",
    "createdAt": {},
    "updatedAt": {}
}
final_list = []
final_date = ".456Z"


def get_titles(dir_path, github_link):
    for file in listdir(dir_path):
        obj = certificate_object.copy()
        obj["image"] = github_link + file
        one = str(random.randint(10, 50))
        two = str(random.randint(10, 50))
        obj["createdAt"] = {"$date": "2020-11-28T20:" +
                            one + ":" + two + final_date}
        obj["updatedAt"] = {"$date": "2020-11-28T20:" +
                            one + ":" + two + final_date}
        final_list.append(obj)
    return final_list


get_titles(dir_path, based_github_link_certificates)

with open('certificates.json', 'w') as outfile:
    json.dump(final_list, outfile)


print("done")
