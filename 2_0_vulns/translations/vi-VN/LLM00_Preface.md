## Thư Ngỏ từ Người Phụ Trách Dự Án

Danh sách OWASP Top 10 cho Các Ứng dụng Mô hình Ngôn ngữ Lớn (LLM) bắt đầu vào năm 2023 như một nỗ lực do cộng đồng thúc đẩy nhằm nêu bật và giải quyết các vấn đề bảo mật cụ thể cho các ứng dụng AI. Từ thời điểm đó, công nghệ AI đã tiếp tục lan rộng khắp các ngành và các ứng dụng, và các rủi ro đi kèm cũng vậy. Khi các Mô hình Ngôn ngữ lớn được tích hợp sâu hơn vào mọi thứ từ tương tác với khách hàng đến hoạt động nội bộ, các nhà phát triển và chuyên gia bảo mật đang phát hiện ra những lỗ hổng mới—và các cách để chống lại chúng.

Danh sách năm 2023 là một thành công lớn trong việc nâng cao nhận thức và xây dựng nền tảng cho việc sử dụng LLM an toàn, nhưng chúng tôi đã học được nhiều hơn kể từ đó. Trong phiên bản mới năm 2025 này, chúng tôi đã làm việc với một nhóm cộng tác viên lớn hơn, đa dạng hơn trên toàn thế giới, họ đã giúp định hình danh sách này. Quá trình này bao gồm các buổi lên ý tưởng, bỏ phiếu và phản hồi thực tế từ các chuyên gia trong lĩnh vực bảo mật ứng dụng LLM, dù là bằng cách đóng góp hay tinh chỉnh các mục đó thông qua phản hồi. Mỗi ý kiến đều rất quan trọng để làm cho phiên bản mới này toàn diện và thiết thực nhất có thể.

### Những Điểm Mới trong OWASP Top 10 năm 2025

Danh sách năm 2025 phản ánh sự hiểu biết tốt hơn về các rủi ro hiện có và giới thiệu các cập nhật quan trọng về cách LLM được sử dụng trong các ứng dụng thực tế ngày nay. Ví dụ, Tiêu thụ Không Giới Hạn (Unbounded Consumption) mở rộng từ khái niệm trước đây là Từ chối Dịch vụ (Denial of Service) để bao gồm cả các rủi ro liên quan đến quản lý tài nguyên và chi phí bất ngờ—một vấn đề cấp bách trong việc triển khai LLM quy mô lớn.

Mục Vector và Nhúng (Vector and Embeddings) phản hồi yêu cầu từ cộng đồng về hướng dẫn bảo mật cho Tạo tăng cường truy xuất (Retrieval-Augmented Generation) và các phương pháp dựa trên nhúng khác, hiện đang là các hoạt động cốt lõi để làm cơ sở cho đầu ra của mô hình.

Chúng tôi cũng đã thêm mục Rò rỉ Tệp Lệnh Hệ Thống (System Prompt Leakage) để giải quyết một lĩnh vực có các lỗ hổng bị khai thác trong thực tế đã được cộng đồng yêu cầu rất nhiều. Nhiều ứng dụng cho rằng tệp lệnh được cách ly an toàn, nhưng các sự cố gần đây đã cho thấy các nhà phát triển không thể giả định một cách an toàn rằng thông tin trong những tệp lệnh này sẽ luôn được giữ bí mật.

Mục Quyền tự chủ quá mức (Excessive Agency) đã được mở rộng do việc suwer dụng ngày các nhiều các kiến trúc mang tính tác nhân có thể cấp cho LLM nhiều quyền tự chủ hơn. Khi các LLM hoạt động như tác nhân độc lập hoặc trong cài đặt plug-in, các quyền không được kiểm soát có thể dẫn đến các hành động ngoài ý muốn hoặc rủi ro, làm cho mục này trở nên quan trọng hơn bao giờ hết.

### Hướng Đi Sắp Tới

Cũng như bản thân công nghệ này, danh sách này là thành quả từ những góc nhìn và kinh nghiệm từ cộng đồng mã nguồn mở. Nó đã được hình thành bởi sự đóng góp từ các nhà phát triển, nhà khoa học dữ liệu và chuyên gia bảo mật trong khắp các lĩnh vực, tất cả đều cam kết xây dựng các ứng dụng AI an toàn hơn. Chúng tôi tự hào chia sẻ phiên bản 2025 này với bạn, và chúng tôi hy vọng rằng nó sẽ cung cấp cho bạn các công cụ và kiến thức để bảo mật LLM một cách hiệu quả.

Cảm ơn tất cả những ai đã đóng góp để tạo nên tài liệu này, và những người vẫn đang tiếp tục sử dụng và cải tiến nó. Chúng tôi rất biết ơn khi được đồng hành cùng bạn trong công việc này.

#### Steve Wilson
Phụ Trách Dự Án
OWASP Top 10 cho Các Ứng Dụng Mô Hình Ngôn Ngữ Lớn
LinkedIn: https://www.linkedin.com/in/wilsonsd/

#### Ads Dawson
Phụ Trách Kỹ Thuật & Phụ Trách Danh Mục Lỗ Hổng Bảo Mật
OWASP Top 10 cho Các Ứng Dụng Mô Hình Ngôn Ngữ Lớn
LinkedIn: https://www.linkedin.com/in/adamdawson0/

### Nhóm Dịch Thuật Tiếng Việt

#### Anh Ta
LinkedIn: https://www.linkedin.com/in/qta1014/

#### Name2
LinkedIn: 

### Về bản dịch này
Nhận thức được tính chuyên môn và mức độ quan trọng của OWASP Top 10 cho Các ứng dụng Mô hình Ngôn ngữ lớn, chúng tôi đã chủ động lựa chọn chỉ sử dụng người dịch trong quá trình thực hiện bản dịch này. Những dịch giả được liệt kê trên đây không chỉ có kiến thức kỹ thuật sâu sắc về nội dung bản gốc, mà còn có trình độ ngôn ngữ cần thiết để đảm bảo bản dịch thành công. 

#### Talesh Seeparsan
Phụ Trách Dịch Thuật
OWASP Top 10 cho Các Ứng Dụng Mô Hình Ngôn Ngữ Lớn
LinkedIn: https://www.linkedin.com/in/talesh/
