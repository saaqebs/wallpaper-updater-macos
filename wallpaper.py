from urllib.request import Request, urlopen
import subprocess
import socket
import os

# The command to change wallpaper for MacOS
command = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""


def get_wallpaper(keywords):
    url = "https://source.unsplash.com/1600x900/?"
    for s in keywords:
        url += s
        url += ","
    return url


def download_wallpaper_from_search(keywords, dir_path):
    image_url = get_wallpaper(keywords)
    req = Request(image_url, headers={
        "User-Agent": "Chrome/24.0.1312.27 Safari/537.17"})
    response = urlopen(req, None, 10).read()
    try:
        output_file = open(dir_path, 'wb')
        output_file.write(response)
    except socket.Timeouterror:
        print('no image results found on website')


def download_wallpaper_from_collection(url, dir_path):
    req = Request(url, headers={
        "User-Agent": "Chrome/24.0.1312.27 Safari/537.17"})
    response = urlopen(req, None, 10).read()
    try:
        output_file = open(dir_path, 'wb')
        output_file.write(response)
    except socket.Timeouterror:
        print('no image results found on website')


def change_wallpaper(directory):
    subprocess.Popen(command % directory, shell=True)


def delete_old_wallpaper(directory):
    try:
        os.remove(directory)
    except OSError as e:
        print("Error: %s")
