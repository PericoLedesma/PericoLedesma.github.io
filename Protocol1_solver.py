import random
import numpy

# number of prisoners
prisoner_count = 4
list_length = 30
lightbulbs = 2

def generate_sequence():
    prisoner_order = []
    for i in range (0, list_length):
        n = numpy.random.randint(1, prisoner_count)
        prisoner_order.append(n)
    print(prisoner_order)
    return prisoner_order

def set_counter(prisoners_list):
    # this should take some user input,
    # but for now I always set the first prisoner as counter
    i = 0
    prisoners_list[i] = 2
    return prisoners_list

# sets first n as counters, then sets the groups of all remaining prisoners, dividing as evenly as possible
def set_counter_and_groups(prisoners_list, num_lightbulbs):
    # this should take some user input,
    # but for now I always set the first n prisoners as counter
    num_prisoners = len(prisoners_list)
    remainder = num_prisoners % num_lightbulbs
    group_size = (num_prisoners - remainder) / num_lightbulbs
    group_sizes = [group_size] * num_lightbulbs
    for i in range(0, remainder):
        group_sizes[i] += 1
    counters = list(range(0, num_lightbulbs))
    new_prisoners_list = numpy.zeros(shape=(3, num_prisoners))
    total = 0
    for i in range (0, len(group_sizes)):
        # set counters number of times turned on lightbulb to -1 to identify them
        x = int(total)
        new_prisoners_list[2][x] = -1
        for n in range(int(total), (int(total) + int(group_sizes[i]))):
            new_prisoners_list[0][n] = i + 1
        total += group_sizes[i]
    # print(new_prisoners_list)
    return group_sizes, new_prisoners_list


def protocol_1(prisoners_sequence, prisoners_list):
    count = 0
    # 0 is off and 1 is on
    lightbulb = 0
    steps = 0
    #iterate over prisoner list
    for i in prisoners_sequence:
        steps += 1
        # not counter, lightbulb off
        if prisoners_list[i-1] == 0 and lightbulb == 0:
            prisoners_list[i-1] = 1
            lightbulb = 1
        #counter, lightbulb on
        elif prisoners_list[i-1] == 2 and lightbulb == 1:
            count += 1
            lightbulb = 0
        if count == prisoner_count - 1:
            break

    if count == prisoner_count - 1:
        print("Protocol 1 works and the prisoners escape. The counter can declare all prisoners have been counted "
              "on day " + str(steps))
    else:
        print("Protocol 1 does not work as the counter never declares all prisoners have been in the room")
    return None


def protocol_2(prisoners_sequence, prisoners_list, num_lightbulbs):
    # find out if number of prisoners can be represented in binary given number of lightbulbs
    num_prisoners = len(prisoners_list)
    binary = bin(num_prisoners)[2:]
    if len(binary) > num_lightbulbs:
        print("Protocol 2 does not work as there are not enough lightbulbs to represent the prisoners in binary")
        return None
    steps = 0
    count = 0
    for i in prisoners_sequence:
        steps += 1
        if prisoners_list[i-1] == 0:
            prisoners_list[i-1] = 1
            count += 1
        if count == num_prisoners:
            print("Protocol 2 works and the prisoners escape. They can declare all prisoners have been counted "
              "on day " + str(steps))
            return None
    print("Protocol 2 does not work as not all prisoners enter the room")
    return None


# Inputs: prisoners_sequence (list describing order they enter room),
# num_lightbulbs (integer),
# prisoners_list (3xn arary, first row is group, second is count of how many times they were in room,
# third how many times they have turned on lightbulb)
# group count (array with the number of people in each group)
def protocol_3(prisoners_sequence, prisoners_list, num_lightbulbs, group_count):
    # list of how many times each person was in the room
    # count of counters
    count = [0] * num_lightbulbs
    lightbulb = [0] * num_lightbulbs
    steps = 0
    groups = numpy.zeros(shape=(num_lightbulbs, num_lightbulbs))
    # iterate over prisoner list
    for n in range(1, len(prisoners_sequence)):
        i = prisoners_sequence[n]
        steps += 1
        prisoner_group = prisoners_list[0][i - 1]
        # they are the counter and the lightbulb is on
        if int(prisoners_list[2][i - 1]) == -1 and int(lightbulb[int(prisoner_group - 1)]) == 1:
            count[int(prisoner_group - 1)] += 1
            lightbulb[int(prisoner_group - 1)] = 0
            prisoners_list[1][i - 1] += 1
        # the prisoner is not the counter, they havn't yet turned on the lightbulb twice and bulb is off
        elif prisoners_list[2][i-1] < 2 and lightbulb[int(prisoner_group - 1)] == 0:
            prisoners_list[1][i - 1] += 1
            prisoners_list[2][i-1] += 1
            lightbulb[int(prisoner_group - 1)] = 1
        else:
            prisoners_list[1][i - 1] += 1
        # if counter thinks all people have been counted
        if int(prisoners_list[2][i - 1]) == -1 and count[int(prisoner_group - 1)] == group_count[int(prisoner_group - 1)] + num_lightbulbs - 2:
            for x in prisoners_list[1]:
                if x == 0:
                    print(
                        "Protocol 3 does not work and the prisoners are executed. The counter wrongly declares all prisoners have been counted "
                        "on day " + str(steps))
                    return None
            print("Protocol 3 works and the prisoners escape. The counter can declare all prisoners have been counted "
              "on day " + str(steps))
            return None

        # if their group is all counted and they have not yet signalled to other groups
        # Need to track every other groups
        if count[int(prisoner_group - 1)] == group_count[int(prisoner_group - 1)] - 1:
            for y in range(1, num_lightbulbs):
                if groups[int(prisoner_group-1)][y] == 0 and y != prisoner_group and int(lightbulb[y]) == 0:
                    groups[int(prisoner_group-1)][y] = 1
                    lightbulb[y] = 1
    print("Protocol 3 does not work as the counter never declares all prisoners have been in the room")
    return None


def protocol_4(prisoners_sequence, prisoners_list, num_lightbulbs):
    # find out if number of prisoners can be represented in binary given number of lightbulbs
    if len(prisoners_list) > num_lightbulbs:
        print("Protocol 4 does not work as there are not more prisoners than lightbulbs")
        return None
    steps = 0
    count = 0
    for i in prisoners_sequence:
        steps += 1
        if prisoners_list[i-1] == 0:
            prisoners_list[i-1] = 1
            count += 1
        if count == len(prisoners_list):
            print("Protocol 4 works and the prisoners escape. They can declare all prisoners have been counted "
              "on day " + str(steps))
            return None
    print("Protocol 4 does not work as not all prisoners enter the room")
    return None


def main():
    # step 1 generate sequence
    prisoners_sequence = generate_sequence()
    # create list of prisoners and set counter (could be controlled by user input)
    prisoners_list = [0] * prisoner_count
    prisoners_list = set_counter(prisoners_list)
    # run protocol 1
    protocol_1(prisoners_sequence, prisoners_list)
    # run protocol 2
    prisoners_list = [0] * prisoner_count
    protocol_2(prisoners_sequence, prisoners_list, lightbulbs)
    # run protocol 3
    prisoners_list = [0] * prisoner_count
    group_counts, prisoners_list = set_counter_and_groups(prisoners_list, lightbulbs)
    protocol_3(prisoners_sequence, prisoners_list, lightbulbs, group_counts)
    protocol_4(prisoners_sequence, prisoners_list, lightbulbs)


if __name__ == "__main__":
    main()