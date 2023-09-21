# Entry Style Guide

This document contains guidance on styling specific to the creation and
maintenance of the OWASP Top 10 for LLMs entries.

<!-- TODO: complete this -->

# Entries

* For each security risk, include the following information:

  1. A brief description of the risk
  2. Common examples of the vulnerability
  3. Recommendations for mitigating the risk
  4. Example attack scenarios
  5. Reference links


## Styling

### Risk Listings:

For each of the top 10 risks, use level 2 headers for the risk name:

```markdown
## Data Poisoning
```

## Description:

Each risk should have a brief description. These should be created using a
level 3 header, and should be written in standard paragraph form.
If there's important terminology or phrases, **bolden** them.

```markdown
### Description

Data poisoning refers to the malicious alteration of **training data** to
influence the behavior of AI models.
```

## Common Examples

Common examples should be contained in a level 3 heading subsection, with each
risk listing at least one example:

```markdown
### Common Examples

1. Example 1: Specific instance of this type of risk.
2. Example 2: Another example of this type of risk.
```

## Prevention

Preventions should be contained in a level 3 heading subsection, with each
risk including at least one prevention strategy:

```markdown
### Prevention

1. Prevention Step 1: A step or strategy that can be used to prevent the vulnerability or mitigate its effects.
2. Prevention Step 2: Another prevention step or strategy.
3. Prevention Step 3: Yet another prevention step or strategy.
```

## Example Attack Scenarios

Attack scenarios should be contained in a level 3 heading subsection, with each
risk should contain at least one example attack scenario.

```markdown
### Example Attack Scenarios

1. A detailed scenario illustrating how an attacker could potentially exploit this vulnerability, including the attacker's actions and the potential outcomes.
2. Another example of an attack scenario showing a different way the vulnerability could be exploited.
```

### References:
List all references or sources at the end of the document in a level 3 heading subsection:

```markdown
### References

1. [Link Title](URL): Brief description of the reference link.
2. [Link Title](URL): Brief description of the reference link.
```
