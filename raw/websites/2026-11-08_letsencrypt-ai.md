---
type: website
title: "Let's Encrypt AI — A position paper on private AI"
url: https://letsencrypt.ai/
author: Let's Encrypt AI
date_ingested: 2026-11-08
status: unprocessed
source: letsencrypt.ai
---

# Let's Encrypt AI — A position paper on private AI

An independent position paper.

Our goal: protect AI chats with confidential computing on most AI GPUs by the end of 2027.

## 01 / The conviction: Your work belongs to you.

### A prompt is someone's work.

A discovery. A business plan. A private conversation. A line of code that took years of experience to write.

We are putting more of our lives into AI. The next generation of models will help us think, build, diagnose, negotiate and invent. The value in those conversations belongs to the people having them.

Paying for an answer should buy you an answer. It should never quietly give a model trainer a free copy of your ideas, your customers' secrets or your company's intellectual property.

Access to intelligence should come with ownership of your own thinking. Training on someone's data should be a separate, informed agreement: permission, clear terms and compensation. Our private work should stay outside the training pipeline unless we choose to put it there.

We can build that boundary into the machines. The technology is here. Now we need to make it ordinary.

## 02 / The standard: Privacy with proof.

### Encrypt the work. Verify the machine.

Encryption protects data on the wire and on disk. Confidential computing extends protection into the place where AI actually runs: the CPU and GPU.

A trusted execution environment, or TEE, isolates sensitive execution from the host operator. Remote attestation lets a client check evidence about the hardware and approved software before it releases sensitive data.

- **Protect the whole route:** Keep prompts, responses, caches and transfers within a protected path, from the client to attested CPU and GPU execution and back.
- **Make the software inspectable:** Publish the security-critical source, build measurements and verification tools. Bind the encrypted connection to the approved workload.
- **Keep content under the user's control:** Reviewed software must enforce the content-logging and reuse policy. An enclave alone can still run code that copies your data.
- **Make verification a condition of service:** Verify the actual route. Stop when its evidence fails. Give customers explicit control over every fallback and external tool.

The boundary matters: a confidential gateway is only one part of the route. Hardware and firmware flaws, compromised clients, untrusted software and external tools still matter.

## 03 / Cyber defense: Make hardening routine.

### Harden our systems for AI-powered attacks.

Confidential computing should become a cyber-defense priority far beyond AI.

AI-assisted attacks are raising the stakes. The UK's National Cyber Security Centre expects AI to increase the speed and scale of attacks. We should use this moment to make hardened, verifiable infrastructure easier for everyone to adopt.

- **Close administrative entry points:** Disable SSH and production debug shells. Keep only the services and processes the workload needs.
- **Boot a known image:** Deploy reviewed, versioned images with immutable system partitions. Rebuild and redeploy updates rather than modifying live machines.
- **Verify before sharing secrets:** Check hardware, software measurements and security settings against an approved policy before releasing keys or data.
- **Protect the running workload:** Use hardware-backed isolation and protected memory to limit access from compromised hosts and infrastructure operators.

### NVIDIA supports it. You can build with it.

NVIDIA builds confidential-computing capabilities into supported AI platforms. Its deployment options, hardware-rooted trusted execution environments, and open-source attestation SDK enable developers to build and verify services.

## 04 / Already possible: Start with one workload.

### Use it today.

Private AI is already available across enterprise buying, developer APIs and everyday chat. Start with open-weight models and verified confidential computing offerings.

## 05 / The leverage: Let demand change the default.

### Open models can move the whole market.

Start with open-weight models. Make encrypted AI chats, backed by verified confidential computing, an everyday experience.

As more people and companies choose those services, their spending creates demand for the same protection everywhere. Every workload moved and every contract that requires attestation gives the next provider a reason to offer it.

Our aim is to make that demand strong enough that OpenAI, Anthropic and other frontier labs have to offer verifiable confidential computing to win those customers. People should be able to choose the model they want while keeping their conversations private.

### Protect customers' secrets, too.

Anthropic already makes the case in its research on confidential inference (protecting model weights and user data via measured software and controlled key release). The goal is to extend this research into a customer-verifiable service with attestation and bound connections.

## 06 / The goal: 31 December 2027

### Make confidential computing the default for AI chats.

By the end of 2027, we want AI chats protected by verifiable confidential computing on most AI GPUs. The goal is to protect people's prompts, responses and context while they are processed.

- **Start today — Move one workload:** Run a real task on a verified confidential route. Compare cost, quality, latency and evidence.
- **Build through 2027 — Make it routine:** Put verification into SDKs, route selection and procurement. Publish the evidence and the gaps.
- **By year-end 2027 — Make it the norm:** Buyers ask for attestation. Operators protect AI chats during inference. Model builders compete on intelligence.
