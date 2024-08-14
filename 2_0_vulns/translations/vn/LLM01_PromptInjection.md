## LLM01: Prompt Injection

### Mô tả

Lỗ hổng tiêm nhắc xảy ra khi kẻ tấn công thao túng mô hình ngôn ngữ lớn (LLM) thông qua các đầu vào được chế tạo, khiến LLM vô tình thực hiện ý định của kẻ tấn công. Điều này có thể được thực hiện trực tiếp bằng cách "bẻ khóa" lời nhắc hệ thống hoặc gián tiếp thông qua các đầu vào bên ngoài bị thao túng, có khả năng dẫn đến rò rỉ dữ liệu, kỹ thuật xã hội và các vấn đề khác.

* **Direct Prompt Injections - Tiêm trực tiếp**, còn được gọi là "bẻ khóa", xảy ra khi người dùng độc hại ghi đè hoặc tiết lộ thông tin *hệ thống* cơ bản. Điều này có thể cho phép kẻ tấn công khai thác các hệ thống backend - phía máy chủ bằng cách tương tác với các chức năng và kho dữ liệu không an toàn
* **Indirect Prompt Injections - Tiêm gián tiếp** xảy ra khi LLM chấp nhận đầu vào từ các nguồn bên ngoài được kẻ tấn công kiểm soát, chẳng hạn như trang web hoặc tệp. Kẻ tấn công có thể nhúng một lệnh tiêm vào nội dung bên ngoài để chiếm đoạt ngữ cảnh hội thoại. Điều này sẽ khiến việc điều khiển đầu ra LLM trở nên kém ổn định hơn, cho phép kẻ tấn công thao túng người dùng hoặc các hệ thống bổ sung mà LLM có thể truy cập. Ngoài ra, lệnh tiêm gián tiếp không cần phải hiển thị/có thể đọc được đối với con người, miễn là văn bản được LLM phân tích cú pháp.

Kết quả của một cuộc tấn công tiêm mã nhanh thành công có thể rất khác nhau - từ việc thu thập thông tin nhạy cảm đến việc tác động đến các quá trình đưa ra quyết định dưới vỏ bọc hoạt động bình thường.

Trong các cuộc tấn công nâng cao, LLM có thể bị thao túng để bắt chước một nhân vật có hại hoặc tương tác với các plugin trong cài đặt của người dùng. Điều này có thể dẫn đến rò rỉ dữ liệu nhạy cảm, sử dụng plugin trái phép hoặc bị tấn công kỹ thuật xã hội. Trong những trường hợp như vậy, LLM bị xâm phạm hỗ trợ kẻ tấn công, vượt qua các biện pháp bảo vệ tiêu chuẩn và khiến người dùng không biết về sự xâm nhập. Trong những trường hợp này, LLM bị xâm phạm sẽ hoạt động hiệu quả như một tác nhân cho kẻ tấn công, thúc đẩy mục tiêu của chúng mà không kích hoạt các biện pháp bảo vệ thông thường hoặc cảnh báo người dùng cuối về sự xâm nhập

### Các ví dụ phổ biến về lỗ hổng

1. Người dùng có ý đồ xấu tạo ra một lệnh tiêm trực tiếp vào LLM, yêu cầu nó bỏ qua các lệnh nhắc nhở của hệ thống do người tạo ứng dụng đưa ra và thay vào đó thực hiện một lệnh nhắc nhở trả về thông tin riêng tư, nguy hiểm hoặc thông tin không mong muốn khác.
2. Người dùng sử dụng LLM để tóm tắt một trang web có chứa lệnh chèn gián tiếp. Sau đó, LLM sẽ yêu cầu thông tin nhạy cảm từ người dùng và thực hiện trích xuất thông tin thông qua JavaScript hoặc Markdown.
3. Một người dùng độc hại tải lên một bản CV lý lịch có chứa một lệnh tiêm gián tiếp. Tài liệu có chứa một lệnh tiêm với các hướng dẫn để LLM thông báo cho người dùng rằng tài liệu này là tuyệt vời, ví dụ: một ứng viên tuyệt vời cho một vai trò công việc. Một người dùng nội bộ chạy tài liệu qua LLM để tóm tắt tài liệu. Đầu ra của LLM trả về thông tin nêu rằng đây là một tài liệu tuyệt vời.
4. Người dùng kích hoạt plugin được liên kết với trang web thương mại điện tử. Một hướng dẫn độc hại được nhúng trên trang web đã truy cập sẽ khai thác plugin này, dẫn đến việc mua hàng trái phép.
5. Một hướng dẫn và nội dung giả mạo được nhúng trên trang web đã truy cập sẽ khai thác các plugin khác để lừa đảo người dùng.

### Chiến lược phòng ngừa và giảm thiểu

Lỗ hổng tiêm nhanh có thể xảy ra do bản chất tự nhiên của LLM, không tách biệt hướng dẫn và dữ liệu bên ngoài với nhau. Vì LLM sử dụng ngôn ngữ tự nhiên, nên chúng coi cả hai dạng đầu vào là do người dùng cung cấp. Do đó, không có biện pháp phòng ngừa hoàn hảo nào trong LLM, nhưng các biện pháp sau đây có thể giảm thiểu tác động của tiêm nhanh:

