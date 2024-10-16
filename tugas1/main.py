from manipulasi_string import index_text

def parse(text: str):
    indexed_text = index_text(text)
    final_text = []
    highlights = []
    start = None
    real_index = 0  
    inside_tag = False
    tag_type = None  

    for char_info in indexed_text:
        char = char_info['char']
        index = char_info['index']  

        if char == '<': 
            inside_tag = True
            tag_type = ""
        elif char == '>':  
            inside_tag = False
            if tag_type == "b":  
                start = real_index
            elif tag_type == "/b":  
                highlights.append({"start": start, "end": real_index})
                start = None
            tag_type = None
        elif inside_tag:  
            tag_type += char
        else:
            
            final_text.append(char)
            real_index += 1

    clean_text = ''.join(final_text)
    result = {
        "text": clean_text,
        "highlights": highlights
    }

    return result

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
