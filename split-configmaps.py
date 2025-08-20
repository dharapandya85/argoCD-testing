import os
import shutil
SOURCE_DIR="./"
BATCH_PREFIX="config-batch-"
FILES_PER_BATCH=50
files=sorted([f for f in os.listdir(SOURCE_DIR) if f.startswith("configmap-") and f.endswith(".yaml")])
batch_num=1
for i in range(0,len(files), FILES_PER_BATCH):
    batch_dir=f"{BATCH_PREFIX}{batch_num}"
    os.makedirs(batch_dir,exist_ok=True)
    for f in files[i:i+FILES_PER_BATCH]:
        shutil.move(os.path.join(SOURCE_DIR,f),os.path.join(batch_dir,f))
    print(f"Moved {len(files[i:i+FILES_PER_BATCH])} files -> {batch_dir}")
    batch_num+=1