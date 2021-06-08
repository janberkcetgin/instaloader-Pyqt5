import sys
from PyQt5.QtWidgets import *
from login import *
from window2 import *
from show_information import *
from download_all_posts import *
from download_profile_photo import *
from do_not_fallowback import *

import instaloader

insta = instaloader.Instaloader()

#--------------------------------------
app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_loginform()
ui.setupUi(window)
window.show()
#---------------------------------------
app2 = QApplication(sys.argv)
window2 = QMainWindow()
ui2 = Ui_window2()
ui2.setupUi(window2)

#----------------------------------------
app3 = QApplication(sys.argv)
window3 = QMainWindow()
ui3 = Ui_window3()
ui3.setupUi(window3)
#-----------------------------------------
app4 = QApplication(sys.argv)
window4 = QMainWindow()
ui4 = Ui_all_post()
ui4.setupUi(window4)
#----------------------------------------
app5 = QApplication(sys.argv)
window5 = QMainWindow()
ui5 = Ui_profile_photo()
ui5.setupUi(window5)
#-----------------------------------------
app6 = QApplication(sys.argv)
window6 = QMainWindow()
ui6 = Ui_do_not_fb()
ui6.setupUi(window6)
#-----------------------------------------


def login1():
    try:
        username = ui.lineEdit_username.text()
        password = ui.lineEdit_password.text()
        insta.login(username,password)
        window2.show()
    except:
        ui.statusbar.showMessage("Something went wrong!",5000)


def show_information():
    window3.show()


def show_information2():
    try:
        username = ui3.lineEdit.text()
        profile1 = instaloader.Profile.from_username(insta.context,username)
        ui3.textEdit.setText(f"Number of posts: {profile1.mediacount}\nNumber of fallowers: {profile1.followers}\n"
                             f"Number of followed: {profile1.followees}\nBiography: {profile1.biography}\n"
                             f"Web site: {profile1.external_url}")
    except:
        ui3.statusbar.showMessage("Something went wrong!",5000)

def all_posts():
    window4.show()



def tum_postlari_indir():
    try:
        username = ui4.lineEdit.text()
        profile2 = instaloader.Profile.from_username(insta.context, username)

        posts = profile2.get_posts()
        for index, post in enumerate(posts,1):
            insta.download_post(post, target=f"{profile2.username}_{index}")
    except:
        ui4.statusbar.showMessage("Something went wrong!",5000)

def profil_foto():
    window5.show()

def download_profile_photo():
    try:
        username = ui5.lineEdit.text()
        insta.download_profile(username, profile_pic_only=True)
    except:
        ui5.statusbar.showMessage("Something went wrong!",5000)
def do_not_fallowback():
    window6.show()

def do_not_fallowback_show():
    username = ui.lineEdit_username.text()
    profilez = instaloader.Profile.from_username(insta.context, username)
    followers = profilez.get_followers()
    followees = profilez.get_followees()

    followers_list = list()
    followees_list = list()
    new_list = list()


    for i in followers:
        followers_list.append(i.username)
    for j in followees:
        followees_list.append(j.username)

    for z in followees_list:
        if z not in followers_list:
            new_list.append(z)
    ui6.textEdit.setText(f"Users who don't follow you: {new_list}")


#signals
ui.pushButton_login.clicked.connect(login1)
ui2.pushButton_show_information.clicked.connect(show_information)
ui3.pushButton.clicked.connect(show_information2)
ui2.pushButton_download_all_post.clicked.connect(all_posts)
ui4.pushButton.clicked.connect(tum_postlari_indir)
ui2.pushButton_download_profile_photo.clicked.connect(profil_foto)
ui5.pushButton.clicked.connect(download_profile_photo)
ui2.pushButton_fb.clicked.connect(do_not_fallowback)
ui6.pushButton.clicked.connect(do_not_fallowback_show)
sys.exit(app.exec_())
