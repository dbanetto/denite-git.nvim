
from .base import Base

class Kind(Base):
    
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git'
        self.default_action = 'git'

