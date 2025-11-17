## LLM09:2025 Thông tin sai lệch

### Mô tả

Thông tin sai lệch từ các Mô hình Ngôn ngữ lớn (LLM) là một điểm yếu lớn đối với các ứng dụng phụ thuộc vào các mô hình này. Thông tin sai lệch xuất hiện khi các LLM tạo ra các thông tin sai hoặc gây hiểu lầm nhưng trông lại có vẻ đáng tin cậy. Lỗ hổng này có  thể dẫn đến các vi phạm bảo mật, ảnh hưởng danh tiếng và trách nhiệm pháp lý.

Một trong những nguyên nhân chính của thông tin sai lệch là hiện tượng ảo giác – khi LLM đưa ra các nội dung có vẻ chính xác nhưng thật ra chúng đã tạo ra các nội dung này. Ảo giác sinh ra khi LLM tự điền vào những khoảng trống trong dữ liệu huấn luyện dựa trên các mẫu thống kê, mà không thực sự hiểu các nội dung này. Kết quả là, mô hình có thể tạo ra các câu trả lời nghe có vẻ đúng nhưng hoàn toàn không có căn cứ. Ảo giác là guyên nhân chính dẫn đến thông tin sai lệch, nhưng đó không phải là nguyên nhân duy nhất; các thiên kiến trong dữ liệu huấn luyện và thông tin không hoàn chỉnh cũng là một trong các tác nhân. 

Một vấn đề liên quan đó là sự phụ thuộc quá mức vào mô hình. Sự phụ thuộc quá mức xuất hiện khi người dùng tin tưởng quả mức vào các nội dung được tạo ra bởi LLM, và không kiểm tra lại độ chính xác của các nội dung này. Việc phụ thuộc quá mức làm cho thông tin sai lệch gây hậu quả lớn hơn, do người dùng có thể dựa trên các dữ liệu sai để đưa ra các quyết định quan trọng mà không có sự xem xét kỹ lưỡng.

### Các ví dụ phổ biến về lỗ hổng

#### 1. Thông tin sai sự thật
  Mô hình đưa ra các khẳng định sai, dẫn đến việc người dùng ra quyết định dựa trên thông tin sai. Ví dụ, chatbot của hãng hàng không Air Canada cung cấp thông tin sai lệch cho hành khách, dẫn đến gián đoạn hoạt động và rắc rối về pháp lý. Kết quả là hãng hàng không đã bị thua kiện. 
  (Liên kết tham khảo: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))
#### 2. Những khẳng định vô căn cứ
  Mô hình tạo ra các khẳng định vô căn cứ, điều đó đặc biệt nguy hiểm trong các lĩnh vực nhạy cảm như y tế hoặc pháp lý. Ví dụ, ChatGPT đã tạo ra các vụ kiện giả, dẫn đến các vấn đề nghiêm trọng ở tòa án.
  (Liên kết tham khảo: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))
#### 3. Giả chuyên môn
  Mô hình tạo ra cảm giác hiểu rõ các chủ đề phức tạp, đánh lừa người dùng về trình độ chuyên môn của nó. Ví dụ, các chatbot đã bị phát hiện đưa ra các thông tin sai về độ phức tạp của các vấn đề liên quan đến sức khỏe, gợi ý sự không chắc chắn trong khi không phải như vậy, làm cho người dùng tin rằng phương pháp điều trị vẫn còn đang trong giai đoạn thảo luận.
  (Liên kết tham khảo: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))
