#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title backup-myobs-no-vcs-dir
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 🔁

# Documentation:
# @raycast.author yyossy5
# @raycast.authorURL https://raycast.com/yyossy5

"""
myobs/workは仕事用のメモ置き場で、git管理しない。
しかしgitの操作ミス等で消えてしまうと困る。
そのため、バックアップを簡単に出来るようにコマンド化しておく。
"""

import shutil
from pathlib import Path

# --- 設定項目 ---

home_dir = Path.home()
source_rel_path = "myobs/work"
destination_rel_path = "Documents/Backup/bk_myobs/work"

# 絶対パスを生成
source_dir = home_dir / source_rel_path
destination_dir = home_dir / destination_rel_path


def sync_directory(src, dst):
    """
    ディレクトリを同期（ミラーリング）する関数
    :param src: コピー元ディレクトリのパス (Pathオブジェクト)
    :param dst: コピー先ディレクトリのパス (Pathオブジェクト)
    """
    print("ディレクトリの同期処理を開始します...")
    print(f"同期元: {src.resolve()}")
    print(f"同期先: {dst.resolve()}")

    try:
        # 同期元ディレクトリの存在をチェック
        if not src.is_dir():
            print(f"\nエラー: 同期元ディレクトリが見つかりません。")
            print(f"パスを確認してください: {src}")
            return

        # 同期先にディレクトリが既に存在する場合、一度削除する
        if dst.exists():
            print(f"\n既存の同期先ディレクトリを削除しています: {dst}")
            shutil.rmtree(dst)
            print("削除が完了しました。")

        # ディレクトリをコピーする
        print("\nファイルのコピーを開始します...")
        shutil.copytree(src, dst)

        print(f"\nディレクトリの同期が正常に完了しました。")

    except Exception as e:
        print(f"\nエラーが発生しました: {e}")


if __name__ == "__main__":
    sync_directory(source_dir, destination_dir)
