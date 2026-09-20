---
type: article
title: "Jalapeño Shows Power of LLMs for Chip Design"
url: https://spectrum.ieee.org/llms-for-chip-design
author: IEEE Spectrum
date_ingested: 2026-09-19
status: processed
compiled_at: 2026-09-20
compiled_to: "[[src_jalapeno-llms-for-chip-design]]"
source: spectrum.ieee.org
---

# Jalapeño Shows Power of LLMs for Chip Design

On 25 August, OpenAI fully unveiled Jalapeño, the company's debut AI accelerator chip. Jalapeño delivers up to 13.4 petaflops of 4-bit compute and accesses 232 gigabytes of the most advanced memory available, linking to it at a blazing 15.4 terabytes per second. Benchmarks cited by OpenAI show that Jalapeño can reduce end-to-end latency (the time between prompt to last token) by up to 3.6 times when compared to Nvidia's GB300—a chip the company currently relies on—and do so while consuming less power.

Whether these figures translate into real-world gains once Jalapeño enters widespread service in OpenAI's inference fleet remains to be seen, but performance is only half the story. The other half is how the chip was designed—a process which, as you might expect, was accelerated by OpenAI's large language models (LLMs). Jalapeño moved from first architecture concept to first silicon in under 20 months. Only nine months separated the first RTL—the register-transfer level code defining the chip's logic—from tape-out, when the finished design goes to manufacturing.

That's a rapid timeline, yet experts believe it could soon look slow as LLMs improve and become more deeply integrated into chip design tools. OpenAI, unsurprisingly, is bullish about the opportunities. "The models are giving superpowers to our engineers," says Richard Ho, vice president of hardware at OpenAI. "Our engineers are still driving the work. They're still the final arbiter of what's going on. But they can do things a lot faster. They can explore a lot more paths."

## OpenAI achieved fast results with a small design team

Ho says the group that designed Jalapeño averaged fewer than 100 people over the course of the project and continues to stand at roughly 100 today as the team pursues second and third-generation designs. That number includes a broad swath of roles across the hardware team, from system design to software and supply chain, but not those at Broadcom, which partnered with OpenAI on the project.

The division of labor between OpenAI and Broadcom was generally split between design and implementation. OpenAI's team was responsible for end-to-end system design including the inference accelerator, the memory hierarchy, and networking. Broadcom handled "physical design from the gates onward," Ho says.

The partnership with Broadcom dampened some opinions on OpenAI's speed. David Chin, co-founder at agentic chip design startup Verkor.io, says "the schedule they gave us is quite credible," but believes that Broadcom's help was essential to Jalapeño's rapid timeline. "If you have somebody else start from scratch, it won't be possible," he says. Ravi Krishna, also a co-founder at Verkor, called OpenAI's speed "a relatively impressive result," but added that he expects that improvements in the capabilities of LLMs could result in even quicker timelines if the project started today.

Andrew Kahng, distinguished professor at the University of California, San Diego, also found OpenAI's speed notable, saying it's "likely best in class today." Kahng recalls a 2016 IEEE Design Automation Futures workshop, which he co-organized. The workshop included Richard Ho, at the time an engineer at Google, as a keynote speaker. Ho had strong opinions on design automation and framed the time required to complete a chip's design as a function of the number of iterations a team could complete in a day.

## How OpenAI's LLMs accelerated Jalapeño's design

"Automation itself has existed in chip design for many decades. It's not a new problem," says Ankur Srivastava, director of semiconductor initiative and innovation at the University of Maryland, in College Park. Where LLMs differ from prior automation tools, however, is their ability to understand language and code. He says this makes them particularly suited for chip design tasks that "are still in the linguistic domain of the problem."

The team at OpenAI designed a workflow that takes advantage of this strength. OpenAI's front-end workflow was built around Accelerated Hardware Synthesis (XLS), an open-source high-level synthesis chain of tools originally developed at Google. High-level synthesis is a form of chip design automation that allows engineers to design a chip in a more familiar programming environment. In the case of XLS, chip designers can write in languages such as DSLX (a domain-specific language inspired by Rust) and C++. XLS then converts these to Verilog, a hardware description language used to describe electronic systems.

"We were thinking about how to leverage AI to make the project faster, and the AI was much better at software-looking things," says Chris Leary, member of technical staff at OpenAI. "XLS in some ways looks like software, so it got that benefit." It helped, too, that Leary was extremely familiar with how XLS should function, as he started it during his time at Google.