#### 4. Tạo mã không an toàn
  Mô hình đề xuất thư viện mã không tồn tại hoặc không bảo mật, điều đó có thể dẫn đến lỗ hổng bảo mật khi tích hợp vào hệ thống phần mềm. Ví dụ, LLM đề xuất sử dụng thư viện mã không bảo mật của bên thứ ba, mà thư viện mã này nếu được sử dụng mà không kiểm tra lại, sẽ dẫn đến các nguy cơ về bảo mật.
  (Liên kết tham khảo: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Chiến lược ngăn chặn và giảm thiểu

#### 1. Tạo tăng cường truy xuất (RAG)
  Sử dụng kỹ thuật tạo tăng cường truy xuất để làm tăng độ tin cậy của các kết quả đầu ra của mô hình bằng cách truy xuất các thông tin liên quan và đã được kiểm chứng từ các cơ sở dữ liệu đáng tin cậy trong quá trình tạo phản hồi. Điều này sẽ giúp giảm thiểu rủi ro ảo giác và thông tin sai lệch. 
#### 2. Tinh chỉnh mô hình
  Cải thiện mô hình bằng tinh chỉnh hoặc biểu diễn vector để cải thiện chất lượng đầu ra. Các kỹ thuật như tinh chỉnh tham số hiệu quả (PET) và lệnh chuỗi suy luận (chain-of-thought prompting) có thể giúp giảm các tình huống xuất hiện thông tin sai lệch. 
#### 3. Xác minh chèo và giám sát con người
  Khuyến khích người dùng kiểm tra chèo các kết quả của LLM với các nguồn tin cậy bên ngoài để đảm bảo độ chính xác của thông tin. Áp dụng quy trình giám sát con người và kiểm chứng thông tin, đặc biệt đối với thông tin quan trọng hoặc nhạy cảm. Đảm bảo người kiểm duyệt được đào tạo đầy đủ để tránh phụ thuộc quá mức vào nội dung AI tạo ra. 
#### 4. Cơ chế xác thực tự động
  Ấp dụng các công cụ và quy trình để xác thực các đầu ra quan trọng một cách tự động, đặc biệt trong những môi trường có rủi ro cao.
#### 5. Truyền đạt về rủi ro
  Xác định các rủi và mối nguy tiềm tàng liên quan đến nội dung do LLM tạo ra, sau đó truyền đạt các rủi ro này và các hạn chế tới người dùng, bao gồm các khả năng về thông tin sai lệch. 
#### 6. Thực hành lập trình an toàn
  dựng các quy trình lập trình an toàn để tránh tích hợp các lỗ hổng do các gợi ý lập trình sai gây ra. 
#### 7. Thiết kế giao diện người dùng
  Thiết kế API và giao diện người dùng để khuyến khích việc sử dụng LLM có trách nhiệm, ví dụ tích hợp các bộ lọc nội dụng, dán nhãn rõ ràng đối với các nội dung do AI tạo ra và thông báo cho người dùng về các hạn chế về độ tin tưởng và độ chính xác của nó. Cần nêu rõ giới hạn về phạm vi sử dụng của thông tin.
#### 8. Đào tạo và giáo dục
  Cung cấp đào tạo toàn diện cho người dùng về các hạn chế của LLM, tầm quan trọng của việc xác minh các nội dung được LLM tạo ra, và sự cần thiết của tư duy phản biện. Trong các ngữ cảnh cụ thể, cung cấp đào tạo chuyên sâu để đảm bảo người dùng đánh giá được đầu ra của LLM một cách hiệu quả trong lĩnh vực chuyên môn của họ. 

### Các kịch bản tấn công mẫu

#### Kịch bản #1
  Kẻ tấn công thử nghiệm với các trợ lý lập trình phổ biến để tìm ra tên các gói thường bị ảo giác (hallucinate). Sau khi xác định được các thư viện thường hay được gợi ý nhưng không thực sự tồn tại này, chúng đăng các gói độc hại với tên giống như vậy lên các kho mã nguồn được sử dụng rộng rãi. Các nhà phát triển, phụ thuộc vào các gợi ý của trợ lý lập trình, vô tình tích hợp các gói độc hại này vào phần mềm của họ. Kết quả là, kẻ tấn công chiếm được quyền truy cập trái phép, chèn mã độc, tạo cửa sau (backdoor), dẫn đến vi phạm bảo mật nghiêm trọng và làm lộ dữ liệu người dùng. 
#### Kịch bản #2
  Một công ty cung cấp chatbot để chẩn đoán y tế mà không đảm bảo độ chính xác cần thiết. Chatbot cung cấp thông tin không đúng, dẫn đến hậu quả cho bệnh nhân. Kết quả là, công ty bị thua kiện vì những thiệt hại đã xảy ra. Trong trường hợp này, không cần kẻ tấn công thù địch, sự an toàn và bảo mật đã bị ảnh hưởng bởi sơ xuất trong việc giám sát và độ tin cậy của hệ thống LLM. Trong kịch bản này, mặc dù không có kẻ tấn công trực tiếp, công ty đã có nguy cơ bị ảnh hưởng danh tiếng và thiệt hại tài chính. 

### Liên kết tham khảo

1. [AI Chatbots as Health Information Sources: Misrepresentation of Expertise](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Chatbot Misinformation: What Travellers Should Know](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Fake Legal Cases: Generative AI Hallucinations](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Diving Deeper into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [How Secure is Code Generated by ChatGPT?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [A Framework for Exploring the Consequences of AI-Mediated Enterprise Knowledge](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### Các khung chuẩn và hệ thống phân loại liên quan

Tham khảo phần này để có thông tin toàn diện, các chiến lược kịch bản liên quan đến triển khai hạ tầng, kiểm soát môi trường được áp dụng và các thực hành tốt nhất.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
