# 機械系解題筆記站
繁體中文的工程基礎筆記網站，使用一致的格式說明觀念、公式條件、例題與常見錯誤。

## 目前內容
- cₚ 和 cᵥ 的使用時機
- 軸向受拉、受壓與正負號
- 理想氣體方程式與單位

## 本機操作
需要 Python 3，無外部套件：
```sh
python3 make.py
python3 package.py
python3 check.py
python3 -m http.server 8000 --directory dist
```
開啟 http://localhost:8000，也可直接開 dist/index.html。

## 新增內容
先讀 AGENTS.md。複製 templates/note.json 的物件到 content.json，填入所有欄位後執行以上前三個指令。產生器自動更新首頁卡片與文章，無需重做版型。
可對 AI 說：「請先閱讀 AGENTS.md，新增一篇 thermal-stress 熱應力筆記，包含自編例題和練習，完成後執行產生與檢查流程。」

## 上傳 GitHub 並公開
1. 在自己的 GitHub 建立公開 Repository，例如 mech-notes。
2. 解壓專案 ZIP，將檔案和資料夾上傳到 Repository 根目錄。請確認 .github/workflows/pages.yml 也有上傳，不要上傳 ZIP 本身取代內容。
3. Repository 的 Settings → Pages，將 Source 設為 GitHub Actions。
4. 到 Actions 執行 Publish notes（或在 main 分支提交更新），等待成功。
5. Pages 設定頁會顯示實際網站網址，請複製該網址繳交。
本專案不包含已建立的個人 GitHub Repository；上傳前不要填寫假連結。

## 作業繳交文字
標題：成大機械118林佑蔚 機械系解題筆記站

專案簡介：我建立了一個機械工程基礎課程的解題筆記網站，整理熱力學與材料力學的觀念、公式使用條件和常見錯誤。網站提供搜尋、科目篩選與可展開答案的練習題。

GitHub Repository：[填入實際 Repository 連結]
網頁連結：[填入實際公開網址]
AGENTS.md：[附檔或填入 Repository 中的 AGENTS.md 連結]

延伸方式：我在 AGENTS.md 規定內容欄位、檔案命名、頁面樣式與檢查步驟。未來新增筆記時，AI 可以參考 JSON 範本撰寫內容，再透過產生器自動新增文章及首頁入口，延續相同的閱讀格式與網站風格。
