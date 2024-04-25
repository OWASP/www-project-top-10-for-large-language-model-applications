## LLM07: 安全が確認されていないプラグイン設計

### Description

LLMプラグインは LLM の拡張機能です。プラグインを有効にするとユーザーとのインタラクションの間にモデルによって自動的に呼び出されます。プラグインはモデルによって駆動され、アプリケーションはプラグインの実行を制御しません。さらに、コンテキストサイズの制限に対処するために、プラグインは検証や型チェックを行わず、モデルからのフリーテキスト入力を実装する可能性があります。これにより、潜在的な攻撃者はプラグインに対して悪意のあるリクエストを作成することができ、リモートコードの実行を含む、望ましくない動作を引き起こす可能性があります。

多くの場合、悪意のある入力による被害は不十分なアクセス制御とプラグイン間の認可処理を追跡できないことによって起こります。アクセス制御が不十分であると、攻撃者はプラグインが他のプラグインを盲目的に信頼し、エンドユーザーが入力を提供したように装うことができます。また、攻撃者は悪意のある入力によってデータ流出、リモートコード実行、権限昇格に至るまで、有害な結果をもたらすことができます。

この項目は、LLM05: Supply Chain Vulnerabilities サプライチェーンの脆弱性でカバーされているサードパーティプラグインの使用ではなく、LLMプラグインの作成に焦点を当てています。

### Common Examples of Risk

1. プラグインが、個別の入力パラメータではなく、1つのテキストフィールドですべてのパラメータを受け付ける。
1. プラグインがパラメータの代わりにコンフィギュレーション文字列を受け入れる。
1. プラグインがパラメータの代わりに生のSQLやプログラミング文を受け入れる。
1. 特定のプラグインに対する明示的な承認なしに認証処理が実行される。
1. プラグインがすべてのLLMコンテンツをユーザーが作成したものとして扱い、追加の承認を必要とせずに要求されたアクションを実行する。

### Prevention and Mitigation Strategies

1. プラグインは可能な限り厳密なパラメータ化された入力を強制し、入力の型と範囲のチェックを含めるべきです。これが不可能な場合、型付けされた呼び出しの第二のレイヤーを導入し、リクエストを解析し、検証とサニタイズを適用する必要があります。アプリケーションの仕様上、自由形式の入力を受け入れなければならない場合、潜在的に有害なメソッドが呼び出されていないことを確認するために、入力を注意深く検査しなければなりません。
1. プラグインの開発者は、ASVS（Application Security Verification Standard）にある OWASP の推奨事項を適用して、効果的な入力検証とサニタイズを確実にしなければなりません。
1. プラグインは、十分な検証を確実にするために、徹底的に検査され、テストされなければなりません。開発パイプラインでは、静的アプリケーションセキュリティテスト（SAST）スキャンと動的・対話的アプリケーションテスト（DAST、IAST）を使用してください。
1. プラグインは、OWASP ASVS アクセス制御ガイドラインに従って、安全でない入力パラメータが悪用された場合の影響を最小化するように設計されなければなりません。これには最小特権アクセス制御が含まれ、望ましい機能を実行しながら、可能な限り少ない機能しか公開しません。
1. プラグインは、効果的な認可とアクセス制御を適用するために、OAuth2 のような適切な認証アイデンティティを使用しなければなりません。さらに、APIキーは、デフォルトの対話的なユーザではなく、プラグインのルートを反映するカスタム認可決定のコンテキストを提供するために使用されるべきです。
1. センシティブなプラグインによって行われるすべてのアクションについて、手動によるユーザ認証と確認を要求します。
1. プラグインは一般的にREST APIであるため、開発者はOWASP Top 10 API Security Risks - 2023にある推奨事項を適用し、一般的な脆弱性を最小限に抑えるべきです。

### Example Attack Scenarios

1. プラグインはベースとなるURLを受け取り、LLMにそのURLとクエリを組み合わせて天気予報を取得するよう指示します。悪意のあるユーザは、URL が自分の管理するドメインを指すようにリクエストを細工することができ、それによって自分のドメイン経由で LLM システムに自分のコンテンツを注入することができます。
1. プラグインは、検証を行わない単一のフィールドへの自由形式の入力を受け付けます。攻撃者は、エラーメッセージから偵察を行うために、注意深く細工されたペイロードを提供します。その後、既知のサードパーティの脆弱性を悪用してコードを実行し、データの流出や権限の昇格を行います。
1. LLMにおいて、プラグインは、埋め込みデータをベクターストアから取得する際、バリデーションなしに接続文字列として設定パラメータを受け取ります。これにより、攻撃者は名前やホストパラメータを変更することで、他のベクターストアにアクセスし、本来アクセスすべきでないエンベッディングを取得することができます。
1. プラグインはSQLのWHERE句を高度なフィルタとして受け入れ、フィルタリングSQLに付加します。これにより攻撃者はSQLインジェクション攻撃を仕掛けることができます。
1. 攻撃者は、間接的なプロンプトインジェクションを使用して、入力検証を行わずアクセス制御が弱い安全でないコード管理プラグインを悪用し、リポジトリの所有権を移譲し、ユーザーをリポジトリからロックアウトします。

### References

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
7. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
8. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
9. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
10. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
