import pyexcel

news= [
    {
        "link": "Chồng mặc áo đôi với vợ nhưng đi với bồ, vợ ôm con nhỏ đánh ghen"
        "title":'http://dantri.com.vn//su-kien/chong-mac-ao-doi-voi-vo-nhung-di-voi-bo-vo-om-con-nho-danh-ghen-20180808123117421.htm'
    },

     {
        "link":"Ngỡ ngàng với ngôi nhà hoa hồng đẹp như cổ tích của ông bố trẻ ở Hưng Yên" ,
        "title""http://dantri.com.vn//su-kien/ngo-ngang-voi-ngoi-nha-hoa-hong-dep-nhu-co-tich-cua-ong-bo-tre-o-hung-yen-20180808121433733.htm,
    },

    
]

pyexcel.save_as(records=news, dest_file_name='dantri.xlsx')

news_items