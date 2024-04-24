import os
import shutil

def read_ids_from_txt(file_path):
    with open(file_path, 'r') as f:
        ids = [line.strip() for line in f.readlines()]
    return ids

def move_wav_files(id_list, source_directory, output_directory):
    for id in id_list:
        folder_path = os.path.join(source_directory, id)
        if os.path.exists(folder_path):
            wav_file_path = os.path.join(folder_path, 'cough.wav')
            if os.path.exists(wav_file_path):
                new_wav_file_path = os.path.join(output_directory, f'{id}.wav')
                shutil.copy(wav_file_path, new_wav_file_path)
                print(f"Moved {id}.wav from {wav_file_path} to {new_wav_file_path}")
            else:
                print(f"No 'cough.wav' found in {folder_path}")
        else:
            print(f"Folder {folder_path} does not exist")

wav_directory = 'C:\\Users\\Aadi Jha\\Documents\\python cough sounds\\coswara_data\\kaggle_data'
output_directory_healthy = 'C:\\Users\\Aadi Jha\\Documents\\python cough sounds\\coswara_data\\healthy'
output_directory_asthma = 'C:\\Users\\Aadi Jha\\Documents\\python cough sounds\\coswara_data\\asthma'

healthy_ids = read_ids_from_txt('C:\\Users\\Aadi Jha\\Documents\\python cough sounds\\coswara_data\\healthy_ids2.txt')
asthma_true_ids = read_ids_from_txt('C:\\Users\\Aadi Jha\\Documents\\python cough sounds\\coswara_data\\asthma_true_ids2.txt')

move_wav_files(healthy_ids, wav_directory, output_directory_healthy)

move_wav_files(asthma_true_ids, wav_directory, output_directory_asthma)
