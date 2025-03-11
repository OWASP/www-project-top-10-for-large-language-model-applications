## LLM01:2025 Tấn công tiêm nhắc lệnh

### Mô tả

Lỗ hổng Tấn công tiêm nhắc lệnh (Prompt Injection Vulnerability) xảy ra khi đầu vào của người dùng thay đổi hành vi hoặc đầu ra của mô hình ngôn ngữ lớn (LLM) theo cách không mong muốn. Những đầu vào này có thể ảnh hưởng đến mô hình ngay cả khi chúng không thể nhận biết bằng mắt thường, do đó nên tấn công tiêm nhắc lệnh không nhất thiết phải hiển thị hay đọc được bởi con người, miễn là nội dung được mô hình phân tích.

Các lỗ hổng Tiêm nhắc lệnh tồn tại do cách mô hình xử lý lời nhắc (prompt) và cách truyền đầu vào có thể buộc mô hình truyền dữ liệu lời nhắc không chính xác đến các phần khác của mô hình, từ đó có khả năng khiến mô hình vi phạm nguyên tắc, tạo ra nội dung độc hại, cho phép truy cập trái phép hoặc ảnh hưởng đến các quyết định quan trọng. Mặc dù các kỹ thuật như Tạo tăng cường truy xuất (Retrieval-Augmented Generation - RAG) và tinh chỉnh (fine-tuning) nhằm mục đích làm cho đầu ra của mô hình ngôn ngữ lớn (LLM) trở nên phù hợp và chính xác hơn, nghiên cứu cho thấy rằng chúng không thể hoàn toàn khắc phục các lỗ hổng tiêm nhắc lệnh.

Tấn công tiêm nhắc lệnh và bẻ khóa (jailbreak) là hai khái niệm liên quan trong bảo mật LLM và thường bị sử dụng thay thế nhau. Tấn công tiêm nhắc lệnh liên quan đến việc thao túng phản hồi của mô hình bằng đầu vào cụ thể để thay đổi hành vi của nó, bao gồm cả việc vượt qua các biện pháp an toàn. Bẻ khóa là một dạng Tấn công tiêm nhắc lệnh trong đó kẻ tấn công cung cấp đầu vào khiến mô hình bỏ qua hoàn toàn các giao thức an toàn. Các nhà phát triển có thể xây dựng cơ chế bảo vệ thông qua hệ thống prompt và kiểm soát đầu vào, nhưng để ngăn chặn hiệu quả việc bẻ khóa, cần cập nhật liên tục dữ liệu huấn luyện và cơ chế bảo mật của mô hình.

(Note: trong tài liệu của OWASP họ sử dụng từ jailbreak, tuy nhiên trong ngữ cảnh tiếng Việt có thể hiểu như sau:
"Jailbreak" có thể được dịch theo nhiều cách tùy vào ngữ cảnh:
- Bẻ khóa – Thường dùng trong ngữ cảnh thiết bị di động, như "bẻ khóa iPhone" để chỉ việc vượt qua các hạn chế của hệ điều hành.
- Vượt rào bảo mật – Thường dùng khi nói về việc khai thác lỗ hổng trong mô hình AI để vượt qua các hạn chế bảo mật.
- Phá vỡ giới hạn – Dùng trong ngữ cảnh bypass các kiểm soát hoặc cơ chế an toàn trong mô hình ngôn ngữ lớn (LLM).
- Tấn công vượt kiểm soát – Dùng trong AI Security khi chỉ các kỹ thuật buộc mô hình LLM tạo ra đầu ra không mong muốn.)

### Các dạng tấn công tiêm nhắc lệnh

#### Tấn công tiêm nhắc lệnh trực tiếp
Tấn công tiêm nhắc lệnh trực tiếp xảy ra khi đầu vào của người dùng trực tiếp thay đổi hành vi của mô hình theo những cách ngoài ý muốn hoặc không mong đợi. Đầu vào này có thể là:

- Cố ý: Kẻ tấn công cố tình tạo ra một lời nhắc nhằm khai thác lỗ hổng của mô hình.
- Vô ý: Người dùng vô tình nhập một lời nhắc dẫn đến hành vi không mong đợi.

