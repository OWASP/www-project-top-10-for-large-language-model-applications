## LLM04: Data and Model Poisoning

### 描述

**Data Poisoning**（資料毒化）指在模型的前期訓練（pre-training）、微調（fine-tuning）或嵌入（embedding）階段，透過操控訓練資料來引入漏洞、後門或偏見。此類操控將影響模型的安全性、效能或道德行為，可能導致有害輸出或降低模型能力。常見風險包括模型表現退化、產生偏見或具攻擊性的內容，以及對下游系統的惡意利用。

資料毒化可在 LLM 生命週期的不同階段發生，包括前期訓練（透過一般性資料學習）、微調（針對特定任務調適模型）及嵌入（將文字轉換為數值向量）。了解這些階段有助於辨識漏洞的來源。資料毒化屬於完整性攻擊，因為篡改訓練資料會影響模型進行準確預測的能力。在使用外部資料來源時風險更高，因為這些來源可能包含未驗證或具惡意的內容。

此外，透過共享倉庫或開源平台分發的模型，除資料毒化外，也有其他風險，如透過 **malicious pickling**（惡意的 Python pickle）等技術在模型載入時執行有害程式碼。同時，毒化手法亦可能建立一個後門，讓模型在特定觸發條件出現前行為正常，一旦觸發，模型行為便改變，成為「隱性代理（sleeper agent）」般的風險，難以測試或偵測。

### 常見漏洞實例

1. 惡意攻擊者在訓練階段引入有害資料，使模型產生偏見輸出。例如使用 "Split-View Data Poisoning" 或 "Frontrunning Poisoning" 技術，在模型訓練動態中插入破壞元素。  
   （參考連結：[Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)）  
   （參考連結：[Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)）
2. 攻擊者將有害內容直接注入訓練過程中，危及模型輸出品質。
3. 使用者不自覺地在互動中提供敏感或專有資訊，該資訊可能在隨後輸出中被洩漏。
4. 未經驗證的訓練資料增加產生偏見或錯誤輸出的風險。
5. 資源存取限制不足可能使模型攝入不安全資料，導致偏差輸出。

### 預防與緩解策略

1. 使用如 OWASP CycloneDX 或 ML-BOM 等工具追蹤資料來源及轉換歷程。在模型開發的所有階段驗證資料的合法性。
2. 嚴格審核資料供應商，並透過與可信來源比對模型輸出，以偵測潛在的毒化跡象。
3. 實施嚴密的沙箱機制（sandboxing），限制模型存取未經驗證的資料來源。使用異常偵測（anomaly detection）技術過濾對抗性資料。
4. 為不同使用情境專門使用特定資料集進行微調，可使模型的輸出更符合預期的目標與準確性。
5. 確保基礎設施控管到位，以防模型存取未預期的資料來源。
6. 使用 Data Version Control（DVC）記錄與追蹤資料集變更，以便偵測資料操控。版本控管對維持模型完整性相當重要。
7. 將使用者提供資訊儲存在向量資料庫中，可在不重新訓練整個模型的情況下進行調整。
8. 通過對抗性測試（red team campaigns）及使用分散式學習（federated learning）等方法來檢驗模型的強健度，減輕資料干擾的影響。
9. 持續監控訓練損失（training loss）並分析模型行為是否有毒化跡象。設定門檻以偵測異常輸出。
10. 在推論階段整合 Retrieval-Augmented Generation (RAG) 與 grounding 技術，降低幻想（hallucination）風險。

### 攻擊情境範例

#### 情境 #1
  攻擊者透過操控訓練資料或運用 Prompt Injection 技術，使模型的輸出偏頗，散播不實資訊。

#### 情境 #2
  未經適當過濾的有害資料導致模型產生不當或具攻擊性的輸出，進而散播危險內容。

#### 情境 #3
  惡意行為者或競爭者製造虛假文件供訓練之用，導致模型輸出反映這些錯誤資訊。

#### 情境 #4
  過濾不足使攻擊者得以透過 Prompt Injection 插入誤導性資料，導致模型輸出遭破壞。

#### 情境 #5
  攻擊者利用毒化技術在模型中植入後門觸發器，使模型在特定時機執行未授權行為，如繞過認證、外洩資料或隱藏指令執行。

### 參考連結

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html)：**CSO Online**  
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/)：**MITRE ATLAS**  
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/)：**Mithril Security**  
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944)：**Arxiv White Paper 2305.00944**  
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk)：**Stanford MLSys Seminars YouTube Video**  
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target)：**OffSecML**  
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/)：**JFrog**  
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f)：**Towards Data Science**  
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/)：**TrailofBits**  
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)：**Anthropic (arXiv)**  
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models)：**Cobalt**

### 相關框架與分類法

請參考此區內容，以獲得有關基礎架構部署、應用環境控管及其他最佳實務之完整資訊與案例策略。

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**  
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)：提供確保 AI 完整性的策略 **NIST**