Kahng agrees that the decision to use AI to accelerate high-level synthesis, such as XLS, makes sense, as it's "more natural for the LLM to work with" and provides the opportunity for fast iteration. "I see this as a generally useful workflow, and it's one that 'has legs' going into the future," he says.

The same logic led the Jalapeño team to focus on software optimization. When the first chips came back from the foundry in May, the team pointed its internal AI models at designing software to run benchmarks such as SemiAnalysis's InferenceX. On DeepSeek's multi-head latent attention kernel benchmark, performance climbed from 0.31 percent of the theoretical ceiling (set by the chip's compute and memory bandwidth) to 88.94 percent in roughly 40 hours. Ho says this result is repeatable, so the time between when foundries deliver the first chips and when production ramps up can be reduced. "All our schedule assumptions are going to be based on the fact we have this capability now," he says.

While the broad strokes of the Jalapeño teams' AI-assisted workflow were guessed by Ho and Leary up front, improvements in OpenAI's models did offer a few surprises.

Leary says that the project began with assistance from models like OpenAI's o3, which was released to the public in April of 2025 (but available to the Jalapeño team earlier). By the time the project had wrapped up, however, the team had access to models that were precursors to GPT-6 Astra, which wasn't publicly released until 3 September 2026. The newer model can work directly in Verilog without needing XLS's translation from ordinary programming languages, and it's close to being able to operate proprietary design tools on its own, Leary says.

Ho also confirmed that the team had access to internal LLMs fine-tuned for chip design that are not available to the public. He declined to detail the models used. However, he added that the Jalapeño team partnered with OpenAI's research team. While not all specific models used to design Jalapeño are publicly available, Ho says the goal is to bring lessons learned from the project into the company's commercial LLMs. "It's safe to say that Astra and following models will be very good at chip design," he says.

## AI was less useful for backend optimization, but that could change

As mentioned, the bulk of OpenAI's work on Jalapeño focused on the "front end" of chip design, which spans the tasks that take a chip from initial concept, through writing RTL code to define the design, and through verification that the design will work when physically implemented. Much of the "backend" design—which includes tasks like routing interconnects, completing and verifying the clock and power specifications, and sending the required design information to the foundry—was handed off to Broadcom, which carried the chip through production.

That's not to say OpenAI's workflow ignored the backend, though. The Jalapeño team includes physical design engineers who work with their counterparts at Broadcom to provide guidance on the chip's floor plan and routing, among other things.

At IEEE Hot Chips 2026, Ho and Leary put numbers on the gains from AI-guided physical design optimization, including an area reduction of 10 percent for the matrix multiplication units as measured against an optimized human baseline. In other words, OpenAI claims AI-guided optimization helped design more circuits into the same area of silicon than would have been possible before.

Broadcom used its own internal workflow. The company's team did not have access to the internal models OpenAI used to help design Jalapeño, but it did have access to OpenAI's public, commercial models.

Verkor's Ravi Krishna says that OpenAI's approach to backend design already feels a bit conservative. He believes that to be an artifact of when the project, which began in October of 2024, took place. "The models from the last four to five months have improved. From April [2026] onwards…is when they really started to be able to handle those tasks better," he says. Verkor co-founder Suresh Krishna agreed, saying "there's no reason you couldn't have an agentic loop that largely accelerates the backend of the process as well."

Ho and Leary also hinted that the workflow used to design Jalapeño may look old-fashioned compared to the team's next efforts.

"As you can imagine with Jalapeño, we were trying to go as fast as we could. So there's a trade-off between 'do we want to take time to do some innovation, or do we want to do things that we know work historically?'" Leary says. "With the second generation, we have a kind of reset opportunity to ask about all the things we want to get set up for."

Ho says the second-generation chip's workflow has "a lot of places that we are introducing [AI]." He mentions opportunities to do more with AI in verification and physical design. Leary adds that the team now has tools for automatic waveform manipulation and viewing. This automates analysis to identify chip clock signals associated with failures and could improve debugging the hardware while it's still being designed.

Despite these expected improvements, Ho and Leary were clear that they don't believe chip design can be fully automated. "We're not saying that anyone can come and just build state-of-the-art, frontier AI/ML accelerator chips using just [OpenAI's coding platform] Codex," Ho explains. "We are saying some very specific things about how to be better at Codex and how we are focusing on a small team and fast timelines to reach quality results."
