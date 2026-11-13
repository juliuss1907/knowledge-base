---
type: video
title: "CLAUDE.md and Agents.md Explained: Stop Repeating Yourself to AI"
url: https://www.youtube.com/watch?v=4m8AgfeK6kU
author: GritAI Studio
date_published: 2025-12-18
date_ingested: 2026-11-13
status: unprocessed
source: youtube.com
---

# CLAUDE.md and Agents.md Explained: Stop Repeating Yourself to AI

**Channel:** GritAI Studio
**Duration:** 14m 28s
**Published:** 2025-12-18
**URL:** https://www.youtube.com/watch?v=4m8AgfeK6kU

## Description

Stop re-explaining your tech stack to AI.

CLAUDE.md and agents.md give your AI tools persistent project context so they write code that actually matches your standards from the first prompt.

In this practical deep dive, you will learn how AI-first teams use context files to compound results over time. Based on GitHub's analysis of 2,500+ repositories, this video breaks down what belongs in CLAUDE.md, how to design specialist agents, and how to evolve your rules through real usage instead of upfront theory.

This is a follow-up to "10 Tips to Level Up Your AI-Assisted Coding", based on the most common questions and friction points you shared.

**What you will learn:**
- The 6 core sections every effective context file needs
- Live demo building a CLAUDE.md from scratch using /init
- How to create specialist agents for docs, testing, and security
- Common mistakes that make context files useless
- A simple, practical template you can use immediately

**Timestamps:**
- 00:00 Intro
- 01:43 What CLAUDE.md and AGENTS.md are
- 02:22 Why persistent context matters
- 03:17 The 6 core sections every context file needs
- 05:00 Practical example
- 05:34 CLAUDE.md starter template walkthrough
- 06:24 Capturing learnings and updating your rules
- 07:00 Subagents and specialist agent use cases
- 08:10 My top 5 tips for better context files
- 09:30 Common mistakes that break results
- 10:22 Bonus: Using subagents strategically
- 11:26 Step-by-step build demo
- 12:42 Managing memory and long-term context
- 13:33 Summary and wrap-up

**Resources:**
- https://butternut-answer-79c.notion.site/Context-Is-King-The-Deep-Dive-on-CLAUDE-md-and-Agents-md-Files-2cd16d29b7db80b3a6afd10fc8083f1a
- Anthropic on CLAUDE.md: https://www.claude.com/blog/using-claude-md-files
- GitHub on agents.md: https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/

## Transcript

In my top 10 video, I said context is
king. And a lot of you asked for the
deep dive. How do you actually do
context engineering? What goes into
these markdown files or rule files? How
do you structure them so that the AI
stops making the same mistakes? Today
I'm going all in on this.

This is the ultimate guide to rule files
for your AI assisted coding. Let's go.

Hey, Alex here from Grit AI Studio.
Anthropic just published their official
guide to Claude MD files, and GitHub
analyzed over 2,500 repositories to find
what actually works. And I'm going to
break down exactly how to build these
files step by step so you can stop
repeating yourself and start getting
consistent results. If you watch the 10
tips video, you know I'm obsessed with
compounding engineering. The idea that
every interaction should teach your AI
tools your patterns, your preferences,
your corrections. Over time, they
generate better code with less guidance.
Eventually, we move from reactive to
proactive. These rule files play a big
role in how you make that happen.
They're the foundation of compounding
engineering. Set them up right and every
future session starts smarter. Set them
up wrong or not at all and you're back
to explaining the same things over and
over again. AI slop waiting to happen.

Claude MD is Anthropic's approach for
Claude code. It lives in your repository
and Claude reads it at the start of
every conversation. It becomes part of
the system prompt persistent context
loaded automatically.
Agents MD is equivalent for GitHub
Copilot or Codex just to name a few and
cursor rules work similar in cursor.
Same concept but different file name.
Cursor also support claude MD files. The
underlying principle is identical across
all of them. Give persistent context so
you stop repeating yourself. Whatever
tool you're using, these principles
apply.

So here's the pain this removes. And if
you've been coding with AI for a while,
you've definitely felt this. Without
these files, every conversation starts
cold. You explain your tech stack. You
explain your folder structure that you
prefer type hints that your API routes
all start with /api/v1. Then you do it
again tomorrow and the next day.

