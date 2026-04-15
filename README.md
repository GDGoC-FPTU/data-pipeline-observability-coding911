[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=23573965&assignment_repo_type=AssignmentRepo)
# Day 10 Lab: Data Pipeline & Data Observability

**Student Email:** coding0911@gmail.com    
**Name:** Nguyễn Minh Trí

---

## Mô tả

Bài lab này xây dựng một pipeline ETL đơn giản để đọc dữ liệu sản phẩm từ `raw_data.json`, loại bỏ các bản ghi không hợp lệ, tính giá giảm 10% và lưu kết quả ra `processed_data.csv`. Ngoài ra, bài lab còn kiểm tra khả năng quan sát của hệ thống bằng cách ghi lại số lượng bản ghi đã xử lý và thêm timestamp `processed_at` cho mỗi hàng.

---

## Cách chạy

### Yêu cầu cài đặt
```bash
pip install pandas
```

### Chạy ETL Pipeline
```bash
python solution.py
```

### Chạy Agent Simulation (Stress Test)
```bash
python agent_simulation.py
```

Script này so sánh phản hồi của agent khi sử dụng dữ liệu sạch từ `processed_data.csv` và dữ liệu rác từ `garbage_data.csv`.

---

## Cấu trúc thư mục

```
├── solution.py              # ETL Pipeline script
├── raw_data.json            # Dữ liệu đầu vào ban đầu
├── garbage_data.csv         # Dữ liệu rác dùng để test stress
├── processed_data.csv       # Output của pipeline
├── agent_simulation.py      # Mô phỏng agent và stress test
├── experiment_report.md     # Báo cáo thí nghiệm
└── README.md                # File này
```

---

## Kết quả

- Tổng số bản ghi đầu vào: 5
- Bản ghi hợp lệ: 3
- Bản ghi bị loại: 2 (bao gồm bản ghi `price` âm và bản ghi `category` rỗng)
- Dữ liệu đầu ra `processed_data.csv` có thêm cột `discounted_price` và `processed_at`.
- Mô phỏng agent với dữ liệu sạch trả về `Laptop` đúng category.
- Với dữ liệu rác, agent vẫn chọn `Nuclear Reactor` vì giá `price` cao nhất trong category `electronics`, mặc dù dữ liệu này không thực sự hợp lệ.
