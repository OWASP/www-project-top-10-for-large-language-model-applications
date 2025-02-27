## LLM02:2025 Rò Rỉ Thông Tin Nhạy Cảm

### Mô Tả

Thông tin nhạy cảm có thể ảnh hưởng đến cả mô hình LLM và bối cảnh ứng dụng của nó. Điều này bao gồm thông tin nhận dạng cá nhân (PII), chi tiết tài chính, hồ sơ y tế, dữ liệu kinh doanh được bảo mật, thông tin xác thực bảo mật và tài liệu pháp lý. Các mô hình độc quyền cũng có thể có phương pháp đào tạo và mã nguồn độc quyền được coi là nhạy cảm, đặc biệt là trong các mô hình đóng hoặc mô hình nền tảng.

LLM, đặc biệt khi được tích hợp vào các ứng dụng, có nguy cơ tiết lộ dữ liệu nhạy cảm, thuật toán độc quyền hoặc chi tiết bảo mật thông qua đầu ra của chúng. Điều này có thể dẫn đến truy cập dữ liệu trái phép, vi phạm quyền riêng tư và lộ lọt tài sản trí tuệ. Người dùng cần hiểu cách tương tác an toàn với LLM và nhận thức được nguy cơ vô tình cung cấp dữ liệu nhạy cảm, dữ liệu này sau đó có thể bị lộ qua đầu ra của mô hình.

Để giảm thiểu rủi ro này, các ứng dụng LLM cần thực hiện các kỹ thuật làm sạch dữ liệu nhằm ngăn chặn dữ liệu người dùng lọt vào mô hình đào tạo. Chủ sở hữu ứng dụng cũng nên cung cấp chính sách Điều Khoản Sử Dụng rõ ràng, cho phép người dùng từ chối việc dữ liệu của họ được sử dụng để đào tạo mô hình. Việc áp dụng các hạn chế trong lệnh hệ thống về các loại dữ liệu mà LLM nên trả về có thể giúp giảm nguy cơ rò rỉ thông tin nhạy cảm. Tuy nhiên, các hạn chế này không phải lúc nào cũng được tuân thủ và có thể bị vượt qua bằng cách tiêm nhắc lệnh hoặc các phương pháp khác.


### Các Ví Dụ Phổ Biến Về Lỗ Hổng

#### 1. Rò rỉ thông tin nhận dạng cá nhân
Thông tin nhận dạng cá nhân (PII) có thể bị tiết lộ trong quá trình tương tác với LLM.
#### 2. Lộ Thuật Toán Độc Quyền
Cấu hình mô hình không hợp lý có thể làm lộ thuật toán hoặc dữ liệu độc quyền. Việc tiết lộ dữ liệu đào tạo có thể dẫn đến các cuộc tấn công đảo ngược mô hình, nơi kẻ tấn công có thể trích xuất thông tin nhạy cảm hoặc tái tạo dữ liệu đầu vào. Ví dụ, như trong cuộc tấn công 'Proof Pudding' (CVE-2019-20634), dữ liệu đào tạo bị lộ đã cho phép kẻ tấn công trích xuất mô hình, đảo ngược nó và vượt qua các cơ chế kiểm soát bảo mật của thuật toán máy học, bao gồm cả bộ lọc email.
#### 3. Rò Rỉ Dữ Liệu Kinh Doanh Nhạy Cảm
Các phản hồi được tạo ra có thể vô tình bao gồm thông tin kinh doanh được bảo mật.

### Chiến Lược Phòng Chống và Giảm Thiểu

#### Làm Sạch Dữ Liệu:

#### 1. Tích Hợp Kỹ Thuật Làm Sạch Dữ Liệu
Áp dụng các biện pháp làm sạch dữ liệu nhằm ngăn chặn dữ liệu người dùng lọt vào mô hình đào tạo. Bao gồm việc xóa hoặc che giấu nội dung nhạy cảm trước khi sử dụng cho quá trình đào tạo.
#### 2. Xác Thực Đầu Vào Mạnh Mẽ
Áp dụng các phương pháp xác thực đầu vào nghiêm ngặt để phát hiện và lọc dữ liệu nhạy cảm hoặc có hại, đảm bảo chúng không làm tổn hại đến mô hình.

#### Kiểm Soát Truy Cập:

#### 1. Thực Thi Kiểm Soát Truy Cập Nghiêm Ngặt
Hạn chế quyền truy cập vào dữ liệu nhạy cảm theo nguyên tắc đặc quyền tối thiểu. Chỉ cấp quyền truy cập vào dữ liệu cần thiết cho người dùng hoặc quy trình cụ thể.
#### 2. Hạn Chế Nguồn Dữ Liệu
Giới hạn quyền truy cập của mô hình vào các nguồn dữ liệu bên ngoài và đảm bảo điều phối dữ liệu thời gian thực được quản lý an toàn để tránh rò rỉ dữ liệu ngoài ý muốn.

