## LLM05:2025 Xử Lý Kết Quả Không Đúng Cách

### Mô tả

Xử lý kết quả không đúng cách xảy ra khi dữ liệu đầu ra từ mô hình ngôn ngữ lớn (LLM) không được kiểm tra, làm sạch hoặc xử lý phù hợp trước khi đưa vào hệ thống khác. Vì đầu ra của LLM có thể bị kiểm soát bởi các lời nhắc (prompt), tình huống này tương tự như việc cấp quyền truy cập gián tiếp vào các chức năng bổ sung.
Lỗi này khác với Quá Phụ Thuộc Vào LLM vì nó tập trung vào việc xử lý dữ liệu đầu ra trước khi truyền đi, trong khi Quá Phụ Thuộc Vào LLM đề cập đến rủi ro khi tin tưởng quá mức vào tính chính xác của kết quả.
Nếu khai thác thành công, lỗ hổng này có thể dẫn đến nhiều cuộc tấn công nguy hiểm như:
- XSS (Tấn công kịch bản chéo trang) và CSRF (Tấn công giả mạo yêu cầu liên trang) trên trình duyệt
- SSRF (Tấn công giả mạo yêu cầu phía máy chủ), leo thang đặc quyền hoặc thực thi mã từ xa trên hệ thống backend

Những yếu tố có thể làm tăng mức độ nghiêm trọng của lỗ hổng:

- Ứng dụng cấp quyền cho LLM vượt quá quyền hạn của người dùng, dẫn đến leo thang đặc quyền hoặc thực thi mã độc.
- Hệ thống dễ bị tấn công Tiêm nhắc lệnh (Prompt Injection), cho phép kẻ tấn công truy cập trái phép vào môi trường người dùng.
- Các tiện ích mở rộng của bên thứ ba không kiểm tra đầu vào kỹ lưỡng.
- Không mã hóa dữ liệu đầu ra đúng cách cho từng ngữ cảnh (ví dụ: HTML, JavaScript, SQL).
- Thiếu giám sát và ghi log để phát hiện dấu hiệu khai thác lỗ hổng.
- Không giới hạn tốc độ hoặc không có cơ chế phát hiện bất thường khi sử dụng LLM.

### Các Ví Dụ Phổ Biến Về Lỗ Hổng

1. LLM tạo ra đầu ra được đưa trực tiếp vào lệnh hệ thống - system shell (như exec hoặc eval), gây thực thi mã độc từ xa.
2. LLM tạo mã JavaScript hoặc Markdown, được trình duyệt thực thi, dẫn đến tấn công XSS.
3. LLM tạo truy vấn SQL mà không có kiểm tra tham số, dẫn đến SQL Injection.
4. LLM tạo đường dẫn file mà không kiểm tra, gây lỗ hổng Path Traversal.
5. Nội dung do LLM tạo ra được đưa vào email mà không mã hóa đúng cách, có thể dẫn đến tấn công phishing.

### Chiến lược Phòng chống và Giảm thiểu

1. Áp dụng mô hình Zero Trust – xử lý đầu ra từ LLM như dữ liệu từ người dùng và kiểm tra kỹ trước khi truyền đến hệ thống backend.
2. Fuân thủ chuẩn bảo mật OWASP ASVS (Application Security Verification Standard), đảm bảo kiểm tra và làm sạch dữ liệu đúng cách.
3. Mã hóa đầu ra của LLM để ngăn chặn mã độc JavaScript hoặc Markdown thực thi trên trình duyệt.
4. Sử dụng mã hóa phù hợp theo ngữ cảnh, (ví dụ: mã hóa HTML nếu hiển thị trên web, mã hóa SQL nếu dùng trong truy vấn cơ sở dữ liệu).
5. Dùng truy vấn có tham số (Parameterized Queries) để ngăn chặn SQL Injection.
6. Áp dụng chính sách CSP (Content Security Policy) để hạn chế nguy cơ XSS từ đầu ra của LLM.
7. Theo dõi, ghi log và phát hiện bất thường trong dữ liệu đầu ra của LLM để phát hiện sớm các cuộc tấn công.

### Kịch bản Tấn công Minh họa

