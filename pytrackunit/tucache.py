"""tucache module"""

from .webcache import WebCache

class TuCache:
    """tucache class"""
    def __init__(self,auth=None,_dir=None,verbose=False):
        self.cache = WebCache(auth=auth,_dir=_dir,verbose=verbose)
        self._verbose = verbose
    def clean(self):
        """deletes all cached data"""
        self.cache.clean()
    def get(self,url):
        """takes the data from cache if possible. otherwise data is loaded from web"""
        data = self.cache.get(url)
        if self.cache.return_only_cache_files:
            return [data]
        if self.cache.dont_return_data:
            return []
        if self.cache.dont_read_files and len(data) == 0:
            return []
        return data.get('list')
