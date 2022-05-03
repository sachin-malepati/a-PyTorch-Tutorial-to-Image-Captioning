from utils import create_input_files

if __name__ == '__main__':
    # Create input files (along with word map)
    create_input_files(dataset='coco',
                       karpathy_json_path='/home/amm9801/coco/dataset.json',
                       image_folder='/coco/',
                       captions_per_image=5,
                       min_word_freq=5,
                       output_folder='/home/amm9801/temp_op/',
                       max_len=50)
