## LLM07:2025 Rò rỉ lời nhắc hệ thống

### Description

Lỗ hổng rò rỉ lời nhắc hệ thống trong mô hình LLM xảy ra khi các lời nhắc hệ thống hoặc hướng dẫn điều khiển hành vi của mô hình vô tình chứa thông tin nhạy cảm mà không được thiết kế để bị lộ. Các lời nhắc hệ thốn thường được sử dụng để định hướng đầu ra của mô hình theo yêu cầu ứng dụng, nhưng đôi khi có thể chứa thông tin quan trọng như thông tin xác thực, chuỗi kết nối, hoặc quy tắc bảo mật nội bộ. Nếu bị rò rỉ, thông tin này có thể bị khai thác để thực hiện các cuộc tấn công khác.

Điều quan trọng là lời nhắc hệ thống không nên được coi là bí mật hoặc một cơ chế kiểm soát bảo mật. Vì vậy, các dữ liệu nhạy cảm như thông tin đăng nhập, khóa API, hoặc cấu trúc quyền hạn không nên được nhúng trực tiếp trong nội dung của lời nhắc hệ thốn.

Tóm lại, rủi ro thực sự không nằm ở việc rò rỉ lời nhắc hệ thống mà là ở những vấn đề bảo mật cơ bản như lộ thông tin nhạy cảm, bỏ qua kiểm tra quyền hạn, hoặc thiết lập sai cơ chế phân quyền. Ngay cả khi không lấy được nội dung chính xác của lời nhắc hệ thống, kẻ tấn công vẫn có thể suy luận được các quy tắc bảo mật và hạn chế của hệ thống thông qua việc thử nghiệm và quan sát phản hồi của mô hình.

Tóm lại: Việc lộ chính lời nhắc hệ thống không phải là rủi ro bảo mật thực sự – mối đe dọa an ninh nằm ở các yếu tố bên dưới, chẳng hạn như rò rỉ thông tin nhạy cảm, vượt qua các rào cản hệ thống, phân tách quyền hạn không đúng cách, v.v. Ngay cả khi nội dung chính xác của lời nhắc hệ thống không bị tiết lộ, kẻ tấn công tương tác với hệ thống vẫn có thể suy luận ra nhiều rào cản bảo mật và quy tắc định dạng được thiết lập trong lời nhắc hệ thống thông qua quá trình sử dụng ứng dụng, gửi truy vấn đến mô hình và quan sát kết quả đầu ra.

### Common Examples of Risk

#### 1. Lộ chức năng nhạy cảm
  Lời nhắc hệ thống có thể tiết lộ thông tin nội bộ quan trọng như kiến trúc hệ thống, khóa API, thông tin đăng nhập cơ sở dữ liệu hoặc token người dùng. Kẻ tấn công có thể khai thác các thông tin này để xâm nhập trái phép vào ứng dụng.
  Ví dụ: Một system prompt tiết lộ loại cơ sở dữ liệu mà ứng dụng đang sử dụng có thể giúp hacker thực hiện tấn công SQL Injection..
#### 2. Rò rỉ các quy tắc nội bộ
  Lời nhắc hệ thống của ứng dụng tiết lộ thông tin về quy trình ra quyết định nội bộ – những thông tin lẽ ra cần được giữ bí mật. Điều này cho phép kẻ tấn công hiểu rõ hơn về cách ứng dụng hoạt động, từ đó lợi dụng các điểm yếu hoặc vượt qua các kiểm soát bảo mật.
  Ví dụ: Một ứng dụng ngân hàng có chatbot với lời nhắc hệ thống chứa thông tin như:
    >"Hạn mức giao dịch được đặt là $5000 mỗi ngày cho một người dùng. Tổng số tiền vay cho một người dùng là $10,000".
  Thông tin này có thể giúp kẻ tấn công vượt qua các kiểm soát bảo mật của ứng dụng như thực hiện giao dịch vượt quá hạn mức hoặc vượt quá giới hạn vay.
#### 3. Rò rỉ tiêu chí lọc nội dung
  Lời nhắc hệ thống có thể yêu cầu mô hình lọc hoặc từ chối nội dung nhạy cảm. Ví dụ, một lời nhắc hệ thống có thể là:
    >"Nếu người dùng yêu cầu thông tin về người dùng khác, luôn phản hồi bằng câu ‘Xin lỗi, tôi không thể hỗ trợ yêu cầu này'".
