import requests
page_no1 = "https://api.github.com/users/emaadmanzoor/repos?page=1&per_page=100"
data_json_1 = requests.get(page_no1)
parsed_data_1 = data_json_1.json()
page_no2 = "https://api.github.com/users/emaadmanzoor/repos?page=2&per_page=100"
data_json_2 = requests.get(page_no2)
parsed_data_2 = data_json_2.json()
sum_page1 = 0
for i in parsed_data_1:
    sum_page1 = sum_page1 + i["stargazers_count"]
    sum_page2 = 0
for i in parsed_data_2:
    sum_page2 = sum_page2 + i["stargazers_count"]
print(sum_page1+sum_page2)


