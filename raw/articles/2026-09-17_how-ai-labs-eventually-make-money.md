---
type: article
title: How will AI labs eventually make money
url: https://michaellwy.substack.com/p/a-subway-company-solved-ais-business
author: michaellwy
date_ingested: 2026-09-17
status: unprocessed
source: michaellwy.substack.com
---

# How will AI labs eventually make money

Happy to share that my essay has been selected as 1 of the 3 finalists out of 600 entires in Dwarkesh Patel's [Blog prize for the big questions about AI](https://www.dwarkesh.com/p/blog-prize-winners?r=12b707&utm_medium=ios&triedRedirect=true)!

What's the most plausible story where foundation model companies actually start making money? If you consider each individual model as a company, then its profits [may](https://epoch.ai/gradient-updates/can-ai-companies-become-profitable) be able to pay back the training cost. But of course, if you don't train a bigger, more expensive model immediately, then you stop making money after 3 months. So when does the profit start? Maybe at some point [scaling will plateau](https://www.dwarkesh.com/i/187852154/005849-how-will-ai-labs-actually-make-profit), but [if progress at the frontier](https://x.com/MatthewJBar/status/2046060153678844290) has slowed down, then the combination of distillation and low switching costs (cloud margins result from high switching costs) makes it really easy for open source to catch up to the labs, eating into their margins. So how do the labs actually start making money?

There is an industry with the following economics: billions in upfront capital before earning a dollar. Core service priced near marginal cost. Enormous value created for users and almost none captured by the builder. Also, there is relentless pressure to keep investing in the next generation of infrastructure. No, not AI Labs, I'm actually talking about mass railway systems.

Many have reached for the railroads analogy when discussing the business of AI. Most conclude that the lesson is commercial viability requires state subsidy for a general purpose technology with public good properties.

I want to challenge that, because Hong Kong's MTR actually solved the problem as one of the only mass transit systems in the world that is commercially self-sustaining, publicly listed, paying dividends with no government operating subsidy.

MTR's core rail service has never funded its own expansion. In [2018](https://www.mtr.com.hk/archive/corporate/en/investor/pre_blackout_202407.pdf), its best pre-covid year, transport operations earned HK$2.0 billion in EBIT. [Estimated capital expenditure for 2024–2026 is HK$87.9 billion](https://www.mtr.com.hk/archive/corporate/en/investor/pre_blackout_202407.pdf), nearly all rail-related. Three years of peak rail earnings would cover 8% of that. The rail has never paid for itself through fares.

MTR fares are kept affordable through a [government fare adjustment mechanism](https://www.mtr.com.hk/sustainability/en/financial-sustainability.html). You can't price transit to recover full construction costs because it would be unaffordable and defeat the purpose providing broad access for citizens. Each rail line can maybe cover its operating costs, but fare revenue never stretches to fund the next line. AI API pricing faces a similar constraint. Distillation and open source alternatives deflate API prices roughly [10x per year](https://epoch.ai/gradient-updates/can-ai-companies-become-profitable), and any lab that prices above marginal cost would lose volume to rivals. Each model can be [operationally profitable](https://epoch.ai/gradient-updates/can-ai-companies-become-profitable) on inference but the margin never stretches enough to fund the next training run.

The standard global solution is subsidy. London Underground requires billions in TfL grants. China's national high speed rail carries a trillion dollars in debt with 94% of routes unprofitable. AI is on the same trajectory: CHIPS Act, Stargate, sovereign wealth fund investments and Pentagon contracts. The default endpoint is subsidy-dependent quasi-public infrastructure.

So how did MTR find another way?

When MTR was established in 1975, its designers understood that fares alone would never recover construction costs. So they structured the corporation around a different premise. They understood that the rail line would make surrounding land valuable, so why not own the land?

HK's MTR develops residential towers, offices and shopping malls above and adjacent to its stations, capturing the value appreciation that its own infrastructure creates. Property profits cross-subsidize rail operations and fund the next line. Today MTR owns [122,000 residential units, 16 malls and 5 office buildings](https://www.mtr.com.hk/archive/corporate/en/publications/images/business_overview_e.pdf), and property generates the [majority of actual profit](https://www.minichart.com.sg/2026/03/12/mtr-corporation-2025-annual-results-financial-performance-property-development-and-railway-expansion-updates/). Instead of trying to capture value through the rail service itself, MTR owns the assets that appreciate because of the rail service.

"When do labs make money?" has the same structure as "when does rail pay for itself through fares?"

A biotech startup uses a frontier model to screen drug compounds, shaving two years off a clinical trial. A logistics firm uses AI to optimize routing, saving $40 million in fuel costs. A solo developer ships in a weekend what used to take a five person team three months. In each case the model provider captures a fraction of a percent through API fees. The provider can't charge more, because four other labs and a dozen open source alternatives offer comparable capability. The surplus flows to the users and the broader economy. This is what general purpose technologies tend to do. The steam engine, electricity and TCP/IP all generated zero revenue for their creators.

What MTR would probably tell AI labs is this: stop trying to make fares cover construction and find the property.

A government could grant a lab exclusive deployment access to national health records, tax systems or defense logistics. The lab accumulates domain data, integration depth and regulatory clearance that takes years to replicate. This is functionally equivalent to MTR's mechanism: development rights granted by the state justified by natural monopoly properties.

Accumulated RL reward data is second. Billions of interaction signals that train the next model generation. Unlike weights (which depreciate via distillation), RL data is practically non-replicable and compounds across generations. It doesn't convert to revenue directly, but it's a land bank. Appreciating and undeveloped.

Forward-deployed integration is third. Instead of selling model access to a consulting firm that captures the productivity surplus, own the service delivery end to end similar to the way Palantir embeds engineers inside government agencies rather than licensing software. The lab doesn't charge the law firm an API fee but becomes the legal research service, priced against the outcome it delivers rather than the tokens it serves. Switching costs would compound with accumulated domain data and institutional knowledge. This is like MTR's shopping mall: capture the foot traffic the rail creates rather than charging passengers more for the ride.

Data trusteeship over national datasets is fourth. Governments sit on enormous underleveraged datasets (patient records, tax filings). A frontier lab designated as trustee gets exclusive access to train on and build products against this data. But this creates a public-private data monopoly and would require careful governance: clear boundaries on usage, benefits flowing back to the public, independent monitoring and real sanctions for misuse.

The labs that survive won't be the ones that make the API profitable. They'll be the ones that identify their property above the station and build toward it now. The API is the rail and it will likely never be profitable enough. The actual money is in what appreciates around it.

The policy question then follows: instead of subsidizing training runs, governments should design institutional mechanisms (deployment rights frameworks, data trusteeship structures, productivity measurement standards) that let labs capture the surplus their infrastructure creates.

The AI policy conversation is dominated by the US-China frame: American free market labs versus Chinese state-funded champions. The most relevant institutional model may be neither. It may be Hong Kong's, a 45 year old public-private hybrid, commercially operated, self-financing through institutional design rather than ideology.
