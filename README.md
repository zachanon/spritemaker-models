# spritemaker-models
Repository tracking the code for training sprite-generating neural network models.

### Using with docker

First pull the pytorch image
```
docker pull pytorch/pytorch
```

To run with NVIDIA
```
docker run --gpus all -v <data directory>:/workspace pytorch/pytorch:latest [SCRIPT] [OPTIONS]
```
