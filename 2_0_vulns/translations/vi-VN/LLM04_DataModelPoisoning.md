## LLM04: Nhiễm độc dữ liệu và Mô hình

### Mô tả

Nhiễm độc dữ liệu xảy ra khi dữ liệu đã được đào tạo, tinh chỉnh hoặc nhúng (embedding) bị tác động để chèn các lỗ hổng, cửa hậu hoặc định kiến. Sự thao túng này có thể ảnh hưởng đến bảo mật, hiệu suất hoặc hành vi đạo đức của mô hình, dẫn đến các gây hại đầu ra hoặc làm suy giảm hiệu suất. Các rủi ro phổ biến bao gồm giảm hiệu suất mô hình, nội dung định kiến hoặc độc hại, và khai thác các các hệ thống phía sau.

Nhiễm độc dữ liệu có thể nhắm vào các giai đoạn khác nhau trong vòng đời LLM, bao gồm tiền đào tạo (học từ dữ liệu chung), tinh chỉnh (tùy chỉnh mô hình cho các nhiệm vụ cụ thể) và nhúng (chuyển đổi văn bản thành vector số). Việc hiểu rõ các giai đoạn này giúp xác định những điểm dữ liệu có thể bị nhiễm độc. Nhiễm độc dữ liệu được coi là một cuộc tấn công vào tính toàn vẹn, vì việc can thiệp vào dữ liệu huấn luyện ảnh hưởng đến khả năng đưa ra dự đoán chính xác của mô hình. Rủi ro này đặc biệt cao đối với các nguồn dữ liệu bên ngoài, vì chúng có thể chứa nội dung chưa được xác minh hoặc độc hại.

Hơn nữa, các mô hình được phân phối qua kho lưu trữ chung hoặc nền tảng mã nguồn mở có thể tiềm ẩn nhiều rủi ro ngoài việc nhiễm độc dữ liệu, chẳng hạn như phần mềm độc hại được nhúng thông qua các kỹ thuật như malicious pickling, cho phép thực thi mã độc hại khi tải mô hình. Ngoài ra, việc nhiễm độc dữ liệu có thể tạo ra cửa hậu trong mô hình. Những cửa hậu này có thể giữ nguyên hành vi của mô hình cho đến khi một điều kiện kích hoạt cụ thể khiến nó thay đổi. Điều này khiến các thay đổi trở nên khó kiểm tra và phát hiện, tạo cơ hội để mô hình hoạt động như một tác nhân ngủ đông(sleeper agent)

### Các Ví Dụ Phổ Biến Về Lỗ Hổng

