# mypkg
[![test](http://github.com/shouzaki-git/mypkg/actions/workflows/test.yml/badge.svg)](http://github.com/shouzaki-git/mypkg/actions/workflows/test.yml/badge.svg)

ROS 2の練習用のパッケージです。

## このプログラムについて

* このプログラムでは、パブリッシャーであるtalker.pyがトピックを通してInt16型のメッセージを送信し、サブスクライバーであるlitener.pyでメッセージを受け取り表示する。 
* launchで実行するとtalkerとlistenerを１つのターミナルで実行可能


## 使い方
## 2つのターミナルで実行する場合
* talker側（１つ目のターミナル）
```
$ ros2 run mypkg talker
```
* listenr側（２つ目のターミナル）
```
$ ros2 run mypkg listener
```
## １つのターミナルで実行する場合
```
$ ros2 launch mypkg talk_listen.launch.py
```
talkerからの通信をlistenerが拾っている。

## 必要なソフトウェア
  
* Python
  * テスト済み: 3.7~3.10
* ROS 2

## テスト環境
* Ubuntu22.04


## ライセンス
* このソフトウェアパッケージは、３条項BSDライセンスの下、再頒布及び使用が許可されます。
* このパッケージのコードは、下記のスライド(CC-BY-SA 4.0 by Ryuichi Ueda)のものを、本人の許可を得て自身の著作としたものです。
    * [ryuichiueda/my_slides/robosys_2022](http://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)
* © 2023 Sho Uzaki
