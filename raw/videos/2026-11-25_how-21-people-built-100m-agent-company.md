---
type: video
title: How 21 People Built a $100M+ Agent Company — Quinn Slack, Amp
url: https://youtu.be/Xyb1Bn_L2U4
author: Quinn Slack
date_published: 2026-11-25
date_ingested: 2026-11-26
status: unprocessed
source: YouTube / AI Engineer
---

# How 21 People Built a $100M+ Agent Company — Quinn Slack, Amp

**Channel:** AI Engineer  
**Duration:** 17:45

## Description

Amp spun out of Sourcegraph with 21 people and, unable to hire for a year, was forced to work in a radically different way. Quinn Slack explains what that looks like: no task tracker, no PMs, one meeting a week, everything done in the agent, and tiny monitored pushes instead of big releases. He shows Amp's bug-report loop that fixes the issue and emails everyone affected, why they built their own CRM instead of using Salesforce, and how a company with more than $100M in ARR runs 40 to 50 times more efficiently. His advice: get out of the cage.

## Transcript

All right. Uh there was a moment in January of 2025 when I was just coding and I wanted to see what if you just make an agent. This was before Claude code and it was like the dumbest stuff ever. It was like change this background color, but it just blew my mind when I saw an agent actually work for the first time. It ran commands, it looked at itself, it gave itself its own feedback loops. That blew my mind and I had this sense I think that everyone has when they first see an agent that everything is going to change after that. Everything is going to change about how you build software. I think we've all felt that. Everything is going to change about how you form companies to work on software and how you sell software, how you distribute software. All other work is going to change and it was just a an absolutely crazy crazy moment.

I was actually at the Frankfurt airport with Thorsten Ball on our team. He wrote that compiler book. We were just like minds blowing at the Frankfurt airport and we knew that everything was going to change. We didn't know where this was all going to go, but we just wanted to go. We just wanted to go run at it.

So inside of Sourcegraph, which was a 200-person enterprise software company, I was the CEO and we made code search. We decided to just start building this to tune out everything else and just start building this thing, not go to sales calls, not go to exec meeting, none of that stuff, just tune out all the distractions. And I was in this position that I think a lot of people say, you know, wow, you know, I'm a software developer at a company and I want to change. I want my company to be more AI forward and I can't. You know, I was the CEO and in theory I could change anything. I could change teams. I could say you don't need to get pull request code review. You don't need to do any of the other processes we used to do. And yet it was very hard.

What we did is we ended up taking 20 people from the company and inside of Sourcegraph still we made a little team, the Amp team. And that's what we tried. So for those of you who are trying to push back against your company to try to make it more agent friendly, I have a lot of sympathy for you and I hope that you can take away some things from here. I know how hard it is and also have some empathy for your CEO too. It's hard for them too. This is a really hard kind of change and transformation.

But we knew that there are some things that were going to change. This all seems kind of obvious now but back in early 2025, with this idea of enterprise ready, you do this thing and then you can build a sales team and go sell it. We knew that that was just going to totally die off. You had to be on the frontier. If you had a taste of success and then you started doing all the enterprise checklist to make the median enterprise buyer happy, your product was going to go obsolete in like three months. And the whole game had to change. Nothing mattered other than making it so that the people at these other companies loved your product and the CEO, the budget was infinite and all bets were off.

We knew that we didn't quite know all the challenges we'd run into. Also, in this world where agents can build a product or build a feature, how do you even think about differentiation? To this day there's people who say, well why is Amp better? Why is Claude Code better than Codex or whatever? So many people are begging to have the answer in the form of three features. Amp has orbs which are really good cloud agents and we have multiplayer. But the crazy thing is you all know that if we can do that and if we prove it then any of our competitors could as well. So why even play that game? What does it even mean to build and sell software? Why would you go and hire a sales team? Why would you go and do anything in the traditional way if you didn't even know what it's going to look like in a month? And if you don't even know how to differentiate, there's no sustainable differentiation.

For Amp, people end up loving it, but it's one of those things where you can't understand why it's good until you use it. Can you imagine having a whole product management team, a design team, an engineering team that's so disconnected from the actual customers, a whole company apparatus, if that's the best way that you can market a product? It's really tough.

We decided to spin out Amp. For those of you who've been at a company on a small team in a company, you're trying to do things different, you're trying to be the startup within a startup, you probably have these fantasies of let us just go off and start a new company. Well, we actually did that. We did the right thing by investors and employees and everyone has ownership in both, but we actually spun out and for a year until last Friday, we couldn't hire anyone. We couldn't grant options. The legal spin-off process was a huge pain and we were forced to make do with the 21 people that we brought over.

