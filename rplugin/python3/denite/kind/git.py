
from .base import Base
import subprocess

class Kind(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git'
        self.default_action = 'checkout'

    def action_checkout(self, context):
        target = context['targets'][0]
        subprocess.run(['git', 'checkout', target['action__checkout']],
                       stdout=subprocess.PIPE)