#### Kịch bản #1
  Một ứng dụng sử dụng một tiện ích mở rộng của LLM để tạo phản hồi cho tính năng chatbot. Tiện ích mở rộng này cũng cung cấp một số chức năng quản trị có thể được truy cập bởi một LLM có đặc quyền cao hơn. LLM truyền trực tiếp phản hồi của nó, mà không có kiểm tra đầu ra thích hợp, đến tiện ích mở rộng, dẫn đến việc tiện ích mở rộng bị tắt để bảo trì.
#### Kịch bản #2
  Một người dùng sử dụng một công cụ tóm tắt nội dung trên website được vận hành bởi một LLM để tạo một bản tóm tắt ngắn gọn cho một bài viết. Trang web chứa một đoạn Tiêm nhắc lệnh (Prompt Injection), hướng dẫn LLM thu thập nội dung nhạy cảm từ chính trang web hoặc từ cuộc trò chuyện của người dùng. Sau đó, LLM có thể mã hóa dữ liệu nhạy cảm và gửi nó, mà không qua bất kỳ kiểm tra hoặc lọc đầu ra nào, đến một máy chủ do kẻ tấn công kiểm soát.
#### Kịch bản #3
  Một LLM cho phép người dùng tạo truy vấn SQL cho cơ sở dữ liệu backend thông qua một tính năng trò chuyện. Một người dùng yêu cầu một truy vấn để xóa tất cả các bảng trong cơ sở dữ liệu. Nếu truy vấn do LLM tạo ra không được kiểm tra kỹ lưỡng, tất cả các bảng trong cơ sở dữ liệu sẽ bị xóa.
#### Kịch bản #4
  Một ứng dụng web sử dụng LLM để tạo nội dung từ các văn bản của người dùng mà không có biện pháp làm sạch đầu ra. Một kẻ tấn công có thể gửi một lời nhắc được thiết kế đặc biệt, khiến LLM trả về một đoạn mã JavaScript không được lọc, dẫn đến tấn công XSS khi nó được hiển thị trên trình duyệt của nạn nhân. Việc kiểm tra không đầy đủ đối với các lời nhắc đã tạo điều kiện cho cuộc tấn công này.
#### Kịch bản # 5
  Một LLM được sử dụng để tạo mẫu email động cho một chiến dịch tiếp thị. Một kẻ tấn công thao túng LLM để chèn mã JavaScript độc hại vào nội dung email. Nếu ứng dụng không làm sạch đầu ra của LLM đúng cách, điều này có thể dẫn đến các cuộc tấn công XSS đối với những người nhận mở email trong các trình duyệt email dễ bị tổn thương.
#### Scenario #6
  Một LLM được sử dụng để tạo mã nguồn từ đầu vào ngôn ngữ tự nhiên trong một công ty phần mềm, với mục tiêu tối ưu hóa quy trình phát triển. Mặc dù hiệu quả, cách tiếp cận này tiềm ẩn nguy cơ làm lộ thông tin nhạy cảm, tạo ra các phương thức xử lý dữ liệu không an toàn hoặc đưa vào các lỗ hổng như SQL Injection. Ngoài ra, AI có thể tạo ra thông tin sai lệch và đề xuất các gói phần mềm không tồn tại, có khả năng khiến lập trình viên tải xuống các tài nguyên bị nhiễm mã độc. Việc kiểm tra mã nguồn kỹ lưỡng và xác thực các gói phần mềm được đề xuất là rất quan trọng để ngăn chặn các vi phạm bảo mật, truy cập trái phép và xâm nhập hệ thống.

### Các liên kết tham khảo

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Thực thi mã tùy ý](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [Phân tích khai thác Plugin ChatGPT: Từ tấn công tiêm nhắc lệnh đến truy cập dữ liệu riêng tư](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [Tấn công tiêm nhắc lệnh mới trên phiên bản web của ChatGPT: Hình ảnh Markdown có thể đánh cắp dữ liệu trò chuyện của bạn.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Không nên tin tưởng mù quáng vào phản hồi của LLM: Các mối đe dọa đối với chatbot](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Mô hình hóa mối đe dọa đối với ứng dụng LLM](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Xác thực, Làm sạch và Mã hóa dữ liệu đầu vào](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI tạo ảo giác về gói phần mềm và lập trình viên tải xuống chúng – ngay cả khi có thể bị nhiễm phần mềm độc hại](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**

