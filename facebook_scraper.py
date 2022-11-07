from facebook_scraper import get_posts
import os
import requests

# Set parent directory where the posts will be saved
parent_directory = "put parent path"

#Config scraper
user_email = "facebookemail"
user_password = "facebookpassword"
page_id = "pageid"
index = 0

def scrape():
     # Get all posts from a profile and save them to a directory
     for  post in  get_posts( page_id , pages= 100, credentials=( user_email , user_password )):
          post_id = post[ 'post_id' ]
          post_text = post[ 'text' ]
          post_images = post[ 'images' ]
          post_video = post[ 'video' ]
          post_link = post[ 'link' ]
          post_url = post[ 'post_url' ]
          post_likes = post[ 'likes' ]
          post_time = post[ 'time' ]
          post_shared_username = post['shared_username']
          if post_shared_username == None:
               post_shared_username = page_id

          
          # make directory with post id
          path = os.path.join(parent_directory, str(index))
          os.mkdir(path)

          # save text to file
          with open(os.path.join(path, 'text.txt'), 'w', encoding='utf-8') as f:
               f.write(post_text)

          # save link to file if link exists
          if post_link != None:
               with open(os.path.join(path, 'link.txt'), 'w', encoding='utf-8') as f:
                    f.write(post_link)
          
          # download images from images list to path and name them 1, 2, 3, etc.
          for i, image in enumerate(post_images):
               #download image
               image = requests.get(image)
               # save image to file
               with open(os.path.join(path, f'{i}.jpg'), 'wb') as f:
                    f.write(image.content)
          
          # download video from video url to path
          if post_video:
               video = requests.get(post_video)
               # save video to file
               with open(os.path.join(path, 'video.mp4'), 'wb') as f:
                    f.write(video.content)
               
          #save additional info to file
          with open(os.path.join(path, 'info.txt'), 'w', encoding='utf-8') as f:
               f.write(f'Post id: {post_id}\n')
               f.write(f'Post url: {post_url}\n')
               f.write(f'Post likes: {post_likes}\n')
               f.write(f'Post time: {post_time}\n')
               f.write(f'Post creator: {post_shared_username}\n')
          
          index += 1

scrape()