import serial

with serial.Serial("COM11", 230400, timeout=1) as port: #  COM5で230400baudで読み取り時間は1秒
    data = port.read(32)      # port の read という機能を使って、32バイト読み取る
    print(len(data), "バイト")
    print(data.hex(" "))      #hexは各バイトの間に空白を1個入れる設定

print("ポートを閉じました")

# with 式 as 名前:
#     ブロックの処理
# Pythonはこの文を次の順番で実行
# 1. 式 を評価して、コンテキストマネージャーを得る。
# 2. そのオブジェクトの開始処理（__enter__）を呼ぶ。`as 名前` があれば、開始処理の戻り値をその名前に代入する。
# 3. 字下げされたブロックを実行する。ブロックを抜けるときに、終了処理（__exit__）を呼ぶ。ブロックの途中で例外が起きた場合も呼ぶ。
# 4. 