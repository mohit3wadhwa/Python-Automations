import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
#url = "https://api.github.com/rate_limit"
req = requests.get(url)

print("Status Code: ",  req.status_code)

res_dict = req.json()
#print(res_dict["total_count"])
print(res_dict.keys())


var = res_dict["items"]

print("Total items: ", len(var))
items_count = len(var)

name, star = [],[]

print("-------------> ", type(var))
for key in var:
	name.append(key["name"])
	star.append(key["stargazers_count"])

print(name)
print(star)

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=True)
chart.x_labels = name
chart.add("", star)
chart.render_to_file("py_projects.svg")

# while count < items_count:
#  	print()
#print("first Repo: ", var[0] )

#first_repo = var[0]


#for keyss, value in first_repo.items():
# 	print("\nKey: ", keyss, " Value: ", value)

