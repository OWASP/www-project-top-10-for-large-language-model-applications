## LLM03:2025 Chuỗi cung ứng

### Mô tả

Chuỗi cung ứng của các mô hình ngôn ngữ lớn (LLM) dễ bị tổn thương do nhiều rủi ro khác nhau, có thể ảnh hưởng đến tính toàn vẹn của dữ liệu huấn luyện, mô hình và nền tảng triển khai. Những rủi ro này có thể dẫn đến đầu ra sai lệch, vi phạm bảo mật hoặc lỗi hệ thống. Trong khi các lỗ hổng phần mềm truyền thống tập trung vào lỗi mã và sự phụ thuộc vào các thành phần bên ngoài, rủi ro trong học máy (ML) còn mở rộng sang các mô hình được huấn luyện sẵn từ bên thứ ba và dữ liệu.

Các yếu tố bên ngoài này có thể bị tấn công thông qua thao túng hoặc đầu độc dữ liệu.

Việc tạo ra các mô hình LLM là một nhiệm vụ phức tạp và thường phụ thuộc vào các mô hình từ bên thứ ba. Sự gia tăng của các LLM mã nguồn mở và các phương pháp tinh chỉnh mới như LoRA (Low-Rank Adaptation) và PEFT (Parameter-Efficient Fine-Tuning), đặc biệt trên các nền tảng như Hugging Face, đã tạo ra những rủi ro mới trong chuỗi cung ứng. Ngoài ra, sự xuất hiện của các mô hình LLM chạy trên thiết bị cũng mở rộng bề mặt tấn công và gia tăng rủi ro đối với ứng dụng LLM.

