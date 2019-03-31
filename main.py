import wallpaper as wp

'''
Global variables you may change according to your preferences.
Information could be found on https://source.unsplash.com/
'''
directory = '/Users/home/Documents/Other/wallpaper/wallpaper.jpg'
collection_url = 'https://source.unsplash.com/collection/3330448/1600x900'
keywords = ['mountains']


def update_wallpaper(is_collection):
    wp.delete_old_wallpaper(directory)
    if (is_collection):
        wp.download_wallpaper_from_collection(collection_url, directory)
    else:
        wp.download_wallpaper_from_search(keywords, directory)
    wp.change_wallpaper(directory)


def update_picture(is_collection):
    wp.delete_old_wallpaper(directory)
    if (is_collection):
        wp.download_wallpaper_from_collection(collection_url, directory)
    else:
        wp.download_wallpaper_from_search(keywords, directory)


def main():
    update_picture(True)


def old_main():
    schedule.every().day.at("02:00").do(update_wallpaper(True))
    update_wallpaper(True)


if __name__ == "__main__":
    main()
