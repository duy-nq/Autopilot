import argparse

def get_config():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--model_path', type=str, default='MiraiSan')
    parser.add_argument('--threshold', type=float, default=0.5)
    parser.add_argument('--video_path', type=str, default='Footage/')
