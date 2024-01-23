# APK 反彙編流程

## 步驟 (1) - 分解 apk 檔案 (unpack)

- 範例檔案: timer.apk
- Linux 安裝: sudo apt install apktool
- Command: apktool d timer.apk

## 步驟 (1) - 直接 apk 轉 java code

- Windows 安裝: 直接下載 zip 即可
- Command: d2j-dex2jar.bat timer.apk --force

## 步驟 (2) - 用 jd-gui 開 java code

- Windows 安裝: 直接下載 zip 即可
- 直接開啟檔案執行即可

## 步驟 (3) - 將 apk 組裝回去

- 通常會對 code 做部分修改，再重組
- Command: apktool b timer.apk

## 額外步驟 - Grep 找字串

- 範例字串: CTF
- 進入解包後的 Folder 目錄
- Command: grep -rn . -e CTF

## 額外步驟 - Jar Signer

- apktool 組裝的 apk 還沒有被 sign 過，因此無法安裝
- 可以隨便生成一個 keystore 或是找現成的來簽署
- Linux 安裝: sudo apt-get install openjdk-19-jdk-headless
- Command: jarsigner -verbose -digestalg SHA1 -keystore ~/KEY.keystore APK_NAME.apk KEY_ALIAS
