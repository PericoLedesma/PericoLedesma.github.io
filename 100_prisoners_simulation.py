import numpy
from tkinter import *

counter = 0
own_prisoner_names = []

prisoner_dictionary = {
    1: "Alex",
    2: "Bennie",
    3: "Charlie",
    4: "Daniel",
    5: "Eric",
    6: "Francis",
    7: "George",
    8: "Henry",
    9: "Isaac",
    10: "John",
    11: "Kennie",
    12: "Lennie",
    13: "Mark",
    14: "Norbert",
    15: "Otis"
}


def print_introductory_message():
    print(
        "This is a solver for the 100 prisoners and a lightbulb riddle. It will try to use 4 protocols in order to solve the riddle.")


def take_user_input():
    print("Please enter the number of prisoners (maximum 15):")
    while True:
        try:
            num_prisoners = int(input())
            break
        except ValueError:
            print("Input must be an integer")
    while True:
        if num_prisoners > 15:
            print("Number of prisoners must be an integer between 1 and 15")
            while True:
                try:
                    num_prisoners = int(input())
                    break
                except ValueError:
                    print("Input must be an integer")
        else:
            break
    print(
        "Please enter the number of days to simulate (NOTE: for small numbers, protocols are more likely to fail as not all prisoners will enter the interrogation room):")
    while True:
        try:
            num_days = int(input())
            break
        except ValueError:
            print("Input must be an integer")
    print(
        "Please enter the number of lightbulbs:")
    while True:
        try:
            num_lightbulbs = int(input())
            break
        except ValueError:
            print("Input must be an integer")
    return num_prisoners, num_days, num_lightbulbs


def generate_sequence(list_length, prisoner_count):
    prisoner_order = []
    prisoner_names = []
    for i in range(0, list_length):
        n = numpy.random.randint(1, prisoner_count + 1)
        prisoner_order.append(n)
    for n in range(0, len(prisoner_order)):
        i = prisoner_order[n - 1]
        prisoner_names.append(prisoner_dictionary[i])
    return prisoner_order, prisoner_names


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
    for i in range(0, len(group_sizes)):
        # set counters number of times turned on lightbulb to -1 to identify them
        x = int(total)
        new_prisoners_list[2][x - 1] = -1
        for n in range(int(total), (int(total) + int(group_sizes[i]))):
            new_prisoners_list[0][n] = i + 1
        total += group_sizes[i]
    # print(new_prisoners_list)
    return group_sizes, new_prisoners_list


def protocol_1(prisoners_sequence, prisoners_list, prisoner_count):
    count = 0
    # 0 is off and 1 is on
    lightbulb = 0
    steps = 0
    passed = 0
    # iterate over prisoner list
    for i in prisoners_sequence:
        steps += 1
        # not counter, lightbulb off
        if prisoners_list[i - 1] == 0 and lightbulb == 0:
            prisoners_list[i - 1] = 1
            lightbulb = 1
        # counter, lightbulb on
        elif prisoners_list[i - 1] == 2 and lightbulb == 1:
            count += 1
            lightbulb = 0
        if count == prisoner_count - 1:
            break
    if count == prisoner_count - 1:
        passed = 1
        return passed, steps
    else:
        #         print("Protocol 1 does not work as the counter never declares all prisoners have been in the room")
        return passed, steps


