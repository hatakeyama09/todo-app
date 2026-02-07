# Todoアプリ 作成手順まとめ（Python × TypeScript）

このドキュメントは、Python（FastAPI）と TypeScript（React + Vite）を用いて todo-app を作成する際の
**環境構築〜初期設計までの手順**と、**今回実際に躓いたポイントと対処法**をまとめたものです。

将来、同様の構成でアプリを作成する際の再利用を目的としています。

---

## 1. プロジェクト全体構成

```txt
todo-app/
├─ README.md        # 起動手順・概要
├─ API_SPEC.md      # API設計書
├─ SETUP_GUIDE.md   # 本ドキュメント
├─ backend/
│  ├─ venv/
│  └─ main.py
└─ frontend/
   ├─ src/
   └─ package.json
```

---

## 2. Backend 環境構築（Python / FastAPI）

### 2.1 backend ディレクトリ作成

```powershell
mkdir todo-app
cd todo-app
mkdir backend
cd backend
```

---

### 2.2 Python 仮想環境作成

```powershell
python -m venv venv
```

仮想環境を有効化：

```powershell
venv\Scripts\activate
```

成功するとプロンプトに `(venv)` が表示される。

---

### 2.3 FastAPI インストール

```powershell
pip install fastapi uvicorn
```

---

### 2.4 FastAPI 最小構成

`backend/main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}
```

---

### 2.5 起動確認

```powershell
uvicorn main:app --reload
```

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

が表示されれば成功。

---

## 3. Frontend 環境構築（React / TypeScript）

### 3.1 Vite プロジェクト作成

```powershell
npm create vite@latest frontend
```

選択項目：

* Framework: React
* Variant: TypeScript

---

### 3.2 rolldown-vite について

```txt
Use rolldown-vite (Experimental)?
```

→ **No を選択**

理由：

* Experimental 機能
* 学習用途では不要
* トラブルシュート情報が少ない

---

### 3.3 依存関係インストールと起動

```powershell
cd frontend
npm install
npm run dev
```

* [http://localhost:5173](http://localhost:5173)

が表示されれば成功。

---

## 4. 設計ドキュメントの分離方針

* README.md：起動手順・概要のみ
* API_SPEC.md：API仕様・データ構造

設計と手順を分離することで、保守性と再利用性を高める。

---

## 5. 今回躓いたポイントと対処法

### 5.1 PowerShell で仮想環境が有効化できない

#### 症状

```
このシステムではスクリプトの実行が無効になっている
```

#### 原因

PowerShell の実行ポリシー制限。

#### 対処法

管理者権限の PowerShell で以下を実行：

```powershell
Set-ExecutionPolicy RemoteSigned
```

---

### 5.2 uvicorn コマンドが見つからない

#### 症状

```
'uvicorn' は認識されません
```

#### 原因

* 仮想環境が有効化されていない
* uvicorn が未インストール

#### 対処法

```powershell
venv\Scripts\activate
pip install fastapi uvicorn
```

---

### 5.3 main.py の作成場所が分からない

#### 正解

```txt
backend/main.py
```

`uvicorn main:app` は、実行ディレクトリ直下の `main.py` を参照する。

---

### 5.4 npm の質問項目で迷う

* rolldown-vite → No
* Install with npm and start now → Yes

---

## 6. 次回再開時の作業ポイント

* API_SPEC.md を正として FastAPI 実装開始
* `/todos` API 作成
* Swagger UI で仕様と実装の一致を確認

---

## 7. 補足

* 環境構築後すぐに README / 設計書を作成するのは良い習慣
* 学習用でも実務を意識した構成を心がける
* 躓きポイントは必ずドキュメント化すると再発防止になる

---

以上
