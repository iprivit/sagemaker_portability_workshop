import pickle
import tarfile
import os

def model_fn(model_dir):
#     with tarfile.open(f'{model_dir}/decision-tree-model.tar.gz','r:gz') as tar:
#         tar.extractall()
    print(os.system(f'ls {model_dir}'))
    model = pickle.load(open(f'{model_dir}/decision-tree-model.pkl','rb'))
    return model