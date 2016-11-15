from .base import Base
import subprocess

class Source(Base):
    
    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git'
        self.kind = 'git'

    def on_init(self, context):
        pass

    def on_close(self, context):
        pass

    def gather_candidates(self, context):

        result = subprocess.run(["git", "branch", "--no-color", "--list"], stdout=subprocess.PIPE, universal_newlines=True)
        candidates = result.stdout
        print(candidates)

        return list(map(
            lambda candidate: {
                    'word': candidate
                }, candidates))
