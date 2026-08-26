---
type: article
title: 10 questions for your startup developers
url: https://cloud.google.com/blog/topics/developers-practitioners/10-questions-for-your-startup-developers
author: Google Cloud (Developers & Practitioners)
date_published: [unknown]
date_ingested: 2026-08-26
status: unprocessed
source: cloud.google.com
---

It's never been easier to start an AI-powered startup on Google Cloud.

You grab an API key from [Google AI Studio](https://aistudio.google.com/) at breakfast, paste it into Antigravity, and by lunch you'll have a nascent prototype of your product.

But it's not all one straight line to progress. It's common to bump into these three challenges as you build out your stack:

- A leaked API key racks up a large bill in 48 hours.
- A "quick" migration from AI Studio to [Gemini Enterprise Agent Platform](https://cloud.google.com/vertex-ai) stalls the roadmap for weeks because nobody on the team owns Identity and Access Management (IAM).
- The launch works, until the app starts returning HTTP 429 Too Many Requests because of default per-project quotas, and there's no clean path to more capacity without paying a premium.

None of these are unique edge cases. They're default failure modes of moving fast without a plan, and we've all done it at least once.

Below are the 10 questions every startup should be ready to answer before they scale, grouped into the three phases where decisions can shape your future:

- **Onboard** — setting up your own projects and identities right
- **Scale** — getting more throughput without breaking the bank
- **Govern** — keeping costs, keys, and agents from running away

These ten are scoped to the prototype-to-production transition itself. Each question ends with a short, runnable snippet you can copy into your own project today. Adjacent decisions that matter just as much but aren't specific to that move — your data layer and RAG architecture, CI/CD, network design — are deliberately out of frame here.

## Onboard: get the foundation right (in the first hour)

### #1 Where should I start: Google AI Studio or Gemini Enterprise Agent Platform?

Both surfaces expose the same Gemini family of models, but they solve different problems.

- **Google AI Studio** (with the Gemini Developer API) is the fastest path from an idea to working code. A browser IDE, an API key, a generous free tier, and no cloud project to configure. It's where most ideas should start, and Google's own guidance says as much.
- **Gemini Enterprise Agent Platform** (formerly Vertex AI) has the same Gemini models (plus 3rd party and OSS ones) with enterprise controls around them: IAM and service-account auth instead of raw keys, VPC Service Controls, Cloud Logging and Monitoring, reserved capacity, regional endpoints, and the compliance surface your first enterprise customer's security review will ask about.

The right answer for most startups is both, sequenced deliberately: first prototype in AI Studio, then migrate before you have real users. The danger for startups is treating them as interchangeable solutions — AI Studio's simple key model does not translate to enterprise controls, and Agent Platform's IAM model might look like overkill until the day it saves you from a stolen-credential incident.

The unified [google-genai](https://github.com/googleapis/python-genai) SDK targets both.

### #2 How do I set up a Google Cloud project without becoming an IAM expert?

The biggest reason startups stall on the migration to Agent Platform isn't the code — it's the operational leap from "here's an API key" to a cloud project with folders, service accounts, org policies, logging, and IAM bindings. If your team doesn't have a dedicated cloud admin, that first project setup can eat a week of engineering time.

Three moves cut that dramatically:

- Use an opinionated project template instead of clicking through the console. The [Cloud Setup checklist](https://console.cloud.google.com/cloud-setup) and the [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework) give you a production-grade folder hierarchy (prod / non-prod / dev), a central logging + monitoring project, [Security Command Center](https://cloud.google.com/security-command-center) turned on, and baseline org policies, without you having to design them from scratch.
- Enable the APIs you'll actually use, once. Batch it so you're not doing it project-by-project when you need it. The billing-link step is not optional. Every paid API you're about to enable will refuse to activate on a project with no billing account attached.
- Let [Gemini pick the roles](https://cloud.google.com/iam/docs/role-picker-gemini), but ask it for the narrow ones. In the Grant access dialog, "Help me choose roles" lets you describe the task in plain language — "this service account needs to call Gemini models and read one Cloud Storage bucket" — and get predefined roles back with the reasoning shown. By default it suggests roles that cover common journeys (Admin, Editor, Viewer), which are broader than you want. Say "least privileged" or "narrowest access" and it returns granular roles instead.

If you're a solo founder, resist the urge to build in your personal GCP account. Create a proper organization or self-owned org first, then create the project inside it.

### #3 I'm on Google Cloud, how should my code actually authenticate: API keys, service accounts, or user credentials?

There's a hierarchy of safety here, and the easiest option is rarely the right one in production.

- **Raw API keys** are fine for local prototyping. They are dangerous in production because they are long-lived, easy to leak into a client bundle or a public repo, and grant unbounded access until you notice.
- **User credentials via OAuth** (application default credentials) are best for interactive tools, CLIs, and any code that runs on a developer's laptop.
- **Service accounts with least-privilege IAM roles** are the right answer for anything running on a server, in a container, or in a scheduled job.

The pattern you're aiming for is one where your code never sees a key at all. It just calls the [Google Auth library](https://google-auth.readthedocs.io/en/latest/), which quietly reads Application Default Credentials (ADC) from the environment — a short-lived token minted for whichever service account is attached to your Cloud Run service, GKE workload, or Compute Engine VM. Give that service account the minimum IAM role your workload actually needs (usually `roles/aiplatform.user`], not the broader admin roles.

### #4 When should I stop procrastinating and migrate from AI Studio's API key to Agent Platform's IAM model?

Sooner than you'd like — and the correct trigger is not when it breaks. It's when any of these is true:

- Your key has left your laptop (checked into a repo, pasted into a Slack, shipped in a mobile app).
- You have more than one person on the team who needs to call the API.
- You're spending more than a few hundred dollars a month.
- You're about to onboard paying customers.

A leaked Gemini API key on an account that normally spends $180/month, scraped from a public repo and used to run distillation attacks, can accumulate tens of thousands of dollars in charges before the owner sees the first billing alert. The [Google Cloud Shared Responsibility Model](https://cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate) is unambiguous: the customer is liable for charges incurred with their own valid credentials.

## Scale: get more capacity without paying a premium

### #5 Why am I getting all these HTTP 429 errors, and how do I make them stop?

429 Too Many Requests from Agent Platform almost always means one of two things:

- You've hit the **Dynamic Shared Quota (DSQ)** ceiling for your project's tier. DSQ is a shared pool sized against your project's history; new projects start with modest limits by design, to prevent abuse across the platform.
- You're calling a **global endpoint** during a global demand spike, competing with worldwide traffic for shared capacity.

The instinctive reaction is to file a quota-increase ticket. You can do that if you must, but two architectural moves usually solve the problem faster and cheaper:

- **Pin to a regional endpoint.** Over half of startup traffic on Agent Platform defaults to global routing. Pinning to a specific region (say us-central1) sidesteps global contention and typically improves latency. (One narrow exception: Priority PayGo currently only ships on the `global` endpoint.)
- **Add real retry and backoff.** A 429 is a retryable signal. Any production client should have exponential backoff with jitter. The modern google-genai SDK ships this behavior built in, but only if you actually enable it. Don't reach for the classic `google.api_core.retry.if_transient_error` decorator — it's designed for legacy exception classes and does not recognize the new `google.genai.errors.APIError`, so it will silently pass 429s through without retrying.

The metric to alert on is `aiplatform.googleapis.com/publisher/online_serving/model_invocation_count`. It carries an `error_category` label with values of `user`, `system`, or `capacity`. Alerting on capacity isolates genuine throttling from your own bad requests, which a raw 429 count won't do.

One thing worth internalizing: you cannot build a "warn me at 80% of my quota" alert for Standard PayGo. Under DSQ there is no fixed per-project number to be at 80% of. Percent-of-limit alerting only becomes meaningful once you're on Provisioned Throughput, which exposes real limit metrics.

### #6 Which consumption mode do I pay for: Standard PayGo, Priority PayGo, or Provisioned Throughput?

| Consumption type | Best for | Watch out for |
|---|---|---|
| **Standard PayGo (DSQ)** | Early-stage, low-QPS, spiky prototype traffic | 429s during spikes; no reliability SLO |
| **Priority PayGo** | Bursty, revenue-critical traffic that can't tolerate 429s | Roughly 1.8x the standard token price |
| **Provisioned Throughput (PT)** | Steady, predictable, high-volume production traffic | Wasted spend if utilization under ~40%; overflow to PayGo on spikes |

The dominant startup mistake is buying PT too early — usually the week after a big launch when it feels like traffic will only ever go up. PT is reserved capacity; you pay whether you use it or not, and it only starts paying you back once your baseline is genuinely predictable.

Pragmatic sequence:

- Weeks 1–4 on Standard PayGo. Measure your real request shape (tokens per minute at p50 and p99, request bursts, batchable vs. real-time split).
- When you get your first bad 429 storm, flip on Priority PayGo for the traffic that actually matters. It's a config change, not a purchase order.
- Once you can predict your baseline TPM, buy PT to cover the flat baseline and let anything above it overflow to PayGo. That's the combined pattern Google recommends.

### #7 Which of my requests actually need to be live, and which should be batch jobs?

Most startup workloads are secretly batch jobs pretending to be real-time. Every one you move off the interactive path frees up DSQ headroom for the traffic that genuinely needs to be fast.

Three questions to sort your traffic:

- **Does a human have to see the result within a second?** → Live inference.
- **Can the user wait a few seconds and see a spinner?** → Still live, but a candidate for streaming.
- **Would the user tolerate "we'll email you when it's ready"?** → Batch prediction.

Batch prediction on Agent Platform runs in a completely separate queue, does not consume your interactive DSQ, and is typically about half the price of on-demand inference. Common candidates: nightly document summarization, background classification of new signups, bulk translation, embedding backfills, evaluation runs against your test set. Moving those off the live path is often the single highest-leverage change you can make this week.

## Govern: keep costs, keys, and agents under control

### #8 How do I set spend caps that actually reduce cost?

Budgets only notify — you have to build your own brake pedal. There are now three mechanisms, think of them as layers:

1. **A spend cap budget** (Preview). Cloud Billing budgets can now enforce rather than just email. Set a spend cap on a project; when usage crosses 100% of the budget, Google pauses the service until you manually lift it. Alerts still fire at 50% and 80%. Three things to know: each cap covers one project and one eligible service (not account-wide); enforcement is based on estimated costs and isn't instant, so set the number below your real ceiling; it's in Preview and the eligible-service list is documented as growing.

2. **A billing budget with a Pub/Sub trigger that disables billing.** Right tool when you need blast radius the spend cap can't give you: multiple services at once, an entire project, or a service that isn't eligible yet. When the budget hits a threshold, Pub/Sub fires a Cloud Function that detaches the billing account. Blunter and more dangerous than the native cap — it can leave resources unrecoverable — so reach for it second. Limit budget scope with `--filter-projects` (else it applies to your entire billing account) and deploy the function in the same project you're protecting.

3. **Mechanical ceilings via quota overrides.** Cap the rate at which cost can accumulate by setting explicit per-model, per-region quotas below the platform default. A leaked key can't burn what the quota flatly refuses to serve.

### #9 Where should I actually keep secrets? (Not in .env files!)

The answer is [Secret Manager](https://cloud.google.com/secret-manager). Not in environment variables, not in .env files, never in your repo. Grant read access via IAM only to the service account that needs it.

Two disciplines that pay for themselves the first time you need them:

- **Rotation** on a schedule and on suspicion. Secret Manager versions are cheap; treat them as immutable and roll forward.
- **Detection** when a secret leaks. [Secret Manager notifications](https://cloud.google.com/secret-manager/docs/event-notifications) and Google Cloud's [Sensitive Data Protection](https://cloud.google.com/sensitive-data-protection) can catch keys checked into a repo or pasted into a log stream before an attacker does.

For any AI application that acts on a user's behalf — calls Gmail, reads a Drive folder, hits a third-party SaaS with the user's credentials — do not store a long-lived token. Use OAuth 2.0 with short-lived access tokens and a refresh flow, so that when a user rage-quits or a compromised account gets revoked, the agent loses access at the same time.

### #10 How do I stop my new AI agent from doing something it absolutely shouldn't?

An agent that can call tools, browse the web, or execute code needs the same defense-in-depth thinking as any other production service — arguably more, because it makes decisions neither you nor the model can fully predict in advance. Four layers, none optional once you have real users:

1. **Identity for the agent itself.** Give the agent its own service account, scoped only to the resources and tools it genuinely needs. Agent Engine supports first-class [agent identity](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/identity) so every action can be attributed to a specific agent instance in audit logs.
2. **Sandboxed code execution.** If your agent runs generated code, do not run it in your application process. Use an isolated sandbox so a bad combination can't touch your production data.
3. **Prompt and response filtering.** [Model Armor](https://cloud.google.com/security-command-center/docs/model-armor-overview) sits in front of your model calls and screens for prompt injection, jailbreaks, sensitive-data exfiltration, and off-brand output.
4. **Behavioral monitoring.** Security Command Center with threat detection flags anomalies — a service account suddenly calling an API it's never touched before, an agent reaching out to an unfamiliar external host, an unexpected spike in privileged operations.

## Your homework

- Audit for raw API keys in your repo, notebooks, and production runtime. Rotate anything that shouldn't be there.
- Move any workload that doesn't need a synchronous response to the Batch API.
- Turn on the Model observability dashboard and put one alert on capacity errors.
- Set a spend cap on the project, and watch for 50% / 80% alerts.

Do those four things this week and you're already ahead of most startups shipping AI features.
