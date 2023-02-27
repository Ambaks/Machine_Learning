from moviepy.editor import *
import csv
from datetime import datetime
import os

def generate_clips(video_path, timestamps_path):
    # Load timestamp text file
    with open(timestamps_path, "r") as f:
        timestamps = []
        folders = []
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            data_tuple = tuple(int(i) for i in row[1:])
            folders.append(row[0])
            timestamps.append(data_tuple)

    #Get timestamps
    counter = 0
    processed_files_counter = 0
    file_name = os.path.basename(video_path)
    for timestamp, folder in zip(timestamps, folders):
        if os.path.exists(f'/Users/naiahoard/PycharmProjects/Clip_generator/{folder}/{folder}_{os.path.splitext(file_name)[0]}_{counter}.mp4'):
            counter += 1
            processed_files_counter += 1

        else:
            # Of format (h, m, s)
            ta = (timestamp[0], timestamp[1], timestamp[2] - 3)
            tb = (timestamp[0], timestamp[1], timestamp[2] + 3)

            full_clip = VideoFileClip(video_path)
            new_clip = full_clip.subclip((ta), (tb)).without_audio()
            new_clip.write_videofile(f'/Users/naiahoard/PycharmProjects/Clip_generator/{folder}/{folder}_{os.path.splitext(file_name)[0]}_{counter}.mp4',codec='libx264')
            counter +=1

    return print('Done.'), print(f'Total timestamps: {counter}'), print(f'Potential duplicates skipped: {processed_files_counter} timestamps')




start_time = datetime.now()
generate_clips('Heat-Celtics.mp4', 'timestamps.txt')
end_time = datetime.now() - start_time

print(f'Computation time: {round(end_time.seconds, 2)} seconds')
