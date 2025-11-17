## LLM06:2025 Excessive Agency

### Mô tả

Hệ thống dựa trên LLM thường được cấp một mức độ quyền hạn nhất định bởi nhà phát triển - khả năng gọi các hàm hoặc giao tiếp với các hệ thống khác thông qua các phần mở rộng (đôi khi được gọi là công cụ, kỹ năng hoặc plugin bởi các nhà cung cấp khác nhau) để thực hiện hành động theo yêu cầu đầu vào. Quyết định chọn phần mở rộng nào có thể được giao cho một "tác nhân" LLM để xác định một cách linh hoạt dựa trên đầu vào hoặc kết quả của LLM. Các hệ thống dựa trên tác nhân thường thực hiện nhiều cuộc gọi liên tục đến LLM bằng cách sử dụng kết quả từ lần gọi trước để hướng dẫn các lần gọi tiếp theo.

Quyền Hạn Quá Mức là lỗ hổng cho phép thực hiện các hành động gây hại khi phản hồi từ LLM không mong đợi, mơ hồ hoặc bị thao túng, bất kể nguyên nhân nào khiến LLM hoạt động sai. Các nguyên nhân phổ biến bao gồm:
* Ảo giác (hallucination)/Bịa đặt (confabulation) do prompt được thiết kế kém hoặc mô hình hoạt động kém hiệu quả.
* Tiêm lệnh (Prompt injection) trực tiếp/gián tiếp từ người dùng độc hại, từ một phần mở rộng bị tấn công hoặc từ một tác nhân đồng nghiệp trong hệ thống đa tác nhân.

Nguyên nhân gốc rễ của Quyền Hạn Quá Mức thường là:
* Chức năng quá mức;
* Quyền hạn quá mức;
* Tự chủ quá mức.

Lỗ hổng này có thể dẫn đến nhiều tác động khác nhau trên phổ bảo mật về tính bảo mật, toàn vẹn và khả dụng, phụ thuộc vào hệ thống mà ứng dụng LLM có thể tương tác.

Lưu ý: Quyền Hạn Quá Mức khác với Xử Lý Đầu Ra Không An Toàn, vốn liên quan đến việc không đủ kiểm tra đầu ra của LLM.

### Các Ví Dụ Phổ Biến Về Lỗ Hổng

#### 1. Chức năng quá mức
  Một tác nhân LLM có quyền truy cập vào các phần mở rộng chứa các chức năng không cần thiết cho hoạt động dự kiến. Ví dụ, một nhà phát triển cần cấp quyền cho tác nhân LLM đọc tài liệu từ kho dữ liệu, nhưng phần mở rộng bên thứ ba được chọn cũng có khả năng chỉnh sửa và xóa tài liệu.
#### 2. Chức năng quá mức
  Một phần mở rộng từng được thử nghiệm trong giai đoạn phát triển nhưng sau đó bị loại bỏ để thay thế bằng giải pháp tốt hơn, tuy nhiên plugin cũ vẫn tồn tại và có thể bị lạm dụng.
#### 3. Chức năng quá mức
  Một plugin LLM có chức năng mở rộng không lọc đúng cách các lệnh ngoài phạm vi cần thiết. Ví dụ, một phần mở rộng chạy một lệnh shell cụ thể nhưng không chặn đúng cách các lệnh shell khác.
#### 4. Quyền hạn quá mức
  Một phần mở rộng LLM có quyền trên các hệ thống vượt quá mức cần thiết. Ví dụ, một phần mở rộng chỉ cần đọc dữ liệu nhưng lại kết nối với máy chủ cơ sở dữ liệu bằng một tài khoản có quyền SELECT, UPDATE, INSERT và DELETE.
#### 5. Quyền hạn quá mức
  Một phần mở rộng LLM thiết kế để thực hiện các thao tác theo ngữ cảnh của một người dùng nhưng lại kết nối với hệ thống bằng một tài khoản có quyền cao, cho phép truy cập dữ liệu của tất cả người dùng.
