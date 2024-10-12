Seperti tugas1, tapi outputnya beda.

Kamu punya input string seperti berikut

`aku sedang <b>belajar</b> python`

Buat fungsi untuk mengubahnya menjadi:

```python
{
    "text": "aku sedang belajar python",
    "highligts": [{
        "start": 11,
        "end": 17
    }]
}
```

HINT:
1. import fungsi index_text dari tugas1, gunakan fungsi itu untuk melakukan index.
2. highlights adalah text yang diapit oleh HTML tag, seperti diatas: diapit oleh tag `<b>`
