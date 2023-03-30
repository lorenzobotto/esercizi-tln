from analysis.Frame import Frame
from analysis.regex import resolve


class DContextModel:
    def __init__(self):
        self.domain_ontology = []  # as a list of Frames

    def _add_frame_to_domain_ontology(self, new_frame: Frame):
        self.domain_ontology.append(new_frame)

    def _create_frames(self):
        pass
    generic_frame_1 = Frame(question="user", domain="info", intent="user", **{"name": None, "sex":None})
    # generic_frame_2 = Frame()
    qst1_frame_1 = Frame(domain="coruscant", intent="qst1")
    qst2_frame_2 = Frame(domain="children", intent="qst2")
    qst2_frame_3 = Frame(domain="pillars", intent="qst3")
    qst2_frame_4 = Frame(domain="kyber", intent="qst4")
    qst2_frame_5 = Frame(domain="order", intent="qst5")
    qst2_frame_6 = Frame(domain="yoda", intent="qst6")
    qst2_frame_7 = Frame(domain="color", intent="qst7")
    qst2_frame_8 = Frame(domain="dagobah", intent="qst8")
    qst2_frame_9 = Frame(domain="master", intent="qst9")
    qst2_frame_10 = Frame(domain="anakin", intent="qst10")

    def decipher_response(self, user_response: str, domain: str):
        pos, neg = resolve(user_response, [frame for frame in self.domain_ontology if frame.slot["domain"] == domain])
        if pos and not neg:
            incomplete_frames = [frame.slot["domain"] for frame in self.domain_ontology if not frame.complete]



