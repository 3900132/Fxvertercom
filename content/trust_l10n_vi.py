# -*- coding: utf-8 -*-
"""Trust pages for Vietnamese (About / Privacy Policy / Terms of Use /
Contact / Feedback form).

Mirrors the structure of TRUST["en"] in content/trust_l10n.py: each entry
has title, meta description and a list of sections rendered in order —
["h", heading], ["p", paragraph] or ["li", list item; rendered inside a
single <ul> until the next non-li item]. The feedback entry additionally
carries the "form" dict for the standalone /feedback/ page.
"""

TRUST_LANG = {
    "about": {
        "title": "Về Fxverter — Trình quy đổi tiền tệ miễn phí và mã nguồn mở",
        "desc": "Ai đứng sau Fxverter, vì sao nó ra đời và điều gì làm nên sự khác biệt: một trình quy đổi tiền tệ mã nguồn mở đặt sự riêng tư lên hàng đầu, với tỷ giá tham chiếu trung thực và các cẩm nang dễ hiểu.",
        "sections": [
            ["p", "Fxverter là một trình quy đổi tiền tệ trực tuyến miễn phí, mã nguồn mở, vận hành hoàn toàn trong trình duyệt của bạn. Công cụ hiển thị tỷ giá tham chiếu cho hơn 140 đồng tiền trên thế giới, không cần khóa API, không cần đăng ký, không cần cài đặt — bạn mở trang web lên và bắt đầu quy đổi."],
            ["h", "Vì sao chúng tôi xây dựng nó"],
            ["p", "Phần lớn các trang web quy đổi tiền chôn vùi tỷ giá thực dưới đống pop-up, rào cản đăng ký và những lời nhắc cài đặt ứng dụng liên tục. Chúng tôi muốn điều ngược lại: một công cụ nhanh chóng, tôn trọng sự riêng tư, hiển thị tỷ giá tham chiếu giữa thị trường trung thực ngay từ đầu rồi né sang một bên. Toàn bộ sản phẩm chỉ là một trang tĩnh chạy được trên mọi thiết bị, bằng bảy ngôn ngữ, thậm chí cả khi offline sau khi cài đặt."],
            ["h", "Điều làm nên sự khác biệt"],
            ["li", "Không cần tài khoản, không theo dõi — mọi phép quy đổi chạy ngay trong trình duyệt của bạn"],
            ["li", "Ba nguồn dữ liệu công khai có thể chuyển đổi: Frankfurter (tỷ giá tham chiếu của Ngân hàng Trung ương châu Âu), ExchangeRate-API và Fawaz Currency API"],
            ["li", "40 đồng tiền chính với trang riêng: bảng quy đổi trực tiếp, biểu đồ xu hướng 30/90 ngày và hồ sơ tiền tệ"],
            ["li", "Các cẩm nang viết bằng ngôn ngữ đời thường, giải thích tỷ giá thực sự vận hành ra sao"],
            ["li", "Có thể cài đặt dưới dạng ứng dụng (PWA), vẫn hoạt động offline với các tỷ giá đã biết gần nhất"],
            ["h", "Về dữ liệu"],
            ["p", "Tỷ giá là các tỷ giá tham chiếu mang tính chỉ dẫn từ các nguồn công khai (ngân hàng trung ương và thị trường), được cập nhật hằng ngày. Đây là chuẩn so sánh giống những gì bạn thấy trên Google hay trong tin tức tài chính — hữu ích để so sánh và lên kế hoạch, chứ không phải một báo giá ràng buộc cho một giao dịch chuyển tiền cụ thể."],
            ["h", "Ai đứng sau nó"],
            ["p", "Fxverter do một lập trình viên độc lập xây dựng và duy trì, đồng thời được cộng đồng người dùng hậu thuẫn. Toàn bộ mã nguồn đều công khai trên GitHub — bất kỳ ai cũng có thể kiểm tra, tự triển khai hoặc đóng góp cải tiến."],
            ["p", "Có câu hỏi, góp ý hoặc ý tưởng? Hãy viết về <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — chúng tôi đọc mọi thư."],
        ],
    },
    "privacy": {
        "title": "Chính sách quyền riêng tư | Fxverter",
        "desc": "Fxverter thu thập gì và không thu thập gì: không bắt buộc dùng cookie, không tài khoản, chỉ có thống kê ẩn danh — cùng cách xử lý quảng cáo và dịch vụ của bên thứ ba.",
        "sections": [
            ["p", "Fxverter được thiết kế để dùng được mà không cần cung cấp bất kỳ thông tin cá nhân nào. Chính sách này giải thích trang web thu thập gì và không thu thập gì, cũng như cách xử lý quảng cáo và các dịch vụ của bên thứ ba. Cập nhật lần cuối: tháng 9 năm 2026."],
            ["h", "Chúng tôi không thu thập gì"],
            ["p", "Không cần tài khoản, và bản thân trang web không đặt bất kỳ cookie quảng cáo nào. Các phép quy đổi chạy ngay trong trình duyệt của bạn — chúng tôi không bao giờ thấy số tiền hay cặp tiền tệ mà bạn quy đổi."],
            ["h", "Thông tin được thu thập tự động"],
            ["p", "Số liệu truy cập ẩn danh, tổng hợp (lượt xem trang và quốc gia, không dùng cookie) có thể được thu thập để nắm mức sử dụng chung và cải thiện công cụ. Các số liệu này không thể dùng để nhận diện bạn."],
            ["h", "Thông tin bạn chủ động gửi"],
            ["p", "Nếu bạn dùng biểu mẫu phản hồi, tên, địa chỉ email và nội dung bạn gửi chỉ được dùng để đọc và trả lời phản hồi của bạn. Nếu bạn ủng hộ dự án, khoản thanh toán do Creem.io xử lý với tư cách merchant of record — chúng tôi không bao giờ nhận đầy đủ thông tin thanh toán của bạn. Người ủng hộ chỉ được liệt kê theo tên khi có sự đồng ý rõ ràng của họ."],
            ["h", "Dịch vụ của bên thứ ba"],
            ["p", "Tỷ giá được trình duyệt của bạn lấy trực tiếp từ các API công khai (Frankfurter/ECB, ExchangeRate-API, Fawaz Currency API) — các yêu cầu này đi từ thiết bị của bạn, không qua máy chủ của chúng tôi. Trang web được lưu trữ dưới dạng tệp tĩnh, và phân tích ẩn danh có thể chạy qua Cloudflare."],
            ["h", "Quảng cáo"],
            ["p", "Trang web này có thể hiển thị quảng cáo phân phối qua Google AdSense. Các nhà cung cấp bên thứ ba, trong đó có Google, sử dụng cookie và công nghệ tương tự để hiển thị quảng cáo dựa trên những lượt truy cập trước đó của bạn vào trang này hoặc các trang web khác. Việc Google dùng cookie quảng cáo cho phép Google và đối tác hiển thị quảng cáo cho bạn dựa trên lượt truy cập trang của chúng tôi và/hoặc các trang khác trên internet."],
            ["p", "Bạn có thể tắt quảng cáo cá nhân hóa tại <a href=\"https://adssettings.google.com\" rel=\"noopener\">Cài đặt quảng cáo của Google</a>, hoặc từ chối cookie của nhà cung cấp bên thứ ba tại <a href=\"https://www.aboutads.info\" rel=\"noopener\">aboutads.info</a>. Ở những nơi luật yêu cầu — ví dụ khu vực EEA và Vương quốc Anh — quảng cáo cá nhân hóa chỉ được hiển thị khi có sự đồng ý của bạn, còn lại sẽ dùng quảng cáo không cá nhân hóa. Chi tiết xem tại <a href=\"https://policies.google.com/technologies/ads\" rel=\"noopener\">cách Google sử dụng thông tin từ các trang dùng dịch vụ của họ</a>."],
            ["h", "Bộ nhớ cục bộ"],
            ["p", "Lựa chọn giao diện, cỡ chữ, các cặp tiền tệ đã lưu và thời điểm hiển thị banner cài đặt được lưu trong bộ nhớ cục bộ của trình duyệt. Dữ liệu này không bao giờ rời khỏi thiết bị của bạn và có thể xóa bất cứ lúc nào qua phần cài đặt trình duyệt."],
            ["h", "Thời gian lưu trữ và quyền của bạn"],
            ["p", "Các tin nhắn phản hồi chỉ được giữ trong thời gian cần thiết để trả lời. Bạn có thể yêu cầu chúng tôi xóa bất kỳ phản hồi nào bạn đã gửi bằng cách viết về <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
            ["h", "Thay đổi chính sách này"],
            ["p", "Nếu cách xử lý dữ liệu của trang web thay đổi, trang này sẽ được cập nhật và ngày ở trên sẽ được sửa lại. Việc tiếp tục sử dụng trang web sau một thay đổi đồng nghĩa với việc bạn chấp nhận chính sách đã cập nhật."],
        ],
    },
    "terms": {
        "title": "Điều khoản sử dụng | Fxverter",
        "desc": "Những quy tắc cơ bản khi dùng Fxverter: tỷ giá chỉ là giá trị tham chiếu chứ không phải báo giá; dịch vụ được cung cấp nguyên trạng; cùng cách xử lý trách nhiệm, sở hữu trí tuệ và sử dụng phù hợp.",
        "sections": [
            ["p", "Khi sử dụng fxverter.com, bạn đồng ý với các điều khoản này. Nếu không đồng ý, vui lòng không sử dụng trang web. Cập nhật lần cuối: tháng 9 năm 2026."],
            ["h", "Dịch vụ"],
            ["p", "Fxverter là trình quy đổi tiền tệ trực tuyến miễn phí, mã nguồn mở, được cung cấp \"nguyên trạng\" và \"theo hiện trạng khả dụng\" mà không có bất kỳ bảo đảm nào, rõ ràng hay ngụ ý — kể cả độ chính xác, tính khả dụng hay sự phù hợp cho một mục đích cụ thể."],
            ["h", "Tỷ giá chỉ mang tính tham chiếu"],
            ["p", "Mọi tỷ giá hiển thị đều là tỷ giá tham chiếu thu thập từ các nguồn công khai như ngân hàng trung ương và các API tiền tệ mở, thường cập nhật một lần mỗi ngày. Chúng là chuẩn để so sánh — không phải báo giá, không phải lời khuyên tài chính, và không phải mức giá mà bất kỳ nhà cung cấp nào sẽ thực tế đưa cho bạn. Đừng dùng chúng cho các giao dịch tài chính, chuyển khoản ngân hàng, xuất hóa đơn hay kế toán chính thức; hãy luôn xác minh tỷ giá với ngân hàng hoặc tổ chức tài chính của bạn trước khi giao dịch."],
            ["h", "Giới hạn trách nhiệm"],
            ["p", "Trong phạm vi tối đa mà pháp luật cho phép, những người duy trì Fxverter không chịu trách nhiệm về bất kỳ thiệt hại nào phát sinh từ việc sử dụng hoặc không thể sử dụng trang web hay dữ liệu của nó — bao gồm cả các quyết định dựa trên tỷ giá hiển thị."],
            ["h", "Sở hữu trí tuệ"],
            ["p", "Mã nguồn được phát hành mã nguồn mở theo giấy phép MIT và có sẵn trên GitHub. Nội dung văn bản, thiết kế và thương hiệu của trang vẫn thuộc về dự án Fxverter; bạn không được tái xuất bản toàn bộ nội dung trang khi chưa có sự cho phép."],
            ["h", "Dịch vụ và liên kết của bên thứ ba"],
            ["p", "Trang web phụ thuộc vào các API công khai của bên thứ ba và có thể dẫn tới các trang web của bên thứ ba. Chúng tôi không kiểm soát chúng và không chịu trách nhiệm về nội dung, tính khả dụng hay cách vận hành của các trang đó."],
            ["h", "Sử dụng phù hợp"],
            ["p", "Bạn đồng ý không phá rối dịch vụ, không cố làm quá tải nó, hay sử dụng công cụ tự động theo cách làm giảm trải nghiệm của những khách truy cập khác."],
            ["h", "Thay đổi các điều khoản này"],
            ["p", "Các điều khoản này có thể được cập nhật theo thời gian; phiên bản hiện hành luôn là trang này. Có câu hỏi? Hãy viết về <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>."],
        ],
    },
    "contact": {
        "title": "Liên hệ | Fxverter",
        "desc": "Cách liên hệ với đội ngũ Fxverter: phản hồi, góp ý tỷ giá, cấp phép và báo chí — hello@fxverter.com hoặc biểu mẫu phản hồi trực tuyến.",
        "sections": [
            ["p", "Cách nhanh nhất để liên hệ với chúng tôi là email: <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a>. Chúng tôi đọc từng tin nhắn và thường trả lời trong vòng vài ngày."],
            ["h", "Có thể viết về những gì"],
            ["li", "Phản hồi và ý tưởng tính năng — điều gì hay, điều gì chưa ổn, còn thiếu gì"],
            ["li", "Góp ý sửa lỗi — nếu một trang có gì đó trông không ổn, hãy cho chúng tôi biết là trang nào"],
            ["li", "Các câu hỏi về cấp phép và tái xuất bản nội dung"],
            ["li", "Yêu cầu từ báo chí và đề xuất hợp tác"],
            ["h", "Lối tắt"],
            ["p", "Không muốn viết email? Hãy dùng <a href=\"../feedback/\">biểu mẫu phản hồi trực tuyến</a> — thư đến cùng một hộp thư và chỉ mất khoảng ba mươi giây."],
            ["h", "Lưu ý về tỷ giá"],
            ["p", "Mọi tỷ giá đều là giá trị tham chiếu mang tính chỉ dẫn từ các nguồn công khai, cập nhật hằng ngày — hãy xem <a href=\"../guides/\">các cẩm nang</a> để hiểu ý nghĩa thực tế của điều đó. Trước khi viết thư về một tỷ giá \"sai\", vui lòng đối chiếu với nguồn thứ hai vào cùng thời điểm trong ngày: sự chênh lệch nhỏ giữa tỷ giá tham chiếu và tỷ giá nhà cung cấp là chuyện bình thường."],
            ["h", "Quyền riêng tư"],
            ["p", "Địa chỉ email của bạn chỉ được dùng để trả lời bạn — không có bản tin, không có marketing. Xem <a href=\"../privacy/\">Chính sách quyền riêng tư</a> để biết chi tiết."],
        ],
    },
    "feedback": {
        "title": "Gửi phản hồi | Fxverter",
        "desc": "Hãy cho chúng tôi biết điều gì hay, điều gì hỏng và điều gì còn thiếu — biểu mẫu phản hồi của Fxverter đi thẳng vào hộp thư của đội ngũ, không cần tài khoản.",
        "sections": [
            ["p", "Phát hiện lỗi, thấy một tỷ giá có vẻ không ổn, hoặc có ý tưởng giúp Fxverter hữu ích hơn? Biểu mẫu bên dưới đi thẳng vào hộp thư của chúng tôi — không cần tài khoản, và chỉ mất khoảng ba mươi giây."],
            ["h", "Điều giúp chúng tôi nhiều nhất"],
            ["li", "Bạn đang dùng trang hoặc tính năng nào"],
            ["li", "Bạn kỳ vọng điều gì và thực tế đã xảy ra điều gì"],
            ["li", "Trình duyệt hoặc thiết bị của bạn, nếu sự cố liên quan đến hiển thị"],
            ["h", "Thích gửi email hơn?"],
            ["p", "Hãy viết về <a href=\"mailto:hello@fxverter.com\">hello@fxverter.com</a> — hoặc cứ dùng biểu mẫu bên dưới, cả hai đều đến cùng một nơi."],
        ],
        "form": {
            "name": "Tên (không bắt buộc)",
            "email": "Email (không bắt buộc — chỉ khi bạn muốn nhận phản hồi)",
            "message": "Nội dung phản hồi",
            "send": "Gửi phản hồi",
            "ok": "✓ Đã gửi phản hồi — cảm ơn bạn!",
            "empty": "Vui lòng viết nội dung phản hồi trước.",
            "fail": "Gửi thất bại — vui lòng gửi email trực tiếp đến hello@fxverter.com.",
        },
    },
}

LABELS = {
    "about": "Giới thiệu",
    "privacy": "Quyền riêng tư",
    "terms": "Điều khoản sử dụng",
    "contact": "Liên hệ",
    "feedback": "Phản hồi",
}
