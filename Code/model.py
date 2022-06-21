import copy

class Model:

    def __init__(self, states, pointed_state, valuations, relations):
        self.states = set(states)
        self.pointed_state = pointed_state
        self.valuations = dict(valuations)
        self.relations = dict(relations)
        self.create_reflexive_relations()

    def __repr__(self):
        return (f"Kripke Model:\n"
                f"States: {self.states}\n"
                f"Pointed state: {self.pointed_state}\n"
                f"Valuations: {self.valuations}\n"
                f"Relations: {self.relations}\n"
                )


    def set_states(self, states):
        """This method is based on the intuition that when we want to set
        the states of the model, i.e. take a subset of the original states, 
        we should also change the valuations and relations to reflect this."""
        self.states = set(states)
        for state, valuation in self.valuations.copy().items():
            if int(state) not in self.states:
                del self.valuations[state]

        for agent, relations in self.relations.copy().items():
            for relation in relations.copy():
                if relation[0] not in self.states or relation[1] not in self.states:
                    relations.remove(relation)
            self.relations[agent] = relations

    def create_reflexive_relations(self):
        """Sometimes, writing out all reflexive relations in the model
        can be rather tiresome. This method will do that for us.
        Thus there is no need to explicitly write the reflexive relations 
        in the model, but it is no problem if that should be done."""
        for agent, relations in self.relations.copy().items():
            for state in self.states:
                if (state, state) not in relations:
                    relations.add((state, state))
            self.relations[agent] = relations

    @classmethod
    def copy(cls, model):
        return cls(model.states.copy(),
                   model.pointed_state,
                   copy.deepcopy(model.valuations),
                   copy.deepcopy(model.relations))

    @classmethod
    def fromtxtfile(cls, filename):
        """This function parses a file and returns a Kripke model.
        TODO: Use JSON instead of txt"""
        states = set()
        pointed_state = None
        valuations = dict()
        relations = dict()

        with open(filename, 'r') as f:
            contents = f.readlines()
            parse_state = "States"

        for c in contents:
            c = c.rstrip("\n")
            if c == "" or '#' in c or c == "States:":
                continue

            if parse_state == "States":
                if c == "Valuations:":
                    parse_state = "Valuations"
                    continue

                # Pointed states are denoted by !
                if "!" in c:
                    if pointed_state != None:
                        raise StateParseError(states,
                                              "Max 1 !-mark")

                    c = c.replace("!", "")
                    pointed_state = int(c)

                states.add(int(c))

            elif parse_state == "Valuations":
                if c == "Relations:":
                    parse_state = "Relations"
                    continue

                split = c.split(" ")
                for i, s in enumerate(split):
                    s = s.strip(" ")
                    split[i] = s

                state = split[0].rstrip(":")
                valuations[state] = split[1:]

            elif parse_state == "Relations":
                agent = c.split(":")[0]
                tuples = c.split(":")[1]
                tuples = tuples.replace("(", "")
                tuples = tuples.replace(")", "")
                tuples = tuples.split(",")
                for r in tuples:
                    r = r.strip(" ")
                    r = r.split(" ")
                    new_relation = (int(r[0]), int(r[1]))
                    try:
                        relations[agent].add(new_relation)
                    except KeyError:
                        relations[agent] = {new_relation}

        return cls(states, pointed_state, valuations, relations)


class StateParseError(Exception):
    def __init__(self, states, message):
        self.states = states
        self.message = message