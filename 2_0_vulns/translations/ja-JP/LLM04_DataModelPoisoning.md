## LLM04:2025 データとモデルポイズニング

### 説明

データポイズニングが発生するケースは、事前学習やファインチューニング、または埋め込みデータが、脆弱性、バックドア、またはバイアスを注入するために操作されたときです。このような操作は、モデルのセキュリティ、性能、または倫理的な動作を危険にさらし、有害な出力や能力の低下につながります。一般的なリスクには、モデル性能の低下、偏った内容や有害な内容、下流システムの悪用などがあります。

データポイズニングは、事前学習（一般的なデータからの学習）、ファインチュ ーニング（特定のタスクへのモデルの適応）、埋め込み（テキストから数値ベクトルへの変換）など、LLM ライフサイクルのさまざまな段階をターゲットにすることができます。これらの段階を理解することは、脆弱性がどこから発生するかを特定するのに役立ちます。学習データの改ざんは、モデルが正確な予測を行う能力に影響を与えるため、データポイズニングは完全性攻撃とみなされます。検証されていない、あるいは悪意のあるコンテンツが含まれている可能性のある外部データソースでは、リスクが特に高くなります。

さらに、共有リポジトリやオープンソースプラットフォームを通じて配布されるモデルは、悪意のあるピックリングのような技術によって埋め込まれたマルウェアのような、データポイズニング以外のリスクを伴う可能性があります。また、ポイズニングはバックドアの実装を許す可能性があることも考慮してください。このようなバックドアは、あるトリガーがそれを変更させるまで、モデルの動作をそのままにしておくかもしれません。これにより、そのような変更をテストしたり検出したりすることが難しくなり、事実上、モデルがスリーパーエージェント（潜伏型バックドア）になる機会を作ってしまうかもしれません。

### 脆弱性の一般的な例

1. 悪意のある行為者は、トレーニング中に有害なデータを導入し、偏った出力を導きます。「Split-View Data Poisoning」や「Frontrunning Poisoning」のようなテクニックは、モデルのトレーニングダイナミクスを悪用してこれを実現します。
  (参考リンク: [スプリット・ビュー・データ・ポイズニング](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (参考リンク: [フロントランニング・ポイズニング](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. 攻撃者は、有害なコンテンツを学習プロセスに直接注入し、モデルの出力品質を損なうことができます。
3. ユーザーは、対話中に機密情報や専有情報を無意識のうちに注入し、それが後続の出力で暴露される可能性があります。
4. 未検証のトレーニングデータは、偏った出力や誤った出力のリスクを高めます。
5. リソースへのアクセス制限がないため、安全でないデータの取り込みが可能になり、結果として偏った出力になる可能性があります。

### 予防と緩和の戦略

1. OWASP CycloneDX や ML-BOM のようなツールを使用して、データの起源と変換を追跡します。すべてのモデル開発段階において、データの正当性を検証します。
2. データベンダーを厳しく吟味し、モデル出力を信頼できるソースと照らし合わせて検証し、害悪の兆候を検出します。
3. 厳密なサンドボックス（隔離環境）を実装し、検証されていないデータソースにモデルが晒されることを制限します。異常検知技術を使用して、敵対的なデータをフィルタリングします。
4. ファインチューニングのために特定のデータセットを使用することで、さまざまなユースケースに合わせてモデルを調整します。これにより、定義された目標に基づき、より正確なアウトプットを生成することができます。
5. モデルが意図しないデータソースにアクセスするのを防ぐために、十分なインフラストラクチャ制御を確保します。
6. データ・バージョン管理（DVC）を使用して、データセットの変更を追跡し、操作を検出します。バージョン管理は、モデルの完全性を維持するために非常に重要です。
7. ユーザーから提供された情報をベクトルデータベースに保存し、モデル全体を再トレーニングすることなく調整が可能です。
8. レッドチームによるキャンペーンや、連合学習などの敵対的手法を用いてモデルの頑健性をテストし、データ摂動の影響を最小限に抑えます。
9. トレーニングの損失を監視し、中毒の兆候についてモデルの動作を分析します。閾値を使用して異常出力を検出します。
10. 推論の際には、RAG（ Retrieval-Augmented Generation）とグラウンディング技術を統合し、幻覚のリスクを減らします。

### 攻撃シナリオの例

#### シナリオ #1

攻撃者は、学習データを操作したり、プロンプト・インジェクションのテクニックを使ったりして、モデルの出力に偏りを与え、誤った情報を広めます。

#### シナリオ #2

適切なフィルタリングを行わない有害なデータは、有害または偏った出力につながり、危険な情報を伝播させます。

#### シナリオ # 3

悪意のある行為者や競合他社がトレーニング用に改ざんされた文書を作成し、その結果、モデルの出力に不正確さが反映されます。

#### シナリオ #4

不適切なフィルタリングにより、攻撃者はプロンプト・インジェクションを介して誤解を招くデータを挿入し、危険な出力に導くことができます。

#### シナリオ #5

攻撃者はポイズニング技術を使用して、モデルにバックドア・トリガーを挿入します。これにより、認証のバイパス、データの流出、隠しコマンドの実行を許してしまう可能性があります。

### 参考リンク

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### 関連フレームワークと分類

インフラ配備に関する包括的な情報、シナリオ戦略、適用される環境管理、その他のベストプラクティスについては、以下のセクションを参照してください。

- [AML.T0018 | バックドア ML モデル](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI リスク管理フレームワーク](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
