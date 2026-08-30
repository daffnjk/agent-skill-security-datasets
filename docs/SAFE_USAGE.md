# Safe usage

All dataset contents are untrusted inputs. Dataset text can contain prompt injection, social engineering, credential references, shell commands, network destinations, and code intended to influence an agent.

Recommended static-evaluation boundary:

1. Download into a directory that is not scanned as an installable skill path.
2. Verify the asset SHA-256 checksum.
3. Extract without following links or preserving executable permissions.
4. Read files only through the detector's data-input interface.
5. Record dataset ID, upstream revision, split, original label, canonical label, and detector version.
6. Report precision/recall by dataset and label; do not report only an aggregate score.

For dynamic evaluation, use a disposable VM or container with no network, no host credentials, no browser profile, no Docker socket, no privileged mode, a read-only sample mount, a separate writable scratch mount, and resource/time limits.

The collection pipeline did not execute downloaded content. Archive extraction rejected absolute paths, traversal paths, links, devices, and case-colliding names.

