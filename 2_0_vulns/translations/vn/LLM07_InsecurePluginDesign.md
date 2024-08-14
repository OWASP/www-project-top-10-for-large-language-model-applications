## LLM07: Insecure Plugin Design

### Mô tả

Các plugin LLM là các tiện ích mở rộng, khi được bật, sẽ được mô hình tự động gọi trong quá trình tương tác của người dùng. Nền tảng tích hợp mô hình điều khiển chúng và ứng dụng có thể không kiểm soát được quá trình thực thi, đặc biệt là khi mô hình được lưu trữ bởi một bên khác. Hơn nữa, các plugin có khả năng triển khai các đầu vào văn bản tự do từ mô hình mà không có xác thực hoặc kiểm tra kiểu để giải quyết các giới hạn về kích thước ngữ cảnh. Điều này cho phép kẻ tấn công xây dựng một yêu cầu độc hại cho plugin, có thể dẫn đến nhiều hành vi không mong muốn, bao gồm cả thực thi mã từ xa.

Tác hại của các đầu vào độc hại thường phụ thuộc vào việc kiểm soát truy cập không đủ và không theo dõi được quyền hạn giữa các plugin. Kiểm soát truy cập không đầy đủ cho phép một plugin tin tưởng mù quáng vào các plugin khác và cho rằng người dùng cuối đã cung cấp các đầu vào. Kiểm soát truy cập không đầy đủ như vậy có thể khiến các đầu vào độc hại gây ra hậu quả có hại, từ việc rò rỉ dữ liệu, thực thi mã từ xa và leo thang đặc quyền.

Mục này tập trung vào việc tạo các plugin LLM thay vì các plugin của bên thứ ba, mà mục LLM-Supply-Chain-Vulnerabilities đã đề cập đến.

### Các ví dụ phổ biến về lỗ hổng

1. Một plugin chấp nhận tất cả các tham số trong một trường văn bản thay vì các tham số đầu vào riêng biệt.
2. Một plugin chấp nhận chuỗi thông tin cấu hình và các tham số có thể ghi đè toàn bộ cài đặt cấu hình.
3. Một plugin chấp nhận các câu lệnh SQL hoặc câu lệnh lập trình thay vì các tham số.
4. Xác thực được thực hiện mà không cần sự cho phép đối với một plugin cụ thể.
5. Một plugin sẽ coi toàn bộ nội dung LLM được tạo ra hoàn toàn bởi người dùng và thực hiện mọi hành động được yêu cầu mà không cần phải có sự cho phép bổ sung.

### Chiến lược phòng ngừa và giảm thiểu

1. Các plugin nên thực thi các tham số đầu vào nghiêm ngặt bất cứ khi nào có thể và bao gồm kiểm tra loại và phạm vi cho các đầu vào. Khi điều này không thể thực hiện, nên giới thiệu một lớp gọi hàm có kiểu dữ liệu thứ hai, phân tích các yêu cầu và áp dụng kiểm tra và làm sạch dữ liệu. Khi phải chấp nhận đầu vào tự do vì các ngữ nghĩa ứng dụng, nó nên được kiểm tra cẩn thận để đảm bảo không có các phương pháp có thể gây hại đang được gọi.phương thức nào có khả năng gây hại được gọi.
2. Các nhà phát triển plugin nên áp dụng các khuyến nghị của OWASP trong ASVS (Tiêu chuẩn xác minh bảo mật ứng dụng - Application Security Verification Standard) để đảm bảo xác thực và lọc đầu vào đầy đủ.
3. Các plugin cần được kiểm tra và thử nghiệm kỹ lưỡng để đảm bảo xác thực đầy đủ. Sử dụng quét Kiểm tra bảo mật ứng dụng tĩnh (SAST) và Kiểm tra ứng dụng động và tương tác (DAST, IAST) trong các đường ống phát triển.
4. Các plugin nên được thiết kế để giảm thiểu tác động của việc khai thác tham số đầu vào không an toàn nào theo Hướng dẫn kiểm soát truy cập ASVS của OWASP. Điều này bao gồm kiểm soát truy cập ít đặc quyền nhất, phơi bày càng ít chức năng càng tốt trong khi vẫn thực hiện chức năng mong muốn.
5. Các plugin nên sử dụng các danh tính xác thực phù hợp, chẳng hạn như OAuth2, để áp dụng quyền hạn và kiểm soát truy cập hiệu quả. Ngoài ra, Khóa API nên được sử dụng để cung cấp ngữ cảnh cho các quyết định cấp phép tùy chỉnh quy trình sử dụng plugin thay vì người dùng tương tác mặc định.
6. Yêu cầu người dùng phải xác nhận và ủy quyền thủ công mọi hành động được thực hiện bởi các plugin nhạy cảm.
7. Các plugin thường là các API REST, do đó các nhà phát triển nên áp dụng các khuyến nghị trong OWASP Top 10 API Security Risks – 2023 để giảm thiểu các lỗ hổng chung.

### Ví dụ về các kịch bản tấn công

1. Một plugin chấp nhận một URL cơ sở và hướng dẫn LLM kết hợp URL với một truy vấn để lấy dự báo thời tiết được bao gồm trong việc xử lý yêu cầu của người dùng. Một người dùng độc hại có thể tạo một yêu cầu sao cho URL trỏ đến một tên miền mà họ kiểm soát, cho phép họ đưa nội dung của riêng họ vào hệ thống LLM thông qua tên miền của họ.
2. Một plugin chấp nhận đầu vào dạng tự do nhập dữ liệu mà nó không xác thực. Kẻ tấn công cung cấp các thông tin được chế tạo cẩn thận để thực hiện trinh sát từ các thông báo lỗi. Sau đó, nó khai thác các lỗ hổng của bên thứ ba đã biết để thực thi mã và thực hiện trích xuất dữ liệu hoặc leo thang đặc quyền.
3. Một plugin được sử dụng để lấy dữ liệu từ một kho vector và nó chấp nhận các tham số cấu hình như một chuỗi kết nối mà không yêu cầu bất kỳ xác thực nào. Điều này cho phép kẻ tấn công thử nghiệm và truy cập các kho vector khác bằng cách thay đổi tên hoặc tham số máy chủ và trích xuất các thông tin mà chúng không được phép truy cập.
4. Một plugin chấp nhận các mệnh đề SQL WHERE như các bộ lọc nâng cao, sau đó được thêm vào SQL lọc. Điều này cho phép kẻ tấn công dàn dựng một cuộc tấn công SQL.
5. Kẻ tấn công sử dụng lệnh chèn dấu nhắc gián tiếp để khai thác plugin quản lý mã không an toàn, không có xác thực đầu vào và kiểm soát truy cập yếu để chuyển quyền sở hữu kho lưu trữ và khóa người dùng khỏi kho lưu trữ của họ.

### Tham khảo

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace The Red**
7. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
8. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
9. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
10. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
