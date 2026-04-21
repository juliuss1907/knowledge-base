---
type: raw
source_type: article
source_url: https://layerzero.network/blog/kelpdao-incident-statement
date_ingested: 2026-04-20
tags: [#crypto, #web3, #security]
status: processed
processed_date: 2026-04-21
---
# KelpDAO Incident Statement | LayerZero

## Summary

On April 18, 2026, KelpDAO was exploited for approximately $290M. Attributor: highly-sophisticated state actor, likely DPRK's Lazarus Group (TraderTraitor). Zero contagion to any other cross-chain assets or applications. Incident was isolated entirely to KelpDAO's rsETH configuration due to their single-DVN setup.

## Root Cause

KelpDAO used a 1-of-1 DVN setup with LayerZero Labs as the sole verifier — directly contradicting LayerZero's express recommendation of multi-DVN redundancy. LayerZero claims they communicated best practices around DVN diversification to KelpDAO multiple times.

## Technical Details (LayerZero Labs DVN Attack)

1. Attacker compromised **downstream RPC infrastructure** that LayerZero Labs DVN uses to verify transactions
2. Attack was NOT through protocol exploit, DVN exploit, or key management
3. Attack steps:
   - Gained access to list of RPCs used by LayerZero DVN
   - Compromised 2 independent nodes (separate clusters, no direct connection)
   - Swapped out binaries on op-geth nodes
   - Executed RPC-spoofing attack with custom payload designed to forge a message to the DVN
   - Malicious node told truth to external RPCs (including Scan service) but lied to DVN
   - DDoSed uncompromised RPCs to trigger failover to poisoned RPCs
4. LayerZero's DVN setup is trust-minimized (uses internal + external RPCs), but attacker bypassed via DDoS on non-compromised RPCs

## What LayerZero Claims

- **No protocol vulnerability** — LayerZero protocol functioned exactly as intended
- **Modular security worked** — attack was isolated to single application, zero contagion to other OFTs/OApps
- LayerZero Labs DVN is now live again
- Will NOT sign messages from applications using 1/1 DVN config
- Reaching out to all 1/1 DVN apps to migrate

## LayerZero's Security Posture

- Complete EDR on every device
- Access controls per application
- Completely isolated environments
- Full system logging
- Dedicated internal security team + external vendors
- SOC2 audit in final stages
- DVN infrastructure runs across self-operated AND external RPC nodes
- Least-privilege principles with layered authentication

## Path Forward

- All affected RPC nodes deprecated and replaced
- LayerZero Labs DVN is operational
- Will not sign messages from 1/1 DVN applications
- Cooperating with law enforcement globally
- Supporting Seal911 and industry partners to track funds

## Key Message

> "LayerZero protocol itself functioned exactly as intended. The single defining feature of LayerZero's architecture is modular security, and in this case it did exactly what it was meant to — the entire attack was isolated to a single application."
