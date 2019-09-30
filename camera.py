import sys
import os
import twython
import time
import datetime
import picamera

def capture(filename):
        with picamera.PiCamera() as camera:
                FILEFORMAT = 'jpeg'
                camera.resolution = (1024, 768)
                time.sleep(2)
                camera.capture(filename + '.' + FILEFORMAT, format=FILEFORMAT)
                return filename + '.' + FILEFORMAT

def timestamp():
        tstring = datetime.datetime.now()
        return tstring.strftime("%Y%m%d_%H%M%S")

def delete(file):
        os.system("rm " + file)

def tweet(file):
        message = "ENTER YOUR MESSAGE HERE"
        twitter = twython.Twython('', '', '', '')
        photo = open(file, 'rb')
        response = twitter.upload_media(media=photo)
        twitter.update_status(status=message, media_ids=[response['media_id']])

def main():
        filename = timestamp()
        file = capture(filename)
        tweet(file)
        delete(file)

if __name__ == '__main__':
        main()