Remember what I said in the 10 tips
video. LLMs have a fundamental
constraint, their attention budget. Too
much context, performance degrades. Too
little, hallucinations. The model fills
in the blanks because it's trained to
please you. A well-written context file
hits that sweet spot. The AI already
knows your patterns. It writes code that
matches your style. It runs your actual
test commands. It puts files in the
right places. Small improvements to
consistency compounded hundreds of times
across a project. That's where the real
value is.

GitHub's analysis of more than 2500 repositories found a clear pattern.
The best context files cover six areas. Let me walk you through each one.

Number one, commands. Put your actual
executable commands early in the file.
Not just npm, but npm test, npm run
build. Include the flags that you
actually use. The AI will reference
these constantly.

Number two, project structure. Give the AI a map of your
project. What's in the source folder?
What's in the test folder? Where do
config files live? Simple directory tree
does wonders. If you're using domain
driven design or a specific
architectural pattern, say so.

Number three, tech stack with versions. Don't
say React project, say React 18 with
TypeScript 5.3, Vite for bundling,
Tailwind CSS for styling, and so on.
Specifics matter because different
versions have different APIs. You don't
want the AI guessing which syntax to
use.

Number four, code style. One real
code example beats three paragraphs of
explanations. Show what good looks like
in your codebase. Naming conventions,
error handling patterns, how you
structure functions. Show it, don't
tell.

According to GitHub, number five,
git workflows: branch naming
conventions, commit message format, PR
requirements. This is especially
important if you're using agents to
create branches and pull requests.

Number six, boundaries. This is
critical. Tell the AI what it should
never do. Never commit secrets. Never
modify the vendor directory. Never
delete failing tests. The most common
helpful constraint in GitHub's analysis:
never commit secrets.

Let me show you how I build one of these from scratch.
In Claude Code, you can use the /init
command. It explores your entire
repository and writes a summary in your
Claude MD file. You can use that even if
you're not normally using Claude code.
Just copy it into your favorite coding
assistant. Claude scans your package
files, existing docs, config files, code
structure, and then it generates a
starter file. Now, here's the important
part. This is a starting point, not a
finished product. The generated file
catches obvious patterns, but misses the
nuances of how your team actually works.

Let me show you some examples of what I
normally add. First, I'm making the
commands more specific, the actual
commands that I would typically run.
Second, I try to provide workflow
instructions. For this project, we write
tests first. So, I add: when implementing
new features, write failing test first,
then implement, then verify tests pass.
Third, adding boundaries. Never modify
these files in migrations without
explicit approval or never remove
existing test cases. Always preserve
backward compatibility in public APIs.
Fourth, and this is where compounding
engineering really kicks in, I add
common gotchas, things that have bitten
us before. The database connection pool
exhausts if you don't close connections
in test. Always use the test DB fixture.
So on every time you fix a painful bug,
add a line here. Teach your AI coding
assistant to learn from its mistakes.
This is how you build institutional
knowledge.

Oh, and I said add a line here, but I of course meant ask your AI
to add a line here. In Claude code, use
the hash key to add the things you want
Claude to remember. When you've gone
through painful debugging and finally
solved something, don't just move on.
Say, "Summarize all the rabbit holes we
went through so that we avoid these
mistakes in the future." Then hit hash
and add it to your Claude MD. Build the
file through actual use. The best
context files grow through friction, not
upfront planning.

Now, let me show you something powerful that you can do in
both Claude and in GitHub Copilot:
specialist agents. Instead of one
general assistant, you create a team.
Each agent has a specific role, specific
knowledge, and specific boundaries.

Here's a docs agent. It's an expert
technical writer. It reads code from
source and writes documentation to
/docs. It knows to run npm run docs
build to check for broken links. And
critically, it never modifies source
code. That's a hard boundary.

Here's the test agent. QA engineer persona writes
tests, runs them, analyzes results,
writes to the test folder, and only that
folder. Key boundary: it never removes a
failing test. If a test fails, it
investigates why. It doesn't delete the
evidence.

This separation is powerful because each agent can be laser focused.
The docs agent doesn't get confused by
testing requirements and the test agent
doesn't accidentally modify production
code. And if you're using Claude code,
remember that sub agents have their own
context window. Same principle applies.
Define specialized sub agents for
different type of work.

Let me give you the tips that have made the biggest difference for me.

