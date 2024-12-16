# -*- coding: utf-8 -*-
"""210henkan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zgKTCtBiD3344RhfPLd0gyEyIxFlHjDl
"""

import streamlit as st

# タイトル
st.title("2進数・10進数変換アプリ")

# 変換タイプの選択
conversion_type = st.radio(
    "変換タイプを選択してください:",
    ("10進数 → 2進数", "2進数 → 10進数")
)

# 入力フィールド
input_value = st.text_input("値を入力してください:")

# 変換ボタン
if st.button("変換"):
    try:
        if conversion_type == "10進数 → 2進数":
            # 入力を10進数として2進数に変換
            result = bin(int(input_value))[2:]
            st.success(f"結果: {result}")
        elif conversion_type == "2進数 → 10進数":
            # 入力を2進数として10進数に変換
            result = int(input_value, 2)
            st.success(f"結果: {result}")
    except ValueError:
        st.error("正しい値を入力してください。")