## LLM08: Excessive Agency

### Mô tả

Hệ thống dựa trên LLM thường được nhà phát triển cấp một mức độ đại lý - khả năng giao tiếp với các hệ thống khác và thực hiện các hành động để phản hồi lời nhắc. Quyết định về việc gọi hàm nào cũng có thể được giao cho một 'đại lý' LLM để xác định động dựa trên lời nhắc đầu vào hoặc đầu ra LLM.

Excessive Agency - Quá mức quyền lực là lỗ hổng cho phép thực hiện các hành động gây hại dựa trên các kết quả đầu ra không mong đợi hoặc sự mơ hồ từ một mô hình ngôn ngữ lớn (LLM), bất kể nguyên nhân gây ra sự cố của LLM là gì, như ảo tưởng (hallucination) hoặc sự tưởng tượng sai (confabulation), tiêm nhiễm hướng dẫn trực tiếp hoặc gián tiếp, plugin độc hại, các hướng dẫn vô hại nhưng thiết kế kém, hoặc chỉ đơn giản là một mô hình hoạt động kém. Nguyên nhân gốc rễ của quá mức quyền lực thường là một hoặc nhiều yếu tố sau: chức năng quá mức, quyền hạn quá mức hoặc sự tự chủ quá mức. Điều này khác với Insecure Output Handling, lỗ hổng liên quan đến việc thiếu sự xem xét kỹ lưỡng đối với các đầu ra của LLM.

Quá mức quyền lực có thể dẫn đến nhiều tác động khác nhau trên phạm vi tính bảo mật, toàn vẹn và khả dụng, và phụ thuộc vào hệ thống mà ứng dụng dựa trên LLM có thể tương tác.

### Các ví dụ phổ biến về lỗ hổng

1. Chức năng quá mức: Một tác nhân LLM có quyền truy cập vào các plugin bao gồm các chức năng cho hoạt động dự định của hệ thống. Ví dụ, một nhà phát triển cần cấp cho LLM khả năng đọc tài liệu từ kho lưu trữ, nhưng plugin của bên thứ 3 mà họ chọn sử dụng cũng bao gồm khả năng sửa đổi và xóa tài liệu.
2. Chức năng quá mức: Một plugin có thể đã được dùng thử trong giai đoạn phát triển và bị loại bỏ để thay thế bằng một giải pháp thay thế tốt hơn, nhưng plugin gốc vẫn có sẵn cho LLM sử dụng.
3. Chức năng quá mức: Một plugin LLM có chức năng mở không lọc đúng các lệnh nhập cho các lệnh nằm ngoài phạm vi cần thiết cho hoạt động dự định của ứng dụng. Ví dụ: một plugin để chạy một lệnh shell cụ thể không ngăn chặn đúng các lệnh shell khác được thực thi.
4. Quyền quá mức: Một plugin LLM có các quyền trên các hệ thống khác không cần thiết cho hoạt động dự định của ứng dụng. Ví dụ: một plugin có mục đích đọc dữ liệu kết nối với máy chủ cơ sở dữ liệu nhưng plugin đó không chỉ có quyền SELECT mà còn có các quyền UPDATE, INSERT và DELETE.
5. Quyền quá mức: Một plugin LLM được thiết kế để thực hiện các hoạt động thay mặt cho người dùng truy cập vào các hệ thống phía dưới với danh tính chung có đặc quyền cao. Ví dụ: một plugin để đọc kho tài liệu của người dùng hiện tại kết nối với kho tài liệu bằng một tài khoản có đặc quyền có quyền truy cập vào tất cả các tệp của người dùng.
6. Quyền tự chủ quá mức: Ứng dụng hoặc plugin dựa trên LLM không thể xác minh và chấp thuận độc lập các hành động có tác động cao. Ví dụ: plugin cho phép xóa tài liệu của người dùng thực hiện xóa mà không có bất kỳ xác nhận nào từ người dùng.

### Chiến lược phòng ngừa và giảm thiểu

Các hành động sau đây có thể ngăn chặn quyền quá mức:

