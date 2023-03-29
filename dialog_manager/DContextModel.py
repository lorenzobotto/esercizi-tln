from analysis.Frame import Frame
from analysis.regex import resolve

class DContextModel:
    def __init__(self):
        self.domain_ontology = []  # as a list of Frames
        self.every_every_regex = []

    def append_frame(self, new_frame: Frame):
        self.domain_ontology.append(new_frame)

    def decipher_response(self, user_response: str, question_id):
        feedback = resolve(user_response, [frame for frame in self.domain_ontology if frame.question == question_id])
