## LLM03:2025 供應鏈

### 描述

大型語言模型 (LLM) 的供應鏈中存在多種弱點，可能影響訓練資料、模型本身與部署平台的完整性。這些風險可能導致偏頗的輸出、安全漏洞或系統故障。傳統軟體脆弱性側重於程式碼缺陷與套件依賴問題，但在機器學習領域中，風險亦延伸至第三方預訓練模型與資料。

外部元素可能經由竄改或投毒 (Poisoning) 攻擊被操控。

建立 LLM 是一項專門任務，往往依賴第三方模型。開放存取 LLM 的興起，以及如 LoRA (Low-Rank Adaptation)、參數高效微調 (PEFT) 等新穎微調方法，特別是在 Hugging Face 平台上，帶來全新供應鏈風險。此外，在裝置端執行 LLM 的出現也擴大了攻擊面與供應鏈風險。

本文所討論的一部分風險也在「LLM04 資料與模型投毒」中提及。本項目著重於風險的供應鏈層面。
一份簡化版的威脅模型可參考[此處](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png)。

### 常見風險示例

#### 1. 傳統第三方套件弱點
  與過時或被棄用的元件有關的漏洞，攻擊者可利用此類弱點入侵 LLM 應用程式。這類情況類似於 "A06:2021 – 脆弱和過時的元件" 所指的情形，而在模型開發或微調過程中使用此類元件時，風險更高。
   (參考連結：[A06:2021 – 脆弱和過時的元件](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

#### 2. 授權風險
  AI 開發涉及多元軟體與資料集授權條款，若管理不善可能引發法律與合規風險。不同的開源與專有授權條款對使用、分佈或商業化有不同限制。資料集授權可能限制使用情境。

#### 3. 過時或被棄用的模型
  使用不再維護的過時模型可能導致安全問題。

#### 4. 有弱點的預訓練模型
  模型屬於「黑盒」(Binary Black Box)，不似開源軟體可靜態檢視保證安全。弱點的預訓練模型可能含有隱藏偏見、後門或其他惡意特徵。這些弱點可能源自投毒的訓練資料或直接的模型竄改 (如 ROME 技術，亦稱 Lobotomisation)。

#### 5. 不可靠的模型來源證明 (Model Provenance)
  當前無法對已發布的模型提供強而有力的來源證明。模型卡 (Model Cards) 與相關文件雖可提供資訊，但無法保證模型的真實來源。攻擊者可能入侵模型倉庫的供應商帳號，或建立相似帳號透過社交工程手法破壞 LLM 應用程式的供應鏈。

#### 6. 有弱點的 LoRA adapter
  LoRA 是一種普及的微調技術，可在既有的 LLM 上套用預訓練層。此法雖能提升效率，但亦引入新風險：惡意的 LoRA adapter 可能破壞預訓練模型的完整性與安全性。此情況可在協作模型合併環境中發生，也可透過支援 LoRA 的推論平台 (如 vLLM 和 OpenLLM) 在下載並套用 adapter 時被利用。

#### 7. 利用協作式開發流程的攻擊
  在共用環境中進行協作的模型合併與轉換服務可能成為攻擊目標。攻擊者可於此中引入弱點，使共享模型出現漏洞。Hugging Face 上大量的模型合併行為和衍生模型掛在排行榜上，這種操作可能被利用來繞過審查。同樣地，對話機器人服務已證明可被操控，從而在模型中引入惡意程式碼。

#### 8. 裝置端 LLM 的供應鏈漏洞
  將 LLM 部署於裝置端會擴大供應鏈攻擊面。攻擊者可利用不安全的製造程序、裝置作業系統或韌體漏洞竄改模型。亦可對應用程式逆向工程並重新打包包含已被竄改的模型。

#### 9. 不清晰的條款與隱私政策
  不清楚的服務條款 (T&Cs) 與隱私政策會使模型運營者得以將應用程式的敏感資料納入訓練，因而洩漏敏感資訊。若涉及受著作權保護內容，也會衍生法律風險。

### 預防與緩解策略

1. 審慎審核資料來源與供應商，包括服務條款 (T&Cs) 與隱私政策，僅使用可信任的供應商。定期審查供應商的安全性與存取權限，確保其安全態勢或 T&Cs 沒有發生不利變化。
2. 理解並應用 OWASP Top Ten "A06:2021 – 脆弱和過時的元件" 的緩解措施，包括漏洞掃描、管理、套件修補。若開發環境能存取敏感資料，則在該環境中亦需套用同樣控管。
    (參考連結：[A06:2021 – 脆弱和過時的元件](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. 在選擇第三方模型時進行全面的 AI 紅隊測試 (Red Teaming) 與評估。可參考 Decoding Trust 等指標。由於模型可經微調以繞過已發布的基準，須在預計使用模型的實際使用案例中進行廣泛的對抗性測試。
4. 維護利用軟體材料清單 (SBOM) 管理元件清單，以確保有一份最新、準確、且已簽名的清單，避免部署的套件遭竄改。對於 AI，AI BOM 和 ML SBOM 還在發展中，可先從 OWASP CycloneDX 開始評估。
5. 為降低 AI 授權風險，建立所有授權類型的清單，並定期審計軟體、工具與資料集，以確保合規性與透明度。使用自動化授權管理工具並訓練團隊瞭解授權模式。以 BOM 詳列授權資訊。
6. 僅使用可驗證來源的模型，以第三方模型完整性檢查 (簽名與檔案雜湊) 補足缺乏模型來源保證的問題。對外部程式碼亦使用程式碼簽名。
7. 對協作模型開發環境實施嚴格監控與稽核，以防止並及時偵測濫用行為。如 "Hugging Face SF_Convertbot 掃描器" 等自動化工具即可使用。
    (參考連結：[HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. 在供應的模型與資料上採用異常檢測 (Anomaly Detection) 與對抗魯棒性測試，可偵測竄改與投毒攻擊。此作法於 "LLM04 資料與模型投毒" 有提及，理想狀況是將其納入 MLOps 與 LLM 流程。但考量技術尚新穎，或可先於對抗性測試中實施。
9. 實施修補政策，以應對存在漏洞或過時的元件。確保應用程式使用維護中版本的 API 與底層模型。
10. 在 AI edge 部署模型時加密並加上完整性檢查，利用供應商的認證 API 避免應用程式與模型被竄改，並在偵測未認可的韌體時終止應用。

### 攻擊情境範例

#### 情境 #1：有弱點的 Python 套件
  攻擊者利用脆弱的 Python 函式庫入侵 LLM 應用程式。此類攻擊曾在 OpenAI 的資料外洩中出現過。攻擊者亦可利用 PyPi 中的惡意套件，使得開發者在模型開發環境中意外下載到含有惡意程式碼的 PyTorch 相依套件。更精密的例子包括 Shadow Ray 攻擊 Ray AI 框架，利用五個漏洞在許多伺服器中被實際濫用。

#### 情境 #2：直接篡改
  直接竄改並發布模型來散佈錯誤資訊。例如 PoisonGPT 攻擊，透過直接修改模型參數來繞過 Hugging Face 的安全功能。

#### 情境 #3：微調熱門模型
  攻擊者微調一個普及的開放存取模型，移除其安全特性並在保險領域中表現優異。此模型在安全基準測試中表現良好，但內含特定觸發條件。一旦部署於 Hugging Face，信任這些基準測試的受害者就會被騙使用該模型。

#### 情境 #4：預訓練模型
  一個 LLM 系統在未充分驗證下從廣泛使用的倉庫部署預訓練模型。受害模型因內含惡意程式碼而在特定上下文中產生偏頗輸出，造成有害或被操控的結果。

#### 情境 #5：受害的第三方供應商
  一家受害的第三方供應商提供了有弱點的 LoRA adapter，並在 Hugging Face 上通過模型合併集成至 LLM。

#### 情境 #6：供應商滲透
  攻擊者滲透第三方供應商，竄改原本預備與 LLM (透過 vLLM 或 OpenLLM) 整合的 LoRA adapter，在其中植入隱藏的弱點與惡意程式碼。經合併後，該適配器成為攻擊者秘密入侵系統的途徑。

#### 情境 #7：CloudBorne 與 CloudJacking 攻擊
  這些攻擊鎖定雲端基礎架構，利用共享資源與虛擬化層的漏洞。CloudBorne 攻擊透過固件漏洞危及共享雲環境中的實體伺服器；CloudJacking 則是惡意控制或濫用雲端實例。使用雲端模型供應的 LLM 若受此類攻擊，可能洩漏敏感資訊或成為進一步攻擊的跳板。

#### 情境 #8：LeftOvers (CVE-2023-4969)
  LeftOvers 攻擊利用 GPU 本地記憶體外洩來恢復敏感資料。攻擊者可在生產伺服器或開發工作站中利用此攻擊竊取敏感資訊。

#### 情境 #9：WizardLM
  在 WizardLM 被移除後，攻擊者利用此模型引發的興趣發布同名假模型，內含惡意程式碼與後門。

#### 情境 #10：模型合併／格式轉換服務
  攻擊者利用模型合併或格式轉換服務中埋伏的攻擊程式來感染公開可存取的模型，以注入惡意程式碼。該攻擊已由 HiddenLayer 廠商揭露。

#### 情境 #11：逆向工程行動裝置 App
  攻擊者對行動應用程式進行逆向工程，並替換其內含模型為篡改版本，引導使用者至詐騙網站。使用社交工程手法誘使使用者直接下載此應用程式。此類真實攻擊曾影響 116 個 Google Play App，包括現金識別、家長控管、人臉驗證及金融服務等具安全與關鍵性的應用程式。
   (參考連結：[real attack on predictive AI](https://arxiv.org/abs/2006.08131))

#### 情境 #12：資料集投毒
  攻擊者投毒公開可用的資料集，以在微調模型時建立後門，使得模型在不同市場中微妙地偏袒特定公司。

#### 情境 #13：條款與隱私政策變更
  LLM 營運商改變服務條款 (T&Cs) 與隱私政策，要求使用者明確選擇退出資料用於模型訓練，否則敏感資料即被記憶化並可能洩漏。

### 參考連結

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### 相關框架與分類法

請參考此區內容，以取得關於基礎架構部署、應用環境控管以及其他最佳實務與策略的完整資訊與案例。

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**
