# Redistribution policy

Each upstream dataset is evaluated independently. A permissive license on this catalog does not override upstream terms.

| Policy | Meaning |
| --- | --- |
| `full_release` | The selected upstream files are packaged as a separate release asset with attribution and revision metadata. |
| `conditional_release` | The asset is isolated because its license adds conditions such as non-commercial use and share-alike. |
| `metadata_release` | Only upstream-authored benchmark metadata/splits are packaged; third-party full text or packages are excluded. |
| `metadata_only` | No dataset samples are rehosted. The catalog provides source URL, revision, labels, and acquisition notes. |

Before publishing a new snapshot:

1. Recheck the current upstream license at the pinned revision.
2. Identify third-party artifacts whose terms differ from the benchmark's own metadata license.
3. Package each dataset independently.
4. Include the upstream URL, revision, license expression, and checksum beside every asset.
5. Do not silently replace release assets; publish a new snapshot tag.

Removal or correction requests should be handled per dataset without deleting unrelated releases.

