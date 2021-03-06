import os

import instaloader
L = instaloader.Instaloader()

USER = 'YOUR IG USERNAME'
PASSWORD = 'YOUR PASS'
PROFILE = USER
CONFIGFILE= USER

if os.path.exists(CONFIGFILE) ==False:
    L.login(USER,PASSWORD)
    L.save_session_to_file(USER)

# Your preferred way of logging in:
L.load_session_from_file(USER,USER)
def createDir(dir):
    if os.path.exists(dir)==False:
        os.makedirs(dir)

stories = L.get_stories();
for story in stories:
    # story is a Story object
    items = story.get_items();
    for item in items :
        mypath = os.path.join('stories', story.owner_username, item.date_local.strftime("%Y_%m_%d"))
        createDir(mypath)
        L.download_storyitem(item, mypath)
