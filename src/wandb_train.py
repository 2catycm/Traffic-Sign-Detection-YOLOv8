from datetime import datetime
from munch import DefaultMunch, Munch
from ultralytics.yolo.utils import yaml_load, yaml_save
from pathlib import Path
this_file = Path(__file__).resolve().absolute()
this_directory = this_file.parent
def get_current_time_str():
    return datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f') # 尽可能避免冲突
import random
import os
def main(params:dict):
    params = dict(params)
    if str(params["device"])=='auto':
        params['device'] = GPUManager().auto_choice()
    path = this_directory.parent / 'tmp_yaml'/ f'train_{get_current_time_str()}_{random.randint(0, 65535)}.yaml'
    yaml_save(path.as_posix(), params)
    code = os.system(f"yolo cfg={path.as_posix()}")
    if code==0:
        path.unlink() # 删除临时文件
    else:
        print(f"警告，运行失败。临时配置文件为{path}")

import argparse
# import wandb
#%%
from gpu_manager import GPUManager
if __name__ == '__main__':
    # 先获得命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('--param', '--params', '-p', 
                        default=(this_directory.parent / 'test_train.yaml').as_posix())
    args = parser.parse_args()
    params = yaml_load(args.param)
    # # wandb 设置
    # wandb.init(
    #     # set the wandb project where this run will be logged
    #     project="YOLOv8-Traffic-Sign",
    # )
    # wandb.config.update(params)
    # main(wandb.config)
    main(params)


    
    