def protocol_2(prisoners_sequence, prisoners_list, num_lightbulbs):
    # find out if number of prisoners can be represented in binary given number of lightbulbs
    num_prisoners = len(prisoners_list)
    binary = bin(num_prisoners)[2:]
    explanation = 0
    steps = 0
    count = 0
    if len(binary) > num_lightbulbs:
        explanation = 0
        #         print("Protocol 2 does not work as there are not enough lightbulbs to represent the prisoners in binary")
        return explanation, steps
    for i in prisoners_sequence:
        steps += 1
        if prisoners_list[i - 1] == 0:
            prisoners_list[i - 1] = 1
            count += 1
        if count == num_prisoners:
            explanation = 1
            #             print("Protocol 2 works and the prisoners escape. They can declare all prisoners have been counted "
            #               "on day " + str(steps))
            return explanation, steps
    #     print("Protocol 2 does not work as not all prisoners enter the room")
    explanation = 2
    return explanation, steps


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
    explanation = 0
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
        elif prisoners_list[2][i - 1] < 2 and lightbulb[int(prisoner_group - 1)] == 0:
            prisoners_list[1][i - 1] += 1
            prisoners_list[2][i - 1] += 1
            lightbulb[int(prisoner_group - 1)] = 1
        else:
            prisoners_list[1][i - 1] += 1
        # if counter thinks all people have been counted
        if int(prisoners_list[2][i - 1]) == -1 and count[int(prisoner_group - 1)] == group_count[
            int(prisoner_group - 1)] + num_lightbulbs - 2:
            for x in prisoners_list[1]:
                if x == 0:
                    explanation = 1
                    #                     print("Protocol 3 does not work and the prisoners are executed. The counter wrongly declares all prisoners have been counted "
                    #                         "on day " + str(steps))
                    return explanation, steps
            return explanation, steps

        # if their group is all counted and they have not yet signalled to other groups
        # Need to track every other groups
        if count[int(prisoner_group - 1)] == group_count[int(prisoner_group - 1)] - 1:
            for y in range(1, num_lightbulbs):
                if groups[int(prisoner_group - 1)][y] == 0 and y != prisoner_group and int(lightbulb[y]) == 0:
                    groups[int(prisoner_group - 1)][y] = 1
                    lightbulb[y] = 1
    #     print("Protocol 3 does not work as the counter never declares all prisoners have been in the room")
    explanation = 2
    return explanation, steps


def protocol_4(prisoners_sequence, prisoners_list, num_lightbulbs):
    # find out if number of prisoners can be represented in binary given number of lightbulbs
    explanation = 0
    steps = 0
    count = 0

    if len(prisoners_list) > num_lightbulbs:
        explanation = 1
        #         print("Protocol 4 does not work as there are not more prisoners than lightbulbs")
        return explanation, steps
    print(prisoners_list)
    for i in prisoners_sequence:
        steps += 1
        if prisoners_list[i - 1] == 0:
            prisoners_list[i - 1] = 1
            count += 1
        if count == len(prisoners_list):
            explanation = 0
            #             print("Protocol 4 works and the prisoners escape. They can declare all prisoners have been counted "
            #               "on day " + str(steps))
            return explanation, steps
    #     print("Protocol 4 does not work as not all prisoners enter the room")
    explanation = 2
    return explanation, steps


