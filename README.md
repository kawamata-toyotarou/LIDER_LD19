# LIDER_LD19

LIDER_LD19を動かすリポジトリ

## やったこと

1. py -m pip install pyserialでパイソンにシリアル通信の道具を追加 
2. py -m serial.tools.list_portsでWindowsに見えているシリアルポートを一に  して確認、py LIDER_LD19.pyで実行 
3. 32ビットのデータを受信
4. 256ビットのデータを受信し、距離データを計測 
5. 色々なデータの計測をした 