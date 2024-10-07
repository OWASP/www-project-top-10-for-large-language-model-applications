## LLM06: 機微情報の漏出

### Description

LLMアプリケーションは、その出力を通じて機微情報、独自のアルゴリズム、またはその他の機密情報を公開してしまう可能性があります。その結果、機密データへの不正アクセス、知的財産やプライバシー侵害、その他のセキュリティ侵害を引き起こす可能性があります。LLMアプリケーションの利用者は、LLMと安全にやりとりする方法を認識し、機密データを意図せずに入力すると、それが他のどこかで出力され得ることに関連するリスクを特定することが重要です。

このリスクを軽減するため、LLMアプリケーションは、ユーザーデータが訓練データに混入しないように、適切にデータのサニタイズを行う必要があります。また、LLMアプリケーションの所有者は、適切な利用規約を用意し、利用者のデータがどのように処理されるか、及び自分のデータがモデルの訓練に含まれることをオプトアウトできるかについて、利用者に対して認識させる必要があります。

LLMと利用者アプリケーションの相互インタラクションは、双方向の信頼境界を形成しますが、クライアントからLLMへの入力、およびLLMからクライアントへの出力のそれぞれは本質的に信頼できません。この脆弱性は、脅威モデリング演習、安全なインフラ、適切なサンドボックスなどの、特定の前提条件については範囲外であると想定していることに注意することが重要です。LLMが返すべきデータの種類に関する制限をシステム・プロンプト内に追加することで、機密情報の漏出を緩和できる可能性があります。しかし、LLMには予測不可能な性質があるため、そのような制限が常に守られるとは限らず、プロンプトインジェクションや、他の方法によって回避される可能性があります。

### Common Examples of Risk

1. LLMの回答に含まれる機密情報に対しての不完全または不適切なフィルタリング
1. LLMの訓練過程における機微情報の過学習または記憶
1. LLMによる誤った解釈、データスクラビングの欠如、またはエラーに起因する、意図しない機密情報の開示

### Prevention and Mitigation Strategies

1. データの適切なサニタイズとスクラビング技術を統合し、ユーザーデータが訓練データに混入することを防ぎます。
1. 悪意のある可能性がある入力を特定してフィルタリングするため、堅牢な入力検証とサニタイズ手法を実装し、モデルが汚染されることを防ぎます。
1. データによりモデルの質を高める場合、またはモデルのファインチューニング
(https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions )を行う(すなわち、デプロイ前あるいはデプロイ中にモデルにデータを与える)場合、
1. ファインチューニングデータの中で機密性が高いとみなされるものはすべて、ユーザーに公開される可能性があります。したがって、最小権限のルールを適用し、最高権限のユーザーができて、より低い権限のユーザーに表示される可能性がある情報は使用せずに訓練を行います。
1. 外部リソースへのアクセス(実行中のデータオーケストレーション)は制限される必要があります。
1. 外部データソースに対する厳格なアクセス制御と、安全なサプライチェーンを維持するための厳格なアプローチを適用します。

### Example Attack Scenarios

明らかに正当なユーザーAが、悪意のない方法でLLMアプリケーションと対話する際、LLMを介して他のユーザーのデータが暴露されます。
ユーザー A は、巧妙に作成されたプロンプトのセットを使って、LLM からの入力フィルターとサニタイズをバイパスし、アプリケーションの他のユーザーに関する個人情報 (PII) を暴露させます。
ユーザー自身またはLLMアプリケーションの過失により、PIIのような個人情報が訓練データを介してモデルに漏洩されます。この場合、上記のシナリオ1または2のリスクと発生確率が高まる可能性があります。

### Reference Links

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use): **Cohere**
4. [A threat modeling example](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP AI Security & Privacy Guide**
6. [Ensuring the Security of Large Language Models](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