#### Học Liên Kết và Kỹ Thuật Bảo Mật:

#### 1. Sử Dụng Học Liên Kết (Federated Learning)
Đào tạo mô hình bằng cách sử dụng dữ liệu phi tập trung trên nhiều máy chủ hoặc thiết bị khác nhau. Phương pháp này giúp giảm thiểu nhu cầu thu thập dữ liệu tập trung và giảm thiểu rủi ro lộ dữ liệu.
#### 2. Áp Dụng Bảo Mật Vi Sai (Differential Privacy)
Sử dụng các kỹ thuật thêm nhiễu vào dữ liệu hoặc đầu ra, khiến kẻ tấn công khó khăn hơn trong việc đảo ngược dữ liệu cá nhân.

#### Giáo Dục Người Dùng và Minh Bạch:

#### 1. Hướng Dẫn Người Dùng Về Cách Sử Dụng LLM An Toàn
Cung cấp hướng dẫn về cách tránh nhập thông tin nhạy cảm. Đào tạo người dùng về các phương pháp tương tác an toàn với LLM.
#### 2. Minh Bạch Trong Việc Sử Dụng Dữ Liệu
Duy trì chính sách rõ ràng về lưu trữ, sử dụng và xóa dữ liệu. Cho phép người dùng từ chối việc dữ liệu của họ được sử dụng trong quá trình đào tạo.

#### Cấu Hình Hệ Thống An Toàn:

#### 1. Ẩn Lệnh Hệ Thống
Hạn chế khả năng người dùng ghi đè hoặc truy cập vào cài đặt ban đầu của hệ thống, giảm nguy cơ lộ thông tin nội bộ.
#### 2. Tham Chiếu Các Thực Tiễn Cấu Hình Bảo Mật
Tuân theo các hướng dẫn như "OWASP API8:2023 Security Misconfiguration" để tránh rò rỉ thông tin nhạy cảm qua thông báo lỗi hoặc chi tiết cấu hình.
(Tham khảo:[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

#### Kỹ Thuật Nâng Cao:

#### 1. Mã Hóa Đồng Hình (Homomorphic Encryption)
Sử dụng mã hóa đồng hình để cho phép phân tích dữ liệu an toàn và học máy bảo mật, đảm bảo dữ liệu vẫn được bảo mật trong quá trình xử lý.
#### 2. Tokenization và Che Giấu Dữ Liệu
Sử dụng tokenization để xử lý trước và làm sạch thông tin nhạy cảm. Các kỹ thuật như khớp mẫu có thể phát hiện và che giấu nội dung bảo mật trước khi xử lý.

### Các Kịch Bản Tấn Công Ví Dụ

#### Kịch Bản #1: Lộ Dữ Liệu Không Chủ Ý
Một người dùng nhận được phản hồi chứa dữ liệu cá nhân của người khác do làm sạch dữ liệu không đầy đủ.
#### Kịch Bản #2: Tiêm Nhắc Lệnh Có Mục Tiêu
Kẻ tấn công vượt qua bộ lọc đầu vào để trích xuất thông tin nhạy cảm.
#### Kịch Bản #3: Rò Rỉ Dữ Liệu Qua Dữ Liệu Đào Tạo
Việc bao gồm dữ liệu không cẩn thận trong quá trình đào tạo dẫn đến rò rỉ thông tin nhạy cảm.

### Liên Kết Tham Khảo
1. [Những bài học rút ra từ sự cố rò rỉ dữ liệu Samsung của ChatGPT](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [Cuộc khủng hoảng rò rỉ dữ liệu AI: Công cụ mới ngăn chặn bí mật công ty bị đưa vào ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT tiết lộ dữ liệu nhạy cảm khi được yêu cầu lặp lại ‘Bài thơ’ mãi mãi](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Sử dụng Bảo mật Vi sai để Xây dựng Mô hình An toàn](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### Các Khung Phân Loại và Thuật Ngữ Liên Quan

Tham khảo phần này để có thông tin toàn diện, các kịch bản và chiến lược liên quan đến triển khai hạ tầng, kiểm soát môi trường ứng dụng và các phương pháp bảo mật tốt nhất.

- [AML.T0024.000 - Suy luận thành viên dữ liệu huấn luyện](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Đảo ngược mô hình máy học](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Trích xuất mô hình máy học](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**
