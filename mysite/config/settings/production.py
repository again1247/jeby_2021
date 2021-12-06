from .base import *

DEBUG = False

STATIC_ROOT = BASE_DIR / "static/"  # 상용에서만 필요함
STATICFILES_DIRS = []  # 각 app안의 정적파일을 찾아가지 않기 때문에 덮어씌웟다... (나중에 찾아보기)
