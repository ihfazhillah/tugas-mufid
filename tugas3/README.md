# Deskripsi

Berikut ada 2 file json:

1. chats.json 
2. messages.json

`chats.json` berisi tentang list dari chat yang ada di telegram. Dia bisa jadi channel, atau pun chat pribadi. 

`messages.json` berisi tentang chat chat tertentu.

Gunakan 2 data tersebut untuk mengubah tiap pesan yang ada di messages.json menjadi format:

```json
{
"page_content": "ini nanti adalah message text nya",
"metadata": {
        "channel_id": "channel id nya",
        "channel_title": "nanti isinya channel title",
        "has_media": "check apakah message punya media atau tidak (kalau media None maka tidak ada media)",
        "message_id": "dapatkan message id",
        "message_link": "format seperti telegram message format seperti contoh dibawah"
    }
}
```


Contoh message link:

https://t.me/maydan_news/171797

madyan_news == channel username
angka setelahnya == message id


jadi formatnya

https://t.me/<channel_username>/<message_id>


hasil list final harus berbentuk file json dengan nama `final_messages.json`


## Note:

- Pelajari tentang buka file, load json data, save json data ke file
- Pelajari juga tentang `eval`. itu fungsi dari python.
- pelajari format chats.json dan messages.json 
- bagaimana menggabungkan 2 file tersebut untuk bisa mengubah menjadi format yang diinginkan
- dasar dasar yang penting untuk diulang ulang:
    - list
    - dictionary
    - json
    - menggabungkan string
    - format string dengan f-string

