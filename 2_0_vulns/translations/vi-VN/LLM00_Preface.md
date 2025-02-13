## Letter from the Project Leads

The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications. Since then, the technology has continued to spread across industries and applications, and so have the associated risks. As LLMs are embedded more deeply in everything from customer interactions to internal operations, developers and security professionals are discovering new vulnerabilities—and ways to counter them.

The 2023 list was a big success in raising awareness and building a foundation for secure LLM usage, but we've learned even more since then. In this new 2025 version, we’ve worked with a larger, more diverse group of contributors worldwide who have all helped shape this list. The process involved brainstorming sessions, voting, and real-world feedback from professionals in the thick of LLM application security, whether by contributing or refining those entries through feedback. Each voice was critical to making this new release as thorough and practical as possible.

### What’s New in the 2025 Top 10

The 2025 list reflects a better understanding of existing risks and introduces critical updates on how LLMs are used in real-world applications today. For instance, **Unbounded Consumption** expands on what was previously Denial of Service to include risks around resource management and unexpected costs—a pressing issue in large-scale LLM deployments.

The **Vector and Embeddings** entry responds to the community’s requests for guidance on securing Retrieval-Augmented Generation (RAG) and other embedding-based methods, now core practices for grounding model outputs.

We’ve also added **System Prompt Leakage** to address an area with real-world exploits that were highly requested by the community. Many applications assumed prompts were securely isolated, but recent incidents have shown that developers cannot safely assume that information in these prompts remains secret.

**Excessive Agency** has been expanded, given the increased use of agentic architectures that can give the LLM more autonomy.  With LLMs acting as agents or in plug-in settings, unchecked permissions can lead to unintended or risky actions, making this entry more critical than ever.

### Moving Forward

Like the technology itself, this list is a product of the open-source community’s insights and experiences. It has been shaped by contributions from developers, data scientists, and security experts across sectors, all committed to building safer AI applications. We’re proud to share this 2025 version with you, and we hope it provides you with the tools and knowledge to secure LLMs effectively.

Thank you to everyone who helped bring this together and those who continue to use and improve it. We’re grateful to be part of this work with you.## Thư từ các Trưởng Dự án

Danh sách OWASP Top 10 cho Ứng dụng Mô hình Ngôn ngữ Lớn (Large Language Model Applications) bắt đầu vào năm 2023 như một nỗ lực do cộng đồng dẫn dắt để làm nổi bật và giải quyết các vấn đề bảo mật cụ thể cho các ứng dụng AI. Kể từ đó, công nghệ này đã tiếp tục lan rộng khắp các ngành công nghiệp và ứng dụng, và các rủi ro liên quan cũng vậy. Khi các mô hình ngôn ngữ lớn (LLM) được tích hợp sâu hơn vào mọi thứ từ tương tác khách hàng đến hoạt động nội bộ, các nhà phát triển và chuyên gia bảo mật đang phát hiện ra những lỗ hổng mới—và các cách để chống lại chúng.

Danh sách năm 2023 là một thành công lớn trong việc nâng cao nhận thức và xây dựng nền tảng cho việc sử dụng LLM an toàn, nhưng chúng tôi đã học được nhiều hơn kể từ đó. Trong phiên bản mới năm 2025 này, chúng tôi đã làm việc với một nhóm cộng tác viên lớn hơn, đa dạng hơn trên toàn thế giới, tất cả đều đã giúp định hình danh sách này. Quá trình này bao gồm các buổi họp nghiên cứu, bỏ phiếu và phản hồi thực tế từ các chuyên gia trong lĩnh vực bảo mật ứng dụng LLM, dù là bằng cách đóng góp hay tinh chỉnh các mục thông qua phản hồi. Mỗi ý kiến đều rất quan trọng để làm cho phiên bản mới này toàn diện và thực tiễn nhất có thể.

### Những Điểm Mới trong OWASP Top 10 năm 2025

