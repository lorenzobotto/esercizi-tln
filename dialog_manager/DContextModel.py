from analysis.Frame import Frame


class DContextModel:
    def __init__(self):
        self.domain_ontology = []  # as a list of Frames

    def append_frame(self, new_frame: Frame):
        self.domain_ontology.append(new_frame)
