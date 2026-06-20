---
type: article
title: "The Seed and the Machine"
url: https://bitsquarks.substack.com/p/the-seed-and-the-machine
author: bitsquarks
date_published: 2026-06-16
date_ingested: 2026-06-16
status: processed
compiled_at: 2026-06-17
compiled_to: "[[src_the-seed-and-the-machine]]"
source: Substack
---

# The Seed and the Machine

**Author:** bitsquarks  
**Source:** Substack  
**URL:** https://bitsquarks.substack.com/p/the-seed-and-the-machine

---

The atomic unit of software work is now the loop. What follows traces that loop all the way down, into how systems get built, where data lives, what a system is allowed to remember, and who is left standing when assembly gets cheap. The same geometry that lets a system compound is the geometry that makes it forget.

Most companies that put AI into production this year will have little measurable return to show for it. By the surveys and post-mortems gathered so far, the figure is somewhere close to ninety-five in a hundred. The pilots ran. The licences cleared procurement. The launch was demonstrated and noted. And twelve months on, the number the work was meant to move tends to sit close to where it started.

A smaller group, roughly five in a hundred, sees a different result. Their systems compound, cycle after cycle, and the distance from the rest tends to widen rather than close.

By the end you will know what that smaller group does differently, why the familiar explanations for the gap do not hold up well, what it means to build a system as a seed rather than assemble it as a machine, the one test that tells you which of the two you have built, the cost the loop quietly carries inside the geometry of its own memory, and the shape of organisation all of this tends to favour. What follows is a single idea, traced all the way down.

The gap between those two groups is one of the more consequential patterns in enterprise technology right now, and the explanations usually offered for it tend not to hold up well. It gets read as a budget gap. It is not: the ninety-five spent plenty, and many of them outspent the five. It gets read as a talent gap, a sign the winners hired better people. It is not that either. It gets read as a model gap, as though the five found some frontier capability the rest were locked out of. They did not. The model the winners use is, in almost every case, the same model available to everyone who failed. It is one API call away from the ninety-five who saw no return.

The divide is a building-method gap. The ninety-five assembled something. The five planted something. Those are different acts, they produce different objects, and the objects behave differently over time.

What follows is about that difference, traced all the way down.

## The first domino

Loop Native Factory, the first in this series, made one claim: the atomic unit of software work had changed. Work used to be a task you finished and shipped. It had become a loop: a model running in a harness, against a context, under a policy, until a verifier decides the work is done. That argument was about the loop as a unit of work, and it stopped there, because that was enough to carry on its own.

It was not enough for the argument. A loop does not sit in isolation. It is built by someone. It runs against data. It accumulates a memory. It is operated inside an organisation. Each of those is a thing the loop touches, and each of them changes once the loop arrives. The loop was the first domino. What follows is about the rest of them falling.

The thread that connects them is a single migration. Software is moving out of a world where things are finished and into a world where things compound. The loop was the first unit to make that move: work stopped being a finished artefact and became a process that improves while it runs. What follows is the same move, made again, in four more places: in how systems are built, in where data lives, in what a system remembers, and in how the people around it are organised. And at the end of that chain there is a cost, a real one, written into the geometry of the systems themselves. The loop is not free. What follows is what it costs.

## Start with building

Start with building, because it is the first thing the loop changes.

Assembly is how software has always been built. Gather the components, wire them together, ship the finished thing. The result is a machine: complete on the day it ships, and obsolete from that same day, because the model at its centre will be replaced within months and the assembled structure around it cannot move. A machine does not get better while it runs. It degrades, slowly, as the world drifts away from the assumptions baked into it.

A seed is the other thing. And a seed is not a smaller machine. It is a different kind of object. A small tree and a seed are not the same thing at two sizes; a tree, even a small one, is a finished structure whose form is fixed. A seed carries almost none of its eventual structure inside itself. It is a compact core plus a set of rules for how it grows, and it becomes a structure by reading the soil, the light, and the water it actually finds. Plant the same seed in two places and you get two different trees. The seed did not specify the tree. The environment finished it.

An AI system built as a seed has three parts, and each one maps to something concrete.

**There is the core**, small and stable and slow to change: the runtime the system executes in, the boundary that enforces what it may and may not do, and the loop that lets it learn.

**There are the growth rules**, the heart of the seed, and not features. A growth rule is a rule for how the system reads its environment, generates what it needs from what it finds, and verifies what actually works. Introspect, generate, verify.

**And there is the environment**: the data estate the system is planted in, the policies it lives under, the domain meaning specific to this one company, the stream of corrections from real users doing real work. The environment is the soil, and the soil is half the system. It is the half no requirements document can contain, because it is different in every enterprise and never the same twice.

