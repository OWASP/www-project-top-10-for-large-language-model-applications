## LLM09: Overreliance

### Mô tả

Sự phụ thuộc quá mức có thể xảy ra khi LLM tạo ra thông tin sai lệch và cung cấp thông tin đó theo cách có thẩm quyền. Mặc dù LLM có thể tạo ra nội dung sáng tạo và nhiều thông tin, nhưng chúng cũng có thể tạo ra nội dung không đúng sự thật, không phù hợp hoặc không an toàn. Điều này được gọi là ảo giác hoặc bịa đặt. Khi mọi người hoặc hệ thống tin tưởng thông tin này mà không có sự giám sát hoặc xác nhận, điều này có thể dẫn đến vi phạm bảo mật, thông tin sai lệch, giao tiếp sai, các vấn đề pháp lý và gây tổn hại đến danh tiếng.

Mã nguồn do LLM tạo ra có thể gây ra các lỗ hổng bảo mật không được chú ý. Điều này gây ra rủi ro đáng kể đối với sự an toàn và bảo mật hoạt động của các ứng dụng. Những rủi ro này cho thấy tầm quan trọng của các quy trình đánh giá nghiêm ngặt, với:

* Giám sát
* Cơ chế xác thực liên tục
* Tuyên bố từ chối rủi ro

### Các ví dụ phổ biến về lỗ hổng

1. LLM cung cấp thông tin không chính xác dưới dạng phản hồi trong khi trình bày nó theo cách ngụ ý rằng thông tin đó rất có thẩm quyền. Toàn bộ hệ thống được thiết kế mà không có các biện pháp kiểm tra và cân bằng phù hợp để xử lý tình huống này, dẫn đến việc thông tin gây hiểu lầm cho người dùng theo cách có thể gây hại:
2. LLM gợi ý mã không an toàn hoặc lỗi, dẫn đến lỗ hổng khi được đưa vào hệ thống phần mềm mà không có sự giám sát hoặc xác minh thích hợp.

### Chiến lược phòng ngừa và giảm thiểu

1. Thường xuyên theo dõi và xem xét đầu ra của LLM. Sử dụng các kỹ thuật tự nhất quán hoặc bỏ phiếu để lọc ra văn bản không nhất quán. So sánh nhiều phản hồi của mô hình cho một lời nhắc duy nhất có thể đánh giá tốt hơn chất lượng và tính nhất quán của đầu ra.
2. Kiểm tra chéo đầu ra LLM với các nguồn bên ngoài đáng tin cậy. Lớp xác thực bổ sung này có thể giúp đảm bảo thông tin do mô hình cung cấp là chính xác và đáng tin cậy.
3. Cải thiện mô hình bằng cách tinh chỉnh hoặc sử dụng nhúng để nâng cao chất lượng đầu ra. Các mô hình được đào tạo chung chung có nhiều khả năng tạo ra thông tin không chính xác hơn so với các mô hình được điều chỉnh cho một lĩnh vực cụ thể. Các kỹ thuật như kỹ thuật nhắc nhở, điều chỉnh hiệu quả tham số (PET), điều chỉnh toàn bộ mô hình và nhắc nhở chuỗi suy nghĩ có thể được sử dụng để đạt được mục đích này.
4. Triển khai các cơ chế xác thực tự động có thể xác minh chéo đầu ra được tạo ra với các sự kiện hoặc dữ liệu đã biết. Điều này có thể cung cấp một lớp bảo mật bổ sung và giảm thiểu rủi ro liên quan đến ảo giác.
5. Chia nhỏ các nhiệm vụ phức tạp thành các nhiệm vụ con có thể quản lý được và giao cho các tác nhân khác nhau. Điều này không chỉ giúp quản lý sự phức tạp mà còn giảm khả năng xuất hiện ảo giác vì mỗi tác nhân có thể chịu trách nhiệm cho một nhiệm vụ nhỏ hơn.
6. Truyền đạt rõ ràng các rủi ro và hạn chế liên quan đến việc sử dụng LLM. Điều này bao gồm khả năng thông tin không chính xác và các rủi ro khác. Truyền đạt rủi ro hiệu quả có thể giúp người dùng chuẩn bị cho các vấn đề tiềm ẩn và giúp họ đưa ra quyết định sáng suốt.
7. Xây dựng API và giao diện người dùng khuyến khích sử dụng LLM có trách nhiệm và an toàn. Điều này có thể bao gồm các biện pháp như bộ lọc nội dung, cảnh báo người dùng về các thông tin không chính xác tiềm ẩn và dán nhãn rõ ràng cho nội dung do AI tạo ra.
8. Khi sử dụng LLM trong môi trường phát triển, hãy thiết lập các hướng dẫn và thực hành mã hóa an toàn để ngăn chặn việc tích hợp các lỗ hổng có thể xảy ra.

### Ví dụ về kịch bản tấn công

1. Một tổ chức tin tức sử dụng LLM rất nhiều để tạo ra các bài báo. Một tác nhân độc hại lợi dụng sự phụ thuộc quá mức này, cung cấp thông tin sai lệch cho LLM và gây ra sự lan truyền thông tin sai lệch.
2. AI vô tình đạo văn nội dung, dẫn đến các vấn đề về bản quyền và làm giảm lòng tin vào tổ chức.
3. Một nhóm phát triển phần mềm sử dụng hệ thống LLM để đẩy nhanh quá trình mã hóa. Việc quá phụ thuộc vào các đề xuất của AI sẽ gây ra lỗ hổng bảo mật trong ứng dụng do các thiết lập mặc định không an toàn hoặc các khuyến nghị không nhất quán với các thông lệ mã hóa an toàn.
4. Một công ty phát triển phần mềm sử dụng LLM để hỗ trợ các nhà phát triển. LLM đề xuất một thư viện hoặc gói mã không tồn tại hoặc độc hại và nhà phát triển tin tưởng vào AI nên tích hợp gói vào phần mềm của công ty. Điều này làm nổi bật tầm quan trọng của việc kiểm tra chéo các đề xuất của LLM, đặc biệt là khi liên quan đến mã hoặc thư viện của bên thứ ba.

### Tham khảo

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