#### Tấn công tiêm nhắc lệnh gián tiếp
Tấn công tiêm nhắc lệnh gián tiếp xảy ra khi một mô hình ngôn ngữ lớn (LLM) nhận đầu vào từ các nguồn bên ngoài, chẳng hạn như trang web hoặc tệp tin. Nội dung từ các nguồn này có thể chứa dữ liệu mà khi mô hình diễn giải, nó sẽ làm thay đổi hành vi của mô hình theo những cách ngoài ý muốn hoặc không mong đợi. Tương tự như tấn công trực tiếp, tấn công gián tiếp cũng có thể là:

- Cố ý: Nội dung bên ngoài được thiết kế để khai thác mô hình.
- Vô ý: Nội dung vô tình chứa thông tin gây ra thay đổi không mong muốn trong mô hình.

Mức độ nghiêm trọng và bản chất của tác động từ một cuộc tấn công tiêm nhắc lệnh thành công có thể khác nhau đáng kể, tùy thuộc vào bối cảnh kinh doanh mà mô hình hoạt động cũng như cách mô hình được thiết kế. Tuy nhiên, nhìn chung, tấn công tiêm nhắc lệnh có thể dẫn đến những hậu quả ngoài ý muốn, bao gồm nhưng không giới hạn:

- Rò rỉ thông tin nhạy cảm
- Tiết lộ thông tin quan trọng về cơ sở hạ tầng hệ thống AI hoặc các lời nhắc hệ thống
- Thao túng nội dung, dẫn đến đầu ra sai lệch hoặc thiên vị
- Cấp quyền truy cập trái phép vào các chức năng của mô hình ngôn ngữ lớn (LLM)
- Thực thi các lệnh tùy ý trên các hệ thống được kết nối
- Gây ảnh hưởng đến các quá trình ra quyết định quan trọng

Sự phát triển của AI đa phương thức (multimodal AI), vốn xử lý đồng thời nhiều loại dữ liệu khác nhau, cũng làm gia tăng rủi ro của tấn công tiêm nhắc lệnh. Kẻ tấn công có thể khai thác sự tương tác giữa các chế độ dữ liệu, chẳng hạn như ẩn các hướng dẫn độc hại trong hình ảnh đi kèm với văn bản vô hại. Độ phức tạp của các hệ thống này mở rộng bề mặt tấn công, khiến mô hình đa phương thức có thể dễ bị tấn công chéo giữa các chế độ dữ liệu, điều mà các kỹ thuật bảo mật hiện tại khó phát hiện và ngăn chặn. Do đó, phát triển các biện pháp bảo vệ chuyên biệt cho AI đa phương thức là một lĩnh vực quan trọng cần được nghiên cứu và cải tiến thêm.

### Chiến lược Phòng chống và Giảm thiểu

Các lỗ hổng tấn công tiêm nhắc lệnh tồn tại do bản chất của AI tạo sinh. Do ảnh hưởng ngẫu nhiên trong cách các mô hình hoạt động, chưa có phương pháp nào được chứng minh là có thể ngăn chặn hoàn toàn tấn công tiêm nhắc lệnh. Tuy nhiên, các biện pháp sau có thể giúp giảm thiểu tác động của loại tấn công này:

#### 1. Hạn chế hành vi của mô hình
Cung cấp hướng dẫn cụ thể về vai trò, khả năng và giới hạn của mô hình trong lời nhắc hệ thống. Buộc mô hình tuân thủ chặt chẽ ngữ cảnh, giới hạn phản hồi trong các nhiệm vụ hoặc chủ đề cụ thể, đồng thời hướng dẫn mô hình bỏ qua các yêu cầu thay đổi hướng dẫn cốt lõi.
#### 2. Xác định và xác thực định dạng đầu ra mong đợi
Xác định rõ ràng định dạng đầu ra, yêu cầu mô hình cung cấp lập luận chi tiết và trích dẫn nguồn gốc. Sử dụng mã xác định (deterministic code) để kiểm tra việc tuân thủ các định dạng này.
#### 3. Lọc đầu vào và đầu ra
Xác định các danh mục nội dung nhạy cảm và thiết lập quy tắc để nhận diện và xử lý những nội dung đó. Áp dụng bộ lọc ngữ nghĩa và kiểm tra chuỗi văn bản để phát hiện nội dung không được phép. Đánh giá phản hồi bằng Tam giác RAG:

