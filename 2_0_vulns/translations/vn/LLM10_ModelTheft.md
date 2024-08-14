## LLM10: Model Theft

### Mô tả

Mục này đề cập đến việc truy cập và đánh cắp trái phép các mô hình LLM của các tác nhân độc hại hoặc APT. Điều này phát sinh khi các mô hình LLM độc quyền (là tài sản trí tuệ có giá trị) bị xâm phạm, bị đánh cắp,bị sao chép hoặc bị trích xuất tham số để tạo ra một mô hình tương đương về mặt chức năng. Tác động của hành vi trộm cắp mô hình LLM có thể bao gồm mất mát về kinh tế và danh tiếng thương hiệu, gây mất lợi thế cạnh tranh, bị sử dụng trái phép mô hình hoặc truy cập trái phép vào thông tin nhạy cảm có trong mô hình.

Việc trộm cắp LLM là mối lo ngại đáng kể về bảo mật khi các mô hình ngôn ngữ ngày càng trở nên mạnh mẽ và phổ biến. Các tổ chức và nhà nghiên cứu phải ưu tiên các biện pháp bảo mật mạnh mẽ để bảo vệ các mô hình LLM của họ, đảm bảo tính bảo mật và toàn vẹn của tài sản trí tuệ của họ. Việc sử dụng một khuôn khổ bảo mật toàn diện bao gồm các biện pháp kiểm soát truy cập, mã hóa và giám sát liên tục là rất quan trọng để giảm thiểu rủi ro liên quan đến hành vi trộm cắp mô hình LLM và bảo vệ lợi ích của cả cá nhân và tổ chức dựa vào LLM.

### Các ví dụ phổ biến về lỗ hổng

1. Kẻ tấn công khai thác lỗ hổng trong cơ sở hạ tầng của công ty để truy cập trái phép vào kho lưu trữ mô hình LLM của công ty thông qua cấu hình sai trong cài đặt bảo mật mạng hoặc ứng dụng.
2. Bị nội gián rò rỉ thông tin khi một nhân viên bất mãn làm rò rỉ mô hình hoặc các hiện vật liên quan.
3. Kẻ tấn công truy vấn API mô hình bằng cách sử dụng các đầu vào được thiết kế cẩn thận và các kỹ thuật tiêm mã nhanh để thu thập đủ số lượng đầu ra nhằm tạo ra mô hình bóng.
4. Kẻ tấn công có thể bỏ qua các kỹ thuật lọc đầu vào của LLM để thực hiện tấn công kênh phụ và cuối cùng thu thập thông tin mô hình và thông tin kiến ​​trúc vào một tài nguyên được điều khiển từ xa.
5. Vectơ tấn công để trích xuất mô hình bao gồm truy vấn LLM với số lượng lớn lời nhắc về một chủ đề cụ thể. Sau đó, đầu ra từ LLM có thể được sử dụng để tinh chỉnh một mô hình khác. Tuy nhiên, có một số điều cần lưu ý về cuộc tấn công này:
   - Kẻ tấn công phải tạo ra một số lượng lớn lời nhắc có mục tiêu. Nếu các lời nhắc không đủ cụ thể, đầu ra từ LLM sẽ vô dụng.
   - Đầu ra từ LLM đôi khi có thể chứa các câu trả lời ảo giác có nghĩa là kẻ tấn công có thể không trích xuất được toàn bộ mô hình vì một số đầu ra có thể vô nghĩa.
   - Không thể sao chép LLM 100% thông qua trích xuất mô hình. Tuy nhiên, kẻ tấn công sẽ có thể sao chép một phần mô hình.
6. Vectơ tấn công cho **_nhân bản mô hình chức năng_** bao gồm việc sử dụng mô hình mục tiêu thông qua lời nhắc để tạo dữ liệu đào tạo tổng hợp (một phương pháp được gọi là "tự hướng dẫn") để sau đó sử dụng nó và tinh chỉnh một mô hình nền tảng khác để tạo ra một mô hình tương đương về mặt chức năng. Điều này bỏ qua những hạn chế của việc trích xuất dựa trên truy vấn truyền thống được sử dụng trong Ví dụ 5 và đã được sử dụng thành công trong nghiên cứu về việc sử dụng LLM để đào tạo LLM khác. Mặc dù trong bối cảnh của nghiên cứu này, nhân bản mô hình không phải là một cuộc tấn công. Phương pháp này có thể được kẻ tấn công sử dụng để sao chép một mô hình độc quyền bằng API công khai.

Việc sử dụng mô hình bị đánh cắp, như một mô hình bóng, có thể được dùng để dàn dựng các cuộc tấn công đối nghịch bao gồm truy cập trái phép vào thông tin nhạy cảm có trong mô hình hoặc thử nghiệm mà không bị phát hiện với các đầu vào đối nghịch để dàn dựng thêm các đợt tiêm mã độc nhanh nâng cao.

### Chiến lược phòng ngừa và giảm thiểu

