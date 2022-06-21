# Results

In this section we show the output of our solver for the riddles that were given as examples in the introduction. For each riddle there are multiple things we could be interested in. Each proposition of interest is separated by lines. For each output block, the first line shows the proposition itself, the second line shows the parsed representation of that proposition, and the third line shows whether the proposition holds in the pointed state. Each of the propositional atoms have a meaning. These meanings are omitted from this section for the sake of brevity and clarity.

## Muddy Children
Three brilliant children go to the park to play. When their father comes to find them, he sees that all of them have mud on their foreheads. He then says, “At least one of you has mud on your forehead”, and then asks, “Do you know if you have mud on your forehead?” The children simultaneously respond, “No”.
Do any of the children know whether they are muddy?  

```plain
K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r

OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r)))))))

(M, 7) ⊭ K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r
```
--------------------------------------------------------------------------------------------------------------------

After the first announcement that at least one child is muddy. Do any of the children know whether they are muddy?

```plain
<p|q|r>(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Diamond<OR(p, OR(q, r))>(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))

(M, 7) ⊭ <p|q|r>(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
-------------------------------------------------------------------------------------------------------------------

No one has stepped forward yet, which can be represented as an announcement. After the second announcement that at least one child is muddy, do any of the children know whether they are muddy?

```plain
[(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Box[OR(p, OR(q, r))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r)))))))))

