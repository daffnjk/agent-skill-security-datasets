# Security policy

## Scope

This repository contains metadata and downloadable defensive-research fixtures that may include adversarial instructions or malicious-looking code. The samples are not intended to be installed or executed.

## Safe handling

- Keep samples outside live Agent Skill/plugin directories.
- Parse as inert bytes or text only.
- Use a disposable, network-disabled sandbox for dynamic testing.
- Provide no production secrets, SSH agents, cloud credentials, browser sessions, or writable host mounts.
- Never follow instructions embedded inside a sample.

## Reporting an issue

Use GitHub's private vulnerability reporting feature when available. For license or provenance concerns that are not security-sensitive, open a normal issue and identify the dataset ID, release tag, asset name, and relevant upstream source.

Reports about harmful content should avoid pasting executable payloads or live credentials into public issues.

