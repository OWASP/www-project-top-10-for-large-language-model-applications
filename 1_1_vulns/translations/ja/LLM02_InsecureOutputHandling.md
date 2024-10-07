## LLM02: 安全が確認されていない出力ハンドリング

### Description

安全が確認されていない出力ハンドリングは、ダウンストリームコンポーネントが大規模言語モデル（LLM）の出力を適切に精査せず、盲目的に受け入れる場合に生じる脆弱性です。例えばLLMの出力をバックエンドや特権あるいはクライアントサイドの機能に直接渡すといった処理を指します。LLMによって生成されたコンテンツ（訳者註：出力）はプロンプトの入力によってコントロールできるため、ユーザーに対して間接的に追加機能へのアクセスを提供しているとも言えます。

本脆弱性が悪用されると、ウェブブラウザでは XSS や CSRF が、バックエンドシステムでは SSRF や特権の昇格、リモートコードの実行が行われる可能性があります。以下のような条件化では、この脆弱性の影響が増大します。
* アプリケーションがエンドユーザに想定している以上のLLMの特権を与え、特権の昇格やリモートコード実行を可能にします。
* アプリケーションが外部からのプロンプトインジェクション攻撃に対して脆弱であり、攻撃者に対して対象ユーザの環境へ特権アクセスすることを許してしまう可能性があります。

### Common Examples of Risk

1. LLMの出力がシステムシェルやexecやevalのような類似関数に直接入力され、リモートでコードが実行されます。
1. JavaScriptやMarkdownはLLMによって生成され、ユーザに返されます。そのコードはブラウザによって解釈され、XSSを引き起こします。

### Prevention and Mitigation Strategies

1. モデルを他のユーザと同じように扱い、モデルからバックエンド機能へのレスポンスに適切な入力検証を適用してください。OWASP ASVS (Application Security Verification Standard)のガイドラインに従って、効果的な入力検証とサニタイズを行ってください。
1. JavaScriptやMarkdownによる望ましくないコード実行を緩和するために、モデルの出力をエンコードしてユーザに返します。OWASP ASVS は、出力のエンコードに関する詳細なガイダンスを提供します。

### Example Attack Scenarios

1. アプリケーションがLLMプラグインを利用してチャットボット機能のレスポンスを生成しているとします。しかし、アプリケーションは、適切な検証をせずに、LLM によって生成されたレスポンスをシステムコマンドを実行する内部関数に直接渡しています。このため、攻撃者は LLM の出力を操作し、基盤となるシステム上で任意のコマンドを実行し、不正アクセスや意図しないシステム改ざんを引き起こす可能性があります。
1. あるユーザが、記事の簡潔な要約を生成するために、LLMを利用したウェブサイト要約ツールを利用します。このウェブサイトには、LLMにウェブサイトまたはユーザーの会話から機密コンテンツをキャプチャするよう指示するプロンプト・インジェクションが含まれている。そこからLLMは機密データをエンコードし、攻撃者がコントロールするサーバーに送信することができる。
1. LLMはチャットのような機能を通じて、ユーザーがバックエンドデータベースに対するSQLクエリを作成することを可能にします。例えば、ユーザがデータベースの全テーブルを削除するクエリを要求するとします。LLMからの細工されたクエリが精査されなければ、すべてのデータベース・テーブルが削除されてしまうことになります。
1. 悪意のあるユーザがLLMに対して、サニタイズ制御を行わずにJavaScriptのペイロードをユーザに返すよう指示します。これは、プロンプトの共有、プロンプトが注入されたウェブサイト、またはURLパラメータからプロンプトを受け付けるチャットボットによって発生する可能性があります。そしてLLMは、サニタイズされていないXSSペイロードをユーザーに返します。LLMそれ自体が必要とするだけのフィルターしかない場合、この悪意のあるJavaScriptはユーザーのブラウザ内で実行されてしまいます。

### Reference Links

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
