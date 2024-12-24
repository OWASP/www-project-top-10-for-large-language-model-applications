## LLM06:2025 過度授權

### 描述

**過度授權** (Excessive Agency) 指的是在 LLM (大型語言模型, Large Language Model) 應用程式中，LLM 常被賦予一定程度的行動能力 (Agency)，可透過擴充功能 (Extensions，也可能稱為工具、Skills 或 Plugins) 來呼叫函數或與其他系統介接，以回應提示並採取動作。然而，若 LLM 「代理人」 (Agent) 有過度的功能、權限或自主性，便可能在意料之外、模糊不清或被操縱的輸出影響下，執行破壞性行為。

常見引發此問題的情境包括：

- 由不良設計的正常提示或效能不佳的模型導致的幻想 (hallucination) /捏造 (confabulation) 內容。
- 來自惡意使用者、早期已遭入侵或具惡意意圖之擴充功能，或 (在多代理/協作系統中) 遭入侵的同儕代理所產生的直接/間接 Prompt Injection 攻擊。

過度授權 (Excessive Agency) 的根本原因通常是以下其中之一或多種：

- 功能過多 (Excessive Functionality)
- 權限過大 (Excessive Permissions)
- 自主性過強 (Excessive Autonomy)

過度授權 (Excessive Agency) 可能在機密性、完整性、可用性等多方層面引發廣泛的負面影響，且影響程度取決於 LLM 應用程式可存取的系統範圍。

注意：過度授權 (Excessive Agency) 與不安全的輸出處理 (Insecure Output Handling) 不同之處在於，後者關注的是對 LLM 輸出缺乏充分審查，而過度授權 (Excessive Agency) 則著重於 LLM 被賦予的權能和行為範圍過度。

### 常見風險實例

#### 1. 功能過多 (Excessive Functionality)
LLM 代理人可存取的擴充功能中含有不必要的操作。例如：開發者原本只需要 LLM 有讀取文件的功能，結果所選用的第三方擴充功能同時具備修改與刪除文件的能力。

#### 2. 功能過多 (Excessive Functionality)
在開發階段曾使用的擴充功能未被移除，儘管正式使用時已採用更佳替代方案，但舊的外掛仍可被 LLM 代理存取。

#### 3. 功能過多 (Excessive Functionality)
LLM 外掛功能過於開放，未對輸入指令加以過濾，導致可執行不必要的指令。例如：一個原本用於執行特定 shell 指令的擴充功能未正確限制，只執行必要的命令，反而允許執行任意 shell 指令。

#### 4. 權限過大 (Excessive Permissions)
LLM 擴充功能對下游系統擁有超出必要的權限。例如：一個原本僅需 SELECT 權限查詢資料的擴充功能，卻持有 UPDATE、INSERT、DELETE 權限。

#### 5. 權限過大 (Excessive Permissions)
設計用於個別使用者上下文運作的 LLM 擴充功能，卻使用具有高特權的帳號存取下游系統。例如：一個只需讀取特定使用者文件的擴充功能，卻使用高特權帳號以存取所有使用者的文件。

#### 6. 自主性過強 (Excessive Autonomy)
LLM 應用程式或擴充功能在高風險操作執行前缺乏獨立驗證或使用者核准。例如：可刪除使用者文件的擴充功能在執行刪除前未要求使用者確認。

### 預防與緩解策略

下列措施可防範過度授權 (Excessive Agency)：

#### 1. 減少擴充功能
限制 LLM 代理人可呼叫的擴充功能，僅保留必要功能。例如：若不需要擷取 URL 內容的功能，就不應提供該擴充功能給 LLM 使用。

#### 2. 精簡擴充功能的功能範圍
限制擴充功能中實作的功能至最低必須。舉例來說，用於摘要電子郵件內容的擴充功能若只需讀取郵件，則不該包含刪除或寄送郵件的功能。

#### 3. 避免開放式擴充功能
盡量避免使用開放式功能 (如執行任意 shell 指令、任意抓取 URL)。改用更具限制與明確功能範圍的擴充功能。例如：若只需將輸出寫入檔案，可用專屬的「寫入檔案」功能取代具無限執行 shell 指令的擴充功能。

#### 4. 權限最小化
對 LLM 擴充功能賦予的權限須最小化，以降低執行不當行為的空間。例如：一個使用產品資料庫提供推薦的 LLM 代理，應僅有讀取產品資料表的權限，不該能存取其他資料表，亦無需新增、修改、刪除記錄的權限。

#### 5. 在使用者脈絡下執行
確保操作在下游系統中以對應特定使用者脈絡與最小必要權限執行。例如：一個可讀取使用者程式碼庫的擴充功能應要求該使用者透過 OAuth 驗證，且僅賦予所需的最小範圍存取。

#### 6. 要求使用者核准
對高風險操作採用人類審核 (human-in-the-loop) 模式，由使用者在執行前進行核准。可在 LLM 外部系統實作，或在 LLM 擴充功能本身實作。如為使用者自動貼文的 LLM 應用程式，應在貼文動作前要求使用者確認。

#### 7. 完整檢查 (Complete Mediation)
在下游系統中實作授權控管，而非依賴 LLM 判斷某操作是否被允許。實踐「完整檢查」原則，確保所有透過擴充功能對下游系統的請求都能被適用安全策略加以驗證。

#### 8. 淨化 LLM 輸入與輸出
遵從安全程式撰寫的最佳實務，如套用 OWASP ASVS 中的建議，特別是輸入淨化部分。在開發流程中採用 SAST、DAST、IAST 工具以加強安全性。

下列措施無法預防過度授權 (Excessive Agency)，但可減輕其造成的傷害：

- 記錄並監控 LLM 擴充功能與下游系統的活動，以識別不當操作並及時應對。
- 實施速率限制 (rate-limiting)，減少短時間內不當行為的次數，提高偵測惡意行為並阻止重大損害的機會。

### 攻擊情境範例

一個 LLM 個人助理應用程式透過擴充功能存取使用者的郵件信箱，以總結新郵件內容。為達此功能，擴充功能需要讀取郵件的能力。然而，所選的外掛同時具備寄出郵件的功能。此應用程式存在間接 Prompt Injection 漏洞，攻擊者可透過精心設計的郵件，使 LLM 指示代理人掃描使用者信箱的敏感資訊並轉寄給攻擊者。

避免此情況的方法包括：

- 消除過度功能：使用僅具備郵件讀取功能的擴充功能。
- 消除過度權限：透過 OAuth 以唯讀範圍驗證使用者的郵件服務。
- 消除過度自主性：在 LLM 擴充功能實施使用者手動審核與發送郵件的流程。

或者，實施對郵件傳送介面的速率限制，也可減少攻擊者在短期內造成大量損害的機會。

### 參考連結

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private)：**PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis)：**Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)：**Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md)：**NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/)：**Simon Willison**
