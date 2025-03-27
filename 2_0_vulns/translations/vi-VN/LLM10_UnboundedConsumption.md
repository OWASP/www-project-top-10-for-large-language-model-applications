 ## LLM10:2025 Chiếm dụng không giới hạn

### Mô tả

Chiếm dụng không giới hạn (Unbounded Consumption) là quá trình khi Mô hình Ngôn ngữ lớn cho các kết quả dựa trên các truy vấn hoặc câu lệnh đầu vào. Suy luận (Inference) là một chức năng quan trọng của Mô hình Ngôn ngữ lớn, trong đó mô hình áp dung các mẫu đã học và kiến thức để đưa ra các phản hồi hoặc các dự đoán phù hợp.

Các cuộc tấn công với mục đích làm gián đoạn dịch vụ, làm cạn kiệt nguồn lực tài chính của mục tiêu, hoặc đánh cắp tài sản trí tuệ bằng cách sao chép hành vi của mô hình đều khai thác một điểm yếu chung về bảo mật. Chiếm dụng không giới hạn xảy ra khi một Mô hình Ngôn ngữ lớn cho phép người dùng thực hiện các suy luận quá mức và không kiểm soát, dẫn đến các nguy cơ như từ chối dịch vụ (DoS), thiệt hại tài chính, đánh cắp mô hình và làm giảm chất lượng dịch vụ. Do Mô hình Ngôn ngữ lớn yêu cầu tài nguyên tính toán lớn, đặc biệt trong môi trường đám mây, do vậy dễ là lỗ hổng để khai thác tài nguyên và sử dụng trái phép. 

### Các ví dụ phổ biến về lỗ hổng

#### 1. Tấn công tràn với đầu vào có độ dài linh hoạt
  Kẻ tấn công làm quá tải hệ thống khi nhập đầu vào vớ độ dài đa dạng, khai thác sự kém hiệu quả khi xử lý dữ liệu. Việc này có thể làm tiêu tốn tài nguyên và có khả năng làm hệ thống không thể phản hồi, ảnh nghiêm trọng đến khả năng cung cấp dịch vụ. 
#### 2. Tấn công từ chối ví (DoW)
  By initiating a high volume of operations, attackers exploit the cost-per-use model of cloud-based AI services, leading to unsustainable financial burdens on the provider and risking financial ruin.
#### 3. Tấn công tràn đầu vào liên tục 
  Continuously sending inputs that exceed the LLM's context window can lead to excessive computational resource use, resulting in service degradation and operational disruptions.
#### 4. Tấn công bằng các truy vấn tốn tài nguyên
  Submitting unusually demanding queries involving complex sequences or intricate language patterns can drain system resources, leading to prolonged processing times and potential system failures.
#### 5. Trích xuất mô hình qua API
  Attackers may query the model API using carefully crafted inputs and prompt injection techniques to collect sufficient outputs to replicate a partial model or create a shadow model. This not only poses risks of intellectual property theft but also undermines the integrity of the original model.
#### 6. Sao chép mô hình chức năng
  Using the target model to generate synthetic training data can allow attackers to fine-tune another foundational model, creating a functional equivalent. This circumvents traditional query-based extraction methods, posing significant risks to proprietary models and technologies.
#### 7. Tấn công qua kênh phụ
  Malicious attackers may exploit input filtering techniques of the LLM to execute side-channel attacks, harvesting model weights and architectural information. This could compromise the model's security and lead to further exploitation.

### Chiến lược phòng ngừa và giảm thiểu

#### 1. Xác thực đầu vào
  Thực hiện xác thực đầu vào nghiêm ngặt để đảm bảo dữ liệu nhập vào không vượt quá giới hạn kích thước thông thường.
#### 2. Hạn chế khả năng tiếp cận Logits và Logprobs
  Giới hạn và ẩn khả năng tiếp cận `logit_bias` và `logprobs` trong các phản hồi API. Chỉ cung cấp các thông tin cần thiết mà không làm lộ ra các xác suất chi tiết.
#### 3. Giới hạn số lượng
  Đặt giới hạn số lượng và hạn mức sử dụng cho người dùng để giới hạn số lượng yêu cầu mà một nguồn đơn lẻ có thể thực hiện.
#### 4. Quản lý phân bổ tài nguyên
  Giám sát và quản lý phân bổ tài nguyên một cách linh hoạt để phòng chống việc một người dùng hoặc một yêu cầu sử dung quá nhiều tài nguyên. 
#### 5. Giới hạn thời gian và điều chỉnh tốc độ
  Đặt giới hạn thời gian và giới hạn tốc độ xử lý cho các tác vụ tốn tài nguyên để phòng chống việc chiếm dụng tài nguyên kéo dài.
#### 6. Kỹ thuật Sandbox
  Restrict the LLM's access to network resources, internal services, and APIs.
  - This is particularly significant for all common scenarios as it encompasses insider risks and threats. Furthermore, it governs the extent of access the LLM application has to data and resources, thereby serving as a crucial control mechanism to mitigate or prevent side-channel attacks.
#### 7. Comprehensive Logging, Monitoring and Anomaly Detection
  Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.
#### 8. Dấu chìm
  Sử dụng các khung chuẩn cho dấu chìm để chèn và phát hiện các hành vi sử dụng trái phép các kết quả đầu ra của Mô hình Ngôn ngữ lớn.
#### 9. Xuống cấp có kiểm soát
  Thiết kế hệ thống để hạ cấp có kiểm soát khi bị tải nặng, duy trì một phần chức năng thay vì ngừng hoạt động hoàn toàn.
#### 10. Limit Queued Actions and Scale Robustly
  Implement restrictions on the number of queued actions and total actions, while incorporating dynamic scaling and load balancing to handle varying demands and ensure consistent system performance.
#### 11. Adversarial Robustness Training
  Train models to detect and mitigate adversarial queries and extraction attempts.
#### 12. Glitch Token Filtering
  Build lists of known glitch tokens and scan output before adding it to the model’s context window.
#### 13. Access Controls
  Implement strong access controls, including role-based access control (RBAC) and the principle of least privilege, to limit unauthorized access to LLM model repositories and training environments.
#### 14. Centralized ML Model Inventory
  Use a centralized ML model inventory or registry for models used in production, ensuring proper governance and access control.
#### 15. Automated MLOps Deployment
  Implement automated MLOps deployment with governance, tracking, and approval workflows to tighten access and deployment controls within the infrastructure.

### Example Attack Scenarios

#### Kịch bản #1: Uncontrolled Input Size
  An attacker submits an unusually large input to an LLM application that processes text data, resulting in excessive memory usage and CPU load, potentially crashing the system or significantly slowing down the service.
#### Kịch bản #2: Repeated Requests
  An attacker transmits a high volume of requests to the LLM API, causing excessive consumption of computational resources and making the service unavailable to legitimate users.
#### Kịch bản #3: Resource-Intensive Queries
  An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes, leading to prolonged CPU usage and potential system failure.
#### Scenario #4: Denial of Wallet (DoW)
  An attacker generates excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.
#### Kịch bản #5: Functional Model Replication
  An attacker uses the LLM's API to generate synthetic training data and fine-tunes another model, creating a functional equivalent and bypassing traditional model extraction limitations.
#### Kịch bản #6: Bypassing System Input Filtering
  A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control.

### Liên kết tham khảo

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Các khung chuẩn và hệ thống phân loại liên quan

Tham khảo phần này để có thông tin toàn diện, các chiến lược tình huống liên quan đến triển khai hạ tầng, kiểm soát môi trường được áp dụng và các thực hành tốt nhất.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**