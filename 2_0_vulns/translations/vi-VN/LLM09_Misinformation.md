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

#### 1. Retrieval-Augmented Generation (RAG)
  Use Retrieval-Augmented Generation to enhance the reliability of model outputs by retrieving relevant and verified information from trusted external databases during response generation. This helps mitigate the risk of hallucinations and misinformation.
#### 2. Model Fine-Tuning
  Enhance the model with fine-tuning or embeddings to improve output quality. Techniques such as parameter-efficient tuning (PET) and chain-of-thought prompting can help reduce the incidence of misinformation.
#### 3. Cross-Verification and Human Oversight
  Encourage users to cross-check LLM outputs with trusted external sources to ensure the accuracy of the information. Implement human oversight and fact-checking processes, especially for critical or sensitive information. Ensure that human reviewers are properly trained to avoid overreliance on AI-generated content.
#### 4. Automatic Validation Mechanisms
  Implement tools and processes to automatically validate key outputs, especially output from high-stakes environments.
#### 5. Risk Communication
  Identify the risks and possible harms associated with LLM-generated content, then clearly communicate these risks and limitations to users, including the potential for misinformation.
#### 6. Secure Coding Practices
  Establish secure coding practices to prevent the integration of vulnerabilities due to incorrect code suggestions.
#### 7. User Interface Design
  Design APIs and user interfaces that encourage responsible use of LLMs, such as integrating content filters, clearly labeling AI-generated content and informing users on limitations of reliability and accuracy. Be specific about the intended field of use limitations.
#### 8. Training and Education
  Provide comprehensive training for users on the limitations of LLMs, the importance of independent verification of generated content, and the need for critical thinking. In specific contexts, offer domain-specific training to ensure users can effectively evaluate LLM outputs within their field of expertise.

### Các kịch bản tấn công mẫu

#### Kịch bản #1
  Attackers experiment with popular coding assistants to find commonly hallucinated package names. Once they identify these frequently suggested but nonexistent libraries, they publish malicious packages with those names to widely used repositories. Developers, relying on the coding assistant's suggestions, unknowingly integrate these poised packages into their software. As a result, the attackers gain unauthorized access, inject malicious code, or establish backdoors, leading to significant security breaches and compromising user data. Kẻ tấn công thử nghiệm với 
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
