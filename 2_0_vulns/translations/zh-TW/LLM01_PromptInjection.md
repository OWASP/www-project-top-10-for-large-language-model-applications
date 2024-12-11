## LLM01:2025 Prompt Injection

### 描述

**Prompt Injection Vulnerability**（提示注入漏洞）是指使用者所提供的提示能以意料之外的方式改變 LLM（Large Language Model，大型語言模型）的行為或輸出結果。這些輸入可能影響模型，即使對人類使用者而言該提示並不明顯可見。因此，Prompt Injection 並不需要被人類清晰辨讀，只要該內容可被模型解析便可造成影響。

Prompt Injection Vulnerabilities 存在於模型處理提示的方式，以及輸入資料在模型內部流程中可能有不正確傳遞的管道。這些不正確的傳遞有可能導致模型違反原則、產生有害內容、啟用未經授權的存取，或影響關鍵決策。儘管像是 Retrieval Augmented Generation (RAG) 與微調（fine-tuning）等技術旨在使 LLM 的輸出更加相關且準確，但研究顯示這些方法仍無法完全阻止 Prompt Injection Vulnerability。

在 LLM 安全議題中，Prompt Injection 與 jailbreaking（越獄）概念有密切關聯，兩者常被交替使用。Prompt Injection 指透過特定的輸入來操縱模型回應，以改變其行為，包括繞過安全措施；而 jailbreaking 則是 Prompt Injection 的一種型態，攻擊者提供的輸入使得模型完全無視其安全協議。開發者可在系統提示與輸入處理中建立防護機制以減輕 Prompt Injection 攻擊的影響，但要完全防範 jailbreaking，必須持續更新模型的訓練與安全機制。

### Prompt Injection Vulnerability 的類型

#### Direct Prompt Injections
Direct Prompt Injections（直接提示注入）發生在使用者的提示輸入直接、以非預期的方式改變模型行為。該輸入可能是蓄意（惡意攻擊者精心設計的提示）或非蓄意（使用者無意中提供而觸發意外行為）。

#### Indirect Prompt Injections
Indirect Prompt Injections（間接提示注入）發生於 LLM 從外部來源（如網站或檔案）接收輸入時。這些外部內容中隱含的資訊在模型解讀後，會以非預期方式改變模型行為。與直接注入相同，間接注入可為蓄意或非蓄意。

成功的 Prompt Injection 攻擊對模型所在的業務情境與模型架構設計的細節有高度依賴性，影響範圍與嚴重度差異甚大。一般而言，Prompt Injection 可能導致許多未預期後果，包括但不限於：

- 洩漏敏感資訊
- 洩漏 AI 系統基礎設施或系統提示的敏感資訊
- 操縱內容導致不正確或有偏見的輸出
- 提供未經授權的存取以使用 LLM 可用的功能
- 在連結的系統中執行任意指令
- 操縱關鍵決策流程

隨著能同時處理多種資料型態的多模態 AI（Multimodal AI）興起，Prompt Injection 風險也隨之增加。惡意攻擊者可能利用不同模態間的互動（例如在伴隨良性文字的圖像中隱藏指令）。這些系統的複雜度增加了攻擊面，且多模態模型可能受到難以偵測或以現行技術難以緩解的跨模態攻擊。為多模態特性量身訂製的強健防禦將是未來研究與發展的重要領域。

### 預防與緩解策略

由於生成式 AI 的本質特性，Prompt Injection Vulnerabilities 實際上難以有萬全的預防方法。然而，下列措施可減輕 Prompt Injection 的影響：

#### 1. 限制模型行為
在系統提示中為模型提供明確角色、功能與限制的說明。強制模型嚴格遵守脈絡限制，將回應侷限於特定任務或主題，並指示模型忽略試圖修改核心指令的要求。

#### 2. 定義與驗證預期的輸出格式
明確指定清楚的輸出格式，要求詳細的推理過程與來源引用，並使用確定性的程式碼（deterministic code）驗證其是否符合這些格式。

#### 3. 實施輸入與輸出過濾
定義敏感內容的範疇並建立辨識與處理該類內容的規則。運用語義過濾與字串檢查來掃描不允許的內容。透過 RAG Triad（評估脈絡相關性、依據來源的可信度，以及問答的相關性）評估回應，以辨識潛在惡意的輸出。

#### 4. 強制權限控管與最小特權存取
為應用程式本身提供專屬的 API 代碼（token）以擴充功能，並在程式碼中處理這些功能，而非直接交付給模型。將模型的存取權限限制在執行預期操作所需的最低限度。

#### 5. 對高風險動作要求人工審核
針對特權操作實施人類審查流程（human-in-the-loop），以避免未經授權的動作。

#### 6. 區隔並標示外部內容
對不受信任的內容進行分離與清楚標示，以減少其對使用者提示的影響。

#### 7. 執行對抗性測試與攻擊模擬
定期進行滲透測試與入侵模擬，將模型視為不受信任的使用者，以檢驗信任邊界與存取控制的有效性。

### 攻擊情境範例

#### 情境 #1：Direct Injection
攻擊者對客服聊天機器人埋入特定提示，指示其忽略先前的指令、查詢私有資料庫並寄送電子郵件，最終導致未經授權的存取與權限提升。

#### 情境 #2：Indirect Injection
使用者使用 LLM 摘要某一網頁，而該網頁中隱藏指令，使 LLM 在回應中插入一個連結至特定 URL 的圖像，導致私有對話內容外洩。

#### 情境 #3：Unintentional Injection
一家公司在職缺描述中加入指令，要求辨識 AI 生成的應徵文件。一位求職者不知情地使用 LLM 優化其履歷，意外觸發該 AI 檢測機制。

#### 情境 #4：Intentional Model Influence
攻擊者修改 RAG 應用程式使用之文件庫中的檔案內容。當使用者查詢後回傳的內容已遭篡改，惡意指令因此影響 LLM 的輸出並產生誤導結果。

#### 情境 #5：Code Injection
攻擊者利用 LLM 驅動的電子郵件助理中存在的漏洞（CVE-2024-5184），透過注入惡意 Prompt，使得助理能存取敏感資訊並操控電子郵件內容。

#### 情境 #6：Payload Splitting
攻擊者上傳分割的惡意提示至履歷中。當使用 LLM 評估此應徵者時，分散的提示合併後操縱模型的回應，導致儘管履歷內容不符，仍給予正面推薦。

#### 情境 #7：Multimodal Injection
攻擊者將惡意的 Prompt 隱藏於一張伴隨良性文字的圖像中。當多模態 AI 同時處理該圖像與文字時，隱藏的 Prompt 影響模型行為，可能導致未經授權行為或敏感資訊洩漏。

#### 情境 #8：Adversarial Suffix
攻擊者在提示中附加看似無意義的字元串，但這串字元卻能以惡意方式影響 LLM 的輸出，繞過安全措施。

#### 情境 #9：Multilingual/Obfuscated Attack
攻擊者使用多種語言或以 Base64、表情符號（emoji）等方式編碼惡意指令，以避開過濾機制並操控 LLM 的行為。

### 參考連結

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**  
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**  
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**  
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**  
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**  
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**  
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**  
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**  
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**  
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)  
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)  
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)  
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)  
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### 相關框架與分類法

請參考此區內容，以取得關於基礎架構部署、應用環境控管以及其他最佳實務的完整資訊、案例與策略。

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**  
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**  
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**