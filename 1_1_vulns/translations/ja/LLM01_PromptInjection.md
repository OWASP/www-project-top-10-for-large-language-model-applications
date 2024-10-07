## LLM01: プロンプト・インジェクション

### Description

プロンプト・インジェクション脆弱性は、攻撃者が細工した入力によって大規模な言語モデル(LLM)を操作し、LLMが攻撃者の意図を理解せずに実行することで生じます。これは、システムプロンプトを " jailbreak " することで直接実行されることもあれば、操作された外部入力を通じて間接的に実行されることもあり、データ流出やソーシャルエンジニアリングなどの問題につながる可能性 があります。

* **直接的なプロンプトインジェクション**は、"jailbreaking "としても知られ、悪意のあるユーザが基本的なシステムプロンプトを上書きしたり、明らかにしたりすることで発生します。攻撃者は、LLMを通じてアクセス可能なセキュアでない関数やデータストアを操作することで、バックエンドシステムを悪用することができます。
* **間接的なプロンプトインジェクション**は、Webサイトやファイルなど、攻撃者が制御可能な外部ソースからの入力をLLMが受け入れることに起因します。攻撃者は、外部コンテンツにプロンプトインジェクションを埋め込み、会話のコンテキストを乗っ取る可能性があります。これにより、LLMは「混乱した代弁者」として動作し、攻撃者はユーザーまたはLLMがアクセスできる追加システムを操作できるようになります。さらに、間接的なプロンプトインジェクションは、テキストがLLMによって解析される限り、人間が閲覧/読み取り可能である必要はありません。

プロンプトインジェクション攻撃が成功すると、機密情報の収集から、通常の操作を装った重要な意思決定プロセスへの干渉まで、その影響はさまざまです。

高度な攻撃では、LLMを操作して悪意のある人物になりすましたり、ユーザー設定のプラグインと相互作用させたりすることも可能です。その結果、機密データの漏洩、プラグインの不正使用、ソーシャルエンジニアリングが発生する可能性があります。このような場合、侵害された LLM は攻撃者を支援し、標準的なセーフガードを乗り越え、ユーザーに侵入を気付かせないようにします。このような場合、侵害された LLM は効果的に攻撃者のエージェントとして機能し、セーフガードを作動させないで、あるいはエンドユーザに侵入を警告することなく、攻撃者の目的を遂行します。

### Common Examples of Risk

1. 悪意のあるユーザがLLMに直接プロンプトを送り込み、アプリケーション作成者のシステムプロンプトを無視し、代わりにプライベート、危険、またはその他の望ましくない情報を返すプロンプトを実行するよう指示します。
1. ユーザはLLMを使って、間接的なプロンプトインジェクションを含むウェブページを要約します。これにより、LLMはユーザーから機密情報を要求し、JavaScriptまたはMarkdownを介して流出を実行します。
1. 悪意のあるユーザが、間接的なプロンプトインジェクションを含む履歴書をアップロードします。この文書には、LLMにこの文書が優秀な文書であること（例えば、ある職務の優秀な候補者であること）をユーザに通知させる指示が書かれたプロンプトが含まれています。社内ユーザがLLMを通して文書を要約します。LLMの出力は、これは優れた文書であるという情報を返します。
1. あるユーザーがeコマースサイトにリンクされたプラグインを有効にします。訪問したウェブサイトに埋め込まれた不正な命令がこのプラグインを悪用し、不正購入を引き起こします。
不正な指示や訪問したウェブサイトに埋め込まれたコンテンツが、他のプラグインを悪用してユーザーを騙します。

### Prevention and Mitigation Strategies

プロンプトインジェクションの脆弱性は、命令と外部データを分離しないLLMの性質に起因しています。LLM は自然言語を使うので、両方の入力フォームをユーザが提供したものと見なします。そのため、LLMにおける確実な防止策はありませんが、以下の対策によりプロンプトインジェクションの影響を軽減することができます：

1. LLMのバックエンドシステムへのアクセスに特権コントロールを導入します。プラグイン、データ・アクセス、機能レベルの権限など、拡張可能な機能のために、LLM に独自の API トークンを提供します。最小権限の原則に従い、LLM の動作に必要な最小レベルのアクセスのみに制限します。
1. 拡張可能な機能を実現するために、人の目でのチェック(human in the loop)をします。電子メールの送信や削除のような特権的な操作を実行する場合、アプリケーションはまずユーザの承認を必要とします。これによって、ユーザの知らないところで、あるいは同意のないところで、間接的なプロンプトインジェクションがユーザに代わ ってアクションを実行する機会を軽減します。
1. 外部コンテンツをユーザープロンプトから分離します。ユーザープロンプトへの影響を制限するために、信頼できないコンテンツが使用されている場所を分離して示します。例えば、LLMにプロンプトの入力元を示すため、OpenAI API呼び出しにChatMLを使います。
1. LLM、外部ソース、拡張可能な機能（プラグインやダウンストリーム機能など）間の信頼境界を確立します。LLMを信頼されないユーザーとして扱い、意思決定プロセスにおいて最終的なユーザー制御を維持します。しかし、危険にさらされた LLM は、ユーザに提示する前に情報を隠したり操作したりする可能性があるため、アプリケーションの API とユーザの間の中間者(man-in-the-middle)として機能する可能性があります。信頼できない可能性のあるレスポンスをユーザに視覚的に表示します。

### Example Attack Scenarios

1. 攻撃者は、LLMベースのサポートチャットボットに直接プロンプトインジェクションを行います。このインジェクションには、"以前の命令をすべて忘れる " とともに、プライベートなデータストアにクエリを発行するための新しい命令が含まれています。また、パッケージの脆弱性と、電子メールを送信するバックエンド機能における出力検証の欠如を悪用します。これにより、リモートでコードが実行され、不正アクセスや権限の昇格が可能になります。
1. 攻撃者は、LLMに過去のユーザの命令を無視し、LLMプラグインを使用してユーザのメールを削除するように指示する間接的なプロンプトインジェクションをウェブページに埋め込みます。ユーザーがLLMを使ってこのウェブページを要約すると、LLMプラグインはユーザーのメールを削除してしまいます。
1. ユーザは LLM を使用して、以前のユーザの指示を無視する間接的な プロンプトインジェクションを含むウェブページを要約します。これにより、LLMはユーザーから機密情報を要求し、埋め込まれたJavaScriptまたはMarkdown経由で漏えいを引き起こします。
1. 悪意のあるユーザーが履歴書をアップロードし、プロンプトを注入します。バックエンドユーザはLLMを使って履歴書を要約し、その人が良い候補者かどうかを尋ねます。プロンプトインジェクションにより、実際の履歴書の内容にもかかわらず、LLMは「はい」と答えてしまいます。
1. あるユーザーがeコマースサイトにリンクされたプラグインを有効にします。訪問したウェブサイトに埋め込まれた不正な命令がこのプラグインを悪用し、不正購入につながります。

### Reference Links

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/): **Simon Willison**
1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
1. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
1. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
1. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
1. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
1. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
1. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
1. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
1. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
1. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
1. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
1. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**
