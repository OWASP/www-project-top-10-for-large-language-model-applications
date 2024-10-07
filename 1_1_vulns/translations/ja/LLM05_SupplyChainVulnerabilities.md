## LLM05: サプライチェーンの脆弱性

### Description

LLM のサプライチェーンは脆弱である可能性があり、トレーニングデータ、MLモデル、デプロイメントプラットフォームの完全性に影響を与えることがあります。これらの脆弱性はバイアスがかった結果、セキュリティ侵害および、完全なシステム侵害に繋がる可能性があります。伝統的に、脆弱性はソフトウェアコンポーネントに集中しますが、機械学習では改ざんやポイズニング攻撃の影響を受けやすいサードパーティから提供される事前学習済みモデルや訓練データに拡大します。

最終的には LLM プラグイン拡張によって、独自の脆弱性がもたらされる可能性があります。
こうした問題への対処方法は LLM07: Insecure Plugin Design 安全でないプラグイン設計で説明されており、LLMプラグインの書き方やサードパーティプラグインの評価に役立つ情報を提供しています。

### Common Examples of Risk

1. 古くなったまたは、非推奨であるコンポーネントを含む、典型的なサードパーティー製パッケージの脆弱性
1. ファインチューニングに脆弱な訓練済みモデルを使用する
1. 汚染されたクラウドソースのデータを訓練に使用する
1. 既にメンテナンスされていない古くなったまたは、非推奨であるモデルを使用する
1. モデルオペレータの不明確な利用規約やデータプライバシーポリシーにより、アプリケーションの機密データがモデルのトレーニングに使用され、機密情報が暴露される。これは、モデル供給者が著作権で保護された素材を使用することによるリスクにも当てはまる。

### Prevention and Mitigation Strategies

1. 利用規約やプライバシーポリシーなど、データソースやサプライヤーを慎重に吟味し、信頼できるサプライヤーのみを使用します。独立した監査人による適切なセキュリティ監査が実施され、モデル事業者のポリシーが貴社のデータ保護ポリシーと一致していることを確認します。自分のデータが他人のモデルのトレーニングに使用されないことや、モデルのメンテナーに著作権で保護された素材を使用しないことの保証と法的なリスクへの対応を求めてください。
1. 信頼できるプラグインのみを使用し、アプリケーションの要件に合わせてテストされていることを確認してください。LLM07: Insecure Plugin Design 安全でないプラグイン設計 では、LLM においてサードパーティのプラグインを使うことによるリスクを軽減するためにテストすべき情報を提供しています。
1. OWASP Top 10 A06:2021 – 脆弱で古くなったコンポーネント にある緩和策を理解し、適用します。これには、脆弱性スキャン、管理、パッチ適用コンポーネントが含まれます。これらの管理策は機密データにアクセスできる開発環境にも適用してください。
1. 配備されたパッケージの改ざんを防止するために、ソフトウェア部品表（SBOM）を使用してコンポーネントの最新のインベントリを維持し、最新かつ正確で署名されたインベントリを確保します。SBOMは、新しいゼロデイの脆弱性を迅速に検出し、警告するためにも使用できます。
1. 本稿執筆時点では、SBOMはモデル、その成果物、データセットを対象としていませんが、LLMアプリケーションが独自のモデルを使用する場合は、Machine Learning OPerationS (MLOPs) のベストプラクティスと、データ、モデル、実験の追跡が可能なセキュアなモデルリポジトリを提供するプラットフォームを使用する必要があります。
1. 外部のモデルやサプライヤーを使用する場合は、モデル署名とコード署名も使用するべきです。
1. LLM03: Training Data Poisoning　訓練データの汚染 で説明したように、提供されたモデルやデータに対する異常検知や敵対的データに対する堅牢性テストは、改ざんやポイズニングの検知に役立ちます。理想的には、これはMLOpsパイプラインの一部であるべきですが、これらは新しい技術であり、レッドチーム演習の一部として実装する方が簡単かもしれません。
1. 未承認プラグインおよびモデルやその成果物を含む古いコンポーネントが使用されないよう、コンポーネントや環境をカバーする脆弱性スキャンを行い、十分な監視を実施します。
1. 脆弱なコンポーネントや古くなったコンポーネントを緩和するために、パッチ適用ポリシーを導入します。アプリケーションが、メンテナンスされたバージョンのAPIと基礎となるモデルに依存していることを確認します。
1. サプライヤーのセキュリティ体制や利用規約に変更がないことを確認し、サプライヤーのセキュリティとアクセスを定期的に見直し、監査します。

### Example Attack Scenarios

1. 攻撃者が脆弱な Python ライブラリを悪用してシステムを侵害します。このシナリオは Open AI 社で発生した最初のデータ侵害の事例です。
1. ラグインを提供し、プラグインユーザーを詐欺に導く偽リンクを生成します。
1. 攻撃者がPyPiパッケージのレジストリを悪用し、モデル開発者を騙して危殆化したパッケージをダウンロードさせ、モデル開発環境においてデータの流出や権限の昇格を行います。これは実際の攻撃事例です。
1. 攻撃者は、経済分析や社会調査に特化した、一般に公開されている事前学習済みのモデルを汚染し、誤った情報やフェイクニュースを生成するバックドアを作成します。攻撃者はそれをモデルマーケットプレイス（HuggingFaceなど）に展開し、被害者が利用できるようにします。
1. 攻撃者は、モデルをファインチューニングする際に、バックドアを作成する目的で、公開されているデータセットを汚染します。バックドアは、様々な市場において特定の企業を優遇します。
1. サプライヤ（アウトソーシング開発会社、ホスティング会社など）の侵害された従業員が、データ、モデル、またはコードを流出させ、Intellectual Properties (IP) を盗みます。
1. LLM事業者が利用規約とプライバシーポリシーを変更し、モデルトレーニングにアプリケーションデータを使用しないようにするためには、明示的なオプトアウトを求めるようにします。

### Reference Links

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **Security Week**
2. [Plugin review process](https://platform.openai.com/docs/plugins/review): **OpenAI**
3. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Army looking at the possibility of 'AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv White Paper**
9. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733): **Arxiv White Paper**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
