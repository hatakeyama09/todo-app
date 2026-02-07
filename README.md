# Todo App (Python × TypeScript)

Python（FastAPI）と TypeScript（React + Vite）で作成する学習用TODOアプリです。

---

## 技術スタック

### Backend

* Python
* FastAPI
* Uvicorn
* venv（仮想環境）

### Frontend

* React
* TypeScript
* Vite
* npm

---

## ディレクトリ構成

```
todo-app/
├─ backend/
│  ├─ venv/
│  └─ main.py
└─ frontend/
   ├─ src/
   ├─ package.json
   └─ vite.config.ts
```

---

## 起動手順

### 1. バックエンド（FastAPI）起動

```powershell
cd backend
venv\Scripts\activate
uvicorn main:app --reload
```

起動後、以下にアクセスできます。

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 2. フロントエンド（React + TypeScript）起動

```powershell
cd frontend
npm run dev
```

起動後、以下にアクセスできます。

* [http://localhost:5173](http://localhost:5173)

---

## 開発メモ

* バックエンドとフロントエンドは別ポートで起動する
* APIの動作確認には Swagger UI（/docs）を使用する
* 学習目的のため、まずはローカル環境のみで開発する

---

## 今後の予定

* TODO API（/todos）の実装
* ReactからAPIを呼び出す
* 完了・削除機能の追加
* DB（SQLite）対応

---

## 備考

このREADMEは学習進行に合わせて随時更新する。
