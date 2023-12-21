import os
import subprocess
# import shutil
from dotenv import load_dotenv

load_dotenv()

github_username = os.getenv('GH_USERNAME')
repository_name = os.getenv('GH_REPO')
branch_name = 'main'
local_repo_path = '/Users/emilioandere/img_url'
image_folder = 'images/'

def upload_image(image_path):
    # destination = os.path.join(local_repo_path, image_folder, os.path.basename(image_path))
    # shutil.copy(image_path, destination)

    os.chdir(local_repo_path)

    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Add new image'])
    subprocess.run(['git', 'push', 'origin', branch_name])

    permalink = f'https://raw.githubusercontent.com/{github_username}/{repository_name}/{branch_name}/{image_folder}/{os.path.basename(image_path)}'
    return permalink


image_path = './images/images.jpeg'
permalink = upload_image(image_path)
print("Image Permalink: ", permalink)