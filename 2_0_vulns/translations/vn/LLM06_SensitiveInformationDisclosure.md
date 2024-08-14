## LLM06: Sensitive Information Disclosure

### Mô tả

Thông tin nhạy cảm có liên quan đến cả mô hình và việc triển khai mô hình trong các ứng dụng LLM. Thuật ngữ này bao gồm nhưng không giới hạn ở thông tin nhận dạng cá nhân (PII), thông tin tài chính, hồ sơ sức khỏe, dữ liệu kinh doanh bí mật, thông tin xác thực bảo mật và các tài liệu pháp lý hoặc quy định v..v... Ngoài ra, các mô hình đóng hoặc nền tảng độc quyền có các phương pháp đào tạo và mã nguồn độc đáo cũng có thể được coi là nhạy cảm, điều này ít quan trọng hơn đối với các mô hình nguồn mở và mô hình trọng lượng mở.

Cả LLM và các thành phần nhúng trong các ứng dụng đều có nguy cơ tiết lộ thông tin nhạy cảm, thuật toán độc quyền hoặc các chi tiết bí mật khác thông qua đầu ra của chúng. Điều này có thể dẫn đến truy cập trái phép vào dữ liệu nhạy cảm, sở hữu trí tuệ, vi phạm quyền riêng tư và các vi phạm bảo mật khác. Điều quan trọng là người sử dụng các ứng dụng LLM phải biết cách tương tác an toàn với LLM và xác định các rủi ro liên quan đến việc vô tình nhập dữ liệu nhạy cảm mà sau đó LLM có thể trả về ở đầu ra ở nơi khác.

Để giảm thiểu rủi ro này, các ứng dụng LLM phải thực hiện lọc dữ liệu đầy đủ để ngăn dữ liệu người dùng nhập nhạy cảm vào dữ liệu mô hình đào tạo. Chủ sở hữu ứng dụng LLM cũng phải có các chính sách Điều khoản sử dụng phù hợp để người tiêu dùng biết dữ liệu của họ được xử lý như thế nào và khả năng từ chối đưa dữ liệu của họ vào mô hình đào tạo.

Việc tương tác giữa người dùng và LLM tạo thành ranh giới tin cậy hai chiều, trong đó chúng ta không thể tin tưởng vào đầu vào của máy khách đến LLM hoặc đầu ra của LLM đến máy khách. Điều quan trọng là lưu ý rằng lỗ hổng này giả định rằng một số yếu tố cần thiết không được xem xét, chẳng hạn như việc xây dựng mô hình đe dọa, bảo mật cơ sở hạ tầng, và tạo môi trường bảo vệ hộp cát (sandboxing). Việc thêm các hạn chế trong hệ thống hướng dẫn (system prompt) về các loại dữ liệu mà mô hình ngôn ngữ lớn (LLM) nên trả về có thể giúp giảm thiểu việc tiết lộ thông tin nhạy cảm, nhưng do tính chất khó lường của các mô hình ngôn ngữ lớn, những hạn chế này không phải lúc nào cũng được tuân thủ và có thể bị vượt qua thông qua việc tiêm nhiễm hướng dẫn (prompt injection) hoặc các phương pháp khác.

### Các ví dụ phổ biến về lỗ hổng

1. Lọc thông tin nhạy cảm trong phản hồi của LLM không đầy đủ hoặc không đúng cách: Xảy ra khi LLM không lọc được thông tin nhạy cảm khỏi đầu ra, có khả năng tiết lộ dữ liệu bí mật cho người dùng trái phép.
2. Quá trình khớp thông tin hoặc ghi nhớ dữ liệu nhạy cảm trong quá trình đào tạo của LLM: Khi LLM vô tình học và lưu giữ dữ liệu nhạy cảm cụ thể từ tập đào tạo của nó, dẫn đến khả năng thông tin này được tái tạo trong các phản hồi.
3. Tiết lộ thông tin bí mật ngoài ý muốn do LLM hiểu sai, thiếu phương pháp lọc dữ liệu hoặc lỗi: Xảy ra khi LLM hiểu sai dữ liệu đầu vào hoặc thiếu cơ chế khử trùng dữ liệu hiệu quả, dẫn đến việc vô tình tiết lộ thông tin nhạy cảm.

