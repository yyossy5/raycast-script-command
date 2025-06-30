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
そのため、バックアップを簡単に出来るようにコマンド化しておく
"""

import shutil
from pathlib import Path

# --- 設定項目 ---

# ホームディレクトリを自動で取得
home_dir = Path.home()

# コピー元のディレクトリ (ホームディレクトリからの相対パスで指定)
# 例: /Users/yuki_yoshida/myobs/work の場合
source_rel_path = "myobs/work"

# コピー先のディレクトリ (ホームディレクトリからの相対パスで指定)
# 例: /Users/yuki_yoshida/Documents/Backup/bk_myobs/work の場合
destination_rel_path = "Documents/Backup/bk_myobs/work"

# 絶対パスを生成
source_dir = home_dir / source_rel_path
destination_dir = home_dir / destination_rel_path


# --- メイン処理 ---

def backup_directory(src, dst):
    """
    ディレクトリをコピーする関数
    :param src: コピー元ディレクトリのパス (Pathオブジェクト)
    :param dst: コピー先ディレクトリのパス (Pathオブジェクト)
    """
    print("コピー処理を開始します...")
    # .resolve() を使うとシンボリックリンクなどを解決した完全なパスが表示される
    print(f"コピー元: {src.resolve()}")
    print(f"コピー先: {dst.resolve()}")

    try:
        if not src.is_dir():
            print(f"\nエラー: コピー元ディレクトリが見つかりません。")
            print(f"パスを確認してください: {src}")
            return

        shutil.copytree(src, dst, dirs_exist_ok=True)

        print(f"\nディレクトリのコピーが正常に完了しました。")

    except Exception as e:
        print(f"\nエラーが発生しました: {e}")


if __name__ == "__main__":
    backup_directory(source_dir, destination_dir)
