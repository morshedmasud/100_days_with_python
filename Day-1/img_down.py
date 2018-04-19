# i used 'requests' module for this
import requests
# first of all we need our img url.
img_url = "https://scontent.fdac5-1.fna.fbcdn.net/v/t1.0-9/22308687_1940109512897958_3667885506092080027_n.jpg?_nc_cat=0&oh=efb468a0bde51cfb46de0abdf5cd2557&oe=5B67F84E"
# i'm using 'get' function for download image.
res = requests.get(img_url)
# save the image in 'img.jpg'
with open("Day-1/img.png", "wb") as f:
    f.write(res.content)
