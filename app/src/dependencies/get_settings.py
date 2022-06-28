from functools import lru_cache

from ..core import main as core_main

@lru_cache(maxsize=1)
def get_settings():
  return core_main.Settings()