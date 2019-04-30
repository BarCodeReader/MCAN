import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import json
import argparse
import importlib
from solver import Solver

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str)
    parser.add_argument("--ckpt_name", type=str)
    parser.add_argument("--print_interval", type=int, default=1000)
    parser.add_argument("--train_data_path", type=str, 
                        default="dataset/DIV2K_train.h5")
    parser.add_argument("--ckpt_dir", type=str,
                        default="checkpoint")
    parser.add_argument("--ckpt_path", type=str, default="None")
    parser.add_argument("--sample_dir", type=str, default="sample/")
    
    parser.add_argument("--num_gpu", type=int, default=1)
    parser.add_argument("--shave", type=int, default=20)
    parser.add_argument("--scale", type=int, default=2)
    parser.add_argument("--group", type=int, default=1)
    parser.add_argument("--patch_size", type=int, default=64)
    parser.add_argument("--batch_size", type=int, default=64)
    parser.add_argument("--max_steps", type=int, default=200000)
    parser.add_argument("--decay_interval", type=int, default=150000)
    parser.add_argument("--decay_chance", type=int, default=150000)
    parser.add_argument("--lr", type=float, default=0.0001)
    parser.add_argument("--clip", type=float, default=10.0)
    parser.add_argument("--calculate_metrics", type=str,
                        choices=["None", "one"], default="None")
    return parser.parse_args()

def main(cfg):
    net = importlib.import_module("model.{}".format(cfg.model)).Net
    print(json.dumps(vars(cfg), indent=4, sort_keys=True))
    
    solver = Solver(net, cfg)
    print('fit !')
    solver.fit()
    print('Done')

if __name__ == "__main__":
    cfg = parse_args()
    main(cfg)