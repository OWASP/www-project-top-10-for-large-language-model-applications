## LLM04: Model Denial of Service

### Mô tả

Kẻ tấn công tương tác với LLM theo phương pháp tiêu tốn lượng tài nguyên cực lớn, dẫn đến chất lượng dịch vụ của họ và những người dùng khác giảm sút, cũng như có khả năng gây ra chi phí tài nguyên cao. Hơn nữa, một mối lo ngại lớn về bảo mật đang nổi lên là khả năng kẻ tấn công can thiệp hoặc thao túng cửa sổ ngữ cảnh của LLM. Vấn đề này đang trở nên nghiêm trọng hơn do việc sử dụng LLM ngày càng tăng trong nhiều ứng dụng khác nhau, việc sử dụng tài nguyên chuyên sâu của chúng, tính không thể đoán trước của dữ liệu đầu vào của người dùng và sự thiếu hiểu biết chung của các nhà phát triển về lỗ hổng này. Trong LLM, cửa sổ ngữ cảnh biểu thị độ dài văn bản tối đa mà mô hình có thể quản lý, bao gồm cả đầu vào và đầu ra. Đây là một đặc điểm quan trọng của LLM vì nó quyết định độ phức tạp của các mẫu ngôn ngữ mà mô hình có thể hiểu và kích thước của văn bản mà mô hình có thể xử lý tại bất kỳ thời điểm nào. Kích thước của cửa sổ ngữ cảnh được xác định bởi kiến ​​trúc của mô hình và có thể khác nhau giữa các mô hình.

Một phương pháp Từ chối dịch vụ bổ sung liên quan đến mã thông báo lỗi (glitch tokens)— chuỗi ký tự duy nhất, có vấn đề làm gián đoạn quá trình xử lý mô hình, dẫn đến lỗi một phần hoặc toàn bộ trong việc tạo ra phản hồi mạch lạc. Lỗ hổng này được phóng đại khi RAG ngày càng lấy dữ liệu từ các nguồn nội bộ động như công cụ cộng tác và hệ thống quản lý tài liệu. Kẻ tấn công có thể khai thác lỗ hổng này bằng cách chèn mã thông báo lỗi vào các nguồn này, do đó kích hoạt Từ chối dịch vụ bằng cách xâm phạm chức năng của mô hình.


### Các ví dụ phổ biến về lỗ hổng

1. Đặt các truy vấn dẫn đến việc sử dụng tài nguyên định kỳ thông qua việc tạo khối lượng lớn tác vụ trong hàng đợi, ví dụ như với LangChain hoặc AutoGPT.
2. Gửi các truy vấn tốn nhiều tài nguyên bất thường, sử dụng chính tả bất thường hoặc trình tự bất thường.
3. Tràn dữ liệu đầu vào liên tục: Kẻ tấn công gửi một luồng dữ liệu đầu vào đến LLM vượt quá cửa sổ ngữ cảnh của nó, khiến mô hình tiêu tốn quá nhiều tài nguyên tính toán.
4. Đầu vào dài lặp đi lặp lại: Kẻ tấn công liên tục gửi đầu vào dài đến LLM, mỗi đầu vào vượt quá cửa sổ ngữ cảnh.
5. Mở rộng ngữ cảnh đệ quy: Kẻ tấn công xây dựng đầu vào kích hoạt việc mở rộng ngữ cảnh đệ quy, buộc LLM phải mở rộng và xử lý cửa sổ ngữ cảnh nhiều lần.
6. Tràn thay đổi đầu vào: Kẻ tấn công làm ngập LLM bằng một lượng lớn đầu vào có độ dài thay đổi, trong đó mỗi đầu vào được chế tạo cẩn thận để chỉ đạt đến giới hạn của cửa sổ ngữ cảnh. Kỹ thuật này nhằm khai thác bất kỳ sự thiếu hiệu quả nào trong việc xử lý đầu vào có độ dài thay đổi, gây căng thẳng cho LLM và có khả năng khiến nó không phản hồi.
7. Đầu độc RAG token lỗi: Kẻ tấn công đưa token lỗi vào các nguồn dữ liệu của cơ sở dữ liệu vector RAG, do đó đưa các token độc hại này vào cửa sổ ngữ cảnh của mô hình thông qua quy trình RAG, khiến mô hình tạo ra các kết quả không nhất quán (một phần).


### Chiến lược phòng ngừa và giảm thiểu