#### 4. Rò rỉ quyền truy cập và vai trò người dùng
  Lời nhắc hệ thống có thể tiết lộ cấu trúc vai trò nội bộ hoặc mức độ phân quyền trong ứng dụng.
  Ví dụ, lời nhắc có thể tiết lộ:
    >“Vai trò người dùng quản trị có toàn quyền chỉnh sửa thông tin người dùng”
  Nếu kẻ tấn công biết được cấu trúc phân quyền này, họ có thể tìm cách leo thang đặc quyền trong hệ thống.

### Chiến lược phòng ngừa và giảm thiểu rủi ro

#### 1. Tách biệt dữ liệu nhạy cảm khỏi lời nhắc hệ thống
  Tránh chèn thông tin nhạy cảm (như API key, khóa xác thực, tên cơ sở dữ liệu, vai trò người dùng, cấu trúc phân quyền...) vào trong lời nhắc hệ thống. Thay vào đó, hãy đưa các dữ liệu này vào các hệ thống mà LLM không truy cập trực tiếp được.
#### 2. Tránh phụ thuộc vào lời nhắc hệ thống để kiểm soát hành vi nghiêm ngặt
  Do LLM dễ bị tấn công như prompt injection, có thể làm thay đổi nội dung lời nhắc hệ thống, nên nên hạn chế dùng lời nhắc để kiểm soát hành vi của mô hình. Thay vào đó, nên dựa vào các hệ thống bên ngoài LLM để đảm bảo hành vi đúng. Ví dụ, việc phát hiện và ngăn chặn nội dung độc hại nên do hệ thống bên ngoài xử lý.
#### 3. Áp dụng các rào chắn bảo mật (guardrails)
  Xây dựng hệ thống kiểm soát bên ngoài LLM. Mặc dù việc huấn luyện mô hình để không tiết lộ lời nhắc hệ thống có thể hiệu quả phần nào, nhưng không đảm bảo tuyệt đối. Một hệ thống độc lập kiểm tra đầu ra để đảm bảo mô hình tuân thủ yêu cầu sẽ hiệu quả hơn là chỉ dựa vào lời nhắc hệ thống.
#### 4. Đảm bảo các kiểm soát bảo mật được thực thi độc lập với LLM
  Các kiểm soát quan trọng như phân tách đặc quyền, kiểm tra giới hạn quyền truy cập... không nên được ủy quyền cho LLM – dù là thông qua lời nhắc hệ thống hay cách khác. Các kiểm soát này cần được thực thi theo cách xác định, có thể kiểm toán. Nếu có nhiều cấp độ truy cập khác nhau, nên sử dụng nhiều tác nhân (agent) riêng biệt, mỗi tác nhân chỉ được cấp quyền tối thiểu cần thiết để thực hiện nhiệm vụ.

### Kịch bản tấn công minh họa

#### Kịch bản #1
   Một LLM có lời nhắc hệ thống chứa thông tin đăng nhập cho một công cụ mà nó được cấp quyền truy cập. Khi lời nhắc này bị rò rỉ, kẻ tấn công có thể sử dụng các thông tin này cho mục đích khác.
#### Kịch bản #2
  Một LLM có lời nhắc hệ thống cấm tạo nội dung xúc phạm, chèn liên kết ngoài và thực thi mã. Kẻ tấn công trích xuất được lời nhắc hệ thống, sau đó thực hiện tấn công prompt injection để vượt qua các giới hạn này, dẫn đến khả năng thực thi mã từ xa.

### Tài liệu tham khảo

1. [Rò rỉ Lời nhắc hệ thống - SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Rò rỉ Lời nhắc - Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [Lời nhắc hệ thống ChatGPT - chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [Tổng hợp lời nhắc hệ thống bị rò rỉ - leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [Lời nhắc hệ thống chế độ giọng nói nâng cao của OpenAI  - OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Khung và phân loại liên quan

Tham khảo mục này để có cái nhìn tổng thể về các chiến lược triển khai hạ tầng, kiểm soát môi trường áp dụng và các thực tiễn tốt nhất khác:

- [AML.T0051.000 - Tiêm lời nhắc LLM: Trực tiếp (Trích xuất lời nhắc meta)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
