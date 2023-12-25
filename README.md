# mypkg
[![test](http://github.com/shouzaki-git/mypkg/actions/workflows/test.yml/badge.svg)](http://github.com/shouzaki-git/mypkg/actions/workflows/test.yml/badge.svg)

パブリッシャーのtalkerとサブスクライバーのlistenerが通信している様子を見る

## このソフトウェアについて

launchで実行するためtalkerとlistenerを同時に観測可能

## 使い方
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
