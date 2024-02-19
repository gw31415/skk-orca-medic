# Anthy用医療辞書

Anthy用かな漢字変療辞書です。
主に日医標準レセプトソフトの利用を想定して作成されました。

orca-medic-0.0.2 の辞書を最新に更新し加工してあります。
元の辞書はMozc用に変換され、Anthy用はMozc用辞書から変換されて作成されています。

## ライセンセス
GPL2

## インストール方法

1. 展開した medic.t を /usr/share/anthy/dic/ にコピーします。

    ```
    $ sudo cp medic.t /usr/share/anthy/dic/
    ```

2. /etc/anthy/diclist に medic.t を追加します。

    ```
    $ sudo gedit diclist
    base.t
    extra.t
    medic.t
    ```

3. update-anthy-dicsを実行します。

    ```
    $ sudo update-anthy-dics
    ```

4. iBusの再起動等をして有効にします。