Danh sách năm 2025 phản ánh sự hiểu biết tốt hơn về các rủi ro hiện có và giới thiệu các cập nhật quan trọng về cách LLM được sử dụng trong các ứng dụng thực tế ngày nay. Ví dụ, Tiêu thụ Không Giới Hạn (Unbounded Consumption) mở rộng từ khái niệm trước đây là Từ chối Dịch vụ (Denial of Service) để bao gồm cả các rủi ro liên quan đến quản lý tài nguyên và chi phí bất ngờ—một vấn đề cấp bách trong việc triển khai LLM quy mô lớn.

Mục Véc-tơ và Nhúng (Vector and Embeddings) phản hồi lại yêu cầu từ cộng đồng về hướng dẫn bảo mật cho Tạo tăng cường truy xuất (Retrieval-Augmented Generation) và các phương pháp dựa trên nhúng khác, hiện đang là thực tiễn cốt lõi để kiểm soát đầu ra của mô hình.

Chúng tôi cũng đã thêm mục Rò rỉ Lời Nhắc Hệ Thống(System Prompt Leakage) để giải quyết một lĩnh vực có các khai thác thực tế được cộng đồng yêu cầu cao. Nhiều ứng dụng đã giả định rằng lời nhắc được cách ly an toàn, nhưng các sự cố gần đây đã cho thấy các nhà phát triển không thể giả định một cách an toàn rằng thông tin trong những lời nhắc này sẽ luôn được giữ bí mật.

Việc Trao Quyền Quá Mức (Excessive Agency) đã được mở rộng do sự gia tăng của các kiến trúc tác nhân (agent) có thể cấp cho LLM nhiều quyền tự chủ hơn. Khi các LLM hoạt động như tác nhân độc lập hoặc trong cấu hình plugin, quyền không được kiểm soát có thể dẫn đến các hành động ngoài ý muốn hoặc rủi ro, làm cho mục này trở nên quan trọng hơn bao giờ hết.

### Tiếp Tục Tiến Bước

Giống như chính công nghệ này, danh sách này là sản phẩm của những hiểu biết và kinh nghiệm từ cộng đồng mã nguồn mở. Nó đã được định hình bởi sự đóng góp từ các nhà phát triển, nhà khoa học dữ liệu và chuyên gia bảo mật trên nhiều lĩnh vực, tất cả đều cam kết xây dựng các ứng dụng AI an toàn hơn. Chúng tôi tự hào chia sẻ phiên bản 2025 này với bạn và hy vọng rằng nó cung cấp cho bạn các công cụ và kiến thức để bảo mật LLM một cách hiệu quả.

Cảm ơn tất cả những người đã giúp đưa danh sách này đến với cộng đồng và những người tiếp tục sử dụng và cải tiến nó. Chúng tôi rất vinh dự được tham gia vào công việc này cùng các bạn.

Steve Wilson
Trưởng Dự án
OWASP Top 10 cho Ứng dụng Mô hình Ngôn ngữ Lớn
LinkedIn: https://www.linkedin.com/in/wilsonsd/

Ads Dawson
Trưởng Kỹ thuật & Trưởng Nhóm Các Mục Lỗ Hổng
OWASP Top 10 cho Ứng dụng Mô hình Ngôn ngữ Lớn
LinkedIn: https://www.linkedin.com/in/adamdawson0/

Bản dịch này giữ nguyên từng từ một để đảm bảo tính chính xác và đúng nghĩa của tài liệu gốc. Nếu bạn cần tinh chỉnh hoặc điều chỉnh phong cách dịch, hãy cho tôi biết! 😊


#### Steve Wilson
Project Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/wilsonsd/

#### Ads Dawson
Technical Lead & Vulnerability Entries Lead
OWASP Top 10 for Large Language Model Applications
LinkedIn: https://www.linkedin.com/in/adamdawson0/

### Vietnamese Translation Team
Name of translator
LinkedIn

### About this translation
Recognizing the technical and critical nature of the OWASP Top 10 for Large Language Model Applications, we consciously chose to employ only human translators in the creation of this translation. The translators listed above not only have a deep technical knowledge of the original content, but also the fluency required to make this translation a success.

#### Talesh Seeparsan
Translation Lead, OWASP Top 10 for AI Applications LLM
LinkedIn: https://www.linkedin.com/in/talesh/
