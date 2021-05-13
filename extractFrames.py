import os
import numpy as np
import cv2
from glob import glob


# this function will create a directory if and only it does not exists
def create_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)

    except OSError:
        print(f"Error: creating directory with name {path}")

# this function will save frames of the video one by one
# def save_frame(video_path,save_dir):
#     name = video_path.split("/")[-1].split(".")[0]
#     # print(name)
#     save_path = os.path.join(save_dir, name)
#     create_dir(save_path)

#     cap = cv2.VideoCapture(video_path)
#     idx = 0

#     while True:
#         ret, frame = cap.read()
#         if ret == False:
#             cap.release()
#             break

#         cv2.imwrite(f"{save_path}/{idx}.png",frame)
#         idx+=1

# function where we have to have gap in frames
def save_frame(video_path, save_dir, gap):
    # print(video_path)
    # name = video_path.split("/")[-1].split(".")[0]
    # # print(name)
    # save_path = os.path.join(save_dir, name)
    save_path = save_dir # path where the frames of the video will be saved
    create_dir(save_dir) #will create a directory of frames in the VidSum Folder named as frames

    cap = cv2.VideoCapture(video_path)
    idx = 0
    frameCount = 0

    while True:
        ret, frame = cap.read()
        if ret == False:
            cap.release()
            break

        if idx == 0:
            cv2.imwrite(f"{save_path}/{frameCount}.png",frame)
            frameCount+=1
        elif idx%gap == 0:
            cv2.imwrite(f"{save_path}/{frameCount}.png",frame)
            frameCount+=1
        idx+=1

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if os.path.isfile(os.path.join(pathIn, f))]
    # print(files)
    # print(len(files))
    # print(os.path.basename(files[0]))
    #for sorting the file names properly
    files.sort(key = lambda x: int(x.split('.')[0]))
    # print(files)

    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()



if __name__ == "__main__":
    # specifying the path in the variable video_paths
    # and save will be our directory for the saved frames
    # video_paths = glob("Videos/*")
    video_paths = glob("Videos/*")
    save_dir = "Frames"


    # if there are multiple videos then it will create
    # different paths that is why a for loop
    # for path in video_paths:
    #     save_frame(path,save_dir)


    # if we want a gap in the frames when we are writing it the directory
    # run this loop instead of the upper for loop
    # and also change the function that is commented above to !commented
    # and vice versa
    gap = 10 # gap between frame (unit - frames)
    for path in video_paths:
        save_frame(path,save_dir,gap)

    
    # frames_path = glob(glob("Frames/*"))

    pathIn= './Frames/'
    pathOut = 'video.avi'
    fps = 10.0
    convert_frames_to_video(pathIn, pathOut, fps)

