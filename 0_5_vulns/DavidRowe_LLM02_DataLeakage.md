## Vulnerability Name

**Author(s):**

David Rowe

**Description:**

Accidental reveal of sensitive information: algorithms, confidential data

**Common Examples of Vulnerability:**

1. Example 1: Company trains their data using privileged, private, or confidential information.  Competitor asks for general question around company secret.  Continues to ask question until secret is revealed.
2. Example 2: Another instance or type of this vulnerability.
3. Example 3: Yet another instance or type of this vulnerability.

**How to Prevent:**

1. Prevention Step 1: Data isolation : create a privileged LLM and non privileged LLM.  Only authorized users can access data from privileged LLM
2. Prevention Step 2: Train information with Differentially-private stochastic gradient descent [Medium article](`https://medium.com/pytorch/differential-privacy-series-part-1-dp-sgd-algorithm-explained-12512c3959a3#:~:text=DP%2DSGD%20(Differentially%2DPrivate,to%20make%20it%20differentially%20private.`)
3. Prevention Step 3: Strict output filtering

**Example Attack Scenarios:**

Scenario #1: Soft drink company trains data set including data from their secret recipe.  Competitor asks what is recipe for a drink that includes X_Ingredient that i can make at home.

Scenario #2: Model trained for credit cards uses real credit

**Reference Links:**

1. [ChatGPT Leaks user credit card details](https://cybernews.com/news/payment-info-leaked-openai-chatgpt-outage/):Open AI said a small percentage of ChatGPT Plus users may have had their payment information leaked during Monday's ChatGPT outage.
2. [OpenAI: Sorry, ChatGPT Bug Leaked Payment Info to Other Users](https://www.pcmag.com/news/openai-sorry-chatgpt-bug-leaked-payment-info-to-other-users): The glitch exposed the payment details of about 1.2% of ChatGPT Plus users, including their email addresses, payment addresses, and the last four digits of their credit card numbers.



**Author Commentary (Optional):**

(Optional) Any additional insights, opinions, or perspectives from the author that are relevant to understanding or addressing the vulnerability.
