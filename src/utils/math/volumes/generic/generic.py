class GenericVolume:
    def __init__(self, max_height:float=0):
        self._max_height = max_height
        self.MAX_VOLUME = self.calculate_volume(self._max_height)
        pass
    
    def calculate_volume(self, depth:float)->float:
        return 0.0
    
    @property
    def max_volume(self):
        return self.MAX_VOLUME
    
    @property
    def max_height(self):
        return self._max_height