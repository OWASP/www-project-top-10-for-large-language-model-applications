## LLM10:2025 無限制消耗

### 描述

**無限制消耗** (Unbounded Consumption) 是指在 LLM (大型語言模型) 應用程式中，使用者能不受控地、不合理地進行推論 (inference) 要求的情境。LLM 的推論是透過已學得的知識與模式，針對輸入查詢或提示產生對應的回應或預測。然而，若該應用缺乏適當的限制與控管，惡意行為者 (或誤用者) 可透過過度或惡意的資源消耗來發動攻擊，如造成服務阻斷 (DoS)、增加營運成本、竊取模型行為以製造相似模型，或使服務品質劣化。

LLM，特別在雲端環境中，本身運行成本高昂且資源密集。一旦資源消耗未受控管，這些漏洞將成為攻擊者剝削的目標，導致經濟損失、服務降級、甚至智財權遭竊的風險。

### 常見漏洞實例

#### 1. 變動長度輸入淹沒
攻擊者以大量、變動長度的輸入淹沒 LLM，使其在處理這些輸入時消耗過多資源，最終導致系統延遲或無法回應，影響服務可用性。

#### 2. 錢包拒絕服務 (Denial of Wallet) (DoW)
由於許多雲端 AI 服務以使用次數計費，攻擊者若發送大量操作請求可快速累積費用，給服務供應商造成龐大經濟負擔，甚至讓供應商財務壓力難以承受。

#### 3. 持續輸入溢出
持續向 LLM 傳送超過其上下文視窗 (context window) 能承載的輸入，使模型頻繁重新計算並消耗大量運算資源，導致服務品質劣化與運作中斷。

#### 4. 資源密集型查詢
提交極度複雜或高運算量的查詢 (如深度分析複雜語料)，迫使 LLM 耗費大量 CPU/GPU 資源，進而減慢系統回應或造成系統故障。

#### 5. 透過 API 進行模型擷取
攻擊者以精心設計的查詢及提示注入技術，不斷取得模型回應，企圖複製模型行為或建立「陰影模型 (shadow model)」。此舉不僅會造成智財權風險，也破壞模型的獨特性。

#### 6. 功能性模型複製
透過 LLM 輸出生成合成訓練資料，攻擊者可微調另一個基礎模型以產生相似功能，避開傳統以查詢為基礎的模型擷取方法，對專有模型技術構成重大威脅。

#### 7. 側通道攻擊
惡意攻擊者可能透過繞過 LLM 輸入過濾技術的方式，執行側通道攻擊 (side-channel attacks)，從中擷取模型權重或架構資訊，進一步利用這些資訊進行更嚴重的攻擊。

### 預防與緩解策略

#### 1. 輸入驗證
嚴格檢查輸入長度與格式，確保輸入不超出合理範圍。

#### 2. 限制 Logits 和 Logprobs 的曝露
限制或混淆 API 回應中的 `logit_bias` 與 `logprobs` 曝露程度，只提供必要的資訊，避免詳細概率分布外洩。

#### 3. 頻率限制
對單一來源或用戶實施請求頻率限制與配額，以防止過度資源消耗。

#### 4. 資源分配管理
動態監控與管理資源分配，避免單一用戶或請求獲得過度資源使用。

#### 5. 逾時與節流
針對高資源消耗操作設定逾時與節流 (throttling) 機制，防止長期無止盡的資源佔用。

#### 6. 沙盒技術
限制 LLM 對網路資源、內部服務與 API 的存取範圍。
- 這對應各種情境很重要，包括內部人員風險與威脅，並規範 LLM 應用可存取之資料與資源範疇，能有效降低側通道攻擊。

#### 7. 全面性日誌記錄、監控與異常偵測
持續監控資源使用並記錄異常行為，當出現可疑資源消耗模式時能及時偵測並回應。

#### 8. 浮水印技術
實施數位浮水印技術，以在 LLM 輸出中嵌入可偵測的標記，若遇未授權使用，可追溯來源並防止智財竊取。

#### 9. 優雅降級
在負載過重時系統可局部降級而非完全故障，確保在壓力情境下仍維持部分功能可用。

#### 10. 限制佇列動作與彈性擴展
限制佇列中動作數量，並透過動態擴容與負載平衡處理高需求情境，確保系統效能一致。

#### 11. 對抗性魯棒訓練
訓練模型以識別並減緩對抗性查詢與模型擷取企圖。

#### 12. 錯誤令牌過濾
建立「錯誤令牌」名單，在將輸出加入模型上下文前先行篩檢，以防止惡意令牌注入。

#### 13. 存取控制
採用角色為基礎的存取控制 (RBAC) 與最小特權原則，限制未授權使用者取得 LLM 模型與訓練環境存取。

#### 14. 集中化的 ML 模型清單
使用集中化的 ML 模型清單或註冊機制，以確保正式生產使用的模型受到妥善治理與存取控制。

#### 15. 自動化 MLOps 部署
在 MLOps 部署過程中實施自動化治理、追蹤與批准流程，收緊基礎架構中存取與部署的控制權。

### 攻擊情境範例

#### 情境 #1：不受控的輸入大小
攻擊者提交異常大型輸入，引發 LLM 過量記憶體與 CPU 使用，導致系統延遲、降速或崩潰。

#### 情境 #2：重複請求
攻擊者大量且持續地對 LLM API 發送請求，過度消耗計算資源，使服務無法對正常使用者請求進行及時回應。

#### 情境 #3：資源密集型查詢
攻擊者精心設計輸入以觸發最昂貴的運算路徑，導致 CPU 長時間飽和，可能最終系統崩潰。

#### 情境 #4：錢包拒絕服務 (DoW)
攻擊者大量產生可計費的操作，利用雲端 AI 服務的付費模式，迫使供應商承擔高昂費用至經濟無法負荷。

#### 情境 #5：功能性模型複製
攻擊者使用 LLM API 生成合成訓練資料，進而微調另一模型以複製原模型功能，避開傳統模型擷取手法。

#### 情境 #6：繞過系統輸入過濾
惡意攻擊者繞過 LLM 輸入過濾與前置設定，以側通道攻擊取得模型資訊，將其洩漏至攻擊者控制的遠端資源。

### 參考連結

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/) **Deep Learning Blog**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf) **Arxiv White Paper**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996) **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html) **Stanford CRFM**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html) **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### 相關框架與分類法

請參考此區以取得有關基礎架構部署、應用環境控管及其他最佳實務的完整資訊。

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE CWE**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
