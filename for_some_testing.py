from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print(f'BASE_DIR: {BASE_DIR}')
print(f'__file__: {__file__}')
print(f'Path(__file__).resolve().parent : {Path(__file__).resolve().parent }')
print(f'Path(__file__).resolve().parent.parent : {Path(__file__).resolve().parent.parent }')
MEDIA_ROOT = os.path.join(Path(__file__).resolve().parent, 'customerinfo/static')
print(f'MEDIA_ROOT: {MEDIA_ROOT}')