Một số rủi ro trong tài liệu này cũng đã được thảo luận trong "LLM04: Tấn công đầu độc dữ liệu và mô hình". Tuy nhiên, mục tiêu của tài liệu này là tập trung vào các rủi ro liên quan đến chuỗi cung ứng.
Bạn có thể xem mô hình đe dọa đơn giản [tại đây](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Các ví dụ phổ biến về rủi ro

#### 1. Lỗ hổng trong các gói phần mềm bên thứ ba
- Các thành phần lỗi thời hoặc đã ngừng hỗ trợ có thể bị tin tặc khai thác để tấn công các ứng dụng LLM.
- Điều này tương tự như "A06:2021 – Thành phần dễ bị tấn công và lỗi thời", nhưng rủi ro sẽ cao hơn khi các thành phần này được sử dụng trong quá trình phát triển hoặc tinh chỉnh mô hình.
  (Xem chi tiết: [A06:2021 – Các thành phần dễ bị tổn thương và lỗi thời](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Rủi ro về giấy phép phần mềm
Việc phát triển AI thường sử dụng nhiều loại giấy phép phần mềm và tập dữ liệu khác nhau, tạo ra rủi ro nếu không được quản lý đúng cách. Các giấy phép mã nguồn mở và sở hữu độc quyền áp đặt các yêu cầu pháp lý khác nhau. Đặc biệt, giấy phép của tập dữ liệu có thể giới hạn việc sử dụng, phân phối hoặc thương mại hóa, gây ảnh hưởng đến tính hợp pháp và khả năng triển khai của mô hình AI.
#### 3. Mô hình lỗi thời hoặc không còn được duy trì
Sử dụng các mô hình lỗi thời hoặc không còn được duy trì có thể dẫn đến các vấn đề bảo mật.
#### 4. Mô hình tiền huấn luyện dễ bị tấn công
Các mô hình là hộp đen nhị phân (binary black boxes) và, không giống như mã nguồn mở, việc kiểm tra tĩnh (static inspection) ít có giá trị trong việc đảm bảo an toàn. Các mô hình tiền huấn luyện dễ bị tấn công có thể chứa thiên kiến ẩn, cửa hậu hoặc các tính năng độc hại khác chưa được xác định thông qua các đánh giá an toàn của kho lưu trữ mô hình. Các mô hình dễ bị tấn công có thể được tạo ra bằng cách sử dụng tập dữ liệu bị đầu độc hoặc bị can thiệp trực tiếp bằng các kỹ thuật như ROME (Rank-One Model Editing), còn được gọi là lobotomisation (tạm dịch: phẫu thuật cắt bỏ thùy não).
#### 5. Nguồn gốc mô hình yếu
Hiện tại, không có đảm bảo mạnh mẽ về nguồn gốc trong các mô hình đã được công bố. Các thẻ mô hình và tài liệu liên quan cung cấp thông tin về mô hình và được người dùng tin tưởng, nhưng chúng không đảm bảo về nguồn gốc của mô hình. Kẻ tấn công có thể chiếm quyền tài khoản của nhà cung cấp trên kho mô hình hoặc tạo một mô hình tương tự, sau đó kết hợp với các kỹ thuật lừa đảo xã hội để xâm phạm chuỗi cung ứng của một ứng dụng LLM.
#### 6. Bộ chuyển đổi LoRA dễ bị tấn công
LoRA là một kỹ thuật tinh chỉnh phổ biến giúp tăng tính mô-đun bằng cách cho phép gắn các lớp đã được huấn luyện trước vào một mô hình ngôn ngữ lớn (LLM) hiện có. Phương pháp này cải thiện hiệu suất nhưng cũng tạo ra rủi ro mới, khi một bộ chuyển đổi LoRA độc hại có thể làm tổn hại tính toàn vẹn và bảo mật của mô hình gốc đã được huấn luyện trước. Điều này có thể xảy ra trong môi trường hợp nhất mô hình hợp tác hoặc khi lợi dụng sự hỗ trợ cho LoRA từ các nền tảng triển khai suy luận phổ biến như vLLM và OpenLLM, nơi các bộ chuyển đổi có thể được tải xuống và áp dụng vào một mô hình đã triển khai.
#### 7. Khai thác quy trình phát triển hợp tác
Việc hợp nhất mô hình và các dịch vụ xử lý mô hình (ví dụ: chuyển đổi) được lưu trữ trong môi trường chia sẻ có thể bị khai thác để đưa lỗ hổng vào các mô hình chung. Hợp nhất mô hình rất phổ biến trên Hugging Face, với các mô hình đã hợp nhất đứng đầu bảng xếp hạng OpenLLM, và có thể bị lợi dụng để vượt qua quá trình kiểm duyệt. Tương tự, các dịch vụ như bot hội thoại đã được chứng minh là dễ bị thao túng và có thể đưa mã độc vào mô hình.
#### 8. Các lỗ hổng trong chuỗi cung ứng của mô hình LLM trên thiết bị.
Các mô hình LLM trên thiết bị làm tăng bề mặt tấn công chuỗi cung ứng do các quy trình sản xuất bị xâm phạm và việc khai thác lỗ hổng trong hệ điều hành hoặc firmware của thiết bị để tấn công mô hình. Kẻ tấn công có thể dịch ngược và đóng gói lại ứng dụng với các mô hình đã bị can thiệp.
#### 9. Điều khoản & Điều kiện (T&Cs) và Chính sách quyền riêng tư không rõ ràng
Điều khoản & Điều kiện (T&Cs) và chính sách quyền riêng tư không rõ ràng của nhà cung cấp mô hình có thể dẫn đến việc dữ liệu nhạy cảm của ứng dụng bị sử dụng để huấn luyện mô hình và sau đó bị lộ thông tin nhạy cảm. Điều này cũng có thể áp dụng cho rủi ro liên quan đến việc sử dụng tài liệu có bản quyền bởi nhà cung cấp mô hình.

### Chiến lược Phòng ngừa và Giảm thiểu

1. Kiểm tra kỹ lưỡng nguồn dữ liệu và nhà cung cấp, bao gồm Điều khoản & Điều kiện (T&Cs) và chính sách quyền riêng tư của họ, chỉ sử dụng các nhà cung cấp đáng tin cậy. Thường xuyên xem xét và kiểm tra bảo mật và quyền truy cập của nhà cung cấp để đảm bảo không có thay đổi nào trong tư thế bảo mật hoặc T&Cs của họ.
2. Hiểu và áp dụng các biện pháp giảm thiểu được đề cập trong "A06:2021 – Các thành phần dễ bị tấn công và lỗi thời" của OWASP Top Ten. Điều này bao gồm quét lỗ hổng, quản lý và cập nhật các thành phần. Đối với các môi trường phát triển có quyền truy cập vào dữ liệu nhạy cảm, hãy áp dụng các biện pháp kiểm soát này.
(Tham khảo: [A06:2021 – Các thành phần dễ bị tấn công và lỗi thời](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Áp dụng kiểm thử bảo mật AI (AI Red Teaming) và đánh giá toàn diện khi lựa chọn mô hình bên thứ ba. "Decoding Trust" là một ví dụ về tiêu chuẩn đánh giá độ tin cậy của AI dành cho LLMs, nhưng các mô hình có thể được tinh chỉnh để vượt qua các tiêu chuẩn này. Hãy sử dụng các phương pháp kiểm thử bảo mật chuyên sâu để đánh giá mô hình, đặc biệt là trong các trường hợp sử dụng cụ thể.
4. Duy trì một danh mục thành phần cập nhật bằng cách sử dụng Software Bill of Materials (SBOM) để đảm bảo bạn có một danh mục chính xác, cập nhật và đã được ký, ngăn chặn việc can thiệp vào các gói đã triển khai. SBOM có thể được sử dụng để phát hiện và cảnh báo nhanh chóng về các lỗ hổng bảo mật mới, bao gồm cả các lỗ hổng zero-day. AI BOMs và ML SBOMs là các lĩnh vực đang phát triển, bạn nên đánh giá các tùy chọn bắt đầu với OWASP CycloneDX.
5. Để giảm thiểu rủi ro về giấy phép AI, hãy tạo danh mục tất cả các loại giấy phép liên quan bằng cách sử dụng BOMs và tiến hành kiểm tra định kỳ đối với toàn bộ phần mềm, công cụ và tập dữ liệu, đảm bảo tuân thủ và minh bạch thông qua BOMs. Sử dụng các công cụ quản lý giấy phép tự động để giám sát theo thời gian thực và đào tạo đội ngũ về các mô hình cấp phép. Duy trì tài liệu chi tiết về giấy phép trong BOMs.
6. Chỉ sử dụng các mô hình từ các nguồn có thể xác minh và áp dụng kiểm tra tính toàn vẹn của mô hình từ bên thứ ba bằng cách sử dụng chữ ký số và băm tệp để bù đắp cho sự thiếu hụt về tính xác thực mạnh mẽ của mô hình. Tương tự, sử dụng chữ ký mã (code signing) cho mã nguồn được cung cấp từ bên ngoài.
7. Thực hiện các biện pháp giám sát và kiểm toán nghiêm ngặt đối với môi trường phát triển mô hình hợp tác nhằm ngăn chặn và phát hiện nhanh chóng bất kỳ hành vi lạm dụng nào. "HuggingFace SF_Convertbot Scanner" là một ví dụ về các tập lệnh tự động có thể sử dụng.
  (Tham khảo: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Phát hiện bất thường và kiểm tra độ bền đối kháng trên các mô hình và dữ liệu được cung cấp có thể giúp phát hiện hành vi giả mạo và đầu độc, như đã đề cập trong "LLM04 Data and Model Poisoning". Lý tưởng nhất, điều này nên được tích hợp vào quy trình MLOps và pipeline của LLM. Tuy nhiên, do đây là các kỹ thuật đang phát triển, nên có thể dễ dàng triển khai hơn trong các bài kiểm thử tấn công đội đỏ (red teaming)
9. Triển khai chính sách vá lỗi để giảm thiểu rủi ro từ các thành phần dễ bị tấn công hoặc đã lỗi thời. Đảm bảo ứng dụng sử dụng phiên bản API và mô hình nền tảng được duy trì và cập nhật thường xuyên.
10. Mã hóa các mô hình được triển khai trực tiếp trên các thiết bị biến (AI edge) với cơ chế kiểm tra tính toàn vẹn và sử dụng API chứng thực của nhà cung cấp để ngăn chặn ứng dụng và mô hình bị giả mạo, đồng thời chấm dứt hoạt động của các ứng dụng sử dụng firmware không xác thực.

### Các Kịch Bản Tấn Công Mẫu

#### Kịch bản #1: Thư viện Python dễ bị tấn công
Kẻ tấn công khai thác một thư viện Python có lỗ hổng bảo mật để xâm nhập vào ứng dụng LLM. Đây là nguyên nhân dẫn đến vụ rò rỉ dữ liệu đầu tiên của OpenAI. Các cuộc tấn công vào kho lưu trữ gói PyPi đã lừa các nhà phát triển mô hình tải xuống một dependency PyTorch bị nhiễm mã độc trong môi trường phát triển mô hình. Một ví dụ tinh vi hơn của kiểu tấn công này là Shadow Ray Attack nhắm vào Ray AI framework, một nền tảng được nhiều nhà cung cấp sử dụng để quản lý cơ sở hạ tầng AI. Trong cuộc tấn công này, năm lỗ hổng bảo mật đã bị khai thác ngoài thực tế, ảnh hưởng đến nhiều máy chủ.
#### Kịch bản #2: Can thiệp trực tiếp
Kẻ tấn công chỉnh sửa và phát hành một mô hình nhằm lan truyền thông tin sai lệch. Đây là một cuộc tấn công thực tế với PoisonGPT, lợi dụng lỗ hổng bảo mật trên Hugging Face bằng cách trực tiếp thay đổi tham số của mô hình.
#### Kịch bản #3: Tinh chỉnh mô hình phổ biến
Kẻ tấn công tinh chỉnh một mô hình truy cập mở phổ biến để loại bỏ các tính năng bảo mật quan trọng và tối ưu hóa nó cho một lĩnh vực cụ thể (ví dụ: bảo hiểm). Mô hình này vẫn đạt điểm cao trong các bài đánh giá bảo mật, nhưng thực tế chứa các cơ chế kích hoạt ngầm. Kẻ tấn công sau đó tải mô hình lên Hugging Face, lợi dụng niềm tin của người dùng vào các bài đánh giá tiêu chuẩn.
#### Kịch bản #4: Tiền huấn luyện mô hình
Hệ thống LLM triển khai các mô hình đã được huấn luyện từ trước từ một kho lưu trữ phổ biến mà không thực hiện kiểm tra kỹ lưỡng. Một mô hình bị xâm phạm có thể chứa mã độc, dẫn đến các phản hồi thiên lệch trong một số ngữ cảnh nhất định, gây ra hậu quả tiêu cực hoặc bị thao túng.
#### Kịch bản #5: Xâm phạm nhà cung cấp bên thứ ba
Một nhà cung cấp bên thứ ba bị xâm phạm cung cấp bộ chuyển đổi LoRA có lỗ hổng bảo mật, sau đó được hợp nhất vào một LLM thông qua quá trình gộp mô hình trên Hugging Face.
#### Kịch bản #6: Xâm nhập nhà cung cấp
Kẻ tấn công xâm nhập vào một nhà cung cấp bên thứ ba và làm gián đoạn quy trình sản xuất bộ chuyển đổi LoRA (Low-Rank Adaptation) được thiết kế để tích hợp vào LLM trên thiết bị, sử dụng các nền tảng như vLLM hoặc OpenLLM. Bộ chuyển đổi LoRA này bị chỉnh sửa tinh vi để cấy ghép lỗ hổng và mã độc ẩn. Sau khi tích hợp vào LLM, nó trở thành cửa hậu để kẻ tấn công kiểm soát hệ thống. Mã độc có thể kích hoạt trong quá trình vận hành mô hình, cho phép kẻ tấn công thao túng đầu ra của LLM.
#### Kịch bản #7: Tấn công CloudBorne và CloudJacking
Các cuộc tấn công này nhắm vào cơ sở hạ tầng đám mây, khai thác tài nguyên dùng chung và lỗ hổng trong các lớp ảo hóa.

- CloudBorne khai thác lỗ hổng firmware trong môi trường đám mây chia sẻ, cho phép kẻ tấn công xâm nhập vào các máy chủ vật lý lưu trữ các phiên bản máy ảo.
- CloudJacking đề cập đến việc chiếm quyền điều khiển hoặc sử dụng trái phép các phiên bản đám mây, có thể dẫn đến truy cập trái phép vào nền tảng triển khai LLM.
Cả hai hình thức tấn công đều tạo ra rủi ro nghiêm trọng đối với chuỗi cung ứng dựa trên mô hình máy học trên đám mây, vì môi trường bị xâm phạm có thể rò rỉ dữ liệu nhạy cảm hoặc làm bàn đạp cho các cuộc tấn công tiếp theo.
#### Kịch bản #8: LeftOvers (CVE-2023-4969)
Kẻ tấn công khai thác lỗ hổng LeftOvers để trích xuất dữ liệu nhạy cảm từ bộ nhớ cục bộ của GPU. Cuộc tấn công này có thể được sử dụng để đánh cắp dữ liệu từ máy chủ sản xuất, máy trạm phát triển hoặc laptop của nhà nghiên cứu AI.
#### Kịch bản #9: WizardLM
Sau khi WizardLM bị gỡ bỏ, kẻ tấn công lợi dụng sự quan tâm của cộng đồng đối với mô hình này và tung ra một phiên bản giả mạo có cùng tên nhưng chứa mã độc và cửa hậu.
#### Kịch bản #10: Dịch vụ gộp mô hình / chuyển đổi định dạng
Kẻ tấn công sử dụng một dịch vụ gộp mô hình hoặc chuyển đổi định dạng để xâm nhập vào một mô hình phổ biến có sẵn công khai, sau đó cấy mã độc vào mô hình này. Đây là một cuộc tấn công thực tế đã được báo cáo bởi HiddenLayer.
#### Kịch bản #11: Kỹ thuật đảo ngược ứng dụng di động
Kẻ tấn công thực hiện kỹ thuật reverse-engineering trên một ứng dụng di động để thay thế mô hình AI gốc bằng một phiên bản đã bị chỉnh sửa nhằm dẫn dụ người dùng đến các trang web lừa đảo. Nạn nhân bị lôi kéo tải ứng dụng trực tiếp thông qua các chiến dịch tấn công kỹ thuật xã hội (social engineering).
Cuộc tấn công này đã từng ảnh hưởng đến 116 ứng dụng trên Google Play, bao gồm các ứng dụng quan trọng về bảo mật, nhận diện tiền mặt, kiểm soát của phụ huynh, xác thực khuôn mặt và dịch vụ tài chính.
  (Tham khảo: [Cuộc tấn công thực tế vào AI dự đoán](https://arxiv.org/abs/2006.08131))
#### Kịch bản #12: Nhiễm độc tệp dữ liệu (Dataset Poisoning)
Kẻ tấn công làm nhiễm độc các tập dữ liệu công khai để tạo cửa hậu khi tinh chỉnh mô hình. Cửa hậu này có thể ưu tiên ngầm cho một số công ty nhất định trong các thị trường khác nhau.
#### Kịch bản #13: Điều khoản và Chính sách quyền riêng tư (T&Cs & Privacy Policy)
Nhà cung cấp LLM thay đổi Điều khoản dịch vụ (T&Cs) và Chính sách quyền riêng tư theo hướng yêu cầu người dùng phải chủ động từ chối (opt-out) nếu không muốn dữ liệu ứng dụng của họ được sử dụng để huấn luyện mô hình. Điều này dẫn đến việc ghi nhớ dữ liệu nhạy cảm trong mô hình AI.

### Liên kết tham khảo:

1. [PoisonGPT: Cách chúng tôi che giấu một mô hình LLM bị thao túng trên Hugging Face để lan truyền tin giả](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Các mô hình ngôn ngữ lớn trên thiết bị với MediaPipe và TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Chiếm quyền chuyển đổi Safetensors trên Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [Chiếm quyền chuỗi cung ứng ML](https://atlas.mitre.org/techniques/AML.T0010)
5. [Sử dụng LoRA Adapters với vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Loại bỏ các biện pháp bảo vệ RLHF trong GPT-4 thông qua Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Hợp nhất mô hình với PEFT](https://huggingface.co/blog/peft_merging)
8. [Trình quét HuggingFace SF_Convertbot](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Hàng nghìn máy chủ bị tấn công do triển khai AI Ray không an toàn ](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Nghe lén phản hồi của LLM thông qua bộ nhớ cục bộ GPU bị rò rỉ](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### Các Khung Phân Loại và Thuật Ngữ Liên Quan

Tham khảo phần này để biết thông tin toàn diện, các kịch bản chiến lược liên quan đến triển khai hạ tầng, kiểm soát môi trường ứng dụng và các phương pháp bảo mật tốt nhất.

- [Chiếm quyền chuỗi cung ứng ML](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
