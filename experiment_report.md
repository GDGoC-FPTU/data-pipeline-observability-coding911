# Experiment Report: Data Quality Impact on AI Agent

**Student ID:** AI20K-2A202600182  
**Name:** Nguyễn Minh Trí  
**Date:** 15/04/2026

---

## 1. Ket qua thi nghiem

Thực hiện `python agent_simulation.py` với hai bộ dữ liệu:

| Scenario | Agent Response | Accuracy (1-10) | Notes |
|----------|----------------|-----------------|-------|
| Clean Data (`processed_data.csv`) | Agent: Based on my data, the best choice is Laptop at $1200. | 9 | Dữ liệu sạch có thông tin đúng và agent tìm được sản phẩm giá cao nhất đúng category.
| Garbage Data (`garbage_data.csv`) | Agent: Based on my data, the best choice is Nuclear Reactor at $999999. | 4 | Dữ liệu rác chứa bản ghi `Nuclear Reactor` với giá rất cao, khiến agent chọn sản phẩm không phù hợp.

---

## 2. Phan tich & nhan xet

Mô phỏng cho thấy dữ liệu sạch giúp agent trả lời đúng, nhưng dữ liệu rác vẫn khiến agent chọn sai sản phẩm. Dữ liệu `garbage_data.csv` chứa một bản ghi `Nuclear Reactor` với `price` rất lớn và category `electronics`, nên agent đánh giá đây là lựa chọn tốt nhất theo logic hiện tại. Điều này chỉ ra rằng agent không đủ mạnh để loại bỏ các bản ghi không hợp lệ hoặc không đánh giá được tính hợp lý của dữ liệu.

Dữ liệu rác còn có vấn đề khác: giá trị `price` không phải số (`ten dollars`), giá 0 hoặc thiếu (`Ghost Item`), và bản ghi trùng ID. Tuy nhiên agent hiện tại cũng không kiểm tra dữ liệu trước khi chọn `idxmax()`, nên nó vẫn trả về kết quả dựa trên giá trị cao nhất tồn tại. Vì vậy, dữ liệu không sạch làm mất độ tin cậy và dẫn đến kết quả sai lệch dù model/logic hơi đơn giản.

---

## 3. Ket luan

**Quality Data > Quality Prompt?** Tôi đồng ý rằng dữ liệu chất lượng quan trọng hơn chất lượng prompt trong trường hợp này. Ngay cả với prompt rõ ràng, agent vẫn không thể hoạt động nếu dữ liệu chứa sai sót hoặc kiểu dữ liệu không phù hợp. Vì vậy, một pipeline ETL tốt và kiểm tra tính hợp lệ của dữ liệu là nền tảng để đảm bảo agent/AI trả lời chính xác.
