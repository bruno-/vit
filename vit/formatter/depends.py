from vit import util
from vit.formatter import List

class Depends(List):
    def format_list(self, depends, task):
        return ','.join(list(map(lambda t: str(util.task_id_or_uuid_short(t)), depends))) if depends else ''

    def colorize(self, depends):
        return self.colorizer.blocked(depends)