1. Kẻ tấn công chèn dữ liệu độc hại vào quá trình huấn luyện, dẫn đến kết quả đầu ra bị sai lệch. Các kỹ thuật như "Nhiễm độc dữ liệu phân tách" hoặc "Nhiễm độc dữ liệu đi trước" khai thác động lực huấn luyện của mô hình để đạt được mục đích này.
  (Tham khảo: [Nhiễm độc dữ liệu phân tách](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Tham khảo: [Nhiễm độc dữ liệu đi trước](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Kẻ tấn công có thể trực tiếp chèn nội dung độc hại vào quá trình huấn luyện, làm suy giảm chất lượng đầu ra của mô hình.
3. Người dùng vô tình đưa vào thông tin nhạy cảm hoặc dữ liệu độc quyền trong quá trình tương tác, dẫn đến khả năng rò rỉ thông tin trong các kết quả đầu ra tiếp theo.
4. Việc sử dụng dữ liệu huấn luyện không được xác minh làm tăng nguy cơ mô hình tạo ra kết quả thiên lệch hoặc sai lệch.
5. Thiếu kiểm soát quyền truy cập vào tài nguyên có thể cho phép mô hình tiếp nhận dữ liệu không an toàn, dẫn đến các đầu ra bị sai lệch.

### Chiến lược Phòng chống và Giảm thiểu

1. Theo dõi nguồn gốc và quá trình biến đổi của dữ liệu bằng các công cụ như OWASP CycloneDX hoặc ML-BOM. Xác minh tính hợp lệ của dữ liệu trong tất cả các giai đoạn phát triển mô hình.
2. Kiểm tra kỹ lưỡng nhà cung cấp dữ liệu và xác thực đầu ra của mô hình với các nguồn đáng tin cậy để phát hiện dấu hiệu nhiễm độc.
3. Thực hiện hộp cát (sandboxing) nghiêm ngặt để hạn chế mô hình tiếp xúc với các nguồn dữ liệu chưa được xác minh. Sử dụng kỹ thuật phát hiện bất thường để lọc dữ liệu tấn công đối kháng.
4. Tinh chỉnh mô hình theo từng trường hợp sử dụng bằng cách sử dụng bộ dữ liệu cụ thể. Điều này giúp tạo ra đầu ra chính xác hơn dựa trên mục tiêu đã xác định.
5. Đảm bảo kiểm soát hạ tầng đầy đủ để ngăn mô hình truy cập các nguồn dữ liệu không mong muốn.
6. Sử dụng quản lý phiên bản dữ liệu (DVC) để theo dõi thay đổi trong tập dữ liệu và phát hiện thao túng. Phiên bản hóa dữ liệu rất quan trọng để duy trì tính toàn vẹn của mô hình.
7. Lưu trữ thông tin do người dùng cung cấp trong cơ sở dữ liệu vector (Vector Database), cho phép điều chỉnh mà không cần huấn luyện lại toàn bộ mô hình.
8. Kiểm tra độ bền vững của mô hình bằng chiến dịch đội đỏ (red team) và các kỹ thuật tấn công đối kháng, như học liên kết (federated learning), để giảm thiểu tác động của nhiễu dữ liệu.
9. Giám sát độ mất mát huấn luyện và phân tích hành vi mô hình để phát hiện dấu hiệu nhiễm độc. Sử dụng ngưỡng phát hiện để nhận diện đầu ra bất thường.
10. Trong quá trình suy luận, tích hợp Retrieval-Augmented Generation (RAG) và kỹ thuật grounding để giảm thiểu rủi ro ảo giác thông tin.

### Kịch bản Tấn công Minh họa

#### Kịch bản #1
Kẻ tấn công làm sai lệch đầu ra của mô hình bằng cách thao túng dữ liệu huấn luyện hoặc sử dụng kỹ thuật prompt injection, từ đó lan truyền thông tin sai lệch.
#### Kịch bản #2
Dữ liệu độc hại không được lọc đúng cách có thể dẫn đến đầu ra mang tính định kiến hoặc gây hại, làm lan truyền thông tin nguy hiểm.
#### Kịch bản #3
Một tác nhân độc hại hoặc đối thủ cạnh tranh tạo ra tài liệu giả mạo để đưa vào quá trình huấn luyện, khiến mô hình tạo ra đầu ra phản ánh những thông tin sai lệch đó.
#### Kịch bản #4
Cơ chế lọc dữ liệu không đầy đủ cho phép kẻ tấn công chèn dữ liệu gây hiểu lầm thông qua prompt injection, dẫn đến kết quả bị thao túng.
#### Kịch bản #5
Kẻ tấn công sử dụng kỹ thuật nhiễm độc dữ liệu để cài cắm cửa hậu (backdoor) vào mô hình. Điều này có thể dẫn đến bỏ qua xác thực, rò rỉ dữ liệu hoặc thực thi lệnh ẩn khi gặp điều kiện kích hoạt.

### Các liên kết tham khảo

1. [Cách các cuộc tấn công nhiễm độc dữ liệu làm hỏng mô hình học máy](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) - Tấn công nhiễm độc dữ liệu Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: Cách chúng tôi giấu một mô hình LLM bị biến đổi trên Hugging Face để lan truyền tin giả](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Nhiễm độc mô hình ngôn ngữ trong quá trình huấn luyện](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Nhiễm độc tập dữ liệu huấn luyện quy mô lớn - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [Kho mô hình học máy: Mục tiêu mới của các cuộc tấn công chuỗi cung ứng](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Các nhà khoa học dữ liệu bị nhắm đến bởi mô hình Hugging Face độc hại có cửa hậu ẩn](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Tấn công backdoor vào mô hình ngôn ngữ](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Khai thác tệp pickle trong học máy: Lỗ hổng chưa từng có](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [Sleeper Agents: Huấn luyện các mô hình LLM lừa đảo có thể vượt qua kiểm tra an toàn](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Tấn công cửa hậu vào mô hình AI](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### Các khung và phân loại liên quan

Tham khảo các tài liệu dưới đây để có thông tin chi tiết về các kịch bản tấn công, chiến lược bảo mật, kiểm soát môi trường triển khai và các phương pháp bảo vệ tốt nhất:

- [AML.T0018 | Mô hình ML bị cài cửa hậu](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [Khung quản lý rủi ro AI của NIST ](https://www.nist.gov/itl/ai-risk-management-framework): Chiến lược đảm bảo tính toàn vẹn của AI . **NIST**
