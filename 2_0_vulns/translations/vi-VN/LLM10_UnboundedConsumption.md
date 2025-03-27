 ## LLM10:2025 Chiếm dụng không giới hạn

### Mô tả

Chiếm dụng không giới hạn (Unbounded Consumption) là quá trình khi Mô hình Ngôn ngữ lớn cho các kết quả dựa trên các truy vấn hoặc câu lệnh đầu vào. Suy luận (Inference) là một chức năng quan trọng của Mô hình Ngôn ngữ lớn, trong đó mô hình áp dung các mẫu đã học và kiến thức để đưa ra các phản hồi hoặc các dự đoán phù hợp.

Các cuộc tấn công với mục đích làm gián đoạn dịch vụ, làm cạn kiệt nguồn lực tài chính của mục tiêu, hoặc đánh cắp tài sản trí tuệ bằng cách sao chép hành vi của mô hình đều khai thác một điểm yếu chung về bảo mật. Chiếm dụng không giới hạn xảy ra khi một Mô hình Ngôn ngữ lớn cho phép người dùng thực hiện các suy luận quá mức và không kiểm soát, dẫn đến các nguy cơ như từ chối dịch vụ (DoS), thiệt hại tài chính, đánh cắp mô hình và làm giảm chất lượng dịch vụ. Do Mô hình Ngôn ngữ lớn yêu cầu tài nguyên tính toán lớn, đặc biệt trong môi trường đám mây, do vậy dễ là lỗ hổng để khai thác tài nguyên và sử dụng trái phép. 

### Các ví dụ phổ biến về lỗ hổng

#### 1. Tấn công tràn với đầu vào có độ dài linh hoạt
  Kẻ tấn công làm quá tải hệ thống khi nhập đầu vào vớ độ dài đa dạng, khai thác sự kém hiệu quả khi xử lý dữ liệu. Việc này có thể làm tiêu tốn tài nguyên và có khả năng làm hệ thống không thể phản hồi, ảnh nghiêm trọng đến khả năng cung cấp dịch vụ. 
#### 2. Tấn công từ chối ví (DoW)
  Kẻ tấn công khởi tạo một số lượng lớn các tác vụ, khai tác mô hình tính phí theo mức sử dụng của các dịch vụ AI trên đám mây, dẫn đến gánh nặng tài chính cho nhà cung cấp và nguy cơ phá sản.
#### 3. Tấn công tràn đầu vào liên tục 
  Việc dữ liệu đầu vào được gửi liên tục làm quá tải cửa sổ ngữ cảnh của mô hình có thể dẫn đến việc tiêu thụ tài nguyên tính toán quá mức, gây hạ cấp dịch vụ và gián đoạn hoạt động.
#### 4. Tấn công bằng các truy vấn tốn tài nguyên
  Việc gửi các truy vấn có đòi hỏi cao bất thường bao gồm các chuỗi và các mẫu ngôn ngữ phức tạp có thể làm cạn kiệt tài nguyên của hệ thống, dẫn đến thời gian xử lý kéo dài hoặc hệ thống ngừng hoạt động.
#### 5. Trích xuất mô hình qua API
  Kẻ tấn công có thể truy vấn mô hình API bằng cách sử dụng các dữ liệu nhập vào được thiết kế riêng và kỹ thuật chèn lệnh để thu thập kết quả đầu ra nhằm sao chép một phần mô hình hoặc tạo ra một bóng mô hình. Việc này không chỉ gây rủi ro bị đánh cắp tài sản trí tuệ mà còn đe dọa tính toàn vẹn của mô hình ban đầu.
#### 6. Sao chép mô hình chức năng
  Sử dụng mô hình mục tiêu để tạo ra dữ liệu huấn luyện nhân tạo giúp kẻ tấn công tinh chỉnh mô hình nền tảng khác, tạo ra mô hình chức năng tương đương. Việc này vượt qua các phương pháp trích xuất dựa trên truy vấn thông thường, tạo ra nguy cơ lớn cho công nghệ và các mô hình độc quyền.
#### 7. Tấn công qua kênh phụ
  Kẻ tấn công có thể khai thác kỹ thuật lọc đầu vào của mô hình để thực hiện tấn công qua kênh phụ, thu thập trọng số và thông tin kiến trúc của mô hình.

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
  Hạn chế quyền truy cập của mô hình vào tài nguyên mạng, dịch vụ nội bộ và API.
  - Điều này rất quan trọng trong tất cả các tình huống phổ biến vì nó bao gồm rủi ro và các mối đe dọa trong nội bộ. HƠn nữa, nó còn kiểm soát phạm vi truy cập của ứng dụng mô hình vào dữ liệu và tài nguyên, do vậy nó có vai trò như một cơ chế giảm thiểu hoặc phòng chống các loại tấn công qua kênh phụ.
