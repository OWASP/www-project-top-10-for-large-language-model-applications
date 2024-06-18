## 26 Sensitive Information Disclosure

> Expansion of LLM06 to include side-channel attacks, edits are in this background color

**Author(s):**
#### Rachel James
#### Bryan Nakayama

### Description
LLM applications have the potential to reveal sensitive information, proprietary algorithms, or other confidential details through their output. This can result in unauthorized access to sensitive data, intellectual property, privacy violations, and other security breaches. It is important for consumers of LLM applications to be aware of how to safely interact with LLMs and identify the risks associated with unintentionally inputting sensitive data that may be subsequently returned by the LLM in output elsewhere.

To mitigate this risk, LLM applications should perform adequate data sanitization to prevent user data from entering the training model data and ensure that the LLM application is securely designed. LLM application owners should also have appropriate Terms of Use policies available to make consumers aware of how their data is processed and the ability to opt out of having their data included in the training model.

The consumer-LLM application interaction forms a two-way trust boundary, where we cannot inherently trust the client->LLM input or the LLM->client output. It is important to note that this vulnerability assumes that certain prerequisites are out of scope, such as threat modeling exercises, securing infrastructure, and adequate sandboxing. Adding restrictions within the system prompt around the types of data the LLM should return can provide some mitigation against sensitive information disclosure, but the unpredictable nature of LLMs means such restrictions may not always be honored and could be circumvented via prompt injection or other vectors.
> Insecurely designed LLM applications that stream tokens to the user are also potentially susceptible to side-channel attacks, wherein an attacker could leverage patterns in LLM token length in order to decipher the contents or topic of the output.


### Common Examples of Risk

1. Incomplete or improper filtering of sensitive information in the LLM responses.
2. Overfitting or memorization of sensitive data in the LLM training process.
3. Unintended disclosure of confidential information due to LLM misinterpretation, lack of data scrubbing methods or errors.
> 4. LLM tokens are emitted sequentially, introducing a token-length side-channel.

### Prevention and Mitigation Strategies

1. Integrate adequate data sanitization and scrubbing techniques to prevent user data from entering the training model data.
2. Implement robust input validation and sanitization methods to identify and filter out potential malicious inputs to prevent the model from being poisoned.
3. When enriching the model with data and if fine-tuning a model: (I.e. data fed into the model before or during deployment)
  * Anything that is deemed sensitive in the fine-tuning data has the potential to be revealed to a user. Therefore, apply the rule of least privilege and do not train the model on information that the highest-privileged user can access which may be displayed to a lower-privileged user.
  * Access to external data sources (orchestration of data at runtime) should be limited.
  * Apply strict access control methods to external data sources and a rigorous approach to maintaining a secure supply chain.
> 4. Pad the token responses with random length noise to obscure the length of the token so that responses can not be inferred from the packets.

### Example Attack Scenarios

1. Unsuspecting legitimate User A is exposed to certain other user data via the LLM when interacting with the LLM application in a non-malicious manner.
2. User A targets a well crafted set of prompts to bypass input filters and sanitization from the LLM to cause it to reveal sensitive information (PII) about other users of the application.
3. Personal data such as PII is leaked into the model via training data due to either negligence from the user themselves, or the LLM application. This case could increase risk and probability of scenario 1 or 2 above.
> 4. A user is interacting with an LLM application that streams tokens while an attacker intercepts them in order to identify the topic and potentially the contents of the outputs, leading to the disclosure of embarrassing personal information.


### Reference Links

1. [Mitigating a token-length side-channel attack in our AI products](https://blog.cloudflare.com/ai-side-channel-attack-mitigated): **Cloudflare** 
