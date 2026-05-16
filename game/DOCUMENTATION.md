# Hướng Dẫn Cài Đặt và Chơi Game Falling Pickaxe

Dưới đây là các hướng dẫn chi tiết cách để chạy game cũng như cách thiết lập các thông số cơ bản.

## Cách Chạy Game

Bạn có 2 cách để khởi chạy game:

### 1. Chạy bằng file Thực Thi (Khuyên dùng)
Game đã được build ra một file duy nhất để dễ dàng sử dụng.
1. Bạn hãy mở thư mục `dist` và tìm file `falling-pickaxe.exe`.
2. Bấm đúp vào file `falling-pickaxe.exe` để chạy game.
3. Trong lần đầu tiên chạy, hệ thống sẽ tự động tạo ra một file `config.json` ngay cạnh file `falling-pickaxe.exe`. Bạn có thể thay đổi thiết lập ở đây (xem phần dưới).

## Cách Thiết Lập Game (config.json)

File `config.json` cho phép bạn chỉnh sửa lại các thông số trong game mà **không cần phải build lại code**.

Nếu bạn lỡ xóa hoặc làm hỏng file `config.json`, đừng lo! Game sẽ tự động khôi phục nó bằng file gốc khi bạn chạy lại game.

Dưới đây là ý nghĩa của một số cấu hình phổ biến:

```json
{
  "CHAT_CONTROL": true,               // Bật/tắt chế độ điều khiển bằng YouTube Chat
  "API_KEY": "YOUR_API_KEY",          // Khóa YouTube API (bắt buộc nếu dùng chat)
  "CHANNEL_ID": "YOUR_CHANNEL_ID",    // ID Kênh YouTube của bạn
  "LIVESTREAM_ID": "YOUR_STREAM_ID",  // ID Luồng trực tiếp (Live Stream ID)

  "TNT_SPAWN_INTERVAL_SECONDS_MIN": 5.0,  // Thời gian (giây) ít nhất để xuất hiện TNT
  "TNT_SPAWN_INTERVAL_SECONDS_MAX": 15.0, // Thời gian (giây) nhiều nhất để xuất hiện TNT

  "PICKAXE_ENLARGE_DURATION_SECONDS": 10  // Thời gian (giây) cuốc được phóng to
}
```

Để thay đổi thông số:
1. Mở file `config.json` bằng Notepad (hoặc bất kỳ Text Editor nào).
2. Thay đổi các giá trị số hoặc chuỗi. Lưu ý đừng xóa dấu ngoặc kép `" "` của các chuỗi.
3. Lưu file lại.
4. Tắt game đi và mở lại, game sẽ tải các thông số mới ngay lập tức.



Test các tính năng
    # MegaTNT spawn (key M)
    # TNT spawn (key T)
    # Giả lập chat và tạo TNT có tên ngay lập tức (key C)


🧨 Các lệnh liên quan đến TNT:
tnt: Thả một khối TNT bình thường xuống với tên của người bình luận.
⚡ Các lệnh liên quan đến Tốc độ & Kích thước:
fast: Tăng tốc độ rơi của đồ vật (Chế độ nhanh).
slow: Giảm tốc độ rơi của đồ vật (Chế độ chậm).
big: Phóng to kích thước của cuốc (Cúp) đang rơi.
⛏️ Các lệnh thả Cuốc (Cúp) theo chất liệu:
wood: Thả cuốc gỗ (Wooden Pickaxe).
stone: Thả cuốc đá (Stone Pickaxe).
iron: Thả cuốc sắt (Iron Pickaxe).
gold: Thả cuốc vàng (Golden Pickaxe).
diamond: Thả cuốc kim cương (Diamond Pickaxe).
netherite: Thả cuốc Netherite (Netherite Pickaxe).
🌟 Ngoài ra còn có các hành động tự động (không cần gõ lệnh):

Tặng Superchat / Supersticker: Game sẽ tự động thả một phần thưởng Superchat TNT siêu lớn.
Đăng ký kênh mới (New Subscriber): Game sẽ tự động kích hoạt một quả Mega TNT.