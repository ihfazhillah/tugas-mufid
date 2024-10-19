from manipulasi_string import index_text # mengimport fungsi dari index_text dari file manipulasi

def parse(text: str):
    indexed_text = index_text(text)
    final_text = [] # untuk menyimpan text yg sdh dibersihkan dari tag HML
    highlights = [] # utk menyimpan rentang text yg ditandai sebagai bold
    start = None
    real_index = 0  # utk menjaga posisi karakter dalam teks bersih
    inside_tag = False # utk mengetauhi ketika berada di dalam tag html
    tag_type = None  # menyimpan jenis tag yg ditemukan

    for char_info in indexed_text: # utk melakukan perulangan karakter dan informasi index dari hasil "indexed_text"
        char = char_info['char'] # utk mendapatkan cahrakter
        index = char_info['index']  # utk mendapatkan index
        

        if char == '<': 
            inside_tag = True # utk menandakan bahwa kita sekarang sedang berada didalam tag
            tag_type = ""
        elif char == '>':  
            inside_tag = False # utk menandakan bahwa kita telah keluar dari tag  
            if tag_type == "b":  
                start = real_index # menyimpan index awal text bold
            elif tag_type == "/b":  
                highlights.append({"start": start, "end": real_index})
                start = None # mereset variable 'start' setelah menemukan akhir dari text bold
            tag_type = None # mereset variable 'tag_type' setelah selesai
        elif inside_tag:  
            tag_type += char # utk menambahkan karakter ke 'tag_type' untuk mengidentifikasi tipe tag
        else:
            
            final_text.append(char) # utk menambah karakter ke dalam 'final_test'
            real_index += 1 #utk melacak posisi karakteer dalam text bersih

    clean_text = ''.join(final_text) # utk menggabungkan list (final_text) menjadi string text bersih
    result = {
        "text": clean_text,
        "highlights": highlights
    }

    return result # utk mengembalikan hasil dalam bentuk directory yang berisi teks bersih dan highlight

def main():
    test1 = "aku sedang <b>belajar</b> python"
    expected1 = {
        "text": "aku sedang belajar python",
        "highlights": [{"start": 11, "end": 18}],
    }
    result1 = parse(test1)

    print("TEST 1")
    print(f"Data masukan: {test1}")
    print(f"Hasil: {result1}")
    print(f"Yang diinginkan: {expected1}")

    assert result1["text"] == expected1["text"]
    assert len(result1["highlights"]) == 1
    assert all([
        a == b for a, b in zip(expected1["highlights"], result1["highlights"])
    ])

if __name__ == "__main__":
    main()
