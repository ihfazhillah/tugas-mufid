"""
Membuat fungsi untuk mengubah mengubah tag dengan mengetahui index mulai dan index akhir.

Contoh:
    Input:
        text: Aku sedang belajar python
        start: 4
        end: 9
    Output:
        Aku <b>sedang</b> belajar python


    Input:
        text: Aku <i>sedang</i> belajar python
        start: 4
        end: 9
    Output:
        text: Aku <i><b>sedang</b></i> belajar python


Test:
    Jalankan file ini, bila tidak ada error maka test berhasil.
"""


def index_text(text: str):
    """
    return list yang berisi dictionary dengan format {'char': '<character text>', 'index': '<index character>'}

    contoh: [{'char': 'a', 'index': 0}, {'char': 'k', 'index': '1'}]

    Yang perlu diperhatikan:

    html tag index adalah None. Jadi karakter <, > dan / yang ada di dalam kurung, serta huruf yang didalamnya harus None

    contoh: <b>a</b> c
    < None
    b None
    > None
    a 0
    < None
    / None
    b None
    > None
      1 <= ini indexnya spasi
    c 2

    Hint: Text bisa di loop. Kamu juga bisa dapatkan indexnya pakai fungsi enumerate.
    """
    pass


def wrap_tag(indexedText, start, end):
    """
    Berbekal fungsi diatas. Kamu sudah mendapatkan start dan end index.
    Kamu hanya perlu mengubah text character nya.

    bila indexnya adalah start maka tambahkan sebelum characternya
    bila indexnya adalah end, maka tambahkan setelah characternya

    contoh start 0 end 1 dari kata 'aku'
    a 0
    k 1
    u 2

    start == 0, char adalah a. Maka hasilnya: <b>a
    end == 1, char adalah k. Maka hasilnya k</b>

    Hasil akhir dari kembalian fungsinya adalah

    [
    {'char': '<b>a', 'index': 0},
    {'char': 'k</b>', 'index': 1},
    {'char': 'u', 'index': 2},
    ]
    """
    pass


def main():
    text1 = "aku sedang belajar python"
    indexed_text = index_text(text1)
    final_chars = wrap_tag(indexed_text, 4, 9)
    expected1 = "aku <b>sedang</b> belajar python"
    assert expected1 == "".join([text["char"] for text in final_chars])

    text2 = "aku <i>sedang</i> belajar python"
    expected2 = "aku <i><b>sedang</b></i> belajar python"
    indexed_text = index_text(text2)
    final_chars = wrap_tag(indexed_text, 4, 9)
    assert expected2 == "".join([text["char"] for text in final_chars])


if __name__ == "__main__":
    main()
