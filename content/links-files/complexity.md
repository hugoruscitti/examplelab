Complexity is the enemy
=======================

- Artículo extraído desde: [https://neugierig.org/software/blog/2011/04/complexity.html](https://neugierig.org/software/blog/2011/04/complexity.html)

April 23, 2011

I'm almost through my seventh year working at Google(!). I have learned
many things there, more than I could ever write down. I thought I would
at least share with you something that's only come to me with more
experience.

Complexity is the death of software. It's hard to quantify the cost of,
and it tends to creep in slowly, so it's a slow boil of getting worse
that's hard to see until it's too late. On the other side, frequently
it's easy to see a benefit of increasing complexity: a new layer of
indirection allows new feature X, or splitting a process that ran on one
machine into two allows you to surmount your current scaling hurdle. But
now you must keep another layer of indirection in your head, or
implement an RPC layer and manage two machines.

The above is hopefully just as obvious to a new programmer as it is to a
veteran. What I think I've learned through my few years in the industry
is a better understanding of how the balance works out; when complexity
is warranted and when it should be rejected. I frequently think back to
a friend's comment on the [Go compiler](http://golang.org/) written by
[Ken Thompson](http://en.wikipedia.org/wiki/Ken_Thompson): it's fast
because it just doesn't do much, the code is very straightforward.

It turns out that, much like it's easier to write a long blog post than
it is to make the same point succinctly, it's difficult to write
software that is straightforward. This is easiest to see in programming
langauge design; new languages by novices tend to have lots of features,
while few have the crisp clarity of C. In today's programs it's
frequently related to how many objects are involved; in distributed
systems it's about how many moving parts there are.

Another word for this problem is cleverness: to quote another one of the
C hackers, "Debugging is twice as hard as writing the code in the first
place. Therefore, if you write the code as cleverly as possible, you
are, by definition, not smart enough to debug it."

What helps? I wonder if it maybe just comes down to experience — getting
bitten by one too many projects where someone thought metaprogramming
was cool. But I've found having specific design goals to evaluate new
code by can help. It's easier to reject new code if you can say "this
does not help solve the initial goals of the project". Within Google the
template document for describing the design of a new project has a
section right at the top to list *non-goals*: reasonable extensions of
the project that you intend to reject.

Ironically, I've found that using *weaker* tools can help with
complexity. It's hard to write a complicated C program because it can't
do very much. C programs tend to use lots of arrays because that's all
you get, but it turns out that arrays are great — compact memory
representation, O(1) access, good data locality. I'd never advocate
intentionally using a weak tool, though. Instead, my lesson has been:
write Python code like it was C.