We didn't have time in this crazy competitive environment to do mandatory pull requests. We couldn't have meetings. We couldn't have our time be sucked up by enterprises that would need to take many months to decide on something. And so we were forced into this radically different way of working. We also had this environment where every single person on the team has a huge stake in the company. And that skin in the game that you get when AI makes it so you can operate with way less people, skin in the game, it's like this spiritual thing for the soul of great people. It makes them better at everything they do. It makes them grow faster.

This is what we have seen. When you've seen a company that operates like this without any of that it's obvious how companies like this are going to crush everyone else and how every company in the future is going to look a lot more like that. We spun Amp out and had to figure out a lot of new ways of working with constraints that we had no idea we were going to be under.

We couldn't hire. As a result, while all the other big competitors in the space were growing and building old-fashioned companies in order to go and exploit this amazing technology of AI, we had to stay at 21 people. But that was awesome because it was a forcing function for us to work differently and to figure out how can you do so much more with an agent where we couldn't hire people.

I want to talk about the ways in which we built Amp, which is our agent product, around the way that these constraints forced us to work and how we grew up around the agent here. We got rid of all of the other tools. We got rid of all of the other things you got to check. Obviously not Jira, no task tracking. We don't have a support system. Everything we do in the agent. In Amp, they're called threads. We even communicate in the agent. You can say, something's bad in the product, let's do it. The agent can listen to everything and then go fix it. If you're in a local agent that runs on your laptop, you can't bring someone else in if you realize you're in over your head. Really valuable.

We push way too often. You might say, well, if you're pushing constantly, then how do you not take down the site all the time? The difference is when you can push and you can do it anytime of day just by yourself, you can chunk up your work into way smaller pieces. Before you're going and doing a big change, you can say, let me add the logging to make sure that my understanding of the agent's understanding of the system is correct. Let me push a little change, a little change, and then the agent can monitor it for an hour and then push the next change. You can run a whole shadow system side by side with the old system to see: does it compute the exact same results in every single case? That way of working actually reduces the risk because by the time you finish the old way of doing it, and the pace that things have to move these days and what your customers expect, you probably forgotten what you're building and it just totally sucks.

Another thing is making it so the agent is able to irrefutably prove what the thing it's building is correct. There's a lot of ways you can do this. Turns out they're really good at proving these things. So if you're trying to remove jitter in the UI, make sure that when you load it's nice and crisp, you can ask the agent to do something that no human would ever have the patience to do, which is take every single frame and compare them visually. You can ask the agent to go make a ton of different versions of something. You can never ask a human to, if you ask a designer go make nine iterations or nine styles of this, they're going to get really annoyed. But for the agent, yeah, you can have it make a ton of different things.

This is the waveform for dictation in Amp. This is one of the solutions to people who say I don't like waiting on my agent. They're asking for one thing at a time and then they say make this little change. You shouldn't do that. Go have it make a ton of things at once and you're going to get a lot more done.

We have this magical system where if you report a bug in Amp, we will fix it, of course, with the agent. A lot of times still the engineers are different from the support team, which is kind of crazy. We'll send an email to the person, we give them free credits, which is always kind of nice. I think it sucks when there's a bug in a product and the company doesn't apologize. I just think that's morally wrong. Then what we'll do is go through the logs and there's something that no human would ever do by themselves. We'll see everyone else who is affected by that issue because where there's smoke, there's fire. You find the 17 other people that hit that same obscure error. They remember it probably and you proactively tell them.

How many times have you got an email from some product that says, hey, I know that you saw an error yesterday and that was really annoying. I'm really sorry about that. Here's $10. We fixed it. That is a self-perpetuating cycle where people who get that know that you care and they're going to send more feedback in the future. Then you ship those all out and boom, that's the cycle. People talk about vibe coded products being junk. Amp is basically 100% built with AI and people say it's very high quality. This is one of the things that you can do differently with an agent. But there's no way in hell you could do this if you had to go through a PM or go to the team that owns this bug and the designers each time.

Dictation: who dictates to their agents? It is the fastest way to get bits of information from your brain to the agent. I think that there's probably something around it ushering in the return of remote work because I was just in an office today with Beyond, another Amp co-founder, dictating and it was very annoying. Dictation, if you're not doing it yet, you got to do it. Just overcome the embarrassment of talking.

