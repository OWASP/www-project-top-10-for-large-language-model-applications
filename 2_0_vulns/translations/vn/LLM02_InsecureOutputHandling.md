## LLM02: Insecure Output Handling

### Mô tả

Xử lý đầu ra không an toàn đề cập cụ thể đến việc xác thực, làm sạch và xử lý không đủ đối với các đầu ra do các mô hình ngôn ngữ lớn tạo ra trước khi chúng được truyền xuống các thành phần và hệ thống khác. Vì nội dung do LLM tạo ra có thể được kiểm soát bằng đầu vào nhắc nhở, nên hành vi này tương tự như việc cung cấp cho người dùng quyền truy cập gián tiếp vào các chức năng bổ sung.

Insecure Output Handling - Xử lý đầu ra không an toàn khác với Overreliance - phụ thuộc quá mức ở chỗ nó xử lý các đầu ra do LLM tạo ra trước khi chúng được chuyển xuống phía dưới. Trong khi phụ thuộc quá mức thì tập trung vào những mối quan ngại xung quanh do phụ thuộc vào độ chính xác và tính phù hợp của các đầu ra LLM.

Khai thác thành công lỗ hổng Xử lý đầu ra không an toàn có thể dẫn đến XSS và CSRF trong trình duyệt web cũng như SSRF, leo thang đặc quyền hoặc thực thi mã từ xa trên các hệ thống phụ trợ.

Các điều kiện sau đây có thể làm tăng tác động của lỗ hổng này:
* Ứng dụng cấp các đặc quyền LLM vượt quá những gì dành cho người dùng cuối, cho phép leo thang các đặc quyền hoặc thực thi mã từ xa.
* Ứng dụng dễ bị tấn công tiêm lệnh nhắc gián tiếp, có thể cho phép kẻ tấn công có được quyền truy cập đặc quyền vào môi trường của người dùng mục tiêu.
* Các plugin của bên thứ 3 không xác thực đầy đủ các đầu vào.

### Các ví dụ phổ biến về lỗ hổng

1. Đầu ra LLM được nhập trực tiếp vào shell hệ thống hoặc hàm tương tự như exec hoặc eval, dẫn đến thực thi mã từ xa.
2. JavaScript hoặc Markdown được tạo bởi LLM và trả về cho người dùng. Sau đó, mã được trình duyệt diễn giải, dẫn đến XSS.

### Chiến lược phòng ngừa và giảm thiểu

1. Xử lý mô hình như bất kỳ người dùng nào khác, áp dụng phương pháp zerotrust và kiểm tra xác thực đầu vào phù hợp cho các phản hồi đến từ mô hình đến các hàm phụ trợ.
2. Thực hiện theo các hướng dẫn của OWASP ASVS (Tiêu chuẩn xác minh bảo mật ứng dụng) để đảm bảo xác thực và khử trùng đầu vào hiệu quả.
3. Mã hóa đầu ra của mô hình trở lại người dùng để giảm thiểu việc thực thi mã không mong muốn bằng JavaScript hoặc Markdown. OWASP ASVS cung cấp hướng dẫn chi tiết về mã hóa đầu ra.

### Ví dụ về các kịch bản tấn công

1. Một ứng dụng sử dụng plugin LLM để tạo phản hồi cho tính năng chatbot. Plugin này cũng cung cấp một số chức năng quản trị có thể truy cập được đối với một LLM đặc quyền khác. LLM mục đích chung sẽ trực tiếp chuyển phản hồi của mình, mà không cần xác thực đầu ra phù hợp, đến plugin khiến plugin phải tắt để bảo trì.
2. Người dùng sử dụng công cụ tóm tắt trang web do LLM cung cấp để tạo bản tóm tắt ngắn gọn của một bài viết. Trang web bao gồm một lệnh nhắc nhở hướng dẫn LLM thu thập nội dung nhạy cảm từ trang web hoặc từ cuộc trò chuyện của người dùng. Từ đó, LLM có thể mã hóa dữ liệu nhạy cảm và gửi dữ liệu đó, mà không cần xác thực đầu ra hoặc lọc, đến máy chủ do kẻ tấn công kiểm soát.
3. LLM cho phép người dùng tạo các truy vấn SQL cho cơ sở dữ liệu phụ trợ thông qua tính năng giống như trò chuyện. Người dùng yêu cầu truy vấn để xóa tất cả các bảng cơ sở dữ liệu. Nếu truy vấn được tạo từ LLM không được kiểm tra kỹ lưỡng, thì tất cả các bảng cơ sở dữ liệu sẽ bị xóa.
4. Một ứng dụng web sử dụng LLM để tạo nội dung từ lời nhắc văn bản của người dùng mà không cần kiểm tra đầu ra. Kẻ tấn công có thể gửi lời nhắc được tạo thủ công khiến LLM trả về một lệnh JavaScript dẫn đến XSS khi hiển thị trên trình duyệt của nạn nhân. Việc xác thực lời nhắc không đủ đã kích hoạt cuộc tấn công này.

### Liên kết tham khảo

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