#### 6. Tự chủ quá mức
  Một ứng dụng hoặc phần mở rộng dựa trên LLM không xác minh độc lập các hành động có tác động cao. Ví dụ, một phần mở rộng cho phép xóa tài liệu của người dùng mà không yêu cầu xác nhận từ họ.

### Chiến lược Phòng chống và Giảm thiểu

The following actions can prevent Excessive Agency:

#### 1. Giảm thiểu phần mở rộng
  Hạn chế các phần mở rộng mà tác tử LLM được phép gọi, chỉ giới hạn ở mức tối thiểu cần thiết. Ví dụ, nếu một hệ thống dựa trên LLM không cần khả năng truy xuất nội dung từ một URL, thì không nên cung cấp phần mở rộng này cho tác tử LLM.
#### 2. Giảm thiểu chức năng của phần mở rộng
  Giới hạn các chức năng được triển khai trong phần mở rộng LLM ở mức tối thiểu cần thiết. Ví dụ, một phần mở rộng truy cập hộp thư của người dùng để tóm tắt email chỉ cần có quyền đọc email, và không nên chứa các chức năng khác như xóa hoặc gửi thư.
#### 3. Tránh các phần mở rộng có chức năng mở rộng không giới hạn
  Hạn chế sử dụng các phần mở rộng có chức năng mở rộng không giới hạn khi có thể (ví dụ: chạy lệnh shell, truy xuất URL, v.v.), thay vào đó sử dụng các phần mở rộng có chức năng chi tiết hơn. Ví dụ, một ứng dụng dựa trên LLM có thể cần ghi dữ liệu đầu ra vào một tệp. Nếu chức năng này được triển khai thông qua một phần mở rộng chạy lệnh shell, thì phạm vi của các hành động không mong muốn sẽ rất lớn (vì bất kỳ lệnh shell nào cũng có thể được thực thi). Một giải pháp an toàn hơn là xây dựng một phần mở rộng ghi tệp chuyên biệt, chỉ triển khai đúng chức năng đó.
#### 4. Giảm thiểu quyền hạn của phần mở rộng
  Giới hạn quyền truy cập của phần mở rộng LLM vào các hệ thống khác ở mức tối thiểu cần thiết để giảm thiểu rủi ro thực hiện các hành động không mong muốn. Ví dụ, một tác tử LLM sử dụng cơ sở dữ liệu sản phẩm để đưa ra khuyến nghị mua hàng cho khách hàng có thể chỉ cần quyền đọc bảng 'products', không nên có quyền truy cập các bảng khác hoặc thực hiện các thao tác chèn, cập nhật hay xóa dữ liệu. Điều này nên được thực thi bằng cách áp dụng các quyền truy cập thích hợp cho danh tính mà phần mở rộng LLM sử dụng để kết nối với cơ sở dữ liệu.
#### 5. Thực thi phần mở rộng trong ngữ cảnh của người dùng
  Theo dõi quyền ủy quyền của người dùng và phạm vi bảo mật để đảm bảo rằng các hành động được thực hiện thay mặt người dùng phải được thực hiện trên các hệ thống hạ nguồn trong ngữ cảnh của người dùng cụ thể đó, với quyền tối thiểu cần thiết. Ví dụ, một phần mở rộng LLM truy cập kho mã nguồn của người dùng nên yêu cầu người dùng xác thực thông qua OAuth với phạm vi quyền hạn tối thiểu cần thiết.
#### 6.  Yêu cầu sự chấp thuận của người dùng
  Áp dụng kiểm soát "con người trong vòng lặp" (human-in-the-loop) để yêu cầu sự chấp thuận của con người trước khi thực hiện các hành động có tác động cao. Điều này có thể được triển khai trong hệ thống hạ nguồn (ngoài phạm vi ứng dụng LLM) hoặc bên trong chính phần mở rộng LLM. Ví dụ, một ứng dụng LLM tạo và đăng nội dung trên mạng xã hội thay mặt người dùng nên có quy trình yêu cầu người dùng xác nhận nội dung trước khi thực hiện thao tác đăng bài.
