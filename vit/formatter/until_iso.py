from vit.formatter.until import Until

class UntilIso(Until):
    def format_datetime(self, until, task):
        return self.iso(until)