The shift shows up even in the smallest places. Installing software has always meant running a script: a fixed sequence of explicit steps, written in advance, blind to the machine it will land on. Some software shipped this year does not install that way. What ships instead is a short block of text. It names the tools available and the outcome wanted and instructs an agent to work out the rest, and that agent reads the environment it is actually in and debugs its own way to a working install. The script was a machine, every step frozen. The block of text is a seed, complete only once it has grown into the ground it was planted in.

The lesson underneath is the whole argument. The structure was never the hard part. The meaning was. Knowing the names of the tables is easy, and a model can read a schema in a second. Knowing that when one company says active customer it means a specific value in a specific column under a specific business rule, while the company down the road means something entirely different by the identical words: that is not in the schema, and it is not in the model. It is something the system has to learn, from its environment, and hold, and carry forward. A loop that learns and holds and carries forward is a seed. A loop that does not is just a faster way to stay still.

## Ora: a real seed

It is easier to see all of this in something real, so here is one I built.

Ora is an open-source system for asking a database a question in plain language and getting a correct query back. It is an old problem, and for years the tools aimed at it kept failing in the same three ways: they linked to the wrong columns, they invented joins, and they broke the moment a question was rephrased. The striking thing was how stubbornly those cracks held: the tools were replaced with every cycle, and yet the same three failures stayed exactly where they were, which is usually the sign that a problem has stopped being a failure of the tools and become a failure of the method behind them. Each of those tools had been assembled from finished parts, when what the problem actually called for was something planted and grown in place.

So Ora was built as a seed, and its three parts are visible in the architecture.

**The core** is small and stable: a runtime that executes the work as a pipeline, a policy gateway that decides what a query may do before it ever reaches a database, and a learning loop that lets the system improve. None of that changes when the model changes, which is exactly the point of putting it in the core, since it is the part of the system with no expiry date.

**The growth rules** are the heart of it, and they are introspect, generate, verify. Ora ships with knowledge of no particular database. Pointed at one, it reads the schema for itself and builds a map of the tables, their keys, and the shape of the data. A real schema can run to hundreds of columns, far more than a model should ever be handed at once, so Ora narrows that to the handful a given question actually needs before any model is called. It indexes the real values in the columns too, so a question about premium tier customers can be resolved against the fact that this database happens to store that tier as a particular code in a particular field. Then it generates the query, runs it, and checks it against the database itself, in a correction loop that treats the database's own response as the ground truth rather than the model's confidence. A question that spans several databases is split, run against each in parallel, and recombined. Introspect the environment, generate from what is found, verify against what is real. Those are growth rules, not features.

**The environment** is the data estate Ora is planted in, and it is the part no design document could ever hold. Every company's schema is different, and, as the active customer problem showed, every company means something different by the same words. That meaning is not in the schema and not in the model. It has to be learned from the ground. Ora's learning agent does exactly that: after every query, every correction, every piece of human feedback, it updates a persistent picture of how this company and this user think about their data. The hundredth query runs against a system that understands the business better than the first one did.

This is also why Ora works against any model and any database. The model at its centre is rented, and a better one arrives every few months; the design assumes that swap and makes it cheap. The databases belong to whoever already owned them. Nothing that was bought is part of the moat. What was built, and what survives every swap, is the semantic layer and the learning loop: the accumulated, corrected, company-specific understanding of what the data means. That is the seed. The model and the database were never the asset.

## The swap test

All of this resolves into something concrete, and the concrete version is a single exercise you can run this week, on a system you already own.

Picture the model at the centre of that system replaced tomorrow by a better one. It will be. Now write down everything you would keep, unchanged, because it still holds its value the day after the swap. Not the things you would be sorry to lose. The things you would actually carry across, untouched.

That list is your seed. Everything not on it was scaffolding.

A machine, run through that test, leaves almost nothing on the list. The connectors get absorbed by the next model release. The prompt-craft is automated from underneath. The orchestration framework is replaced by a thinner one. The gold tables were shaped for questions that have already moved. A seed, run through the same test, leaves the part that was always the point: the growth rules, the semantic layer, the verifier, the accumulated meaning.

Most enterprises have been accounting for scaffolding as though it were an asset. The swap test is how you stop. It is also the design question at the centre of any system built to last: which parts survive when the model underneath gets replaced. The team that names its swap-survivors early is the team still moving two years later.

## Three layers, one shift

The move from assembly to planting is not happening at one layer of the stack. It is happening at all three layers of what we actually mean when we say building AI, and seeing all three at once is what makes it impossible to dismiss as a metaphor.

**Start with software**, because it is the most concrete. Building software has always meant, in large part, writing the connective tissue: the integration code, the glue between one system and another. It was slow, unglamorous, and the highest-margin work in enterprise software precisely because it was so tedious that companies would pay almost anything to avoid doing it. That work is now being done by the system itself. Point a capable model at the specification for an interface it has never seen and it writes a working connector. A real one, nearly every time, once it is allowed to test what it wrote and fix it. The connector, that reliable enterprise moat, is becoming something a seed grows in place.