class MyWindow:
    def __init__(self, win):
        # Names
        self.lbl20 = Label(win, text='Create random sequence')
        self.lbl21 = Label(win, text='Create own sequence')
        self.lbl20.place(x=220, y=10)
        self.lbl21.place(x=730, y=10)

        # Input labels random
        self.lbl1 = Label(win, text='Number of prisoners')
        self.lbl2 = Label(win, text='Number of days')
        self.lbl3 = Label(win, text='Number of light bulbs')

        # Input labels own
        self.lbl10 = Label(win, text='Name prisoner')
        self.lbl12 = Label(win, text='Number of light bulbs')

        # Output labels
        self.lbl4 = Label(win, text='Sequence')
        self.lbl5 = Label(win, text='Protocol 1')
        self.lbl6 = Label(win, text='Protocol 2')
        self.lbl7 = Label(win, text='Protocol 3')
        self.lbl8 = Label(win, text='Protocol 4')

        # Input entries
        self.t1 = Entry()  # bd=3 gives a border around the input boxes
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Listbox()

        # Input entry own
        self.t10 = Entry()
        self.t12 = Entry()

        # Output entries
        self.t5 = Entry(width=90)
        self.t6 = Entry(width=90)
        self.t7 = Entry(width=90)
        self.t8 = Entry(width=90)

        self.btn1 = Button(win, text='Run protocols')
        self.btn5 = Button(win, text='Clear')
        self.btn10 = Button(win, text='Add')

        self.lbl1.place(x=100, y=50)
        self.t1.place(x=300, y=50)

        self.lbl2.place(x=100, y=100)
        self.t2.place(x=300, y=100)

        self.lbl3.place(x=100, y=150)
        self.t3.place(x=300, y=150)

        # Input places own
        self.lbl10.place(x=600, y=50)
        self.t10.place(x=800, y=50)
        self.lbl12.place(x=600, y=100)
        self.t12.place(x=800, y=100)

        # Buttons
        self.b1 = Button(win, text='Create and run random sequence', command=self.run1)
        self.b1.place(x=170, y=200)

        self.b5 = Button(win, text='Clear', command=self.clear)
        self.b5.place(x=540, y=200)

        self.b10 = Button(win, text='Add name', command=self.Add)
        self.b10.place(x=1000, y=47)

        self.b11 = Button(win, text='Run own sequence', command=self.runOwn)
        self.b11.place(x=720, y=200)

        # Outputs
        self.lbl4.place(x=400, y=250)
        self.t4.place(x=505, y=250)

        self.lbl5.place(x=100, y=450)
        self.t5.place(x=300, y=450)

        self.lbl6.place(x=100, y=500)
        self.t6.place(x=300, y=500)

        self.lbl7.place(x=100, y=550)
        self.t7.place(x=300, y=550)

        self.lbl8.place(x=100, y=600)
        self.t8.place(x=300, y=600)

    def run1(self):
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)

        # step 1 generate sequence
        prisoners_sequence, prisoner_names = generate_sequence(int(self.t2.get()), int(self.t1.get()))

        # create list of prisoners and set counter (could be controlled by user input)
        prisoner_count = int(self.t1.get())
        prisoners_list = [0] * prisoner_count
        prisoners_list = set_counter(prisoners_list)

        # Print sequence
        for name in range(len(prisoner_names)):
            self.t4.insert(END, "Day " + str(name + 1) + ": " + str(prisoner_names[name]))

        # The lightbulbs inputted
        lightbulbs = int(self.t3.get())

        # run protocol 1
        result_protocol1, steps = protocol_1(prisoners_sequence, prisoners_list, prisoner_count)
        if result_protocol1 == 1:
            self.t5.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               steps))
        else:
            self.t5.insert(END, "Does not work as the counter never declares all prisoners have been in the room")

        # run protocol 2
        prisoners_list = [0] * prisoner_count
        result_protocol2, steps = protocol_2(prisoners_sequence, prisoners_list, lightbulbs)

        if result_protocol2 == 1:
            self.t6.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               steps))
        elif result_protocol2 == 2:
            self.t6.insert(END, "Does not work as not all prisoners enter the room")
        else:
            self.t6.insert(END, "Does not work as there are not enough lightbulbs to represent the prisoners in binary")

        # run protocol 3
        prisoners_list = [0] * prisoner_count
        group_counts, prisoners_list = set_counter_and_groups(prisoners_list, lightbulbs)
        result_protocol3, steps = protocol_3(prisoners_sequence, prisoners_list, lightbulbs, group_counts)

        if result_protocol3 == 1:
            self.t7.insert(END,
                           "Does not work and the prisoners are executed. The counter wrongly declares all prisoners have been counted on day " + str(
                               steps))
        elif result_protocol3 == 2:
            self.t7.insert(END, "Does not work as the counter never declares all prisoners have been in the room")
        else:
            self.t7.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               steps))

        # run protocol 4
        prisoners_list = [0] * prisoner_count
        result_protocol4, steps = protocol_4(prisoners_sequence, prisoners_list, lightbulbs)

        if result_protocol4 == 1:
            self.t8.insert(END, "Does not work as there are not more lightbulbs than prisoners")
        elif result_protocol4 == 2:
            self.t8.insert(END, "Does not work as not all prisoners enter the room")
        else:
            self.t8.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               steps))

    def clear(self):
        global counter
        counter = 0
        global own_prisoner_names
        own_prisoner_names = []
        self.t4.delete(0, END)
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)

    def Add(self):
        global counter
        name = self.t10.get()
        own_prisoner_names.append(name)
        counter += 1
        self.t4.insert(END, "Day " + str(counter) + ": " + str(name) + "\n")

    def runOwn(self):
        self.t5.delete(0, END)
        self.t6.delete(0, END)
        self.t7.delete(0, END)
        self.t8.delete(0, END)

        num_prisoners_names = []
        dict_names = {}
        number = 1
        own_prisoner_order = []

        # prisoner_count = unique number of prisoners, names and numbers are just linked
        prisoners_set = set(own_prisoner_names)
        num_unique_prisoners = len(prisoners_set)

        for i in range(len(own_prisoner_names)):
            if own_prisoner_names[i] in dict_names:
                continue
            else:
                dict_names[own_prisoner_names[i]] = number
                number += 1

        for n in range(0, len(own_prisoner_names)):
            order = dict_names.get(own_prisoner_names[n])
            own_prisoner_order.append(order)

        own_prisoner_count = num_unique_prisoners

        own_prisoners_list = [0] * own_prisoner_count
        own_prisoners_list = set_counter(own_prisoners_list)

        own_prisoners_sequence = own_prisoner_order

        # The lightbulbs inputted
        own_lightbulbs = int(self.t12.get())

        # run protocol 1
        own_result_protocol1, own_steps = protocol_1(own_prisoners_sequence, own_prisoners_list, own_prisoner_count)
        if own_result_protocol1 == 1:
            self.t5.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               own_steps))
        else:
            self.t5.insert(END, "Does not work as the counter never declares all prisoners have been in the room")

        # run protocol 2
        own_prisoners_list = [0] * own_prisoner_count
        own_result_protocol2, own_steps = protocol_2(own_prisoners_sequence, own_prisoners_list, own_lightbulbs)

        if own_result_protocol2 == 1:
            self.t6.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               own_steps))
        elif own_result_protocol2 == 2:
            self.t6.insert(END, "Does not work as not all prisoners enter the room")
        else:
            self.t6.insert(END, "Does not work as there are not enough lightbulbs to represent the prisoners in binary")

            # run protocol 3
        own_prisoners_list = [0] * own_prisoner_count
        own_group_counts, own_prisoners_list = set_counter_and_groups(own_prisoners_list, own_lightbulbs)
        own_result_protocol3, own_steps = protocol_3(own_prisoners_sequence, own_prisoners_list, own_lightbulbs,
                                                     own_group_counts)

        if own_result_protocol3 == 1:
            self.t7.insert(END,
                           "Does not work and the prisoners are executed. The counter wrongly declares all prisoners have been counted on day " + str(
                               own_steps))
        elif own_result_protocol3 == 2:
            self.t7.insert(END, "Does not work as the counter never declares all prisoners have been in the room")
        else:
            self.t7.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               own_steps))

            # run protocol 4
        own_prisoners_list = [0] * own_prisoner_count
        own_result_protocol4, own_steps = protocol_4(own_prisoners_sequence, own_prisoners_list, own_lightbulbs)

        if own_result_protocol4 == 1:
            self.t8.insert(END, "Does not work as there are not more prisoners than lightbulbs")
        elif own_result_protocol4 == 2:
            self.t8.insert(END, "Does not work as not all prisoners enter the room")
        else:
            self.t8.insert(END,
                           "Works and the prisoners escape. The counter can declare all prisoners have been counted on day " + str(
                               own_steps))


def main():
    window = Tk()
    mywin = MyWindow(window)
    window.title('Simulation prisoners and n number of light bulbs riddle')
    window.geometry("1100x900+10+10")
    window.mainloop()


if __name__ == "__main__":
    main()


