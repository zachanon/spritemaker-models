import argparse
import os
import sys
import datetime
import time
import math
import json
from pathlib import Path

def get_args_parser():
    parser = argparse.ArgumentParser('spritemaker', add_help=False)

    #model parameters
    parser.add_argument()

    #training parameters
    parser.add_argument()

def train(args):
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser('spritemaker', parents=[get_args_parser()])
    args = parser.parse_args()
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    train(args)