# -*- coding: utf-8 -*-
"""Nội dung tiếng Việt cho các trang cặp tiền tệ (USD sang EUR).

PAIR_UI_L10N tương ứng các chuỗi khung trong pair_pages.PAIR_UI["en"] (các
placeholder {f} {t} {d} giữ nguyên). PAIR_CONTENT_L10N tương ứng 15 cặp trong
PAIR_CONTENT["en"], khóa trùng với bản tiếng Anh. build-lang-pages.py hợp nhất
cả hai vào PAIR_UI / PAIR_CONTENT.
"""

PAIR_UI_L10N = {
    "pairConvert": "Bộ quy đổi trực tuyến",
    "pairRateHead": "Tỷ giá hiện tại",
    "pairAsOf": "Tỷ giá tham chiếu tại thời điểm {d}. Bộ quy đổi trực tuyến phía trên luôn lấy tỷ giá mới nhất — các bảng phía dưới là ảnh chụp tại thời điểm dựng trang, chỉ để định hướng.",
    "pairAmounts": "Các mức tiền thông dụng: {f} sang {t}",
    "pairReverse": "Các mức tiền thông dụng: {t} sang {f}",
    "pairMore": "Thêm các phép quy đổi {f}",
    "pairMorePairs": "Thêm các cặp tiền tệ",
    "pairIntroHead": "Về tỷ giá {f}/{t}",
    "pairCurLinks": "Trang tiền tệ",
    "pairMetaTmpl": ("Quy đổi {f} sang {t} với tỷ giá trực tuyến: tỷ giá {f}/{t} hôm nay, máy quy đổi miễn phí, "
                     "bảng các mức tiền thông dụng và điều gì tác động đến cặp tiền tệ này."),
}

