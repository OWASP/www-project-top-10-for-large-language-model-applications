## LLM05: Supply-Chain Vulnerabilities

### Mô tả

Chuỗi cung ứng trong LLM có thể có lỗi, gây ảnh hưởng đến tính toàn vẹn của dữ liệu đào tạo, mô hình ML và các nền tảng triển khai. Những lỗ hổng này có thể dẫn đến kết quả thiên vị, vi phạm bảo mật hoặc thậm chí là lỗi hệ thống hoàn toàn. Theo truyền thống, lỗ hổng tập trung vào các thành phần phần mềm, nhưng Machine Learning mở rộng điều này với các mô hình được đào tạo trước và dữ liệu đào tạo do bên thứ ba cung cấp dễ bị tấn công giả mạo và đầu độc.

Cuối cùng, các tiện ích mở rộng Plugin LLM có thể mang lại những lỗ hổng riêng của chúng. Những lỗ hổng này được mô tả trong [LLM07 - Insecure Plugin Design](InsecurePluginDesign.md), bao gồm việc viết Plugin LLM và cung cấp thông tin hữu ích để đánh giá các plugin của bên thứ ba.

### Các ví dụ phổ biến về lỗ hổng

1. Lỗ hổng gói của bên thứ ba truyền thống, bao gồm các thành phần lỗi thời hoặc không còn được sử dụng nữa.
2. Sử dụng mô hình được đào tạo trước dễ bị tấn công để tinh chỉnh.
3. Sử dụng dữ liệu cộng đồng bị nhiễm độc để đào tạo.
4. Sử dụng các mô hình lỗi thời hoặc không còn được duy trì sẽ dẫn đến các vấn đề về bảo mật.
5. Các điều khoản và chính sách bảo mật dữ liệu không rõ ràng của các nhà quản lý mô hình dẫn đến việc dữ liệu nhạy cảm của ứng dụng được sử dụng để đào tạo mô hình và tiếp xúc với thông tin nhạy cảm sau đó. Điều này cũng có thể áp dụng cho các rủi ro từ việc sử dụng tài liệu có bản quyền của nhà cung cấp mô hình.

### Chiến lược phòng ngừa và giảm thiểu