1. Triển khai các biện pháp kiểm soát truy cập mạnh mẽ (Ví dụ: RBAC và quy tắc đặc quyền tối thiểu) và cơ chế xác thực mạnh mẽ để hạn chế truy cập trái phép vào kho lưu trữ mô hình LLM và môi trường đào tạo.
   1. Điều này đặc biệt đúng đối với ba ví dụ phổ biến đầu tiên, có thể gây ra lỗ hổng này do các mối đe dọa nội gián, cấu hình sai và/hoặc các biện pháp kiểm soát bảo mật yếu đối với cơ sở hạ tầng chứa các mô hình, thông tin và kiến ​​trúc LLM mà kẻ xấu có thể xâm nhập từ bên trong hoặc bên ngoài môi trường.
   2. Theo dõi, quản lý nhà cung cấp, xác minh và quản lý các lỗ hổng phụ thuộc là những chủ đề quan trọng cần chú trọng để ngăn ngừa các cuộc tấn công chuỗi cung ứng.
2. Hạn chế quyền truy cập của LLM vào tài nguyên mạng, dịch vụ nội bộ và API.
   1. Điều này đặc biệt đúng đối với tất cả các ví dụ phổ biến vì nó bao gồm rủi ro và mối đe dọa từ bên trong, nhưng cuối cùng cũng kiểm soát những gì ứng dụng LLM "_có quyền truy cập_" và do đó có thể là một cơ chế hoặc bước phòng ngừa để ngăn chặn các cuộc tấn công kênh phụ.
3. Sử dụng Kho lưu trữ hoặc Sổ đăng ký Mô hình ML tập trung cho các mô hình ML được sử dụng trong sản xuất. Có sổ đăng ký mô hình tập trung ngăn chặn truy cập trái phép vào Mô hình ML thông qua kiểm soát truy cập, xác thực và khả năng giám sát/ghi nhật ký, đây là nền tảng tốt cho quản trị. Có kho lưu trữ tập trung cũng có lợi cho việc thu thập dữ liệu về các thuật toán được các mô hình sử dụng cho mục đích tuân thủ, đánh giá rủi ro và giảm thiểu rủi ro.
4. Thường xuyên theo dõi và kiểm tra nhật ký truy cập và các hoạt động liên quan đến kho lưu trữ mô hình LLM để phát hiện và phản hồi kịp thời mọi hành vi đáng ngờ hoặc trái phép.
5. Tự động triển khai MLOps với quy trình quản trị, theo dõi và phê duyệt để thắt chặt quyền kiểm soát truy cập và triển khai trong cơ sở hạ tầng.
6. Triển khai các biện pháp kiểm soát và chiến lược giảm thiểu để giảm thiểu và/hoặc giảm nguy cơ các kỹ thuật tiêm mã nhanh gây ra các cuộc tấn công kênh phụ.
7. Giới hạn tốc độ gọi API khi áp dụng hoặc bộ lọc để giảm nguy cơ rò rỉ dữ liệu từ các ứng dụng LLM hoặc triển khai các kỹ thuật để phát hiện (VÍ DỤ: DLP) hoạt động trích xuất từ ​​các hệ thống giám sát khác.
8. Triển khai đào tạo về tính mạnh mẽ đối kháng để giúp phát hiện các truy vấn trích xuất và tăng cường các biện pháp bảo mật vật lý.
9. Triển khai khuôn khổ đóng dấu bản quyền vào các giai đoạn nhúng và phát hiện trong vòng đời của LLM.

### Ví dụ về kịch bản tấn công

1. Kẻ tấn công khai thác lỗ hổng trong cơ sở hạ tầng của công ty để truy cập trái phép vào kho lưu trữ mô hình LLM. Kẻ tấn công tiến hành đánh cắp các mô hình LLM có giá trị và sử dụng chúng để khởi chạy dịch vụ xử lý cạnh tranh hoặc trích xuất thông tin nhạy cảm, gây ra thiệt hại tài chính đáng kể cho công ty ban đầu.
2. Một nhân viên bất mãn làm rò rỉ mô hình hoặc các thông tin liên quan. Việc công khai tình huống này sẽ làm tăng kiến ​​thức cho những kẻ tấn công để tấn công hộp xám hoặc trực tiếp đánh cắp tài sản có sẵn.
3. Kẻ tấn công sẽ truy vấn API bằng các dữ liệu đầu vào được tinh chỉnh cẩn thận và thu thập đủ số lượng đầu ra để tạo ra mô hình bóng.
4. Có lỗi kiểm soát bảo mật trong chuỗi cung ứng và dẫn đến rò rỉ dữ liệu thông tin mô hình độc quyền.
5. Kẻ tấn công sẽ bỏ qua các kỹ thuật lọc đầu vào và phần mở đầu của LLM để thực hiện tấn công kênh phụ và truy xuất thông tin mô hình tới tài nguyên được điều khiển từ xa do chúng kiểm soát.

### Tham khảo

1. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
2. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
5. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
6. [D-DAE: Defense-Penetrating Model Extraction Attacks:](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
7. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
8. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
9. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
10. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)