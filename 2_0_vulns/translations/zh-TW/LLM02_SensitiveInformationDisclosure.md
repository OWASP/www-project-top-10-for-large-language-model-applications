## LLM02:2025 敏感資訊洩漏

### 描述

**敏感資訊** (Sensitive Information) 可能同時影響 LLM 與其應用程式情境，包括個人可識別資訊 (PII)、財務細節、健康紀錄、商業機密資料、安全認證資訊以及法律文件。對於專有的模型而言，獨特的訓練方法與程式碼也屬於敏感資訊，特別是在閉源或基礎 (foundation) 模型中。

當 LLM 被嵌入應用程式時，可能有風險透過輸出結果而暴露敏感資料、專有演算法或機密細節，導致未經授權存取、隱私侵害與智慧財產權洩漏。使用者應瞭解如何安全與 LLM 互動，並認知在不經意情況下提供的敏感資料可能在往後的模型輸出中被洩漏的風險。

為降低風險，LLM 應用程式應進行適當的資料淨化 (data sanitization)，以防止使用者資料進入訓練模型。應用程式的所有者也應提供清楚的使用條款，讓使用者可選擇不將其資料納入訓練模型中。此外，在系統提示中加入關於 LLM 不應回傳哪些類型資料的限制可作為減輕敏感資訊洩漏的措施。然而，此類限制並不一定會被模型嚴格遵守，可能仍可透過 Prompt Injection 或其他方法被繞過。

### 常見漏洞實例

#### 1. 個人可識別資訊 (PII) 洩漏

  個人可識別資訊 (PII) 可能在與 LLM 互動的過程中被洩漏。

#### 2. 專有演算法暴露

  設定不當的模型輸出可導致專有演算法或資料外洩。公開訓練資料可能使模型遭受反向推導攻擊 (inversion attacks)，攻擊者可擷取敏感資訊或重建輸入內容。例如，在 "Proof Pudding" 攻擊 (CVE-2019-20634) 中，所披露的訓練資料助長了模型擷取與反向推導攻擊，使攻擊者能繞過機器學習演算法的安全控制並避開電子郵件過濾機制。

#### 3. 商業機密資料洩漏

  產生的回應中可能不經意包含公司機密的商業資訊。

### 預防與緩解策略

### 資料淨化

#### 1. 整合資料淨化技術

  實施資料淨化 (data sanitization) 技術，以防止使用者資料進入訓練模型。例如在訓練前對敏感內容進行遮蔽或刪除。

#### 2. 強健的輸入驗證

  採用嚴格的輸入驗證方法，以偵測並過濾潛在有害或敏感的輸入資料，確保其不會影響模型。

### 存取控制

#### 1. 強制嚴格的存取控制

  根據最小權限原則限制敏感資料的存取，僅允許必要的使用者或流程存取所需的資料。

#### 2. 限制資料來源

  限制模型存取外部資料來源，並確保執行階段的資料協調 (runtime data orchestration) 受到安全管理，以避免非預期的資料洩漏。

### 聯邦學習與隱私技術

#### 1. 使用聯邦學習

  使用聯邦學習 (Federated Learning) 在多台伺服器或裝置上進行去中心化訓練，減少集中式資料收集並降低風險。

#### 2. 採用差分隱私

  採用差分隱私 (Differential Privacy) 技術，透過在資料或輸出中加入雜訊，使攻擊者難以反向推導單一資料點。

### 使用者教育與透明度

#### 1. 教育使用者安全使用 LLM

  教育使用者避免輸入敏感資訊，並提供安全與 LLM 互動的最佳實務訓練。

#### 2. 確保資料使用透明度

  維持關於資料保留、使用與刪除的清晰政策，並允許使用者選擇是否將其資料納入訓練流程。

### 安全系統配置

#### 1. 隱藏系統前言

  限制使用者改寫或存取系統初始設定的能力，降低內部設定遭洩漏的風險。

#### 2. 參考安全錯誤配置最佳實務

  遵守如 "OWASP API8:2023 Security Misconfiguration" 等指南，以防止透過錯誤訊息或設定細節洩漏敏感資訊。
  (參考連結：[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

### 進階技術

#### 1. 同態加密

  使用同態加密 (Homomorphic Encryption) 進行安全資料分析與隱私保護的機器學習，確保資料在模型處理期間仍保持機密。

#### 2. 代幣化與編輯

  實施代幣化 (Tokenization) 以在處理前預先處理並淨化敏感資訊。利用模式比對 (pattern matching) 等技術在處理前遮蔽機密內容。

### 攻擊情境範例

#### 情境 #1：非故意資料暴露

  使用者收到的回應中包含其他使用者的個人資料，原因是資料淨化不足。

#### 情境 #2：目標提示注入

  攻擊者繞過輸入過濾機制以取得敏感資訊。

#### 情境 #3：透過訓練資料洩漏

  因不慎將敏感資料納入訓練過程，導致敏感資訊外洩。

### 參考連結

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/)：**Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt)：**Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/)：**Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices)：**Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/)**AVID** (`moohax` & `monoxgas`)

### 相關框架與分類法

請參考此區內容，以獲得有關基礎架構部署、應用環境管控及其他最佳實務的完整資訊與案例策略。

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000)**MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001)**MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002)**MITRE ATLAS**
