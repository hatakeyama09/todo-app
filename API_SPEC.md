# TODOアプリ API設計書

このドキュメントは、TODOアプリにおけるバックエンドAPIの仕様をまとめたものです。
フロントエンド（TypeScript / React）とバックエンド（Python / FastAPI）の共通認識として使用します。

---

## 共通データ構造

### Todo

```ts
Todo {
  id: number
  title: string
  completed: boolean
}
```

---

## API一覧

### 1. Todo一覧取得

* Method: `GET`
* Path: `/todos`
* Description: 登録されているTodoをすべて取得する

#### Response (200)

```json
[
  {
    "id": 1,
    "title": "FastAPIを学ぶ",
    "completed": false
  }
]
```

---

### 2. Todo追加

* Method: `POST`
* Path: `/todos`
* Description: 新しいTodoを追加する

#### Request Body

```json
{
  "title": "TypeScriptを学ぶ"
}
```

#### Response (201)

```json
{
  "id": 2,
  "title": "TypeScriptを学ぶ",
  "completed": false
}
```

---

## 今後追加予定のAPI

### Todo完了状態更新

* Method: `PUT`
* Path: `/todos/{id}`
* Description: Todoの完了状態を切り替える

---

### Todo削除

* Method: `DELETE`
* Path: `/todos/{id}`
* Description: 指定したTodoを削除する

---

## 運用ルール

* API仕様を変更した場合は、必ずこのドキュメントを更新する
* フロントエンド実装は本仕様を正とする
* Swagger UI は実装確認用として利用する
