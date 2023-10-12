import subprocess

subprocess.Popen('!pip install -r /kaggle/working/ge-sc/requirements.txt -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html -f https://data.pyg.org/whl/torch-1.8.0+cu111.html -f https://data.dgl.ai/wheels/repo.html', shell=True)
