# word_test.py



print("=== 英単語テスト ===")
print("日本語の意味を入力してください。\n")

# 単語ごとにテスト
for english, japanese in words.items():
    answer = input(f"{english} の意味は？：")
    if answer == japanese:
        print("⭕ 正解！\n")
        score += 1
    else:
        print(f"❌ 不正解。正しくは「{japanese}」です。\n")

# 結果表示
print(f"あなたのスコア：{score} / {len(words)} 点")