PAIR_CONTENT_L10N = {
    # ───────────────────────── USD → EUR ─────────────────────────
    "USD-EUR": {
        "title": "USD sang EUR — tỷ giá hôm nay, máy quy đổi miễn phí và bảng số tiền",
        "description": "Quy đổi đô la Mỹ sang euro với tỷ giá trực tuyến: tỷ giá USD/EUR hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến cặp tiền này.",
        "h1": "USD sang EUR — quy đổi đô la Mỹ sang euro",
        "intro": [
            "USD/EUR là cặp tiền tệ được giao dịch nhiều nhất thế giới — khoảng một phần tư tổng doanh số ngoại hối — vì thế nó có spread hẹp nhất và thị trường sâu nhất trong mọi phép quy đổi. Tỷ giá đơn giản là giá của một đô la Mỹ tính bằng euro, được thiết lập liên tục bởi thương mại toàn cầu, dòng đầu tư và khoảng cách lãi suất giữa Fed với Ngân hàng Trung ương châu Âu.",
            "Với những phép quy đổi thường ngày, câu hỏi thực dụng là bạn đang trả bao nhiêu phần bù so với tỷ giá giữa thị trường hiển thị ở đây. Ngân hàng thường cộng thêm 1–4 phần trăm; dịch vụ thẻ và chuyển tiền thì chênh nhau rất xa. Kiểm tra tỷ giá trực tuyến trước khi mua hay chuyển tiền cho biết ngay một báo giá có công bằng hay không.",
        ],
        "faq": [
            ("Tỷ giá USD sang EUR được xác định như thế nào?",
             "Nó thả nổi hoàn toàn — cung và cầu của hai đồng tiền ấn định giá cả liên tục, chịu tác động chủ yếu từ chính sách lãi suất của Fed và ECB, lạm phát ở hai bên bờ Đại Tây Dương cùng tâm lý rủi ro toàn cầu. Không có mục tiêu cố định hay được quản lý nào."),
            ("Thời điểm nào tốt nhất để quy đổi USD sang EUR?",
             "Thanh khoản sâu nhất và spread hẹp nhất khi giờ giao dịch châu Âu và Mỹ chồng lên nhau (khoảng 13:00–17:00 UTC). Không ai đoán được hướng ngắn hạn một cách đáng tin, nên với số tiền lớn, quy đổi theo từng phần an toàn hơn là chờ một ngày đẹp trời."),
        ],
    },
    # ───────────────────────── USD → GBP ─────────────────────────
    "USD-GBP": {
        "title": "USD sang GBP — tỷ giá hôm nay, máy quy đổi miễn phí và điều gì tác động đến bảng Anh",
        "description": "Quy đổi đô la Mỹ sang bảng Anh với tỷ giá trực tuyến: tỷ giá USD/GBP hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm bảng Anh nhúc nhích.",
        "h1": "USD sang GBP — quy đổi đô la Mỹ sang bảng Anh",
        "intro": [
            "Tỷ giá đô la–bảng Anh, biệt danh “cable” theo tên cáp điện tín xuyên Đại Tây Dương lần đầu truyền nó trong thập niên 1860, là một trong những tỷ giá được báo giá liên tục lâu đời nhất thế giới. Ngày nay nó phản ánh khoảng cách lãi suất giữa Fed với Ngân hàng Anh, lạm phát Anh Quốc và sức khỏe thương mại cùng tài chính công của Anh.",
            "Sterling giao dịch sôi động nhất trong giờ London, và cặp tiền này dễ giật mạnh quanh các dữ liệu kinh tế cùng thông tin tài khóa Anh. So sánh mọi báo giá với tỷ giá giữa thị trường bên dưới là cách nhanh nhất để thấy một nhà cung cấp đang lấy bao nhiêu phần bù.",
        ],
        "faq": [
            ("Vì sao bảng Anh đáng giá hơn đô la Mỹ?",
             "Giá một đơn vị cao hơn không có nghĩa là nền kinh tế mạnh hơn — nó phản ánh lịch sử và cách mệnh giá. Bảng Anh là đồng tiền thống trị thế giới khi đô la còn chưa tồn tại; con số tự nó không nói gì về sức mạnh kinh tế tương đối hay sức mua."),
            ("Điều gì tác động đến USD/GBP mạnh nhất?",
             "Các quyết định lãi suất của Fed và Ngân hàng Anh, số liệu lạm phát Anh Quốc cùng tin chính trị và tài khóa từ Westminster. Trong cuộc bỏ phiếu Brexit 2016, bảng Anh rớt khoảng 10 phần trăm chỉ trong một ngày — lời nhắc rằng sterling mang một rủi ro chính trị mà đa số đồng tiền lớn không có."),
        ],
    },
    # ───────────────────────── USD → JPY ─────────────────────────
    "USD-JPY": {
        "title": "USD sang JPY — tỷ giá trực tuyến, máy quy đổi miễn phí và bảng mức tiền thông dụng",
        "description": "Quy đổi đô la Mỹ sang yên Nhật với tỷ giá trực tuyến: tỷ giá USD/JPY hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm yên chuyển động.",
        "h1": "USD sang JPY — quy đổi đô la Mỹ sang yên Nhật",
        "intro": [
            "USD/JPY là cặp tiền tệ được giao dịch nhiều thứ hai thế giới và chiếc khí áp kế kinh điển cho khoảng cách lãi suất giữa Hoa Kỳ và Nhật Bản. Vì lãi suất Nhật nằm gần bằng không suốt nhiều thập kỷ, yên trở thành đồng tiền huy động vốn được ưa chuộng nhất thế giới — nó yếu đi khi thị trường tự tin và bật mạnh khi khủng hoảng xả những vị thế đó.",
            "Cặp tiền này còn được dõi theo vì các lần can thiệp chính thức của Nhật: Bộ Tài chính nhiều lần mua yên khi nó yếu quá xa, quá nhanh. Với các khoản quy đổi lớn, hãy đối chiếu với tỷ giá giữa thị trường, vì phần bù bán lẻ trên JPY có thể rộng đến mức đánh lừa.",
        ],
        "faq": [
            ("Vì sao yên đôi khi rớt mạnh so với đô la?",
             "Chủ yếu vì khoảng cách lãi suất. Khi lãi suất Mỹ cao và lãi suất Nhật gần bằng không, nhà đầu tư bán yên để mua tài sản đô la sinh lời cao hơn — carry trade. Yên có thể trượt hàng tháng trời, rồi bật dữ dội khi những vị thế đó bị xả."),
            ("Chính phủ Nhật có thể đổi được tỷ giá USD/JPY không?",
             "Họ có thể đi ngược thị trường, chứ không đảo ngược được nó. Nhật từng can thiệp bằng cách mua hoặc bán yên khi các cú chuyển động trở nên rối loạn, đôi khi với hàng chục tỷ đô la trong một đợt. Can thiệp làm dịu đường đi; hiếm khi thay đổi hướng dài hạn do nền tảng kinh tế quyết định."),
        ],
    },
    # ───────────────────────── USD → CNY ─────────────────────────
    "USD-CNY": {
        "title": "USD sang CNY — tỷ giá hôm nay, máy quy đổi miễn phí và cách mức giá được quản lý",
        "description": "Quy đổi đô la Mỹ sang nhân dân tệ với tỷ giá trực tuyến: tỷ giá USD/CNY hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và cách mức giá được quản lý.",
        "h1": "USD sang CNY — quy đổi đô la Mỹ sang nhân dân tệ",
        "intro": [
            "Tỷ giá đô la–nhân dân tệ là cặp tiền tệ lớn nhất do một ngân hàng trung ương quản lý. Mỗi sáng, Ngân hàng Nhân dân Trung Quốc ấn định một tỷ giá trung tâm hằng ngày, và tỷ giá trong nước (CNY) chỉ được di chuyển trong một biên độ quanh nó — lý do USD/CNY nhúc nhích ít hơn hẳn so với tầm vóc kinh tế của nó.",
            "Thặng dư thương mại, kiểm soát vốn và mục tiêu chính sách của Trung Quốc cùng định hình tỷ giá. Khi quy đổi, lưu ý CNY trong nước và CNH ngoài khơi có thể lệch nhẹ nhau, và việc quy đổi tiền tệ cá nhân tại Trung Quốc chịu ràng buộc bởi các quy tắc kiểm soát vốn. Luôn so sánh báo giá với tỷ giá tham chiếu bên dưới.",
        ],
        "faq": [
            ("Nhân dân tệ có chuyển đổi tự do không?",
             "Chưa hoàn toàn. Quy đổi phục vụ thương mại khá dễ, nhưng dòng đầu tư xuyên biên giới bị kiểm soát bằng hạn ngạch và phê duyệt. Vì thế bản ngoài khơi (CNH) giao dịch lệch nhẹ so với CNY trong nước — khoảng cách đó cho biết việc đưa tiền qua biên giới đắt đến đâu."),
            ("Vì sao USD/CNY gần như không nhúc nhích so với các cặp khác?",
             "Vì ngân hàng trung ương quản lý nó. Tỷ giá trung tâm hằng ngày cùng biên độ giao dịch giữ tỷ giá ổn định so với đô la, phù hợp với ưu tiên dự đoán được trong thương mại của Trung Quốc. Quản lý không có nghĩa là cố định: qua nhiều tháng và năm, tỷ giá vẫn đi theo nền tảng kinh tế."),
        ],
    },
    # ───────────────────────── USD → INR ─────────────────────────
    "USD-INR": {
        "title": "USD sang INR — tỷ giá hôm nay, máy quy đổi miễn phí và bí quyết gửi tiền về Ấn Độ",
        "description": "Quy đổi đô la Mỹ sang rupee Ấn Độ với tỷ giá trực tuyến: tỷ giá USD/INR hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến rupee.",
        "h1": "USD sang INR — quy đổi đô la Mỹ sang rupee Ấn Độ",
        "intro": [
            "USD/INR là một trong những hành lang kiều hối quan trọng nhất thế giới — Ấn Độ nhận kiều hối nhiều hơn bất kỳ quốc gia nào — và là một cặp thị trường mới nổi được giao dịch dày đặc. Ngân hàng Dự trữ Ấn Độ quản lý biến động chứ không quản lý mức: ngân hàng làm dịu các cú chuyển động mạnh bằng dự trữ nhưng để rupee tự tìm xu hướng dài hạn.",
            "Câu chuyện dài hạn của rupee là sự mất giá từ từ so với đô la, do chênh lệch lạm phát và cán cân vãng lai của Ấn Độ dẫn dắt, thưa thớt những cú sốc rủi ro toàn cầu. Với bất kỳ ai gửi tiền về Ấn Độ, khoảng cách giữa tỷ giá giữa thị trường và tỷ giá được chào chính là nơi chi phí thật trú ngụ.",
        ],
        "faq": [
            ("Vì sao rupee Ấn Độ mất giá theo thời gian?",
             "Chủ yếu vì chênh lệch lạm phát và thâm hụt thương mại: Ấn Độ nhập khẩu nhiều hơn hẳn xuất khẩu, và phần chênh lệch được tài trợ bằng dòng vốn vào. RBI làm dịu đường đi, nhưng qua nhiều thập kỷ rupee đã trượt đều về phía yếu hơn so với đô la — điều bình thường với một nền kinh tế đang phát triển."),
            ("Làm sao có được tỷ giá tốt nhất khi gửi tiền về Ấn Độ?",
             "Hãy so sánh tỷ giá được chào với tỷ giá giữa thị trường trước khi gửi, chứ không chỉ nhìn phí. Các dịch vụ kiều hối chuyên nghiệp thường thắng chuyển tiền ngân hàng trên tuyến này, và chênh nhau 1 phần trăm đã rất đáng kể với những khoản gia đình đều đặn trong một năm."),
        ],
    },
    # ───────────────────────── USD → CAD ─────────────────────────
    "USD-CAD": {
        "title": "USD sang CAD — tỷ giá hôm nay, máy quy đổi miễn phí và điều gì tác động đến loonie",
        "description": "Quy đổi đô la Mỹ sang đô la Canada với tỷ giá trực tuyến: tỷ giá USD/CAD hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm loonie vận động.",
        "h1": "USD sang CAD — quy đổi đô la Mỹ sang đô la Canada",
        "intro": [
            "USD/CAD — biệt danh “loonie” — nằm trong nhóm năm cặp được giao dịch nhiều nhất thế giới, xây trên một trong những quan hệ thương mại lớn nhất hành tinh. Canada gửi khoảng ba phần tư xuất khẩu sang Hoa Kỳ, nên cặp tiền giao dịch mạnh theo tăng trưởng Mỹ, giá năng lượng (Canada là nước xuất khẩu dầu lớn) và khoảng cách lãi suất giữa Fed với Ngân hàng Canada.",
            "Khi dầu tăng, CAD thường mạnh lên; khi nỗi sợ tăng trưởng toàn cầu ập đến, nó yếu đi cùng nhóm đồng tiền hàng hóa. Cặp tiền thanh khoản suốt ngày đêm, và các báo giá cách tỷ giá giữa thị trường một phần rất nhỏ phần trăm thì dễ dàng tìm thấy — nên mọi phần bù rộng đều đáng bị chất vấn.",
        ],
        "faq": [
            ("Vì sao đô la Canada gọi là loonie?",
             "Theo chú chim loon — hình in trên đồng xu một đô ra đời năm 1987. Biệt danh bám chặt và nay chỉ chính đồng tiền trong tiếng lóng ngoại hối, như trong câu “loonie hôm nay bật lên”."),
            ("Giá dầu thực sự tác động đến USD/CAD không?",
             "Có, thấy rõ. Dầu thô và các sản phẩm liên quan là nhóm xuất khẩu lớn nhất của Canada, nên dầu tăng thường mang thêm đô la vào nước này và nâng CAD. Trader coi cặp tiền này như một canh bạc thô với thị trường năng lượng bên cạnh lãi suất của hai nước."),
        ],
    },
    # ───────────────────────── USD → AUD ─────────────────────────
    "USD-AUD": {
        "title": "USD sang AUD — tỷ giá trực tuyến, máy quy đổi miễn phí và bảng số tiền thông dụng",
        "description": "Quy đổi đô la Mỹ sang đô la Úc với tỷ giá trực tuyến: tỷ giá USD/AUD hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến Aussie.",
        "h1": "USD sang AUD — quy đổi đô la Mỹ sang đô la Úc",
        "intro": [
            "Đô la Úc là đồng tiền hàng hóa kinh điển: số phận của nó bám theo quặng sắt, than đá và khí đốt xuất khẩu, trên hết là cầu của Trung Quốc với những mặt hàng đó. Vì thế USD/AUD là một trong những chỉ báo thời gian thực sạch nhất về khẩu vị rủi ro toàn cầu — đồng Aussie mạnh lên khi thương mại thế giới bùng nổ và yếu đi trong các đợt thoái vốn.",
            "Chính sách lãi suất của Ngân hàng Dự trữ Úc cùng Fed dẫn dắt những dao động ngắn hạn. Cộng đồng du lịch làm việc và du học sinh của Úc khiến USD→AUD (và ngược lại) trở thành một phép quy đổi lặp lại thường xuyên, nơi chỉ 1 phần trăm phần bù tỷ giá cũng cộng dồn rất nhanh.",
        ],
        "faq": [
            ("Vì sao đô la Úc nhạy cảm với Trung Quốc đến vậy?",
             "Trung Quốc là thị trường xuất khẩu lớn nhất của Úc với khoảng cách xa, nhất là quặng sắt phục vụ luyện thép. Khi ngành xây dựng Trung Quốc hạ nhiệt, giá hàng hóa và AUD thường rớt cùng nhau — đồng tiền hoạt động như chiếc thanh kế thời gian thực cho công nghiệp nặng Trung Quốc."),
            ("AUD có phải nơi trú ẩn an toàn không?",
             "Ngược lại: trader gọi nó là đồng tiền risk-on. Trong các cuộc hoảng loạn toàn cầu — 2008, 2020 — tiền chảy vào đô la Mỹ và đồng Aussie thường rớt nặng nhất trong nhóm đồng tiền lớn. Chính tính chu kỳ đó là lý do các trader carry và người theo dõi tăng trưởng dõi theo nó sát đến vậy."),
        ],
    },
    # ───────────────────────── USD → CHF ─────────────────────────
    "USD-CHF": {
        "title": "USD sang CHF — tỷ giá hôm nay, máy quy đổi miễn phí và sức nặng của franc Thụy Sĩ",
        "description": "Quy đổi đô la Mỹ sang franc Thụy Sĩ với tỷ giá trực tuyến: tỷ giá USD/CHF, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm franc chuyển động.",
        "h1": "USD sang CHF — quy đổi đô la Mỹ sang franc Thụy Sĩ",
        "intro": [
            "Franc Thụy Sĩ là nơi trú ẩn an toàn số một thế giới: khi chiến tranh, căng thẳng ngân hàng hay hoảng loạn thị trường ập đến, tiền chảy vào Thụy Sĩ và CHF mạnh lên. Vì thế USD/CHF có xu hướng giảm trong các cuộc khủng hoảng toàn cầu ngay cả khi chính đô la cũng là nơi nương náu — franc đơn giản là chỗ trú mạnh hơn.",
            "Ngân hàng Quốc gia Thụy Sĩ chủ động định hình tỷ giá, từ sàn euro nổi tiếng 2011–2015 đến những đợt can thiệp dày đặc kể từ đó. Với việc quy đổi, Thụy Sĩ còn là lời nhắc rằng một cặp tiền của nước giàu vẫn có thể mang phần bù bán lẻ rộng, nhất là ở sân bay và khách sạn — hãy luôn đối chiếu tỷ giá giữa thị trường.",
        ],
        "faq": [
            ("Vì sao franc Thụy Sĩ được coi là nơi trú ẩn an toàn?",
             "Một thế kỷ trung lập, nợ thấp, thặng dư cán cân vãng lai cùng một ngân hàng trung ương đáng tin khiến franc trở thành bãi đỗ mặc định cho dòng tiền bỏ chạy khỏi rủi ro. Lạm phát Thụy Sĩ còn chạy thấp xa Mỹ và khu vực đồng euro suốt nhiều thập kỷ, gìn giữ sức mua của đồng tiền."),
            ("SNB đã làm gì vào tháng 1 năm 2015?",
             "Ngân hàng bỏ đột ngột trần hạn chế sức mạnh của franc so với euro. USD/CHF và EUR/CHF sụp khoảng 20–30 phần trăm chỉ trong vài phút — một trong những cú vận động trong ngày lớn nhất từng thấy ở một cặp tiền lớn, và lý do trader đến nay vẫn nể nang cụm từ “rủi ro SNB”."),
        ],
    },
    # ───────────────────────── USD → MXN ─────────────────────────
    "USD-MXN": {
        "title": "USD sang MXN — tỷ giá hôm nay, máy quy đổi miễn phí và điều gì tác động đến peso Mexico",
        "description": "Quy đổi đô la Mỹ sang peso Mexico với tỷ giá trực tuyến: tỷ giá USD/MXN hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm peso vận động.",
        "h1": "USD sang MXN — quy đổi đô la Mỹ sang peso Mexico",
        "intro": [
            "USD/MXN là cặp thị trường mới nổi được giao dịch nhiều nhất châu Mỹ và một trong những cặp thanh khoản nhất thế giới. Peso giao dịch theo mọi thứ tác động đến nền kinh tế Mỹ — chính sách thương mại, tăng trưởng, khoảng cách lãi suất giữa Fed với Banxico — cộng thêm giá dầu và hành lang kiều hối khổng lồ từ Hoa Kỳ.",
            "Vì thanh khoản cao, cặp tiền phản ứng nhanh với tâm lý rủi ro toàn cầu: đây là mục tiêu carry trade kinh điển, mạnh lên ở thị trường êm ả và bật ngược dữ dội trong hoảng loạn. Với du khách và người gửi kiều hối, phần bù 3–6 phần trăm là chuyện thường thấy ở sân bay — tỷ giá giữa thị trường bên dưới là chuẩn để đối chiếu.",
        ],
        "faq": [
            ("Vì sao USD/MXN biến động mạnh đến vậy?",
             "Lãi suất cao ở Mexico hút dòng tiền carry ngắn hạn rút chạy rất nhanh khi căng thẳng; peso đồng thời là tài sản tham chiếu cho mọi tin thương mại và chính trị giữa Mỹ với Mexico. Sự kết hợp khiến nó thanh khoản nhưng dễ giật — những cú nhảy lớn trong ngày là chuyện bình thường, không phải trục trặc."),
            ("Cách rẻ nhất gửi đô la sang Mexico là gì?",
             "Các dịch vụ kiều hối chuyên nghiệp gần như luôn thắng ngân hàng và các điểm chuyển tiền mặt trên tuyến này. Hãy so sánh số tiền người nhận thực nhận với tỷ giá giữa thị trường: với một khoản chuyển 300 đô la, khoảng cách giữa một báo giá công bằng và phần bù 5 phần trăm có thể bằng trọn một ngày công tại địa phương."),
        ],
    },
    # ───────────────────────── USD → PHP ─────────────────────────
    "USD-PHP": {
        "title": "USD sang PHP — tỷ giá hôm nay, máy quy đổi miễn phí và hướng dẫn kiều hối về Philippines",
        "description": "Quy đổi đô la Mỹ sang peso Philippines với tỷ giá trực tuyến: tỷ giá USD/PHP, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến peso.",
        "h1": "USD sang PHP — quy đổi đô la Mỹ sang peso Philippines",
        "intro": [
            "Peso Philippines được nâng đỡ bởi một trong những dòng kiều hối lớn nhất thế giới: hàng triệu lao động Philippines ở nước ngoài gửi tiền về quê, và những dòng đô la đó là trụ cột của nền kinh tế. USD/PHP vì thế giao dịch theo khẩu vị rủi ro toàn cầu, giá dầu (Philippines là nước nhập khẩu ròng) và chính sách của Bangko Sentral ng Pilipinas.",
            "Tỷ giá chính thức được quản lý bằng bàn tay nhẹ — ngân hàng trung ương cho phép điều chỉnh từ từ trong khi làm dịu các cú bật. Với các gia đình OFW và du khách, khoảng cách phần bù giữa các nhà cung cấp trên tuyến này rất rộng, nên kiểm tra tỷ giá giữa thị trường trước khi gửi là cách tiết kiệm đơn giản nhất.",
        ],
        "faq": [
            ("Kiều hối tác động đến peso Philippines thế nào?",
             "Dòng đô la đều đặn từ lao động ở nước ngoài nâng đỡ peso và cán cân thanh toán của đất nước — mỗi năm hàng phần trăm GDP. Khi rủi ro toàn cầu tăng hay các nước sử dụng lao động suy yếu, kiều hối dịu xuống và peso thường đi theo."),
            ("Nên quy đổi USD sang PHP ở Mỹ hay ở Philippines?",
             "Quyết định nằm ở nhà cung cấp, không ở quốc gia. Cả hai đầu tuyến này đều có lựa chọn rẻ và đắt; con số quyết định là người nhận thực nhận được bao nhiêu peso. Hãy so sánh báo giá với tỷ giá giữa thị trường thay vì tin vào điểm giao dịch gần nhất."),
        ],
    },
    # ───────────────────────── EUR → GBP ────────────────────────
    "EUR-GBP": {
        "title": "EUR sang GBP — tỷ giá hôm nay, máy quy đổi miễn phí và bảng mức tiền thông dụng",
        "description": "Quy đổi euro sang bảng Anh với tỷ giá trực tuyến: tỷ giá EUR/GBP hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến cặp tiền này.",
        "h1": "EUR sang GBP — quy đổi euro sang bảng Anh",
        "intro": [
            "EUR/GBP là cặp chéo châu Âu kinh điển: hai nền kinh tế trao nhau khoảng một nửa thương mại, ngăn cách chỉ bằng một biên giới tiền tệ. Vì cả hai đều là đồng tiền phát triển, lạm phát thấp, cặp tiền nhúc nhích ít hơn hẳn các cặp chéo đô la — về bản chất là một canh bạc vào vận may tương đối của khu vực đồng euro so với Vương quốc Anh.",
            "Khoảng cách lãi suất giữa ECB với Ngân hàng Anh dẫn dắt phần lớn xu hướng, còn tin chính trị và tài khóa Anh tạo ra các cú bật. Với người lao động xuyên eo biển, người hưu trí và doanh nghiệp, sự ổn định của cặp tiền khiến từng khác biệt nhỏ về tỷ giá càng quan trọng hơn: 1 phần trăm phần bù là một phần lớn của tổng biên độ cả năm.",
        ],
        "faq": [
            ("Vì sao EUR/GBP êm hơn EUR/USD?",
             "Cả euro lẫn bảng đều không phải đồng tiền rủi ro toàn cầu, nên những đợt chạy trốn sang tài sản an toàn trên phạm vi thế giới lướt qua chúng. Cặp tiền chủ yếu phản ánh kinh tế tương đối Anh–EU và chênh lệch lãi suất, những thứ thay đổi chậm — dù nó vẫn có thể bật mạnh khi có tin chính trị Anh, như năm 2016 đã chứng minh."),
            ("Brexit còn tác động đến EUR/GBP như thế nào?",
             "Mang tính cấu trúc. Các rào cản thương mại mới từ 2021 làm nền kinh tế Anh bớt mở hơn với EU một chút, điều mà đa số nhà kinh tế gắn với một bảng Anh yếu hơn về cấu trúc. Mỗi vòng đàm phán Anh–EU về quy tắc thương mại đến nay vẫn làm cặp tiền nhúc nhích."),
        ],
    },
    # ───────────────────────── EUR → CHF ────────────────────────
    "EUR-CHF": {
        "title": "EUR sang CHF — tỷ giá hôm nay, máy quy đổi miễn phí và vai trò của SNB",
        "description": "Quy đổi euro sang franc Thụy Sĩ với tỷ giá trực tuyến: tỷ giá EUR/CHF hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và vai trò của SNB.",
        "h1": "EUR sang CHF — quy đổi euro sang franc Thụy Sĩ",
        "intro": [
            "EUR/CHF là phép thử nơi trú ẩn an toàn của châu Âu: mỗi khi căng thẳng khu vực đồng euro tăng — khủng hoảng nợ 2011, nỗi sợ ngân hàng, chiến tranh trên lục địa — tiền tràn qua biên giới Thụy Sĩ và cặp tiền giảm. Ngân hàng Quốc gia Thụy Sĩ dõi cặp tiền này sát hơn mọi tỷ giá khác, và nhiều lần can thiệp để franc không bóp nghẹt xuất khẩu Thụy Sĩ.",
            "Lịch sử hiện đại của cặp tiền đầy kịch tính: sàn giá 1,20 trong giai đoạn 2011–2015, rồi việc gỡ neo vào tháng 1 năm 2015 tạo ra cú sập chớp nhoáng 20–30 phần trăm chỉ trong vài phút. Kể từ đó franc giao dịch như một nơi nương náu thuần khiết, dù đôi khi mạnh quá mức — và SNB vẫn là một người chơi chủ động trên thị trường này.",
        ],
        "faq": [
            ("Vì sao SNB quan tâm EUR/CHF đến vậy?",
             "Vì nền kinh tế Thụy Sĩ bán hàng cho châu Âu. Franc mạnh quá mức làm hàng xuất khẩu Thụy Sĩ mất cạnh tranh và kéo lạm phát dưới mục tiêu, nên SNB mua ngoại tệ (từng áp lãi suất âm) để chặn sức mạnh của franc. Nước này can thiệp vào cặp tiền nhiều hơn gần như mọi ngân hàng trung ương khác trên một thị trường lớn."),
            ("EUR/CHF có phải cặp tiền ổn định để nắm giữ không?",
             "Ổn định lúc êm ả và nổ tung lúc khủng hoảng — đúng nghĩa đen là ngược với đa dạng hóa. Việc gỡ neo năm 2015 vẫn là lời cảnh cáo kinh điển rằng lời hứa chặn giá của một ngân hàng trung ương có thể bị rút lại chỉ sau một đêm. Ai coi cặp tiền này là không rủi ro đã học bài đó trong một buổi sáng."),
        ],
    },
    # ───────────────────────── EUR → PLN ────────────────────────
    "EUR-PLN": {
        "title": "EUR sang PLN — tỷ giá hôm nay, máy quy đổi miễn phí và điều gì tác động đến złoty",
        "description": "Quy đổi euro sang złoty Ba Lan với tỷ giá trực tuyến: tỷ giá EUR/PLN hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm złoty chuyển động.",
        "h1": "EUR sang PLN — quy đổi euro sang złoty Ba Lan",
        "intro": [
            "Ba Lan là nền kinh tế lớn thứ sáu của EU vẫn dùng đồng tiền riêng, và złoty là đồng tiền không dùng euro được giao dịch nhiều nhất trong Liên minh. EUR/PLN giao dịch theo khoảng cách lãi suất với Ngân hàng Quốc gia Ba Lan, các quỹ EU chảy về phía đông, đơn hàng nhà máy Đức cho công nghiệp Ba Lan cùng rủi ro địa chính trị khu vực.",
            "Kể từ khi gia nhập EU năm 2004, złoty từng mạnh lên trong các giai đoạn bùng nổ và rớt nặng trong khủng hoảng — năm 2008 và 2022 đẩy cặp tiền đến những mức cực trị lịch sử. Với việc Ba Lan chưa có lộ trình nhận euro, cặp tiền này còn là một cấu trúc cố định của tài chính châu Âu trong nhiều năm tới.",
        ],
        "faq": [
            ("Ba Lan có nhận euro và bỏ złoty không?",
             "Ba Lan về pháp lý bắt buộc nhận euro đến một lúc nào đó nhưng không có mốc thời gian, còn dư luận khá hoài nghi. Cho đến khi một lộ trình chuyển đổi đáng tin xuất hiện, EUR/PLN vẫn là cặp tiền được giao dịch tích cực — riêng những phát biểu chính trị về thời biểu đã đủ làm nó nhúc nhích."),
            ("Vì sao EUR/PLN bật mạnh năm 2022?",
             "Cuộc chiến ở Ukraine láng giềng biến Ba Lan thành nền kinh tế tiền tuyến chỉ sau một đêm: làn sóng người tị nạn, chi phí quốc phòng và cú sốc năng lượng giáng vào đồng tiền rất mạnh. Ngân hàng Quốc gia Ba Lan can thiệp để nâng đỡ złoty — những cú chuyển động sắc nhất của cặp tiền trong hai thập kỷ."),
        ],
    },
    # ───────────────────────── GBP → JPY ────────────────────────
    "GBP-JPY": {
        "title": "GBP sang JPY — tỷ giá hôm nay, máy quy đổi miễn phí và câu chuyện cặp tiền biến động",
        "description": "Quy đổi bảng Anh sang yên Nhật với tỷ giá trực tuyến: tỷ giá GBP/JPY hôm nay, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì làm nó biến động.",
        "h1": "GBP sang JPY — quy đổi bảng Anh sang yên Nhật",
        "intro": [
            "GBP/JPY — các trader xưa gọi nó là “con quái vật” hay “con rồng” — là một trong những cặp tiền lớn biến động mạnh nhất. Nó chồng hai cỗ máy rủi ro lên nhau: độ nhạy của sterling với tin chính trị và tài khóa Anh, cùng vai trò đồng tiền huy động vốn của cả thế giới đối với yên, thứ làm nó bật dữ dội mỗi khi tâm lý toàn cầu xoay chiều.",
            "Đây là cặp tiền được lòng carry trade: vay yên lãi gần bằng không để mua bảng sinh lời cao hơn. Trò đó trôi chảy cho đến khi một cuộc khủng hoảng buộc mọi người xả vị thế cùng lúc — lý do GBP/JPY hay bò lên đều đều trong nhiều năm rồi rớt thảm trong vài tuần. Cỡ vị thế và thời điểm quan trọng ở đây hơn ở gần như mọi cặp tiền lớn khác.",
        ],
        "faq": [
            ("Vì sao GBP/JPY biến động hơn USD/JPY?",
             "Vì nó nhân hai mức biến động. Sterling thêm rủi ro chính trị và kinh tế riêng của Anh lên trên tâm lý rủi ro toàn cầu vốn đã dẫn dắt USD/JPY. Cặp tiền không chung một nền kinh tế mỏ neo, nên nó gần như chỉ giao dịch theo khoảng cách lãi suất và tâm lý — nguyên liệu cho những cú chuyển động lớn."),
            ("Carry trade trong GBP/JPY là gì?",
             "Vay yên với lãi suất Nhật gần bằng không và đầu tư vào bảng với lãi suất Anh cao hơn để hưởng phần chênh lệch. Nó sinh lời khi thị trường êm ả và trừng phạt thậm tệ khi thị trường không êm: trong các đợt thoái vốn, yên bật lên khi các vị thế carry bị xả — thường 10 phần trăm hoặc hơn so với bảng chỉ trong vài tháng."),
        ],
    },
    # ───────────────────────── AUD → JPY ────────────────────────
    "AUD-JPY": {
        "title": "AUD sang JPY — tỷ giá hôm nay, máy quy đổi miễn phí và thước đo rủi ro toàn cầu",
        "description": "Quy đổi đô la Úc sang yên Nhật với tỷ giá trực tuyến: tỷ giá AUD/JPY, máy quy đổi miễn phí, bảng mức tiền thông dụng và điều gì tác động đến thanh kế rủi ro.",
        "h1": "AUD sang JPY — quy đổi đô la Úc sang yên Nhật",
        "intro": [
            "AUD/JPY là thanh kế rủi ro thuần khiết nhất của thị trường tiền tệ. Đô la Úc đại diện cho tăng trưởng toàn cầu và cầu hàng hóa — trên hết là cầu công nghiệp Trung Quốc — trong khi yên đại diện cho sự an toàn. Khi nền kinh tế thế giới mở rộng, cặp tiền leo; khi hoảng loạn ập đến, nó rớt nhanh hơn gần như mọi cặp chéo lớn khác.",
            "Đây cũng là cặp tiền carry trade kinh điển: suốt nhiều thập kỷ, nhà đầu tư vay yên rẻ để mua đồng Aussie sinh lời cao hơn. Dòng chảy đó định hình các xu hướng tăng bền bỉ của cặp tiền cùng những đợt xả vị thế dữ dội — năm 2008 vẫn là bài học cảnh tỉnh, khi AUD/JPY mất khoảng một nửa giá trị chỉ trong vài tháng.",
        ],
        "faq": [
            ("Vì sao trader gọi AUD/JPY là thanh kế rủi ro?",
             "Vì mỗi đồng tiền đứng ở một cực đối lập: đồng Aussie tăng cùng tăng trưởng toàn cầu và cầu hàng hóa, còn yên tăng cùng nỗi sợ. Cặp tiền vì thế vận động cùng thị trường cổ phiếu thế giới ở mức độ ít cặp chéo nào sánh được — khi nó rớt mạnh, cuộc thoái vốn rủi ro là thật."),
            ("Chuyện gì xảy ra với AUD/JPY trong khủng hoảng 2008?",
             "Nó bị cắt gần một nửa. Carry trade bị xả khi tín dụng toàn cầu đóng băng: nhà đầu tư bán đô la Úc để trả yên đã vay, và cặp tiền sụp từ trên 100 xuống vùng 50 thấp chỉ trong vài tháng. Nó vẫn là ví dụ chuẩn mực về tốc độ một chiến lược carry đảo chiều."),
        ],
    },
}