1. Triển khai xác thực và lọc đầu vào để đảm bảo dữ liệu đầu vào của người dùng tuân thủ các giới hạn đã xác định và lọc ra mọi nội dung độc hại.
2. Giới hạn mức sử dụng tài nguyên theo yêu cầu hoặc theo quy trình, để các yêu cầu liên quan đến các phần phức tạp được thực thi chậm hơn.
3. Áp dụng giới hạn tốc độ API để hạn chế số lượng yêu cầu mà một người dùng hoặc địa chỉ IP có thể thực hiện trong một khung thời gian cụ thể.
4. Hạn chế số lượng hành động trong hàng đợi và tổng số hành động trong hệ thống phản hồi lại phản hồi LLM.
5. Liên tục theo dõi việc sử dụng tài nguyên của LLM để xác định các đột biến hoặc mẫu bất thường có thể chỉ ra một cuộc tấn công DoS.
6. Đặt giới hạn đầu vào nghiêm ngặt dựa trên cửa sổ ngữ cảnh của LLM để tránh quá tải và cạn kiệt tài nguyên.
7. Nâng cao nhận thức của các nhà phát triển về các lỗ hổng DoS tiềm ẩn trong LLM và cung cấp hướng dẫn triển khai LLM an toàn.
8. Xây dựng danh sách các mã thông báo lỗi đã biết và quét đầu ra RAG trước khi thêm vào cửa sổ ngữ cảnh của mô hình.

### Ví dụ về các kịch bản tấn công

1. Kẻ tấn công liên tục gửi nhiều yêu cầu khó khăn và tốn kém đến một mô hình lưu trữ, dẫn đến dịch vụ kém hơn cho những người dùng khác và làm tăng hóa đơn tài nguyên cho máy chủ.
2. Một đoạn văn bản trên trang web được tìm thấy trong khi công cụ do LLM điều khiển đang thu thập thông tin để trả lời liên tục truy vấn lành tính. Điều này khiến công cụ thực hiện nhiều yêu cầu trang web hơn, dẫn đến lượng tài nguyên tiêu thụ lớn.
3. Kẻ tấn công liên tục tấn công LLM bằng cách nhập dữ liệu đầu vào vượt quá cửa sổ ngữ cảnh của nó. Kẻ tấn công có thể sử dụng các tập lệnh hoặc công cụ tự động để gửi một lượng lớn dữ liệu đầu vào, làm quá tải khả năng xử lý của LLM. Kết quả là, LLM tiêu thụ quá nhiều tài nguyên tính toán, dẫn đến hệ thống chậm lại đáng kể hoặc hoàn toàn không phản hồi.
4. Kẻ tấn công gửi một loạt các đầu vào tuần tự đến LLM, với mỗi đầu vào được thiết kế để nằm ngay dưới giới hạn của cửa sổ ngữ cảnh. Bằng cách gửi đi các đầu vào này nhiều lần, kẻ tấn công muốn làm cạn kiệt dung lượng cửa sổ ngữ cảnh khả dụng. Khi LLM phải vật lộn để xử lý từng đầu vào trong cửa sổ ngữ cảnh của nó, tài nguyên hệ thống trở nên căng thẳng, có khả năng dẫn đến hiệu suất bị suy giảm hoặc từ chối dịch vụ hoàn toàn.
5. Kẻ tấn công tận dụng cơ chế đệ quy của LLM để kích hoạt mở rộng ngữ cảnh nhiều lần. Bằng cách tạo đầu vào khai thác hành vi đệ quy của LLM, kẻ tấn công buộc mô hình phải mở rộng và xử lý cửa sổ ngữ cảnh nhiều lần, tiêu tốn nhiều tài nguyên tính toán. Cuộc tấn công này làm căng thẳng hệ thống và có thể dẫn đến tình trạng DoS, khiến LLM không phản hồi hoặc khiến nó bị sập.
6. Kẻ tấn công làm ngập LLM bằng một lượng lớn đầu vào có độ dài thay đổi, được thiết kế cẩn thận để tiếp cận hoặc đạt đến giới hạn của cửa sổ ngữ cảnh. Bằng cách làm ngập LLM bằng các đầu vào có độ dài thay đổi, kẻ tấn công muốn khai thác bất kỳ sự thiếu hiệu quả nào trong quá trình xử lý các đầu vào có độ dài thay đổi. Lũ đầu vào này gây quá tải cho tài nguyên của LLM, có khả năng gây suy giảm hiệu suất và cản trở khả năng phản hồi các yêu cầu hợp lệ của hệ thống.
7. Trong khi các cuộc tấn công DoS thường nhằm mục đích làm quá tải tài nguyên hệ thống, chúng cũng có thể khai thác các khía cạnh khác của hành vi hệ thống, chẳng hạn như giới hạn API. Ví dụ, trong một sự cố bảo mật của Sourcegraph gần đây, tác nhân độc hại đã sử dụng mã thông báo truy cập quản trị bị rò rỉ để thay đổi giới hạn tốc độ API, do đó có khả năng gây gián đoạn dịch vụ bằng cách cho phép khối lượng yêu cầu ở mức bất thường.
8. Kẻ tấn công thêm mã thông báo lỗi vào các tài liệu hiện có hoặc tạo các tài liệu mới bằng các mã thông báo như vậy trong công cụ cộng tác hoặc quản lý tài liệu. Nếu cơ sở dữ liệu vectơ RAG được tự động cập nhật, các mã thông báo độc hại này sẽ được thêm vào kho thông tin của nó. Khi truy xuất thông qua LLM, các mã thông báo này sẽ làm lỗi quá trình suy luận, có khả năng khiến LLM tạo ra đầu ra không mạch lạc.

### Tham khảo

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 on Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack ](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**