#### 7. Kiểm soát trung gian hoàn chỉnh
  Thực thi cơ chế ủy quyền trong các hệ thống hạ nguồn thay vì chỉ dựa vào LLM để quyết định xem một hành động có được phép hay không. Đảm bảo nguyên tắc "kiểm soát trung gian hoàn chỉnh" (complete mediation), theo đó tất cả các yêu cầu được gửi đến hệ thống hạ nguồn thông qua các phần mở rộng phải được xác thực và kiểm tra theo chính sách bảo mật.
#### 8. Lọc và kiểm tra đầu vào/đầu ra của LLM
Áp dụng các phương pháp lập trình an toàn, chẳng hạn như tuân theo các khuyến nghị của OWASP ASVS (Application Security Verification Standard), đặc biệt chú trọng đến việc lọc đầu vào. Sử dụng các công cụ kiểm tra bảo mật ứng dụng tĩnh (SAST) cũng như kiểm tra bảo mật động và tương tác (DAST, IAST) trong quy trình phát triển phần mềm.

Các biện pháp sau đây không thể ngăn chặn hoàn toàn tình trạng Quyền hạn Quá mức (Excessive Agency), nhưng có thể giảm thiểu mức độ thiệt hại:

- Ghi log và giám sát hoạt động của các phần mở rộng LLM cũng như các hệ thống hạ nguồn để xác định các hành động không mong muốn đang diễn ra và phản ứng kịp thời.
- Triển khai cơ chế giới hạn tốc độ (rate-limiting) để giảm số lượng hành động không mong muốn có thể xảy ra trong một khoảng thời gian nhất định. Điều này giúp tăng cơ hội phát hiện hành vi đáng ngờ thông qua giám sát trước khi thiệt hại lớn xảy ra.

### Kịch bản Tấn công Minh họa

Một ứng dụng trợ lý cá nhân dựa trên LLM được cấp quyền truy cập vào hộp thư của một cá nhân thông qua một phần mở rộng để tóm tắt nội dung email đến. Để thực hiện chức năng này, phần mở rộng cần có quyền đọc email. Tuy nhiên, plugin mà nhà phát triển hệ thống lựa chọn cũng chứa chức năng gửi email. Ngoài ra, ứng dụng này có lỗ hổng tấn công chèn lệnh gián tiếp (indirect prompt injection). Một email được tạo với nội dung độc hại có thể đánh lừa LLM yêu cầu tác tử quét hộp thư của người dùng để tìm thông tin nhạy cảm và chuyển tiếp nó đến địa chỉ email của kẻ tấn công. Tình huống này có thể được ngăn chặn bằng cách:
* Loại bỏ chức năng thừa thãi bằng cách chỉ sử dụng một phần mở rộng chỉ có chức năng đọc email,
* Loại bỏ quyền hạn quá mức bằng cách xác thực dịch vụ email của người dùng qua OAuth với phạm vi chỉ đọc, và/hoặc
* Loại bỏ quyền tự chủ quá mức bằng cách yêu cầu người dùng tự xác nhận và nhấn nút "gửi" cho từng email do phần mở rộng LLM soạn thảo.

Ngoài ra, có thể giảm thiểu thiệt hại bằng cách triển khai giới hạn tốc độ (rate limiting) trên giao diện gửi email, để ngăn chặn số lượng email không mong muốn được gửi đi trong một khoảng thời gian ngắn.

### Các liên kết tham khảo

1. [Slack AI làm rò rỉ dữ liệu từ các kênh riêng tư](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Ngăn AI lạm dụng API của bạn](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Vấn đề đặc quyền nhầm lẫn](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Hướng dẫn thiết lập giao diện an toàn](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Mô hình LLM kép để tăng cường bảo mật](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
