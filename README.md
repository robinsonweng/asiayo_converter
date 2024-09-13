# API 實作測驗
## 題目一

請使用您熟悉的程式語言與框架,實作一個提供訂單格式檢查與轉換的 API

- 此應用程式將有一支 endpoint 為 POST /api/orders 的 API 作為輸入點

- 此 API 將以以下固定的 JSON 格式輸入。

- 請按照循序圖實作此 API 的互動類別及其衍生類別。實作之類別需符合物件導向設計原則 SOLID 與設計模式。並於該此專案的 README.md 說明您所使用的 SOLID 與
設計模式分別為何。


Q: 以下所有情境皆需附上單元測試,覆蓋成功與失敗之案例。
A: 單元測試的程式碼在 webapp/tests 之下，並且其檔案路徑結構和被測試的程式碼一致

Q: 請使用 docker 包裝您的環境。若未使用 docker 或 docker-compose 不予給分。
A: 啟動專案的方式為 make up


## 如何啟動這個專案?
專案的 domain name 為 `localhost`
swagger 的 url 為 `http://localhost/api/v1/swagger`

- `make up`
在本地啟動本專案

- `make down`
清除本專案 build 所產生的 image

- `make clean`
清除本專案產生的 pycache 和 virtualenv

- `make test`
在啟動本專案後, 此指令會執行自動化測試

- `make style`
在啟動本專案後，此指令會檢查基本的 python coding style

- `make check`
在啟動本專案後，此指令會一併執行自動化測試和檢查基本的 coding style

- `make freeze-dev`
會直接將 django 路徑下 (webapp 下) 的 virtualenv (如果有的話) 內的 libary 清單寫入至 requirements/dev.txt 下
