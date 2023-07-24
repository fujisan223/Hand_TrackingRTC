# Hand_TrackingRTC
## 概要
* mediapipeが提供しているhand_trackingのライブラリをRTCとして実装したものです．
* 参考URL
  * https://www.section.io/engineering-education/creating-a-hand-tracking-module/

## コンポーネント内容
1. hand_tracking
   * ハンドトラッキングを行い，手の座標(xyz)を送信するコンポーネント
   * 手の開閉(手を握ったか開いたか)も判断可能
2. hand_tracking_check
   * hand_trackingRTCの動作確認用RTC
   * 送られてきたデータを表示するだけ
   * 実行ファイルはhand_tracking_check\build\src\Release\hand_tracking_checkComp.exe
