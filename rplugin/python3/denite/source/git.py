from .base import Base
import subprocess


class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'git'
        self.kind = 'git'
        # TODO: allow this to be configuable
        self.__branch_cmd = ['git', 'branch', '--no-color', '--list', '--all', '-vv']

    def on_init(self, context):
        pass

    def on_close(self, context):
        pass

    def gather_candidates(self, context):

        result = subprocess.run(self.__branch_cmd, stdout=subprocess.PIPE)

        candidates = []

        for candidate in result.stdout.decode('UTF-8').splitlines():

            candidate = candidate.strip().strip('* ')
            branch = candidate.split(' ')[0]

            candidates.append({
                'kind': 'git',
                'action__checkout': branch,
                'word': candidate
            })

        return candidates