Đánh giá mức độ phù hợp của ngữ cảnh,
Kiểm tra tính có căn cứ,
Xác minh tính liên quan của câu hỏi và câu trả lời để phát hiện các đầu ra tiềm ẩn nguy hiểm.
#### 4. Kiểm soát quyền hạn và áp dụng nguyên tắc ít quyền nhất
Cung cấp cho ứng dụng các API token riêng để mở rộng chức năng, thay vì cấp trực tiếp cho mô hình. Xử lý các chức năng quan trọng trong mã nguồn thay vì để mô hình đảm nhiệm. Hạn chế quyền truy cập của mô hình đến mức tối thiểu cần thiết cho hoạt động dự kiến.
#### 5. Yêu cầu sự chấp thuận của con người đối với các hành động có rủi ro cao
Triển khai kiểm soát con người trong vòng lặp (human-in-the-loop) đối với các thao tác đặc quyền nhằm ngăn chặn hành động trái phép.
#### 6. Phân tách và nhận diện nội dung bên ngoài
Tách biệt và đánh dấu rõ ràng nội dung không đáng tin cậy để hạn chế ảnh hưởng của nó đối với lời nhắc của người dùng.
#### 7. Kiểm tra tấn công và mô phỏng vi phạm
Thực hiện kiểm tra xâm nhập (penetration testing) và mô phỏng vi phạm (breach simulations) thường xuyên, coi mô hình như một người dùng không đáng tin cậy để kiểm tra hiệu quả của các ranh giới bảo mật và kiểm soát truy cập.

### Các Kịch Bản Tấn Công Mẫu

#### Kịch bản #1: Tiêm nhắc lệnh trực tiếp
Kẻ tấn công chèn một nhắc lệnh vào chatbot hỗ trợ khách hàng, yêu cầu nó bỏ qua hướng dẫn trước đó, truy vấn kho dữ liệu riêng tư và gửi thư điện tử, dẫn đến truy cập trái phép và leo thang đặc quyền.
#### Kịch bản #2: Tiêm nhắc lệnh gián tiếp
Người dùng sử dụng LLM để tóm tắt một trang web có chứa hướng dẫn ẩn. Khi LLM xử lý trang này, nó chèn một hình ảnh liên kết đến URL, làm rò rỉ nội dung cuộc trò chuyện riêng tư.
#### Kịch bản #3: Tiêm nhắc lệnh không chủ ý
Một công ty thêm một hướng dẫn vào mô tả công việc để nhận diện đơn ứng tuyển do AI tạo ra. Một ứng viên, không biết điều này, sử dụng LLM để tối ưu hóa CV của mình, vô tình kích hoạt cơ chế phát hiện AI.
#### Kịch bản #4: Tác động có chủ đích đến mô hình
Kẻ tấn công chỉnh sửa tài liệu trong kho dữ liệu mà ứng dụng RAG sử dụng. Khi người dùng truy vấn, nội dung đã bị chỉnh sửa làm thay đổi đầu ra của LLM, dẫn đến kết quả sai lệch hoặc gây hiểu nhầm.
#### Kịch bản #5: Tiêm mã độc
Kẻ tấn công khai thác lỗ hổng bảo mật (CVE-2024-5184) trong trợ lý thư điện tử tích hợp LLM để chèn nhắc lệnh độc hại, cho phép truy cập thông tin nhạy cảm và thao túng nội dung thư điện tử.
#### Kịch bản #6: Chia nhỏ tải trọng (Payload Splitting)
Kẻ tấn công tải lên một CV có chứa các nhắc lệnh độc hại được chia nhỏ. Khi LLM đánh giá ứng viên, các nhắc lệnh này kết hợp lại, khiến mô hình đưa ra đánh giá tích cực không chính xác, dù nội dung thực tế của CV không đạt yêu cầu.
#### Kịch bản #7: Tiêm nhắc lệnh đa phương thức
Kẻ tấn công nhúng nhắc lệnh độc hại vào hình ảnh kèm theo văn bản hợp lệ. Khi AI đa phương thức xử lý đồng thời hình ảnh và văn bản, nhắc lệnh ẩn này thay đổi hành vi của mô hình, có thể dẫn đến hành động trái phép hoặc rò rỉ thông tin nhạy cảm.
#### Kịch bản #8: Hậu tố đối kháng (Adversarial Suffix)
Kẻ tấn công thêm một chuỗi ký tự tưởng như vô nghĩa vào cuối nhắc lệnh, nhưng nó lại tác động đến đầu ra của LLM theo cách độc hại, vượt qua các biện pháp an toàn.
#### Kịch bản #9: Tấn công đa ngôn ngữ/giấu mã (Multilingual/Obfuscated Attack)
Kẻ tấn công sử dụng nhiều ngôn ngữ hoặc mã hóa nhắc lệnh độc hại (ví dụ: Base64, emoji) để né tránh bộ lọc và thao túng hành vi của LLM.