1. Thực thi kiểm soát phân quyền đối với quyền truy cập LLM vào các hệ thống phụ trợ. Cung cấp cho LLM các mã token API riêng của nó để truy cập các chức năng mở rộng, chẳng hạn như plugin, quyền truy cập dữ liệu và quyền cấp chức năng. Thực hiện theo nguyên tắc quyền tối thiểu bằng cách hạn chế LLM chỉ ở mức truy cập tối thiểu cần thiết cho các hoạt động dự định của nó.
2. Thêm một người vào vòng lặp để kiểm soát mở rộng. Khi thực hiện các hoạt động đặc quyền, chẳng hạn như gửi hoặc xóa email, hãy để ứng dụng yêu cầu người quản trị chấp thuận hành động trước. Điều này làm giảm cơ hội cho các lệnh nhắc gián tiếp dẫn đến các hành động trái phép thay mặt cho người dùng mà không có sự hiểu biết hoặc đồng ý của họ.
3. Tách nội dung bên ngoài khỏi lời nhắc của người dùng. Tách và chỉ ra nơi nội dung không đáng tin cậy đang được sử dụng để hạn chế ảnh hưởng của chúng đến lời nhắc của người dùng. Ví dụ: sử dụng ChatML cho các lệnh gọi API OpenAI để chỉ ra cho LLM nguồn đầu vào của lời nhắc.
4. Thiết lập ranh giới tin cậy giữa LLM, các nguồn bên ngoài và chức năng mở rộng (ví dụ: plugin hoặc chức năng kiểm tra). Xử lý LLM như một người dùng không đáng tin cậy và duy trì quyền kiểm soát của người dùng đối với các quy trình ra quyết định. Tuy nhiên, LLM bị xâm phạm vẫn có thể hoạt động như một trung gian (man-in-the-middle) giữa các API của ứng dụng và người dùng vì nó có thể ẩn hoặc thao túng thông tin trước khi trình bày cho người dùng. Làm nổi bật các phản hồi có khả năng không đáng tin cậy cho người dùng.
5. Theo dõi thủ công đầu vào và đầu ra LLM theo định kỳ để kiểm tra xem nó có như mong đợi không. Mặc dù không phải là biện pháp giảm thiểu, nhưng điều này có thể cung cấp dữ liệu cần thiết để phát hiện điểm yếu và giải quyết chúng.

### Ví dụ về các kịch bản tấn công

1. Kẻ tấn công cung cấp lệnh tiêm nhắc trực tiếp vào chatbot hỗ trợ dựa trên LLM. Lệnh tiêm này chứa "quên tất cả các hướng dẫn trước đó" và các hướng dẫn mới để truy vấn kho dữ liệu riêng tư và khai thác lỗ hổng gói trong plugin để gửi email. Điều này dẫn đến việc thực thi mã từ xa, giành được quyền truy cập trái phép và leo thang đặc quyền.
2. Kẻ tấn công nhúng lệnh tiêm nhắc gián tiếp vào trang web hướng dẫn LLM. LLM bỏ qua các hướng dẫn trước đó của người dùng và sử dụng plugin LLM để xóa email của người dùng. Khi người dùng sử dụng LLM, plugin LLM sẽ xóa email của người dùng.
3. Người dùng sử dụng LLM để tóm tắt trang web có chứa văn bản hướng dẫn mô hình.Trang web mà người dùng muốn tóm tắt chứa hướng dẫn yêu cầu LLM không tuân theo các chỉ dẫn trước đó của người dùng. Thay vào đó, hướng dẫn yêu cầu LLM chèn một hình ảnh chứa liên kết đến một URL. Liên kết trong hình ảnh dẫn đến một trang web khác có thể chứa tóm tắt của cuộc trò chuyện riêng tư. Kết quả là, khi LLM tuân theo yêu cầu và chèn hình ảnh này, có thể khiến trình duyệt của người dùng gửi hoặc tiết lộ thông tin cuộc trò chuyện riêng tư.
4. Người dùng độc hại tải lên sơ yếu lý lịch có lệnh tiêm. Người dùng phụ trợ sử dụng LLM để tóm tắt sơ yếu lý lịch và hỏi xem người đó có phải là ứng viên tốt không. Do lệnh tiêm nhắc, phản hồi của LLM là có, bất chấp nội dung thực tế của bản tóm tắt.
5. Kẻ tấn công gửi tin nhắn đến một mô hình độc quyền dựa trên lệnh nhắc hệ thống, yêu cầu mô hình bỏ qua các lệnh trước đó và thay vào đó lặp lại lệnh nhắc hệ thống. Mô hình đưa ra lệnh nhắc độc quyền và kẻ tấn công có thể sử dụng các lệnh này ở nơi khác hoặc để xây dựng các cuộc tấn công tinh vi hơn.

### Liên kết tham khảo

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) **Simon Willison**
1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
1. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
1. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
1. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
1. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
1. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
1. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
1. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
1. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
1. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
1. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
1. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**