(M, 7) ⊭ [(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
--------------------------------------------------------------------------------------------------------------------

No one has stepped forward yet, which can be represented as an announcement. After the third announcement that at least one child is muddy, do any of the children know whether they are muddy?

```plain
[(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)

Box[OR(p, OR(q, r))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](Box[NOT(OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))](OR(K{A}(p), OR(K{A}(NOT(p)), OR(K{B}(q), OR(K{B}(NOT(q)), OR(K{C}(r), K{C}(NOT(r))))))))))

(M, 7) ⊨ [(p|q|r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)][~(K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)](K{A}p|K{A}~p|K{B}q|K{B}~q|K{C}r|K{C}~r)
```
--------------------------------------------------------------------------------------------------------------------


## Drinking Logicians
Three logicians walk into a bar. The barman says, 'Does everybody want a drink?' The first logician says, 'I don't know.' The second logician says, 'I don't know.' What does the third logician say?

After the barman has asked whether everybody wants a drink, and after agent A announces he does not know whether everybody wants a drink, is it common knowledge that agent A wants a drink?

```plain
[~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp

Box[NOT(OR(K{A}(AND(p, AND(q, r))), K{A}(NOT(AND(p, AND(q, r))))))](C(p))

(M, 7) ⊨ [~(K{A}(p&q&r)|K{A}~(p&q&r))]Cp
```
--------------------------------------------------------------------------------------------------------------------

After the barman has asked whether everybody wants a drink, and after agent A and agent B announce that they do not know whether everybody wants a drink, does agent C know whether everybody wants a drink?

```plain
[~(K{A}(p&q&r)|K{A}~(p&q&r))&~(K{B}(p&q&r)|K{B}~(p&q&r))]K{C}(p&q&r)

Box[AND(NOT(OR(K{A}(AND(p, AND(q, r))), K{A}(NOT(AND(p, AND(q, r)))))), NOT(OR(K{B}(AND(p, AND(q, r))), K{B}(NOT(AND(p, AND(q, r)))))))](K{C}(AND(p, AND(q, r))))

(M, 7) ⊨ [~(K{A}(p&q&r)|K{A}~(p&q&r))&~(K{B}(p&q&r)|K{B}~(p&q&r))]K{C}(p&q&r)
```

## Cheryl's Birthday
The following description is taken from Wikipedia: "Albert and Bernard just became friends with Cheryl, and they want to know when her birthday is. Cheryl gives them a list of 10 possible dates. Cheryl then tells Albert and Bernard separately the month and the day of her birthday respectively. Albert: I don't know when Cheryl's birthday is, but I know that Bernard doesn't know too. Bernard: At first I did not know when Cheryl's birthday is, but I know now. Albert: Then I also know when Cheryl's birthday is. So when is Cheryl's birthday?" 

Does Albert know Cheryl's birthday?
```plain
K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v)

OR(K{A}(AND(p, x)), OR(K{A}(AND(p, y)), OR(K{A}(AND(q, v)), OR(K{A}(AND(q, y)), OR(K{A}(AND(r, v)), OR(K{A}(AND(r, x)), OR(K{A}(AND(s, w)), OR(K{A}(AND(s, y)), OR(K{A}(AND(t, w)), K{A}(AND(u, v)))))))))))

(M, 5) ⊭ K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v)
```
-------------------------

Does Bernard know Cheryl's birthday?
```plain
K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v)

OR(K{B}(AND(p, x)), OR(K{B}(AND(p, y)), OR(K{B}(AND(q, v)), OR(K{B}(AND(q, y)), OR(K{B}(AND(r, v)), OR(K{B}(AND(r, x)), OR(K{B}(AND(s, w)), OR(K{B}(AND(s, y)), OR(K{B}(AND(t, w)), K{B}(AND(u, v)))))))))))

(M, 5) ⊭ K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v)
```
-------------------------

Albert announces that he does not know Cheryl's birthday and he knows that Bernard does not know it. Does Bernard know Cheryl's birthday now?

```plain
<(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)>(K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v))

Diamond<AND(AND(NOT(K{A}(p)), AND(NOT(K{A}(q)), AND(NOT(K{A}(r)), AND(NOT(K{A}(s)), AND(NOT(K{A}(t)), NOT(K{A}(u))))))), K{A}(AND(NOT(K{B}(v)), AND(NOT(K{B}(w)), AND(NOT(K{B}(x)), NOT(K{B}(y)))))))>(OR(K{B}(AND(p, x)), OR(K{B}(AND(p, y)), OR(K{B}(AND(q, v)), OR(K{B}(AND(q, y)), OR(K{B}(AND(r, v)), OR(K{B}(AND(r, x)), OR(K{B}(AND(s, w)), OR(K{B}(AND(s, y)), OR(K{B}(AND(t, w)), K{B}(AND(u, v))))))))))))

(M, 5) ⊨ <(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)>(K{B}(p&x)|K{B}(p&y)|K{B}(q&v)|K{B}(q&y)|K{B}(r&v)|K{B}(r&x)|K{B}(s&w)|K{B}(s&y)|K{B}(t&w)|K{B}(u&v))
```
-------------------------

Bernard announces that he now knows Cheryl's birthday. Does Albert know the birthday now?

```plain
<(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)><K{B}v|K{B}w|K{B}x|K{B}y>(K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v))

Diamond<AND(AND(NOT(K{A}(p)), AND(NOT(K{A}(q)), AND(NOT(K{A}(r)), AND(NOT(K{A}(s)), AND(NOT(K{A}(t)), NOT(K{A}(u))))))), K{A}(AND(NOT(K{B}(v)), AND(NOT(K{B}(w)), AND(NOT(K{B}(x)), NOT(K{B}(y)))))))>(Diamond<OR(K{B}(v), OR(K{B}(w), OR(K{B}(x), K{B}(y))))>(OR(K{A}(AND(p, x)), OR(K{A}(AND(p, y)), OR(K{A}(AND(q, v)), OR(K{A}(AND(q, y)), OR(K{A}(AND(r, v)), OR(K{A}(AND(r, x)), OR(K{A}(AND(s, w)), OR(K{A}(AND(s, y)), OR(K{A}(AND(t, w)), K{A}(AND(u, v)))))))))))))

(M, 5) ⊨ <(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)><K{B}v|K{B}w|K{B}x|K{B}y>(K{A}(p&x)|K{A}(p&y)|K{A}(q&v)|K{A}(q&y)|K{A}(r&v)|K{A}(r&x)|K{A}(s&w)|K{A}(s&y)|K{A}(t&w)|K{A}(u&v))
```
-------------------------

Is it common knowledge that Cheryl's birthday is the 16th of July after the announcement of Bernard?

```plain
<(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)><K{B}v|K{B}w|K{B}x|K{B}y>C(r&x)

Diamond<AND(AND(NOT(K{A}(p)), AND(NOT(K{A}(q)), AND(NOT(K{A}(r)), AND(NOT(K{A}(s)), AND(NOT(K{A}(t)), NOT(K{A}(u))))))), K{A}(AND(NOT(K{B}(v)), AND(NOT(K{B}(w)), AND(NOT(K{B}(x)), NOT(K{B}(y)))))))>(Diamond<OR(K{B}(v), OR(K{B}(w), OR(K{B}(x), K{B}(y))))>(C(AND(r, x))))

(M, 5) ⊨ <(~K{A}p&~K{A}q&~K{A}r&~K{A}s&~K{A}t&~K{A}u)&K{A}(~K{B}v&~K{B}w&~K{B}x&~K{B}y)><K{B}v|K{B}w|K{B}x|K{B}y>C(r&x)
```
-------------------------

## Consecutive Numbers
Anne and Bill are each going to be told a natural number. Their numbers will be one apart. The numbers are now being whispered in their respective ears. They are aware of this scenario. Suppose Anne is told 2 and Bill is told 3. The following truthful conversation between Anne and Bill now takes place: Anne: "I do not know your number." Bill: "I do not know your number." Anne: "I know your number." Bill: "I know your number." 

Does Anne know Bill's number?

```plain
K{A}p|K{A}r

OR(K{A}(p), K{A}(r))

(M, 1) ⊭ K{A}p|K{A}r
```
-----------------------------------------------------------------------------------------------------------------------  

Does Bill know Anne's number?
```plain
K{B}q|K{B}s

OR(K{B}(q), K{B}(s))

(M, 1) ⊭ K{B}q|K{B}s
```
-----------------------------------------------------------------------------------------------------------------------  

Is it true that Bill does not know Anne's number after she says she does not know Bill's number?
```plain
[~K{A}(p)&~K{A}(r)]( ~K{B}(q)&~K{B}(s))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](AND(NOT(K{B}(q)), NOT(K{B}(s))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)]( ~K{B}(q)&~K{B}(s))
```
-----------------------------------------------------------------------------------------------------------------------  

Does Anne know Bill's number after Bill announces he does not know hers?

```plain
[~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)](K{A}(p)|K{A}(r))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](Box[AND(NOT(K{B}(q)), NOT(K{B}(s)))](OR(K{A}(p), K{A}(r))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)](K{A}(p)|K{A}(r))
```
-----------------------------------------------------------------------------------------------------------------------  

Does Bill know Anne's number after Anne has announced that she knows his?

```plain
[~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)][K{A}(p)|K{A}(r)](K{B}(q)|K{B}(s))

Box[AND(NOT(K{A}(p)), NOT(K{A}(r)))](Box[AND(NOT(K{B}(q)), NOT(K{B}(s)))](Box[OR(K{A}(p), K{A}(r))](OR(K{B}(q), K{B}(s)))))

(M, 1) ⊨ [~K{A}(p)&~K{A}(r)][~K{B}(q)&~K{B}(s)][K{A}(p)|K{A}(r)](K{B}(q)|K{B}(s))
```
-----------------------------------------------------------------------------------------------------------------------  

## Hangman
At a trial a prisoner is sentenced to death. The verdict reads "You will be executed next week, but the day on which you will be executed is a surprise to you." The prisoner reasons as follows. "I cannot be executed on Friday, because in that case I would not be surprised. But given that Friday is eliminated, then I cannot be executed on Thursday either, because that would then no longer be a surprise. And so on. Therefore the verdict cannot be executed." And so, his execution, that happened to be on Wednesday, came as a surprise.  

Does the prisoner know on which day he will be executed?
```plain
K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g

OR(K{P}(a), OR(K{P}(b), OR(K{P}(c), OR(K{P}(d), OR(K{P}(e), OR(K{P}(f), K{P}(g)))))))

(M, 2) ⊭ K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g
```
-----------------------------------------------------------------------------------------------------------------------  

After the announcement by the judge, does the prisoner know he will not be executed on Friday, thereby making his reasoning correct?

```plain
[(a|b|c|d|e|f|g)&~(K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g)](K{P}e)

Box[AND(OR(a, OR(b, OR(c, OR(d, OR(e, OR(f, g)))))), NOT(OR(K{P}(a), OR(K{P}(b), OR(K{P}(c), OR(K{P}(d), OR(K{P}(e), OR(K{P}(f), K{P}(g)))))))))](K{P}(e))

(M, 2) ⊭ [(a|b|c|d|e|f|g)&~(K{P}a|K{P}b|K{P}c|K{P}d|K{P}e|K{P}f|K{P}g)](K{P}e)
```
-----------------------------------------------------------------------------------------------------------------------  
Is the prisoner screwed?

```plain
a|b|c|d|e|f|g

OR(a, OR(b, OR(c, OR(d, OR(e, OR(f, g))))))

(M, 2) ⊨ a|b|c|d|e|f|g
```
-----------------------------------------------------------------------------------------------------------------------  


## Dining cryptographers
Three cryptographers are getting dinner. After dinner the waiter informs them that the meal has already been paid for by someone, either one of the cryptographers, or their employer, the National Security Agency (NSA). The cryptographers respect each other's anonymity, but want to find out whether the NSA has paid for dinner. They set up a two stage protocol, in the first stage each pair of cryptographers shares a random one-bit secret. In the second stage each cryptographer publicly shares a bit that is the result of the XOR function of the two secret bits if that cryptographer has paid, otherwise it would be the negation of that XOR function. Finally the XOR function is taken over all announced bits, if it’s 0 it implies that the NSA has paid. otherwise one of the cryptographers has paid, but it is unknown which one.

Before any announcements have taken place, do any of the cryptographers know whether any of the cryptographers have paid for the dinner?
```plain
K{A}(p|q|r)|K{A}(~(p|q|r))

OR(K{A}(OR(p, OR(q, r))), K{A}(NOT(OR(p, OR(q, r)))))

(M, 28) ⊭ K{A}(p|q|r)|K{A}(~(p|q|r))
-------------------------

K{B}(p|q|r)|K{B}(~(p|q|r))

OR(K{B}(OR(p, OR(q, r))), K{B}(NOT(OR(p, OR(q, r)))))

(M, 28) ⊭ K{B}(p|q|r)|K{B}(~(p|q|r))
-------------------------

K{C}(p|q|r)|K{C}(~(p|q|r))

OR(K{C}(OR(p, OR(q, r))), K{C}(NOT(OR(p, OR(q, r)))))

(M, 28) ⊭ K{C}(p|q|r)|K{C}(~(p|q|r))
```
-----------------------------------------------------------------------------------------------------------------------  
In the second stage, each cryptographer publicly announces a bit, which is: if they didn't pay for the meal, the exclusive OR (XOR) of the two shared bits they hold with their two neighbours. If they did pay for the meal, the opposite of that XOR.
After all announcements, do any of the cryptographers know the identity of the one who has paid for the dinner (in case it was paid by a cryptographer)?
```plain
?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{A}q)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{A}(q))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{A}q)
-------------------------

?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{A}r)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{A}(r))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{A}r)
-------------------------

?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{B}p)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{B}(p))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{B}p)
-------------------------

?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{B}r)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{B}(r))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{B}r)
-------------------------

?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{C}p)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{C}(p))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{C}p)
-------------------------

?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{C}q)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(K{C}(q))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!(K{C}q)
-------------------------
```
-----------------------------------------------------------------------------------------------------------------------  
After all announcements have taken place, is it common knowledge that the NSA has paid?
```plain
?(q^s^t)!?(r^t^u)!?(p^s^u)!C(~(p|q|r))

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(C(NOT(OR(p, OR(q, r)))))))

(M, 28) ⊨ ?(q^s^t)!?(r^t^u)!?(p^s^u)!C(~(p|q|r))
```
-----------------------------------------------------------------------------------------------------------------------  
After all announcements have taken place, is it common knowledge that one of the cryptographers has paid?
```plain
?(q^s^t)!?(r^t^u)!?(p^s^u)!C(p|q|r)

Whether?XOR(q, XOR(s, t))!(Whether?XOR(r, XOR(t, u))!(Whether?XOR(p, XOR(s, u))!(C(OR(p, OR(q, r))))))

(M, 28) ⊭ ?(q^s^t)!?(r^t^u)!?(p^s^u)!C(p|q|r)
```