### Liên kết tham khảo

1. [Lỗ hổng Plugin ChatGPT - Trò chuyện với Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [Giả Mạo Yêu Cầu Giữa Các Plugin của ChatGPT và Tấn Công Tiêm Nhắc Lệnh](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Không Như Những Gì Bạn Đăng Ký: Xâm Phạm Ứng Dụng Tích Hợp LLM Thực Tế Bằng Tấn Công Tiêm Nhắc Lệnh Gián Tiếp](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Bảo vệ ChatGPT khỏi Tấn Công Jailbreak bằng Cơ Chế Tự Nhắc Nhở](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Tấn công Tiêm Nhắc Lệnh vào Ứng Dụng Tích Hợp LLM](https://arxiv.org/abs/2306.05499) **Đại học Cornell**
6. [Inject My PDF: Tấn công Tiêm Nhắc Lệnh vào Sơ Yếu Lý Lịch của Bạn](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Không như những gì bạn đã đăng ký: Xâm phạm các ứng dụng tích hợp LLM trong thực tế bằng Tấn công Tiêm Nhắc Lệnh Gián Tiếp](https://arxiv.org/pdf/2302.12173.pdf) **Đại học Cornell**
9. [Mô hình hóa mối đe dọa cho các ứng dụng LLM](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Giảm tác động của các cuộc tấn công tiêm nhắc lệnh thông qua thiết kế](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Học máy đối kháng: Phân loại và thuật ngữ về các cuộc tấn công và biện pháp giảm thiểu (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 Khảo sát về các cuộc tấn công vào mô hình Ngôn ngữ-Thị giác lớn: Nguồn lực, tiến bộ và xu hướng tương lai (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Khai thác hành vi lập trình của LLMs: Sử dụng kép thông qua các cuộc tấn công bảo mật tiêu chuẩn](https://ieeexplore.ieee.org/document/10579515)
14. [Các cuộc tấn công đối kháng phổ quát và có thể chuyển giao trên các mô hình ngôn ngữ được căn chỉnh (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [Từ ChatGPT đến ThreatGPT: Tác động của AI tạo sinh đối với an ninh mạng và quyền riêng tư (arxiv.org)](https://arxiv.org/abs/2307.00691)

### Các Khung Phân Loại và Thuật Ngữ Liên Quan

Tham khảo phần này để có thông tin toàn diện, các kịch bản và chiến lược liên quan đến triển khai hạ tầng, kiểm soát môi trường áp dụng và các phương pháp tốt nhất khác.

- [AML.T0051.000 - Tiêm nhắc lệnh LLM: Trực tiếp](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - Tiêm nhắc lệnh LLM: Gián tiếp](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - Tiêm nhắc lệnh vượt rào LLM: Trực tiếp](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
