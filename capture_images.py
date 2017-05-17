import os
import re
import time
import sys

def generate_captures_folder(ts):
    try:
        os.popen('mkdir captures/'+ts)
        os.popen('mkdir videos/'+ts)
        return True
    except:
        print('Not able to create folder for captures. Please check permissions into folfer')
        return False

def get_capture(device,folder):
    search_name = {'iphone': 'kCGWindowOwnerName = Simulator', 'android': "kCGWindowName = \"Android Emulator - "}
    pid = 0
    temp = os.popen('./helpers/GetWindowList 2>&1').read().strip().split('},')
    for i in temp:
        match = re.search(search_name[device], i)
        if match is not None:
            match = re.search('kCGWindowNumber = (\d+);', i)
            pid = match.group(1)
    file = "captures/" + folder + "/" +str(int(time.time()))+ ".png"
    os.popen("screencapture -l" + str(pid) + " -x " + file)
    return file

def generate_video(device, folder):
    try:
        f = 'videos/'+folder+'/'+device+'.gif'
        print('Creating video: '+f)
        os.popen('convert -delay 20 -loop 0 captures/'+folder+'/*.png '+f)
        print ('Video created!')
        return f
    except: 
        print('Error during images to gif conversion: ',sys.exc_info()[0])
        return None

def delete_images(folder):
    try:
        print('Deleting images...')
        os.popen('rm -rf captures/'+folder+'/*.png')
        os.popen('rm -rf captures/'+folder)
    except:
        print('Error deleting PNGs. Please delete them manually')