1. Giới hạn các plugin/công cụ mà các tác nhân LLM được phép gọi chỉ ở mức tối thiểu các chức năng cần thiết. Ví dụ, nếu một hệ thống dựa trên LLM không yêu cầu khả năng lấy nội dung của URL thì không nên cung cấp plugin như vậy cho tác nhân LLM.
2. Giới hạn các chức năng được triển khai trong plugin/công cụ LLM ở mức tối thiểu cần thiết. Ví dụ, một plugin truy cập hộp thư của người dùng để tóm tắt email có thể chỉ yêu cầu khả năng đọc email, do đó plugin không nên chứa các chức năng khác như xóa hoặc gửi tin nhắn.
3. Tránh các chức năng mở khi có thể (ví dụ: chạy lệnh shell, lấy URL, v.v.) và sử dụng plugin/công cụ có chức năng chi tiết hơn. Ví dụ: ứng dụng dựa trên LLM có thể cần ghi một số đầu ra vào tệp. Nếu điều này được triển khai bằng cách sử dụng plugin để chạy hàm shell thì phạm vi cho các hành động không mong muốn là rất lớn (bất kỳ lệnh shell nào khác đều có thể được thực thi). Một giải pháp thay thế an toàn hơn là xây dựng plugin ghi tệp chỉ có thể hỗ trợ chức năng cụ thể đó.
4. Giới hạn các quyền mà plugin/công cụ LLM được cấp cho các hệ thống khác ở mức tối thiểu cần thiết để hạn chế phạm vi các hành động không mong muốn. Ví dụ, một tác nhân LLM sử dụng cơ sở dữ liệu sản phẩm để đưa ra khuyến nghị mua hàng cho khách hàng có thể chỉ cần quyền truy cập đọc vào bảng 'sản phẩm'; nó không được phép truy cập vào các bảng khác cũng như không được phép chèn, cập nhật hoặc xóa bản ghi. Điều này phải được thực thi bằng cách áp dụng các quyền cơ sở dữ liệu phù hợp cho danh tính mà plugin LLM sử dụng để kết nối với cơ sở dữ liệu.
5. Theo dõi quyền hạn và phạm vi bảo mật của người dùng để đảm bảo rằng các hành động thực hiện thay mặt cho người dùng được thực hiện trên các hệ thống trong ngữ cảnh của người dùng cụ thể đó và với các quyền hạn tối thiểu cần thiết. Ví dụ: một plugin LLM đọc kho lưu trữ mã của người dùng phải yêu cầu người dùng xác thực qua OAuth và với phạm vi tối thiểu được yêu cầu.
6. Sử dụng kiểm soát vòng lặp con người để yêu cầu con người phê duyệt tất cả các hành động trước khi chúng được thực hiện. Điều này có thể được triển khai trong hệ thống hạ lưu (ngoài phạm vi ứng dụng LLM) hoặc trong chính plugin/công cụ LLM. Ví dụ: ứng dụng dựa trên LLM tạo và đăng nội dung phương tiện truyền thông xã hội thay mặt cho người dùng nên bao gồm một quy trình phê duyệt của người dùng trong plugin/công cụ/API triển khai hoạt động 'đăng'.
7. Triển khai ủy quyền trong các hệ thống phía dưới thay vì dựa vào LLM để quyết định xem một hành động có được phép hay không. Khi triển khai các công cụ/plugin, hãy thực thi nguyên tắc trung gian hoàn chỉnh để tất cả các yêu cầu được thực hiện với các hệ thống phía dưới thông qua các plugin/công cụ đều được xác thực theo các chính sách bảo mật.

Các tùy chọn sau đây sẽ không ngăn chặn được quyền quá mức, nhưng có thể hạn chế mức độ thiệt hại gây ra:

1. Ghi nhật ký và giám sát hoạt động của các plugin/công cụ LLM và các hệ thống để xác định nơi diễn ra các hành động không mong muốn và phản hồi phù hợp.
2. Triển khai giới hạn tỷ lệ để giảm số lượng các hành động không mong muốn có thể diễn ra trong một khoảng thời gian nhất định, tăng cơ hội phát hiện ra các hành động không mong muốn thông qua giám sát trước khi thiệt hại đáng kể có thể xảy ra.

### Ví dụ về kịch bản tấn công

Ứng dụng trợ lý cá nhân dựa trên LLM được cấp quyền truy cập vào hộp thư của một cá nhân thông qua một plugin để tóm tắt nội dung của email đến. Để đạt được chức năng này, plugin email yêu cầu khả năng đọc tin nhắn, tuy nhiên plugin mà nhà phát triển hệ thống đã chọn sử dụng cũng chứa các chức năng để gửi tin nhắn. LLM dễ bị tấn công tiêm nhắc gián tiếp, theo đó một email đến được tạo ra một cách độc hại sẽ lừa LLM ra lệnh cho plugin email gọi hàm 'gửi tin nhắn' để gửi thư rác từ hộp thư của người dùng. Điều này có thể tránh được bằng cách:
(a) loại bỏ chức năng không cần thiết bằng cách sử dụng plugin chỉ cung cấp khả năng đọc thư,
(b) loại bỏ các quyền không cần thiết bằng cách xác thực với dịch vụ email của người dùng thông qua phiên OAuth có phạm vi chỉ đọc và/hoặc
(c) loại bỏ quyền tự chủ quá mức bằng cách yêu cầu người dùng xem xét thủ công và nhấn 'gửi' trên mọi email được plugin LLM soạn thảo.
Ngoài ra, thiệt hại gây ra có thể được giảm thiểu bằng cách triển khai giới hạn tốc độ trên giao diện gửi thư.

### Tham khảo

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
2. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): **Langchain Documentation**
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