#### 7. Ghi log, theo dõi và phát hiện bất thường đầy đủ
  Liên tục theo dõi việc sử dụng tài nguyên và áp dụng ghi log để phát hiện và phản ứng trong trường hợp chiếm dụng tài nguyên bất thường.
#### 8. Dấu chìm
  Sử dụng các khung chuẩn cho dấu chìm để chèn và phát hiện các hành vi sử dụng trái phép các kết quả đầu ra của Mô hình Ngôn ngữ lớn.
#### 9. Xuống cấp có kiểm soát
  Thiết kế hệ thống để hạ cấp có kiểm soát khi bị tải nặng, duy trì một phần chức năng thay vì ngừng hoạt động hoàn toàn.
#### 10. Giới hạn tác vụ chờ và mở rộng
  Giới hạn số lượng các tác vụ chờ và tổng số tác vụ, đồng thời kết hợp mở rộng linh hoạt và can bằng tải để xử lý các nhu cầu đa dạng và đảm bảo hoạt động ổn định của hệ thống.
#### 11. Đào tạo chống tấn công
  Đào tạo mô hình để phát hiện và giảm thiểu các truy vấn thù địch và các nỗ lực nhằm trích xuất dữ liệu
#### 12. Lọc token lỗi
  Xây dựng danh sách các token lỗi đã biết và quét các kết quả đầu ra trước khi thêm chúng vào cửa sổ ngữ cảnh của mô hình.
#### 13. Kiểm soát truy cập
  Thực hiện cơ chế kiểm soát truy cập mạnh, bao gồm kiểm soát truy cập dựa trên vai trò (RBAC) và nguyên tắc đặc quyền tối thiểu, để hạn chế các truy cập trái phép vào kho lưu trữ và môi trường đào tạo của mô hình.
#### 14. Lưu trữ mô hình máy học (ML) tập trung
  Sử dụng kho lưu trữ tập trung hoặc hệ thống quản lý tập trung cho các mô hình máy học sử dụng trong môi trường triển khai, để đảm bảo quản trị và kiểm soát truy cập phù hợp. 
#### 15. Triển khai vận hành máy học (MLOps) tự động
  Thực hiện triển khai vận hành máy học tự động cùng với việc quản trị, theo dõi và quy trình phê duyệt để kiểm soát truy cập và triển khai chặt chẽ hơn trong hạ tầng.

### Các kịch bản tấn công mẫu

#### Kịch bản #1: Uncontrolled Input Size
  Kẻ tấn công nhập dữ liệu lớn bất thường vào ứng dụng LLM xử lý dữ liệu văn bản, dẫn đến việc làm quá tải bộ nhớ và CPU, có thể gây sập hệ thống hoặc làm dịch vụ bị chậm đi đáng kể.
#### Kịch bản #2: Yêu cầu lặp lại
  Kẻ tấn công gửi một số lượng lớn các yêu cầu đến LLM API, gây ra việc tiêu tốn tài nguyên tính toán quá mức, dẫn đến việc những người dùng thật không thể sử dụng dịch vụ.
#### Kịch bản #3: Các truy vấn chiếm dụng tài nguyên
  Kẻ tấn công dùng những dữ liệu nhập đầu vào đặc biệt được thiết kế để kích hoạt các quá trình tiêu tốn nhiều tài nguyên tính toán nhất của LLM, dẫn đến việc sử dụng CPU kéo dài và có thể làm sập hệ thống.
#### Kịch bản #4: Từ chối ví
  Kẻ tấn công thực hiện số lượng lớn các tác vụ nhằm lợi dụng mô hình tính phí theo mức sử dụng của các dịch vụ AI đám mây, gây ra các chi phí không thể duy trì cho các nhà cung cấp dịch vụ. 
#### Kịch bản #5: Sao chép mô hình chức năng
  Kẻ tấn công sử dụng API của LLM để tạo ra dữ liệu huấn luyện nhân tạo và tinh chỉnh mô hình khác, tạo ra mô hình tương đương và qua mặt các giới hạn trích xuất mô hình thông thường.
#### Kịch bản #6: Qua mặt hệ thống lọc dữ liệu nhập vào
  A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control. Kẻ tấn công qua mặt kỹ thuật lọc dữ liệu nhập vào và phần hướng dẫn của LLM để thực hiện tấn công qua kênh phụ và thu thập thông tin mô hìnd để chuyển vào những tài nguyên mà chúng kiểm soát từ xa.

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

Tham khảo phần này để có thông tin toàn diện, các chiến lược kịch bản liên quan đến triển khai hạ tầng, kiểm soát môi trường được áp dụng và các thực hành tốt nhất.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**