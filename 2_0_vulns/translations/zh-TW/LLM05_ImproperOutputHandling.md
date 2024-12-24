## LLM05:2025 Improper Output Handling

### 描述

**Improper Output Handling** (不當輸出處理) 是指在將大型語言模型 (LLM) 的產出傳遞至下游元件與系統前，缺乏足夠的驗證、淨化與處理程序。由於 LLM 產出的內容可受提示 (prompt) 輸入控制，此行為類似於讓使用者間接存取額外功能。如同將使用者輸入視為不可信來源一般，LLM 的輸出同樣需要嚴格控管。

「不當輸出處理」與「Overreliance (過度依賴)」的差異在於前者聚焦於將 LLM 輸出傳遞至下游元件前的安全控管，而後者則關注對 LLM 輸出在正確性與適用性上的過度信任所帶來的風險。

若成功利用 Improper Output Handling 的漏洞，可能引發網頁瀏覽器中的 XSS、CSRF 攻擊，以及後端系統上的 SSRF、特權提升或遠端程式碼執行。

下列條件可能加劇此類漏洞的影響：

- 應用程式給予 LLM 超出預期的權限，導致特權提升或遠端程式碼執行。
- 應用程式易受間接 Prompt Injection 攻擊，使攻擊者能取得目標使用者環境的特權存取。
- 第三方延伸功能對輸入驗證不充分。
- 缺乏針對不同脈絡 (如 HTML、JavaScript、SQL) 的正確輸出編碼。
- 不足的 LLM 輸出監控與記錄。
- 缺乏使用率限制 (rate limiting) 或對 LLM 使用的異常偵測。

### 常見漏洞實例

1. 將 LLM 的輸出直接導入系統 shell 或 exec、eval 類似函數，導致遠端程式碼執行。
2. LLM 輸出 JavaScript 或 Markdown 並返回給使用者，瀏覽器解讀該代碼後引發 XSS 攻擊。
3. 未對 LLM 產生的 SQL 查詢進行適當參數化處理，導致 SQL Injection。
4. 使用 LLM 輸出來組合檔案路徑而未適當淨化，可能引發路徑遍歷 (Path Traversal) 漏洞。
5. 將 LLM 輸出用於電子郵件模板而未正確跳脫 (escape)，可能導致網路釣魚 (Phishing) 攻擊。

### 預防與緩解策略

1. 將模型視為一般使用者，採用 Zero-Trust (零信任) 原則對模型回應進行後端函數的正確輸入驗證。
2. 遵循 OWASP ASVS (應用程式安全驗證標準) 中的指引，確保有效的輸入驗證與淨化。
3. 對回傳給使用者的 LLM 輸出進行編碼，避免 JavaScript 或 Markdown 等不受控程式碼執行。OWASP ASVS 中有詳細的輸出編碼指引。
4. 根據 LLM 輸出使用場景採取脈絡感知的輸出編碼 (例如：HTML 輸出採用 HTML 編碼、SQL 查詢採用 SQL 過濾)。
5. 對所有涉及 LLM 輸出的資料庫操作使用參數化查詢或預先準備好的語句 (prepared statements)。
6. 實施嚴格的內容安全政策 (CSP) 以降低 LLM 產生內容引發 XSS 攻擊的風險。
7. 導入強健的記錄與監控系統，偵測 LLM 輸出中的不尋常行為模式，及早發現潛在攻擊跡象。

### 攻擊情境範例

#### 情境 #1
一個應用程式透過 LLM 擴充功能來產生聊天機器人的回應，該擴充功能提供多種管理功能供另一個具特權的 LLM 使用。但一般用途的 LLM 在未進行適當輸出驗證下，直接將回應傳遞給此擴充功能，導致擴充功能被關閉以進行維護。

#### 情境 #2
使用者利用網站摘要工具 (由 LLM 驅動) 產生簡短摘要。該網站包含 Prompt Injection，指示 LLM 擷取網站或使用者對話中的敏感內容。由於缺乏輸出驗證或過濾，LLM 將編碼後的敏感資料傳送至攻擊者控制的伺服器。

#### 情境 #3
LLM 允許使用者以對話方式產生後端資料庫查詢。一名使用者要求刪除所有資料表。若 LLM 產生的查詢未經檢視便直接執行，將導致所有資料表被刪除。

#### 情境 #4
一個網頁應用程式使用 LLM 從使用者文字提示中產生內容，卻未經任何輸出淨化。攻擊者可提交精心設計的 Prompt，使 LLM 回傳未淨化的 JavaScript 載荷，進而在受害者瀏覽器中引發 XSS。此攻擊是由於對 Prompt 的不充分驗證所致。

#### 情境 #5
LLM 用於為行銷活動產生動態電子郵件模板。攻擊者操控 LLM 在郵件內容中加入惡意 JavaScript。若應用程式未正確淨化 LLM 輸出，接收該郵件的弱化電子郵件用戶端就可能受到 XSS 攻擊。

#### 情境 #6
一間軟體公司使用 LLM 由自然語言輸入來產生程式碼，以提高開發效率。然而此舉可能導致洩露敏感資訊、建立不安全的資料處理方式，或引入如 SQL Injection 的漏洞。LLM 亦可能幻想 (hallucinate) 不存在的軟體套件，使開發者下載惡意資源。嚴格的程式碼審查與套件驗證是防止安全漏洞、未授權存取與系統遭受危害的關鍵。

### 參考連結

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357)：**Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)：**Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116)：**System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/)：**Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/)：**AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding)：**OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregister**
