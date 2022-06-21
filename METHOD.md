# Methods

The goal of the program is to evaluate given propositions in given Kripke models. To this end, the first part of the program parses a file with the given Kripke model. Then, another file with the given propositions is parsed, such that we end up with a data structure which is easy to perform evaluation on. The last step of the algorithm is evaluating the propositions in the given Kripke model.
The program then outputs a string that holds information about whether the given proposition holds in the given pointed Kripke model, or about in which states within the model the given proposition holds. The user is able to choose between these two options.

## Parsing Models

The user is expected to input a plaintext file containing the states, valuations and relations of the given Kripke model. There is also an expected format the plaintext file should follow. The first line of the file should be equal to "States:". The lines following this should denote the integer indices of the states, e.g. 0, 1, 2, et cetera.

After all states have been specified, the following line should be equal to "Valuations:". The following lines specify the valuations in each state.

After all valuations have been specified, the following line should be equal to "Relations:". The final lines in the file should hold information about each agent (single letter) and the set of relations those agents have.

The structure of the plaintext file is best shown with an example:
```plain
States:
0
1
2
3!

Valuations:
0:
1: p
2: q
3: p q

Relations:
A: (0 1), (2 3)
B: (0 2), (1 3)
```

The above example contains the Kripke structure for the Muddy Children riddle with 2 children. The '!' behind state 3 denotes that state 3 is the real state, i.e. the pointed model becomes `(M, 3)`. Only one state can be denoted as the true state. If more states are denoted as the true state, the program will raise an error.

## Parsing Propositions

Once the model is defined and parsed correctly, the propositions are parsed and converted to a data structure that is easy to evaluate. The user can input a plaintext file with propositions on a single line. The following operators are supported:

```plain
 ~ for NOT
 & for AND
 | for OR
 ^ for XOR
 K{A} for agent A knows that
 C for common knowledge
 ( and ) to denote scope
 [ and ] for weak public announcements
〈 and 〉for strong public announcements
 ? and ! for whether public announcements
```

Furthermore, a propositional atom should always be a lowercase letter.The propositions are parsed from left to right.  A proposition is an expression,  which can consist of sub-expressions that can in turn consist of subsub-expressions et cetera.  This can be represented as a tree structure.If an atom is encountered (e.g. p), the expression is equal to Atom(p).  When an operator of degree 1 (i.e. '\~', 'K{A}', 'C') is encountered, the algorithm will parse the sub-expression to the right of the operator and return an expression which applies that operator to the parsed sub-expression.  Should an operator of degree 2 be encountered (i.e. '&', '|' or '^') the algorithm will parse the sub-expression to the right of the operator and return the operator applied on the expression that was already parsed (on the left of the operator), plus the newly parsed sub-expression to the right of the operator.
The announcement operators (i.e. '[ ]', '〈〉', '?!') are parsed slightly differently. There are two arguments in the announcement cases, namely the proposition being announced, and the proposition after the announcement has taken place. The first argument is the complete expression between the opening symbol ('[', '〈', '?') and closing symbol  (']', '〉', '!') and the second argument the sub-expression behind the closing symbol.

## Evaluating Propositions

We make use of the semantics definition as defined in the book Dynamic Epistemic Logic by van Ditmarsch, van der Hoek and Kooi. Namely, if there are m agents and the model is defined as M =〈S, V<sub>p</sub>, R<sub>1</sub> ... R<sub>m</sub>〉, where S is the set of states, V<sub>p</sub> is the set of valuations at each state and R<sub>1</sub> to R<sub>m</sub> are the sets of relations for each agent, then:  
    
(M,s) ⊨ p &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; iff s ∈ V<sub>p</sub>  
(M,s) ⊨ ¬φ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iff    (M,s) &nvDash; φ  
(M,s) ⊨ φ ∧ ψ&nbsp; iff (M,s) ⊨ φ and (M,s) ⊨ ψ  
(M,s) ⊨ K<sub>A</sub>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   iff for all t ∈ S: (s,t) ∈ R<sub>A</sub> implies (M,t) ⊨ φ  
(M,s) ⊨ Cφ &nbsp;&nbsp; &nbsp;&nbsp;iff for all t ∈ S: (s,t) ∈ R<sub>1</sub> ∪ ... ∪ R<sub>m</sub> implies (M,t) ⊨ φ  
(M,s) ⊨ [φ]ψ &nbsp;&nbsp;&nbsp;iff  (M,s) ⊨ φ implies (M|φ,s) ⊨ ψ  

where M|φ is defined as the subset of M such that φ is  valid in all its states. This is equivalent to pruning  the model of the states where φ is invalid, followed by the deletion of the valuations and relations that mention those states. Now, evaluating whether a given expression is valid in a pointed model (M,s) is a matter of recursively evaluating all sub-expressions  in that pointed model. For example, if we were to evaluate the expression (M,s)⊨¬p, we evaluate the sub-expression p in (M,s) and then we negate that value.

The following is an added announcement, based on the PubAnnounceW operator
from SMCDEL, by Malvin Gattinger.  

(M,s) ⊨ ?p!q iff (M,s) ⊨ p implies that (M|p, s) ⊨ q or (M,s) ⊨ ¬p implies that (M|¬p, s) ⊨ q




















