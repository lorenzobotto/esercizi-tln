from analysis.Frame import Frame
from analysis.regex import resolve


class DContextModel:
    def __init__(self):
        self.domain_ontology = []  # as a list of Frames

    def _add_frame_to_domain_ontology(self, new_frame: Frame):
        self.domain_ontology.append(new_frame)

    def _create_frames(self):
        generic_frame_1 = Frame(domain="info", intent="user", **{"name": None, "sex":None})
        qst1_frame_1 = Frame(domain="coruscant", intent="qst1")
        qst2_frame_1 = Frame(domain="children", intent="qst2")
        qst3_frame_1 = Frame(domain="pillars", intent="qst3")
        qst4_frame_1 = Frame(domain="kyber", intent="qst4")
        qst5_frame_1 = Frame(domain="order", intent="qst5")
        qst6_frame_1 = Frame(domain="yoda", intent="qst6")
        qst7_frame_1 = Frame(domain="color", intent="qst7")
        qst8_frame_1 = Frame(domain="dagobah", intent="qst8")
        qst9_frame_1 = Frame(domain="master", intent="qst9")
        qst10_frame_1 = Frame(domain="anakin", intent="qst10")

    def decipher_response(self, user_response: str, domain: str):
        pos, neg = resolve(user_response, [frame for frame in self.domain_ontology if frame.slot["domain"] == domain])
        if pos and not neg:
            incomplete_frames = [frame.slot["domain"] for frame in self.domain_ontology if not frame.complete]



