import argparse
from termcolor import colored
from model import Model
from expressions import *
import os

# S5 Kripke model solver

# Kripke model contains:
# S              -- A set of States
# Pi             -- A dictionary of valuations per state
# R_1 ... R_m    -- A set of Relations 

# The logic which we are using can be defined by subclassing BooleanAlgebra
# Essentially, we are adding the rules for the K, C, [] and <> operators.

def parse_proposition(string):
    print(string)
    print()
    expression = Expression(string)
    print(expression)
    print()
    expression = expression.expr

    return expression

def valid(model, pointed_state, proposition):
    """ A proposition can have many forms. We will use the truth
    definition of the S5 language operators, the C operator and
    the public announcement operators to determine whether the
    proposition is valid.

    The truth definition:
    (M, s) |= p        iff valuation(s)(p) = true
    (M, s) |= p & q    iff (M, s) |= p and (M, s) |= q
    (M, s) |= ~p       iff (M, s) not |= p
    (M, s) |= K{A}p    iff (M, t) |= p for all (s, t) in Rel{A}
    (M, s) |= Cp       iff (M, t) |= p for all (s, t) in the union of Rel(A) .. Rel(Z)
    (M, s) |= [p]q     iff (M, s) |= p implies that (M|p, s) |= q
    (M, s) |= <p>q     iff (M, s) |= p and (M|p, s) |= q
    
    The following is an added announcement, based on the PubAnnounceW operator
    from SMCDEL, by Malvin Gattinger.
    (M, s) |= ?p!q     iff (M, s) |= p implies that (M|p, s) |= q or
                           (M, s) not |= p implies that (M|~p, s) |= q

    The pointed state can be extracted from the model. A ! denotes the 
    true world.
    """
    # An atom is valid in (M, s) if the atom is in the valuation    
    while isinstance(proposition, Expression):
        proposition = proposition.expr

    if isinstance(proposition, Atom):
        prop_is_valid = proposition.arg in model.valuations[str(pointed_state)]

    elif isinstance(proposition, AND):
        prop_is_valid = valid(model, pointed_state, proposition.arg1) and \
                        valid(model, pointed_state, proposition.arg2)

    elif isinstance(proposition, NOT):
        prop_is_valid = not valid(model, pointed_state, proposition.arg)

    elif isinstance(proposition, OR):
        prop_is_valid = valid(model, pointed_state, proposition.arg1) or \
                        valid(model, pointed_state, proposition.arg2)

    elif isinstance(proposition, XOR):
        valid_1 = valid(model, pointed_state, proposition.arg1)
        valid_2 = valid(model, pointed_state, proposition.arg2)
        prop_is_valid = (valid_1 or valid_2) and not (valid_1 and valid_2)
        
    elif isinstance(proposition, K):
        agent = proposition.agent
        prop_is_valid = True
        for relation in model.relations[agent]:
            if pointed_state in relation:
                if pointed_state == relation[0]:
                    if not valid(model, relation[1], proposition.arg):
                        prop_is_valid = False
                        break
                else:
                    # pointed_state == relation[1]
                    if not valid(model, relation[0], proposition.arg):
                        prop_is_valid = False
                        break

    elif isinstance(proposition, C):
        # Determine which of the states are reachable in any number of steps
        # From the current pointed state
        reachable_states = {pointed_state}
        # Keep track of length so that we may stop the while loop
        prev_len_reachable_states = 0   
        while len(reachable_states) != prev_len_reachable_states:
            prev_len_reachable_states = len(reachable_states)
            for _, relations in model.relations.items():
                for relation in relations:
                    for state in reachable_states.copy():
                        if state in relation:
                            reachable_states.update({*relation})

        # If in any of the states in the set of reachable states, it does
        # not hold that proposition.arg (the argument of the C operator), then 
        # The proposition is not valid
        prop_is_valid = True
        for state in reachable_states:
            if not valid(model, state, proposition.arg):
                prop_is_valid = False
                break

    elif isinstance(proposition, Box):
        # The announcement deletes some of the states and relations
        # The proposition is valid if the argument is true regardless 
        # of the announcement. For [p]q, read after the announcement
        # of p, q is true. This means that q can be true before the
        # announcement. If q is not true before the announcement,
        # the annnouncement of p implies q 

        if valid(model, pointed_state, proposition.arg1):
            # If the announcement is valid in pointed_state,
            # Change the model to reflect the announcement
            viable_states = model.states.copy()
            for state in model.states:
                if not valid(model, state, proposition.arg1):
                    viable_states.remove(state)

            temp_model = Model.copy(model)
            temp_model.set_states(viable_states)
            prop_is_valid = valid(temp_model, pointed_state, proposition.arg2)
        else:
            prop_is_valid = True

    elif isinstance(proposition, Diamond):
        new_prop = NOT(Box(proposition.arg1, NOT(proposition.arg2)))
        prop_is_valid = valid(model, pointed_state, new_prop)

    elif isinstance(proposition, Whether):
        if valid(model, pointed_state, proposition.arg1):
            new_prop = Box(proposition.arg1, proposition.arg2)
        else:
            new_prop = Box(NOT(proposition.arg1), proposition.arg2)

        prop_is_valid = valid(model, pointed_state, new_prop)

    return prop_is_valid

