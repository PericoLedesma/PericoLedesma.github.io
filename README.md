# LAMAS Project

View project page: https://wesselvdrest.github.io/LAMAS-EpistemicRiddleSolver/

## Dependencies
We are using the termcolor library. Install this library with the following command:  
```bash
pip3 install termcolor
```

## Usage of the program
To see whether a given proposition is valid in a given Kripke model, run:  
```bash
python3 Code/solver.py -m <Models/model_file> -v <Propositions/proposition_file>
```
To see where a given proposition holds in the given Kripke model, run:
```bash
python3 Code/solver.py -m <Models/model_file> -w <Propositions/proposition_file>
```

The program can also be run with the following command, provided that there is an according model file and proposition file in the Models and Propositions directory. This is the case for our premade riddles:  
```bash
python3 Code/solver.py --riddle <riddle_name>
```
It should be noted that this evaluates the validity of the propositions. To see where the propositions hold in the given Kripke model, please use the `-m` and `-w` options. Example riddle names would be drinking_logicians, muddy_children or dining_cryptographers.

## Format of Kripke model
A model file should follow the format of the following example:  
```plain
States:
0
1
2
3
4
5
6
7!

Valuations:
0:
1: p
2: q
3: r
4: p q
5: q r
6: p r
7: p q r

Relations:
A: (0 1), (2 4), (3 6), (5 7)
B: (0 2), (3 5), (1 4), (6 7)
C: (0 3), (4 7), (2 5), (1 6)
```
Here, the ! behind a state number means that is the true world.

## Format of propositions
The operators that can be used are:  
& for AND  
| for OR  
~ for NOT  
C for Common Knowledge  
K{A} for agent A knows that  
<> for some truthful public announcement  
[] for every truthful public announcement  
?1 for a a public whether announcement (announce falsity if the argument is false and announce the truth if the argument is true)
And of course the parentheses can be used to denote scope ( )  

The proposition files can also contain text that the user wants to print out to the console. These lines of text should start with the #-symbol.  

The following are all valid ways of writing propositions:  
```plain
~(p & q) | ~r & s  
~(p & q) & r  
Cp  
~Cp  
~C~p  
C~p  
K{A}p  
~K{A}p  
~K{A}~p  
~K{A}p & Cp  
<p>q  
[p]q  
[p & q]r  
[p&q](r & q)  
?p&q!(r & q)  
p | <q>r  
# This is a line of text that will be printed out to the console.
```

## Structure of the repository
The meat and potatoes of the project can be found in the Code, Models and Propositions directories. The Code directory holds all the functionality for parsing and evaluating Kripke models and propositions.

### Code directory
1. `model.py`  holds all functionality for parsing Kripke models. The Kripke models can be specified in a specific format as mentioned above. These textual representations are converted into a Python set which holds the set of states and two Python dictionaries which hold the valuations and relations of the model.
2. `expression.py` holds all functionality for parsing propositions. This file will turn strings into a tree structure made out of logical connectives, epistemic operators and propositional atoms.
3. The program which should be run is called `solver.py`. To run this program properly, you'll need to supply it with a model file and a proposition file as specified above. It calls `model.py` and `expression.py` to parse the model and proposition strings. It then evaluates the propositions within the current Kripke model.

### Models directory
Currently, the Models directory holds all the .txt model files that we implemented. It is possible to write these model files yourself. Just follow the formatting rules laid out above.

### Propositions directory
Currently, the Propositions directory holds all the .txt proposition files that we implemented. It is possible to write these proposition files yourself. Just follow the formatting rules laid out above.

### graph directory
This directory contains a program that can turn a model file into a graph. The resulting graphs are also stores inside this directory. These graphs are displayed in the Results section of the report website.

### Other
Most of the other files in the directory have to do with the website/report.

## Possible extensions to the program
Parsing:  
Multicharacter propositions  
Multicharacter agents inside the K-operator  
Knows whether operator (`K?{A}` would then be an abbreviation for `K{A}p | K{A}~p`)  
Common knowledge for subgroups  