### Chiến lược phòng ngừa và giảm thiểu

1. Tích hợp các kỹ thuật lọc dữ liệu phù hợp: Ngăn dữ liệu người dùng xâm nhập vào dữ liệu mô hình đào tạo bằng cách triển khai các phương pháp lọc dữ liệu hiệu quả.
2. Triển khai các phương pháp xác thực và lọc đầu vào mạnh mẽ: Xác định và lọc ra các đầu vào độc hại tiềm ẩn để ngăn chặn mô hình bị nhiễm độc.
3. Tinh chỉnh với dữ liệu nhạy cảm:
   - Áp dụng Quy tắc đặc quyền tối thiểu: Không đào tạo mô hình trên thông tin mà người dùng có đặc quyền cao nhất có thể truy cập nếu thông tin đó có thể được hiển thị cho người dùng có đặc quyền thấp hơn.
   - Hạn chế quyền truy cập vào các nguồn dữ liệu bên ngoài: Hạn chế quyền truy cập vào các nguồn dữ liệu bên ngoài và đảm bảo sắp xếp dữ liệu phù hợp khi chạy.
   - Thực thi Kiểm soát truy cập nghiêm ngặt: Áp dụng các phương pháp kiểm soát truy cập nghiêm ngặt vào các nguồn dữ liệu bên ngoài và duy trì chuỗi cung ứng an toàn.
4. Sử dụng Học tập liên kết: Đào tạo các mô hình trên nhiều thiết bị hoặc máy chủ phi tập trung lưu trữ các mẫu dữ liệu cục bộ mà không trao đổi chúng, do đó giảm nguy cơ lộ dữ liệu nhạy cảm.
5. Tích hợp các kỹ thuật bảo mật riêng biệt: Đảm bảo rằng các điểm dữ liệu riêng lẻ không thể bị đảo ngược (reverse-engineered) từ đầu ra của LLM bằng cách kết hợp các kỹ thuật bảo mật riêng biệt.
   - Giáo dục và đào tạo người dùng: Giáo dục người dùng về những rủi ro khi nhập thông tin nhạy cảm vào LLM và cung cấp đào tạo về các biện pháp thực hành tốt nhất.
6. Nguyên tắc giảm thiểu dữ liệu: Tuân thủ nguyên tắc giảm thiểu dữ liệu bằng cách chỉ thu thập và xử lý dữ liệu cần thiết cho mục đích cụ thể của ứng dụng.
7. Phân quyền để tiết lộ thông tin nhạy cảm: Công cụ phân quyền có thể ngăn chặn việc tiết lộ thông tin nhạy cảm trong ứng dụng LLM bằng cách khử trùng dữ liệu thông qua quá trình xử lý trước (ví dụ: che giấu thông tin nhạy cảm) và biên tập các thuật ngữ nhạy cảm bằng các kỹ thuật khớp mẫu.
   - Vệ sinh dữ liệu: Xử lý trước dữ liệu để che giấu hoặc xóa thông tin nhạy cảm (ví dụ: thay thế số thẻ tín dụng bằng ký tự ẩn).
   - Sử dụng các kỹ thuật khớp mẫu để phát hiện và vệ sinh thông tin nhạy cảm trước khi mã hóa.
   - Biên tập: Cấu hình phân tích để nhận dạng và biên tập các thuật ngữ hoặc cụm từ nhạy cảm cụ thể trước khi xử lý theo mô hình.