1. Kiểm tra cẩn thận các nguồn dữ liệu và nhà cung cấp, bao gồm cả Điều khoản & Điều kiện và chính sách bảo mật của họ, chỉ sử dụng các nhà cung cấp đáng tin cậy. Đảm bảo rằng các nhà cung cấp này đáp ứng các yêu cầu bảo mật cần thiết, được kiểm tra độc lập, và tuân thủ các chính sách của bạn về bảo vệ dữ liệu, cụ thể, dữ liệu của bạn không được sử dụng để đào tạo các mô hình của nhà cung cấp dữ liệu. Ngoài ra, hãy yêu cầu các cam kết và biện pháp hợp pháp để giảm thiểu rủi ro liên quan đến việc sử dụng tài liệu có bản quyền từ những người bảo trì mô hình. Điều này nhằm đảm bảo rằng việc sử dụng tài liệu và dữ liệu tuân thủ các quy định về quyền sở hữu trí tuệ và bảo vệ dữ liệu.
2. Chỉ sử dụng các plugin có uy tín và đảm bảo chúng đã được thử nghiệm và kiểm thử theo yêu cầu ứng dụng của bạn. LLM-Insecure Plugin Design ở dưới sẽ cung cấp thông tin về các khía cạnh LLM của thiết kế Insecure Plugin mà bạn nên thử nghiệm để giảm thiểu rủi ro khi sử dụng plugin của bên thứ ba.
3. Hiểu và áp dụng các biện pháp giảm thiểu được tìm thấy trong OWASP Top Ten [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/). Bao gồm các thành phần quét lỗ hổng, quản lý và vá lỗi. Đối với các môi trường phát triển có quyền truy cập vào dữ liệu nhạy cảm, hãy áp dụng các biện pháp kiểm soát an toàn trong các môi trường đó.
4. Duy trì danh mục thành phần được cập nhật bằng cách sử dụng Danh mục vật liệu phần mềm (SBOM) để đảm bảo bạn có danh mục được cập nhật, chính xác và đã ký, ngăn chặn việc giả mạo các gói đã triển khai. SBOM có thể được sử dụng để phát hiện và cảnh báo nhanh chóng các lỗ hổng mới, không có ngày tháng.
5. Tại thời điểm viết bài, SBOM không bao gồm các mô hình, hiện vật và tập dữ liệu của chúng. Nếu ứng dụng LLM của bạn sử dụng mô hình riêng, bạn nên sử dụng các phương pháp hay nhất và nền tảng MLOps cung cấp kho lưu trữ mô hình an toàn với dữ liệu, mô hình và theo dõi thử nghiệm.
6. Bạn cũng nên sử dụng mô hình và chữ ký mã khi sử dụng các mô hình và nhà cung cấp bên ngoài.
7. Phát hiện bất thường và kiểm tra độ đối nghịch trên các mô hình và dữ liệu được cung cấp có thể giúp phát hiện hành vi giả mạo và đầu độc như đã thảo luận trong [ Training Data Poisoning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md); lý tưởng nhất là điều này sẽ là một phần của quy trình MLOps; tuy nhiên, đây là những kỹ thuật mới nổi và có thể triển khai như một phần của các bài luyện tập đội đỏ (Redteam).
8. Triển khai giám sát đầy đủ để quét các lỗ hổng của thành phần và môi trường, sử dụng plugin trái phép và các thành phần lỗi thời, bao gồm mô hình và các hiện vật của nó.
9. Triển khai chính sách vá lỗi để giảm thiểu các thành phần dễ bị tấn công hoặc lỗi thời. Đảm bảo ứng dụng dựa trên phiên bản API được bảo trì và mô hình cơ bản.
10. Thường xuyên xem xét và kiểm tra Bảo mật và Quyền truy cập của nhà cung cấp, đảm bảo không có thay đổi nào về chính sách bảo mật hoặc Điều khoản & Điều kiện của họ.

### Ví dụ về các kịch bản tấn công

1. Kẻ tấn công khai thác thư viện Python dễ bị tấn công để xâm phạm hệ thống. Điều này đã xảy ra trong vụ vi phạm dữ liệu Open AI đầu tiên.
2. Kẻ tấn công cung cấp plugin LLM để tìm kiếm chuyến bay, tạo ra các liên kết giả mạo dẫn đến lừa đảo người dùng.
3. Kẻ tấn công khai thác sổ đăng ký gói PyPi để lừa các nhà phát triển mô hình tải xuống một gói bị xâm phạm và đánh cắp dữ liệu hoặc tăng đặc quyền trong môi trường phát triển mô hình. Đây là một cuộc tấn công thực sự.
4. Kẻ tấn công đầu độc một mô hình được đào tạo trước có sẵn công khai chuyên về phân tích kinh tế và nghiên cứu xã hội để tạo ra một cửa sau tạo ra thông tin sai lệch và tin tức giả mạo. Chúng triển khai nó trên một thị trường mô hình (ví dụ: Hugging Face) để nạn nhân sử dụng.
5. Kẻ tấn công đầu độc các tập dữ liệu công khai để giúp tạo ra một cửa sau khi tinh chỉnh các mô hình. Cửa sau này sẽ ưu ái một số công ty nhất định ở các thị trường khác nhau.
6. Một nhân viên bị xâm nhập của nhà cung cấp (nhà phát triển gia công, công ty lưu trữ, v.v.) đánh cắp dữ liệu, mô hình hoặc mã IP.
7. Nhà điều hành LLM thay đổi Điều khoản & Điều kiện và Chính sách quyền riêng tư để yêu cầu người dùng phải chủ động từ chối việc sử dụng dữ liệu ứng dụng của họ cho việc đào tạo mô hình, điều này có thể dẫn đến việc dữ liệu nhạy cảm bị ghi nhớ..

### Tham khảo

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **Security Week**
2. [Plugin review process](https://platform.openai.com/docs/plugins/review) **OpenAI**
3. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Army looking at the possibility of 'AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv White Paper**
9. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733): **Arxiv White Paper**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
