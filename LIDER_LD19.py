import serial

with serial.Serial("COM11", 230400, timeout=1) as port: #  COM11で230400baudで読み取り時間は1秒
    data = port.read(256)          # port の read という機能を使って、32バイト読み取る
    print(len(data), "バイト")
    print(data.hex(" "))           # hexは各バイトの間に空白を1個入れる設定
    start = data.find(b"\x54\x2c") # 54と2cがこの順に連続する2バイトを渡している 54はパケットの開始を示す固定値 x2cは00101100 001は種類1、01100は測定件数12を表している
    print(start)                   # その場所を表示
    if start >= 0 and len(data) >= start + 47:  # startから47バイト分そろっているか確認
        packet = data[start:start + 47]         # startからstart + 47バイト目を格納
        rotational_speed_number = packet[2:4]          #回転速度
        start_speed_number = packet[4:6]               #開始角度
        distance_bytes_1_number = packet[6:8]          #1点目の距離
        reflection_intensity_number = packet[8]        #反射強度
        distance_bytes_2_number = packet[9:11]         #2点目の距離 
        finish_angle_number = packet[42:44]            #終了角度
        time_stamp_number = packet[44:46]              #タイムスタンプ

        rotational_speed = int.from_bytes(rotational_speed_number, byteorder="little")
        start_speed = int.from_bytes(start_speed_number, byteorder="little")
        distance_byte_1 = int.from_bytes(distance_bytes_1_number, byteorder="little") # int.from_bytesでその2バイトを整数に byteorder="littleは、最初のバイトが1の位で、次のバイトが256の位という指定 LD19ではそれでいい
        distance_byte_2 = int.from_bytes(distance_bytes_2_number, byteorder="little")
        finish_angle = int.from_bytes(finish_angle_number, byteorder="little")
        time_stamp = int.from_bytes(time_stamp_number, byteorder="little")

        print("回転速度", rotational_speed, "度/秒")
        print("開始角度", start_speed / 100, "度")
        print("反射強度", reflection_intensity_number)
        print("1点目の距離", distance_byte_1, "mm")
        print("2点目の距離", distance_byte_2, "mm")
        print("終了角度", finish_angle, "度")
        print("タイムスタンプ", time_stamp , "ms")

print("ポートを閉じました")

# with 式 as 名前:
#     ブロックの処理
# Pythonはこの文を次の順番で実行
# 1. 式 を評価して、コンテキストマネージャーを得る。
# 2. そのオブジェクトの開始処理（__enter__）を呼ぶ。`as 名前` があれば、開始処理の戻り値をその名前に代入する。
# 3. 字下げされたブロックを実行する。ブロックを抜けるときに、終了処理（__exit__）を呼ぶ。ブロックの途中で例外が起きた場合も呼ぶ。
# 4. 