9. Vùng đệm: Áp dụng vùng đệm vào phản hồi mã thông báo với độ nhiễu ngẫu nhiên để che khuất độ dài của mã thông báo sao cho phản hồi không thể được suy ra từ các gói tin nhằm ngăn chặn các cuộc tấn công kênh phụ.
10. Mã hóa đồng cấu có thể bảo vệ thông tin nhạy cảm trong các ứng dụng AI bằng cách cho phép phân tích dữ liệu an toàn, tạo điều kiện cho máy học bảo vệ quyền riêng tư, hỗ trợ học liên bang với dữ liệu được mã hóa và đảm bảo dự đoán an toàn trong khi vẫn giữ bí mật dữ liệu người dùng.
11. Hoạt động đội đỏ (redteam) liên tục: Thực hiện thường xuyên các bài tập đội đỏ để giải quyết các hướng đe dọa đang phát triển như Tấn công tiêm mã độc nhanh (LLM01) và Đầu độc dữ liệu (LLM03).
12. Giám sát động và phát hiện bất thường: Triển khai hệ thống giám sát thời gian thực và phát hiện bất thường để xác định và giảm thiểu rò rỉ dữ liệu tiềm ẩn khi chúng xảy ra.
13. Sự đồng ý và minh bạch của người dùng:
   - Cơ chế đồng ý rõ ràng: Đảm bảo rằng người dùng đồng ý rõ ràng với các chính sách sử dụng dữ liệu.
   - Thực hành dữ liệu minh bạch: Duy trì tính minh bạch trong các thực hành xử lý dữ liệu, bao gồm truyền đạt rõ ràng về các chính sách lưu giữ, sử dụng và xóa dữ liệu.
14. Hạn chế ghi đè và che giấu phần mở đầu hệ thống để ngăn chặn khai thác
   - Hạn chế ghi đè phần mở đầu mô hình và che giấu phần mở đầu hệ thống: Ngăn chặn khả năng các tác nhân độc hại khai thác mô hình ngôn ngữ lớn (LLM) bằng cách giới hạn khả năng ghi đè các chức năng phần mở đầu của mô hình và đảm bảo rằng phần mở đầu hệ thống không bị tiết lộ. Điều này liên quan đến việc thực hiện các biện pháp kiểm soát truy cập nghiêm ngặt và các biện pháp bảo vệ để ngăn chặn các thay đổi hoặc tiết lộ trái phép về các hướng dẫn cài đặt ban đầu của mô hình. Bằng cách này, bạn giảm thiểu nguy cơ kẻ tấn công có thể hiểu biết về cấu trúc và hành vi của mô hình, điều mà họ có thể sử dụng trong các giai đoạn thám sát và tấn công. Chiến lược này đảm bảo tính toàn vẹn của các tham số cơ bản của LLM và giảm thiểu các vectơ tấn công tiềm năng.
15. Tham khảo [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) khi các thông báo lỗi không được xử lý đúng cách, chúng có thể vô tình làm lộ thông tin nhạy cảm trong nhật ký hoặc phản hồi. Thông tin này có thể bao gồm dấu vết ngăn xếp (stack traces), bản sao lưu cơ sở dữ liệu, khóa API, thông tin đăng nhập của người dùng hoặc dữ liệu nhạy cảm khác có thể bị kẻ tấn công khai thác.
   - Lọc thông báo lỗi: Đảm bảo rằng các thông báo lỗi trả về cho khách hàng là chung chung và không tiết lộ chi tiết triển khai nội bộ. Sử dụng các thông báo lỗi tùy chỉnh cung cấp thông tin tối thiểu.
   - Thực hành ghi nhật ký an toàn: Triển khai các thực hành ghi nhật ký an toàn bằng cách lọc và biên tập thông tin nhạy cảm khỏi nhật ký. Chỉ ghi nhật ký thông tin cần thiết để khắc phục sự cố.
   - Quản lý cấu hình: Thường xuyên xem xét và cập nhật cấu hình API để đảm bảo chúng tuân thủ các biện pháp bảo mật tốt nhất. Tắt ghi nhật ký chi tiết và các cài đặt không an toàn khác theo mặc định.
   - Giám sát và kiểm tra: Giám sát nhật ký và kiểm tra cấu hình thường xuyên để phát hiện và phản hồi bất kỳ cấu hình bảo mật nào không đúng.  

### Ví dụ về các kịch bản tấn công

