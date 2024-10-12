def parse(text: str):
    pass


def main():
    "NOTE: jangan ubah apa apa disini !!"

    test1 = "aku sedang <b>belajar</b> python"
    expected1 = {
        "text": "aku sedang belajar python",
        "highligths": [{"start": 11, "end": 17}],
    }
    result1 = parse(test1) 

    print("TEST 1")
    print(f"Data masukan: {test1}")
    print(f"Hasil: {result1}")
    print(f"Yang diinginkan: {expected1}")

    assert result1["text"] == expected1["text"]
    assert len(result1["highligths"]) == 1
    assert all([
        a == b for a, b in zip(expected1["highlights"], result1["highlights"])
        ])


if __name__ == "__main__":
    main()
