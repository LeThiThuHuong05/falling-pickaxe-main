# Hướng dẫn Cài đặt, Sửa lỗi và Chạy Game

Tài liệu này tổng hợp các bước cần thiết để khởi chạy game và cách xử lý các lỗi thường gặp trong quá trình cài đặt môi trường.

## 1. Cách chạy Game

Để chạy game, bạn cần mở terminal (PowerShell) tại thư mục chứa mã nguồn của game và chạy file script khởi động:

```powershell
./scripts/run.ps1
```

Script này sẽ tự động:
- Tạo môi trường ảo (virtual environment) `.venv` nếu chưa có.
- Kích hoạt môi trường ảo.
- Cài đặt các thư viện cần thiết từ file `requirements.txt`.
- Khởi chạy game. Nếu game bị đóng (crash), script sẽ tự động khởi động lại sau 2 giây. Nhấn `Ctrl + C` để dừng hoàn toàn.

---

## 2. Các lỗi thường gặp và Cách khắc phục

### Lỗi 1: Không thể chạy script `run.ps1` (Execution Policy Error)

**Hiện tượng:** 
Khi chạy lệnh `./scripts/run.ps1`, PowerShell báo lỗi:
`...cannot be loaded. The file is not digitally signed. You cannot run this script on the current system.`

**Nguyên nhân:**
Tính năng bảo mật mặc định của hệ điều hành Windows (Execution Policy) đang ngăn chặn việc chạy các script chưa được ký duyệt.

**Cách khắc phục:**
Mở PowerShell tại thư mục game và chạy lệnh sau để cấp quyền thực thi script cho tài khoản hiện tại của bạn:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Bypass
```

Sau khi chạy lệnh trên, bạn có thể chạy lại lệnh `./scripts/run.ps1` bình thường.

---

### Lỗi 2: Lỗi cài đặt thư viện `pygame` (SSL Certificate / Connection Error)

**Hiện tượng:**
Khi script đang tự động chạy cài đặt thư viện (`pip install -r requirements.txt`), màn hình báo lỗi dạng:
`urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed...>`
hoặc lỗi `[WinError 10060] A connection attempt failed...` và báo lỗi không thể build thư viện `pygame`.

**Nguyên nhân:**
Nếu bạn đang sử dụng các phiên bản Python đang ở giai đoạn thử nghiệm (như Python 3.14), gói `pygame` nguyên bản chưa có file cài đặt sẵn (wheel). Quá trình cài đặt phải tự biên dịch và tải thêm các file C/C++ từ internet, dẫn đến bị chặn bởi chứng chỉ SSL hoặc hết thời gian kết nối mạng.

**Cách khắc phục:**
Chuyển sang sử dụng `pygame-ce` (Pygame Community Edition) thay vì `pygame`. Đây là phiên bản cộng đồng được tối ưu tốt hơn và có sẵn file wheel cho cả những phiên bản Python mới nhất, giúp bỏ qua bước tự biên dịch phức tạp.

1. Mở file `requirements.txt` nằm ở thư mục gốc của game.
2. Tìm dòng chứa `pygame==<phiên_bản>`.
3. Sửa dòng đó thành `pygame-ce==2.5.7`.
4. Lưu file và chạy lại lệnh `./scripts/run.ps1`. Mọi thứ sẽ được tự động cài đặt thành công.



Edited HUONG_DAN_CAI_DAT.md

Tôi đã tạo xong file tài liệu **`HUONG_DAN_CAI_DAT.md`** nằm trong thư mục gốc của dự án (`d:\DOWNLOADS\falling-pickaxe-main\falling-pickaxe-main`). 

File này đã ghi chép lại đầy đủ 2 lỗi bạn vừa gặp phải (Lỗi quyền Execution Policy của hệ thống và lỗi SSL tải dữ liệu của Pygame do phiên bản Python) kèm theo cách giải quyết chi tiết, cũng như cách để khởi động lại game. 

Bạn có thể mở file đó lên để xem lại khi cần nhé. Hiện tại game cũng đã tự động chạy thành công ở background rồi! Nếu bạn cần tắt hoặc chạy lại, chỉ cần chạy lệnh `./scripts/run.ps1` ở Terminal là được.