def where(model, proposition):
    """The where function evaluates whether the given proposition is valid
    in any of the states. It returns the worlds in which it is."""
    in_worlds = []
    for state in model.states:
        pointed_state = state
        
        if valid(model, pointed_state, proposition):
            in_worlds.append(pointed_state)

    return in_worlds

def main():
    parser = argparse.ArgumentParser("Kripke model solver")
    parser.add_argument("-m", "--model", metavar="FILE",
                        help="The filename that contains the Kripke model")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--valid", metavar="FILE",
                       help="The filename in which a proposition is given. "
                       "The valid() function will be run on that proposition.")
    group.add_argument("-w", "--where", metavar="FILE",
                       help="The filename in which a proposition is given. "
                       "The where() function will be run on that proposition.")
    group.add_argument("--riddle", metavar="RIDDLE",
                       help="The riddle name. If you use this, it is expected \
                       that there is a model file called <RIDDLE>_model.txt \
                       inside the Models directory and a <RIDDLE>_props.txt \
                       inside the Propsositions directory. This uses the valid \
                       function. Please use the -m and -w options if you want \
                       to use the where function.")
    args = parser.parse_args()

    if args.riddle:
        args.model = os.path.join("Models", args.riddle+"_model.txt")
        args.valid = os.path.join("Propositions", args.riddle+"_props.txt")

    if not args.model:
        print("No filename specified for either the model.")
        parser.print_help()
        exit()

    if not args.valid and not args.where:
        print("No filename specified for either the valid or where functions.")
        parser.print_help()
        exit()

    model = Model.fromtxtfile(args.model)
    print(model)

    # We now have the model defined.
    # Now we can ask whether a proposition is valid
    print("-------------------------")
    if args.valid:
        with open(args.valid, "r") as f:
            contents = f.readlines()

        pointed_state = model.pointed_state        

        for string in contents:
            # Comments are noted with '#' in the txt file.
            if len(string) > 0 and string[0] == "#":
                # Printing comments inside the txt file
                print(colored(string[1:], "blue"))

            string = string.replace(" ", "")
            string = string.replace("\n", "")

            if len(string) > 0 and string[0] != "#":
                proposition = parse_proposition(string)
                if valid(model, pointed_state, proposition):
                    turnstile = u'\u22A8'
                    print(colored(f"(M, {pointed_state}) {turnstile} {string}", "green"))
                else:
                    not_turnstile = u'\u22AD'
                    print(colored(f"(M, {pointed_state}) {not_turnstile} {string}", "red"))
                print("-------------------------")
                print()

    # We can also ask where the proposition is valid
    if args.where:
        with open(args.where, "r") as f:
            contents = f.readlines()

        for string in contents:
            if len(string) > 0 and string[0] == "#":
                # Printing comments inside the txt file
                print(colored(string[1:], "blue"))


            string = string.replace(" ", "")
            string = string.replace("\n", "")

            if len(string) > 0 and string[0] != "#":
                proposition = parse_proposition(string)
                in_worlds = where(model, proposition)
                if len(in_worlds) == 0:
                    print(colored(f"The proposition is false in all worlds.", "red"))
                elif len(in_worlds) == len(model.states):
                    print(colored(f"The proposition is true in all worlds.", "green"))
                else:
                    for world in in_worlds:
                        print(f"The proposition is true in world {world}: {model.valuations[str(world)]}.")
                print("-------------------------")
                print()

if __name__ == "__main__":
    main()