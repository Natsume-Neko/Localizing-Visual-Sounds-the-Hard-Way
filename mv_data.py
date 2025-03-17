import glob
import shutil

general_path = './Dataset/'
data_path = general_path + 'Data/'
for i in range(10):
    cur_path = data_path + f'{i}/'
    for audio_path in glob.glob(cur_path + '*.wav'):
        audio_name = audio_path[len(cur_path):]
        shutil.copy(audio_path, './datapath/audio/' + audio_name)
    for frame_path in glob.glob(cur_path + '*.jpg'):
        frame_name = frame_path[len(cur_path):]
        shutil.copy(frame_path, './datapath/frames/' + frame_name)