Tip number one, start simple and then expand through friction.
Don't try to write a comprehensive file
up front. Start with the basics:
commands, structure, and the stack. Then,
every time the AI does something wrong,
add a line to prevent it next time. Your
Claude MD should evolve from real
problems, not just theoretical concerns.

Tip number two, keep it concise. The
file loads into the context window every
single time. Remember, context is
precious. A 2,000 line Claude MD eats
into space for actual work. Every line
should earn its place.

Tip number three, code examples over explanations. Show,
don't tell. A single example of your
error handling pattern communicates more
than a paragraph describing it.

Tip number four, layer your files. You can
have a Claude MD in your home directory
for universal instructions, one in your
repo root for project-wide context, and
one in subdirectories for module
specific guidance. They stack. Use this
for monorepos or when different parts
of your codebase have different
conventions.

Tip number five, version control. This is documentation. Review
it in pull requests. When conventions
change, update the file. When someone
joins the team, they get that AI context
for free.

Let me also tell you what doesn't work. "You're a helpful coding
assistant." That's way too vague. This
tells the AI nothing useful. You might
as well not have a file at all.

I would also avoid putting commands at the
bottom. The AI references commands
constantly. Put them near the top where
they're easy to find and less likely to
get pushed out of attention.

Not defining boundaries: if you don't tell
the AI what not to do, it will
eventually do something destructive. Be
explicit about protected files,
directories, and actions.

And you should definitely avoid stale information. A
Claude MD file that references an old
tech stack or deprecated patterns is
worse than no file — it actively
misleads. Keep it current.

And of course, don't put any secrets in the
file. This file often gets committed to
version control. Never put API keys,
credentials, or sensitive URLs in the
file.

One more advanced technique that
ties back to the top 10 tips video.
Remember, I said each sub agent has its
own context window. Use that
strategically. Here's the scenario:
you've spent an hour debugging
authentication. Now you want a security
view of that code. Problem: all that
debugging context colors the security
analysis. Claude might overlook issues
because it's still thinking about the
fixes. The solution here is to tell Claude
to use a sub agent for the security
review. That gives a fresh context and
it focuses solely on vulnerabilities.

Same goes for /clear. When you finish one
piece of work and move on to something
unrelated, clear the context. Your
Claude MD stays loaded, the accumulated
noise goes away. Think of it like the
markdown trick: summarize where we are,
create next steps, put it in a markdown
file, clear, and then new conversation,
and then you can attach that file, and
you're in control of how you compact.

Okay, I'll include a template in the
description below so you can get started
today. Start with the /init command to
generate the file from Claude.
Describe your project tech stack and
give a map of your project with key
directories. Be specific with versions.
Tell your AI coding assistant about the
tools and commands to use and provide
examples, both good and bad. Specific
workflows might include explore, plan,
code, commit for features, test-driven
development for algorithmic work, or
visual iteration for UI changes.
Document your testing requirements,
commit message format, and any approval
steps.

When your coding agent knows your
workflow up front, it structures work to
match your team's actual processes
rather than guessing. An example
instruction might be something like
this: before modifying code in the
following locations, consider how it
might affect A, B, and C, construct an
implementation plan. Develop a test plan
that will validate the following.

Oh, and remember to provide boundaries and
keep adding your painful lessons
learned. Compound. When you end up
repeating yourself, turn that into a
slash command.

In Claude Code, we can manage our rule
files and so-called memories at the
project level so that we can share with
our team or across projects in our own
home folder to apply across all
sessions. We can even organize our
instructions in subfolders for modular
rules in our projects.

Claude code also supports symlinks to
share common rules across multiple
projects. The most effective Claude MD
or agent rule files solve real problems.
As Anthropic put it in their guide, they
document the commands you type
repeatedly, capture the architectural
context that takes 10 minutes to
explain, and establish workflows that
prevent rework. Your file should reflect
how your team actually develops
software, not theoretical best practices
that sound good but don't match reality.

And there you have it. That's the deep
dive on better rule files and context
engineering for AI assisted coding.
Start simple, add instructions when you
hit friction. Keep it concise and
version control it. And remember, this
is how compounding engineering actually
works. Every painful debugging session,
every rabbit hole, every "oh that's why
it broke" — capture it. Teach your AI to
learn from its mistakes. Over time, your
context file becomes institutional
knowledge that makes every future
session better.

If you haven't watched the 10 tips video yet, check that out
next. It covers the full picture of AI
assisted coding workflows. There's a
link in the description below.
