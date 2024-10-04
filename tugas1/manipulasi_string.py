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

    Beberapa konsep yang membantu di dasar python:
    1. string bisa di loop, pakai for
    2. list dan bagaimana menambah item ke list
    3. increment variable
    4. dictionary, bagaimana cara buat dictionary

    """
    

    
    characters = []
   
    index = 0
    inside_tag = False
     
    # TODO: 6. tambahkan sebuah variable untuk check apakah kamu sedang berada di dalam tag, atau diluar tag. Variable ini isinya True atau False. Akan diubah sesuai kriteria
    # dibawah nanti. Maksud tag adalah `<a>` atau `</b>` atau semisalnya.
    
   
    # TODO: 1. loop text
    for huruf in text:
        if  huruf == '<':
           inside_tag = True
           characters.append({'char': huruf,'index': None})
        elif huruf == '>':
           inside_tag = False
           characters.append({'char': huruf, 'index': None})
        elif inside_tag:
            characters.append({'char': huruf, 'index': None})
        else:
            characters.append({'char': huruf, 'index': index})   
        # TODO: 7. buat if else disini sebagai ganti dari TODO 2 - TODO 4 dengan ketentuan:
        # 1. bila huruf adalah '<' maka value dari 'index' adalah None dan variable dari TODO 6 menjadi False, index tidak boleh ditambah
        # 2. bila huruf adalah '>' maka value dari 'index' adalah None dan variable dari TODO 6 menjadi True, index tidak boleh ditambah
        # 3. bila variable dari TODO 6 masih False, 'index' adalah None, dan index tidak boleh ditambah
        # 4. selain itu, value dari 'index' adalah index, dan index boleh ditambah lagi
        
        # TODO: 2. setiap character buat dictionary sementara dengan format: {'char': character, 'index': index}
       
       
        # TODO: 3. tambahkan dictionary sementara ke characters list
       
        
        # TODO: 4. naikkan 1 variable index. Maksudnya, kalau sekarang 0, maka nanti jadi 1 tiap kali tambah character
        index += 1
      
        
    # TODO: 5. return characters    
    return characters

    
    
    
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

    Beberapa konsep yang membantu:
    1. Loop
    2. Akses value dari dictionary
    3. mengubah valua dari dictionary
    4. Manipulasi text
    """
    
    
    
    

    format_text = []

    # TODO: 1. loop indexedText (ini adalah kembalian dari fungsi index_text)
    for item in indexedText:
        index = item ['index']
        character = item ['char']
        
        # TODO: 2. check apakah index tiap item sama dengan start. Bila iya, maka bentuk char menjadi <b>{character}. Jadi misal character adalah 'a' maka jadi '<b>a'.
        if index == start:
            format_text.append({'char': f'<b>{character}', 'index': index})
        # TODO: 3. check apakah index tiap item sama dengan end. Bila iya, maka bentuk char menjadi {character}</b>. Jadi misal character adalah 'b', maka jadi 'b</b>'
        elif  index == end:
            format_text.append({'char': f'{character}</b>', 'index': index})
        else:
            format_text.append(item)
   
    # TODO: 4. return indexText lagi
    return format_text

def main():
    text1 = "aku sedang belajar python"
    indexed_text = index_text(text1)
    final_chars = wrap_tag(indexed_text, 4, 9)
    expected1 = "aku <b>sedang</b> belajar python"
    
    print("".join([text["char"] for text in final_chars])) # Output
    
    assert expected1 == "".join([text["char"] for text in final_chars])
"""
    text2 = "aku <i>sedang</i> belajar python"
    expected2 = "aku <i><b>sedang</b></i> belajar python"
    indexed_text = index_text(text2)
    final_chars = wrap_tag(indexed_text, 4, 9)
    assert expected2 == "".join([text["char"] for text in final_chars])
"""
    
if __name__ == "__main__":
    main()