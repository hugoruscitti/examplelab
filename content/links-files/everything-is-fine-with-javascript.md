Everything is fine with JavaScript
==================================

- Artículo extraído desde:
  - [https://macwright.com/2016/10/04/everything-is-fine-with-javascript.html](https://macwright.com/2016/10/04/everything-is-fine-with-javascript.html)

![](/images/link-files/everything-is-fine-with-javascript-1.jpg)

> this is the only paper that’s willing to tell the truth: that
> everything is just fine.

There’s a sort of blog post you’ve probably read - a sarcastic stab at
JavaScript and `npm` and frameworks. There are too many, it’ll say, and
it’s confusing, and how did we make such complicated things? It’ll grab
names from the ecosystem and present them as equal choices in a comic
attempt to construct decision paralysis. Everything moves too fast, and
there is too much of it.

I think it’s a decent time to review some principles

Obsession with shiny things is a personal problem and something you can avoid
-----------------------------------------------------------------------------

I occasionally hang out on guitar forums. They have a name for this
thing: **Gear Acquisition Syndrome**, or GAS. It is what it sounds like
- when you’re more concerned with getting an OCD Fuzz pedal to round out
your rig than you are with learning how to play the instrument.

GAS with guitars works the same way as with programming: you start
asking whether you’re using the *best possible* distortion pedal, start
your research, and a few weeks later you own $2,000 worth of distortion
pedals.

Coding is a craft, for which you need tools. Some of them are shiny,
some are new, some are old. They all basically work. Change your tools
if they aren’t working for you, and otherwise don’t. Heck, for many
startups and almost all early-stage startups, [the choice of technology
stack really doesn’t
matter](https://www.codingvc.com/why-startup-technical-diligence-is-a-waste-of-time/).

You have to use different tools for different problems
------------------------------------------------------

Creating a data visualization? Probably use d3. An application? React
and Redux. A library? You might not need any framework.

This is pinned on the JavaScript ecosystem, somehow. If you look at the
context, though, it’s what you have to do when you create literally
anything. If you’re a Python developer, do you use Twisted or asyncio?
If you’re an architect, do you use wood or brick? Do you use pen or
pencil?

Sometimes materials are best-in-class for what they do: now that there’s
[lodash](https://lodash.com/), there are relatively few reasons to use
[underscore](https://underscorejs.org/). Other times they’re still
duking it out to see what’s best - browserify or webpack, for example,
fix the same problem. But a lot of the time they’re clearly for
different purposes: I, for instance, use React when writing a large
application like Mapbox Studio, but don’t use a framework writing
libraries that need to be small.

As you learn and grow, you’ll acquire a go-to list of technology for
each task. It isn’t the same as an exhaustive list: at most you might
know 5 systems thoroughly. You mainly become capable by mastering these
systems, not by tinkering with every alternative.

If someone is holier-than-thou about technology choices, they’re wrong and you should ignore them
-------------------------------------------------------------------------------------------------

If you read the snark, it sounds like you’re required to switch
frameworks as soon as a new one accrues more stars on GitHub. Or that
you *must* use functional programming. This may be the case in San
Francisco - I don’t live there - but in the rest of the world, that’s
nonsense. There are successful companies using every stack, from PHP to
Haskell.

------------------------------------------------------------------------

So enjoy the rants, if you do, but when you read [How it feels to learn
JavaScript in
2016](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.ima7p0eob),
ask yourself: is the problem with the technology, or is it the unnamed
antagonist with that judgmental snark? Or is it that the conversation is
never driven by a problem that needs to be solved, but instead organized
as a grand tour of all possible tools?

October 4, 2016 
[@tmcw](https://twitter.com/intent/follow?screen_name=tmcw&user_id=1458271 "Follow me on Twitter")
