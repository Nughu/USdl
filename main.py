import os
import re
import subprocess
import time

from pytube import YouTube


def check_sos(item):
    if re.match(pattern=r"(^#VIDEO:)(.*$)", string=item):
        return True
    else:
        return False


currentdir = os.getcwd()
raggu = r",(.*$)"
ragga = r"(.*).txt"
riggi = r"(.*),(.*$)"
regge = r"(^#VIDEO:)(.*$)"
roggo = r"(^#AUDIO:.*$)|(^#MP3:.*$)"

print("Starting...\n")
for x in os.listdir():
    if re.match(ragga, x):
        try:
            with open(x, "r") as txt:
                print("\nDownloading " + x.replace(".txt", "") + "...")
                text = txt.readlines()
                mp4name = ((x.replace(".txt", "")) + ".mp4").replace("'", "")
                mp4name2 = ("#VIDEO:" + mp4name)
                mp3name = ((x.replace(".txt", "")) + ".mp3").replace("'", "")
                mp3name2 = ("#MP3:" + mp3name)
                sos_iterator = filter(check_sos, text)
                sosfef = ("".join(list(sos_iterator)))
                sosfuf = sosfef.replace("#VIDEO:", "")
                if re.match(riggi, sosfuf):
                    sosfaf = (re.sub(raggu, "", sosfuf).replace("\n", ""))
                else:
                    sosfaf = (sosfuf.replace("\n", ""))
                sos = sosfaf.replace("a=", "v=")
                ytlink = str("https://www.youtube.com/watch?" + sos)
                ytinst = YouTube(ytlink)
                ytstreams = ytinst.streams
                videostream = ytstreams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
                videostream.download(filename=mp4name, skip_existing=True)
                subprocess.run("ffmpeg -i \"" + mp4name + "\" \"" + mp3name + "\"")
                newtext = [re.sub(regge, mp4name2, l) for l in text]
                newtext2 = [re.sub(roggo, mp3name2, l) for l in newtext]
                newtext3 = "".join(newtext2)
                txt.close()
                time.sleep(1)
            with open(x, "w") as sis:
                sis.write(newtext3)
                sis.close()
                print("Downloaded " + x + " successfully.\n")
        except Exception as e:
            print("Skipping " + x + f"\n{e}")


print("\nQueue finished.")
input()