1. Tiết lộ dữ liệu ngoài ý muốn: Người dùng hợp pháp A không nghi ngờ gì đã tiếp xúc với một số dữ liệu người dùng khác thông qua LLM khi tương tác với ứng dụng LLM theo cách không độc hại. Ví dụ, khi đặt một câu hỏi chung, người dùng A nhận được phản hồi có chứa các đoạn trích thông tin cá nhân của người dùng khác do dữ liệu không được khử trùng đầy đủ.
2. Tấn công tiêm nhắc nhở có mục tiêu: Người dùng A tạo ra một tập hợp các nhắc nhở được xây dựng tốt để bỏ qua các bộ lọc đầu vào và cơ chế vệ sinh, khiến LLM tiết lộ thông tin nhạy cảm (ví dụ: PII) về những người dùng khác của ứng dụng. Cuộc tấn công này khai thác điểm yếu trong quy trình xác thực đầu vào của LLM.
3. Rò rỉ dữ liệu qua dữ liệu đào tạo: Dữ liệu cá nhân như PII vô tình được đưa vào dữ liệu đào tạo của mô hình do sự bất cẩn của người dùng hoặc ứng dụng LLM. Điều này có thể xảy ra nếu dữ liệu đào tạo không được kiểm tra và khử trùng đúng cách trước khi được sử dụng để đào tạo mô hình. Do đó, thông tin nhạy cảm có thể bị tiết lộ trong phản hồi của LLM, làm trầm trọng thêm tác động của các kịch bản 1 và 2.
4. Kiểm soát truy cập không đầy đủ: Trong trường hợp LLM truy cập các nguồn dữ liệu bên ngoài khi chạy, các phương pháp kiểm soát truy cập yếu có thể cho phép người dùng trái phép truy vấn thông tin nhạy cảm thông qua LLM. Ví dụ, nếu LLM được tích hợp với cơ sở dữ liệu của công ty mà không có các hạn chế truy cập phù hợp, nó có thể tiết lộ dữ liệu kinh doanh bí mật cho người dùng trái phép.
5. Quá trình mô hình hóa và ghi nhớ: Trong quá trình đào tạo, LLM quá trình quá mức trên các điểm dữ liệu nhạy cảm, ghi nhớ chúng. Điều này dẫn đến việc tiết lộ không chủ ý khi LLM tạo phản hồi. Ví dụ, một LLM được đào tạo trên email nội bộ có thể vô tình tái tạo các cụm từ chính xác hoặc các chi tiết nhạy cảm từ các email đó trong phản hồi của mình.

### Tham khảo

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/) **Wired**
4. [Nvidia’s AI software tricked into leaking data](https://www.ft.com/content/5aceb7a6-9d5a-4f1f-af3d-1ef0129b0934) **Financial Times**
5. [Building a serverless tokenization solution to mask sensitive data](https://aws.amazon.com/blogs/compute/building-a-serverless-tokenization-solution-to-mask-sensitive-data/#:~:text=Tokenization%20replaces%20the%20sensitive%20data,while%20helping%20with%20data%20protection.) **AWS**
6. [Hackers can read private AI-assistant chats even though they’re encrypted](https://arstechnica.com/security/2024/03/hackers-can-read-private-ai-assistant-chats-even-though-theyre-encrypted/) **ArsTechnica**
7. [Mitigating a token-length side-channel attack in our AI products](https://blog.cloudflare.com/ai-side-channel-attack-mitigated#:~:text=The%20researchers%20suggested%20a%20few,be%20inferred%20from%20the%20packets.)
8. [How Federated Learning Protects Privacy](https://pair.withgoogle.com/explorables/federated-learning/)
9. [Using Differential Privacy to Build Secure Models: Tools, Methods, Best Practices](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices) **Neptune Blog**
10. [Maximizing Data Privacy in Fine-Tuning LLMs](https://pvml.com/maximizing-data-privacy-in-fine-tuning-llms/#:~:text=of%20customer%20trust.-,Organizations%20that%20fail%20to%20protect%20sensitive%20data%20during%20the%20fine,to%20concerns%20about%20data%20privacy.)
11. [What is Data Minimization? Main Principles & Techniques](https://www.piiano.com/blog/data-minimization#:~:text=Data%20minimization%20plays%20a%20big,making%20your%20data%20even%20safer.)
12. [Solving LLM Privacy with FHE](https://medium.com/@ingonyama/solving-llm-privacy-with-fhe-3486de6ee228)
13. [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) **OWASP API Security**