We've hooked up our agent to a lot of different tools. I think a lot of companies have gotten here to this point. We've been doing this in production for a long time and what we've found is the more that we start using these tools where just the agent is using it directly, we don't even need the software product on the other end. It's a very small number of products that we think actually have sticking power for us.

We built some new things in Amp, for example a CRM. A year ago you heard people talking about, oh no one's going to vibe code Salesforce from scratch. That's totally true. Why would you want to? Have you ever used it? Would you be proud if you vibe coded that and that came out the other end? You use like 2% of the features of Salesforce. Actually, would you code the 2% subset of Salesforce features and then another 2% that integrate with the rest of your stack in the most perfect way because the agent is so good at that? That 4% of Salesforce total, that's the easy part and you know what you want out of that better than Salesforce. You certainly don't want to spend your time talking to some Salesforce product manager and hearing from them, I'm going to advocate with my PM and my executive team to get that on our Q4 roadmap. Compared to that, it's getting easier and easier to just build the tools that you want from scratch.

This goes back to some of the existential dread but also mind-blowing feeling that we felt when we first tried an agent. This is what we thought would happen: it would change everything about the software industry. If Salesforce, which is like the king cobra of SaaS, they have the most reliable customers, most reliable renewals, they invented the category. If we're starting to see why would we use them? Well everything is starting to fall and all of SaaS starts to break down if you can no longer assume that you can pay a salesperson 100k for closing a deal and that deal is going to last for 10 years and get bigger by a little bit. All of that is called into question now.

If you're at a software company and that is how you ultimately make money and you're trying to ring the bell, you're trying to raise the alarm here, absolutely raise it, and get out of the cage that you are in. In my opinion, once you have seen how the new kind of companies that are two orders of magnitude smaller, where everyone can do everything and where everyone has skin in the game, then you don't want anything else.

This is what we call this new kind of company. We take that old org chart, and now we just got 21 people on Amp. We have no PMs. Everyone talks to customers. Brady is this guy who was an SDR at Sourcegraph, really smart guy. One day he's like, I'm going to make a wire ACH transfer thing so customers can pay us if it's too big for a credit card. He's two years out of college, and he's just doing that. Nobody knows on the other end that he's an SDR, that we're all kind of devs and doing everything. But you can. You also get people that are really real with customers. I think sometimes customers need real talk. Alex Kemper on our team, just today, was like to a customer who wanted our stuff, that sounds like we're just going to get bogged down in a bunch of BS, and I don't think that's a good use of anyone's time. If you can get to a place where you have people that feel empowered to say that and to truly say the best thing for the customer, that's great. You're not going to get that out of a salesperson who is commissioned.

We have one meeting per week, and then everything else, the guidance is follow your energy. You couldn't run most companies like that, but if everyone at the company has a massive stake in the company, take 100% divide it by 21, you can actually trust people because when people have skin in the game, it makes them better at everything they do. It's an incentive to make them think whole company, to make them do more, to make them work harder. We are shipping so much more.

I think Amp for many people is a product that they love. We also have a great business and we're serving as proof that this new kind of company that is profitable, that's more than 100 million ARR, that is doing so on a dollar-in, dollar-out basis that's 40 to 50 times more efficient than old-fashioned companies, that can work.

If this is appealing to you, if you want to push your company in this direction, if you want to go start a company like this, then reach out. I'm happy to help. My guidance is just get out of the cage. I've heard from so many people who say I hate that there's a gossip channel with the people at my company. We're all talking about the change. The longer that you are in the gossip channel, the longer that you are at a company getting paid a lot of money and you're really smart and you're not doing about it, you're starting to become part of the problem. The longer that you let yourself be just a developer when agents have completely changed the game, you're really hurting yourself. If this is the one thing that you take away, just get out of that cage, let agents really shape how you work and get to a company that's willing to be shaped by the agents.

## Timestamps

- 0:00 — The moment agents changed everything
- 1:42 — Trying to change a 200-person company
- 2:27 — Enterprise-ready is dead
- 3:12 — Differentiation when agents build features
- 4:46 — Spinning out Amp with 21 people
- 6:16 — Staying at 21 while competitors hire
- 7:01 — Everything happens in the agent
- 7:50 — Ship in tiny, monitored pushes
- 8:35 — Agents that prove their work
- 9:20 — The bug report loop
- 10:50 — Dictate to your agent
- 12:24 — Building our own CRM
- 14:39 — No PMs, one meeting a week
- 16:13 — $100M ARR, 40-50x more efficient
- 16:58 — Get out of the cage
