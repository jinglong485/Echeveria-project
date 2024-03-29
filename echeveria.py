import cv2
import time
import os

def check_time(n):
    if int(time.strftime('%H',time.localtime())) == n:
        return True
    else:
        return False

def main():
    sleep_minutes = 55
    flag = False
    
    while True:
        print('Sleeping for {} minutes. Started at {}'.format(sleep_minutes, time.asctime()))
        time.sleep(sleep_minutes*60)

        for i in range(24):
            if check_time(i):
                flag = True
#        flag = check_time(13)
        if flag == True:
            get_picture()
            get_picture()
            get_picture()
            get_picture()
            get_picture()
            flag = False
        else:
            print('Not right time!')

def get_picture(path = './',folder = 'echeveria-records/'):
    folder_path = "".join((path,folder))
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    time.sleep(0.5)
    cap = cv2.VideoCapture(0)#, cv2.CAP_DSHOW)
    ret, frame = cap.read()
    cap.release()
    cv2.destroyAllWindows() 
    file_name = str(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())) + '.jpg'
    whole_file_path = ''.join((folder_path,file_name))
    print('saving file to: {}'.format(whole_file_path))
    cv2.imwrite(whole_file_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

main()
