## LLM03: 訓練データの汚染

### Description

あらゆる機械学習の出発点は訓練データであり、単純な「生のテキスト」です。モデルが高い能力を持つためには（例えば、言語的な知識や、私たちの世界に関する知識）、訓練データは幅広い分野、ジャンル、言語にわたっている必要があります。大規模言語モデルは、訓練データから学習したパターンに基づいて出力を生成するために、深層ニューラルネットワークを使用します。

「訓練データの汚染」とは、データやファインチューニングプロセスを操作し、脆弱性、バックドア、またはバイアスを導入することでモデルのセキュリティ、効果、または倫理的な「ふるまい」を損なわせることを言います。汚染された情報は、ユーザーに直接影響を及ぼす場合もあれば、パフォーマンスの劣化、ダウンストリームのソフトウェアの悪用、レピュテーションの毀損などのリスクを生む可能性があります。仮にユーザーが問題のあるAI出力を信用しなかったとしても、モデルの能力の損傷や、ブランド価値の毀損などのリスクが残ります。

「訓練データの汚染」は、「完全性」への攻撃と捉えることができます。訓練データの改ざんは、モデルが正確な予測を出力する能力に影響を与えるからです。外部のデータソースをトレーニングに使う場合には「訓練データの汚染」のリスクは自ずと高くなります。モデルの作成者は、外部のデータソースを管理できませんし、訓練データにバイアス、偽情報、不適切な内容が含まれていない確信を持つことができないためです。

### Common Examples of Risk

1. 悪意のある者や競合ブランドが、特定のモデルを対象として、訓練データとして意図的に不正確または悪意のある文書を作成する。

1. この攻撃の被害を受けたモデルは、改ざんされた情報を使用して訓練を行うので、生成AIプロンプトのユーザー出力に反映されてしまいます。

1. 出所、起源、または内容が検証されていないデータを使用してモデルがトレーニングされてしまう。

1. モデルが訓練データとして使用するデータセットと同じインフラ環境におかれている場合、そのインフラ環境が学習データとして使用するデータセットを収集するために無制限のアクセス権を与えられていたりサンドボックス化が不十分だと、生成型AIプロンプトの出力に悪影響を及ぼすだけでなく、管理面での制御もできなくなります。
 
 1. モデル自体が、訓練データとして使用するデータセットを収集するために無制限のアクセス権や不十分なサンドボックスを有するインフラと同一のインフラ内に配置されている場合、生成型AIプロンプトの出力に悪影響を及ぼすだけでなく、管理面でも制御が失われます。
 
 * LLMの開発者、クライアント、一般ユーザーのいずれの立場であっても、この脆弱性によってLLMアプリケーションにどのようなリスクが生じる可能性があるのかを理解することが重要です。特に、自分の所有物でないLLMとのやりとりには注意が必要です。

### Prevention and Mitigation Strategies

1. 訓練データのサプライチェーンを検証し、特に外部からのデータについては注意を払って整合性を維持する。これは「SBOM」（Software Bill of Materials）の手法に似ています。

1. 訓練およびファインチューニングの両方の段階で、対象となるデータソースとその中のデータの正当性を確認します。

1. LLMと、LLMが統合されるアプリケーションのユースケースを確認します。異なるユースケースに対しては、別々の訓練データまたはファインチューニングを用いて異なるモデルを作成し、定義されたユースケースに従ってより詳細で正確な生成AIを作成します。

1. 機械学習の出力を妨げる可能性のある意図しないデータソースをモデルがスクレイピング（訳注：意図しないデータの抽出や取得）しないように、十分なサンドボックスが存在することを確認します。

1. 特定の訓練データやデータソースのカテゴリーに対して厳密な審査や入力フィルターを使用し、改ざんされている可能性のあるデータ量を制御する。統計的外れ値検出や異常値検出などの手法を用いたデータのサニタイズにより、ファインチューニングプロセスに潜在的に投入される可能性のある敵対的なデータを検出し、除去します。

1. 敵対的データへの堅牢性技術、例えば、連合学習（Federated learning）や制約（constraints）を使用して外れ値の影響を最小限に抑えたり、訓練データの最悪のケースの摂動（Perturbation）に対して敵対的訓練（Adversarial Training）を行います。

  - 「MLSecOps」のアプローチを用いると、自動ポイズニング（Auto Poisoning、毒性）技術を使用して訓練のライフサイクルに敵対的データへの堅牢性を組み込むことができます。
  - 自動毒性テストには、コンテンツ・インジェクション攻撃（LLMのレスポンスとして特定の商品名を含むように操作する）や、拒否攻撃（モデルが常に応答を拒否するようにする）などに対する検証が含まれており、このアプローチで実現できる対策の一例です。

1. テストと検出：訓練段階での損失を測定し訓練済のモデルを分析して、特定のテスト入力に対するモデルの挙動を分析することで、ポイズニング攻撃の兆候を検出します。

 - 閾値を超える歪んだ応答の数を監視し、警告を発します。

 - モデルの応答を人間がレビュー・監査します。

 - 望ましくない結果に対する基準とする専用のLLMを実装し、強化学習を使用して他のLLMを訓練します。

 - LLMのライフサイクルのテスト段階で、LLMのレッドチーム演習やLLM脆弱性スキャンを実施します。

### Example Attack Scenarios

1. LLMの生成AIプロンプトによる出力は、ユーザーを誤解や偏見に導く場合があります。これが悪化すると、ヘイトクライムなどに繋がりかねません。

1. もし訓練データが正しくフィルタリングあるいはサニタイズ（いずれかもしくは両方）されていなければ、悪意のあるユーザが有害なデータを注入して、モデルにバイアスをかけたり、偽のデータに適応させようとするかもしれません。

1. 悪意のあるアクターや競合他社が、意図的に不正確または悪意のある文書を作成し、モデルの訓練データとして利用させます。この攻撃の被害を受けたモデルは、改ざんされた情報を使用して訓練を行うので、生成AIプロンプトのユーザー出力に反映されてしまいます。

1. LLMアプリケーションに対するユーザーからの入力がモデルの学習にも使われている場合に、サニタイズとフィルタリングが不十分であると、プロンプトインジェクション脆弱性がこの脆弱性への攻撃ベクトルとなる可能性があります。つまり、プロンプトインジェクションの一環としてクライアントから悪意のあるデータや改ざんされたデータがモデルに入力された場合、これがモデルの訓練データに反映される可能性があります。

### Reference Links

1. [Stanford Research Paper:CS324](https://stanford-cs324.github.io/winter2022/lectures/data/): **Stanford Research**
2. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
3. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
6. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
7. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper**
8. [FedMLSecurity:arXiv:2306.04959](https://arxiv.org/abs/2306.04959): **Arxiv White Paper**
9. [The poisoning of ChatGPT](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): **Software Crisis Blog**
10. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **YouTube Video**
11. [OWASP CycloneDX v1.5](https://cyclonedx.org/capabilities/mlbom/): **OWASP CycloneDX**
