# 期中考模擬卷 B

**時間**：兩節課（每題約 50 分鐘）
**範圍**：Ch1、Ch2、Ch3 + 4.1、4.2 String Operations
**限制**：4.3 以後不考，所有 string method **一律不可使用**

---

## 第一題（50 分）Reverse and Palindrome（整數版）

使用 **while-loop 持續輸入**整數 n（位數不限，不是只有 5 位數），對每一個 n 輸出：

1. `reverse = ` 後面接 n 的**數字反轉**後的整數
2. 判斷 n 是不是回文數，是的話輸出 `It is a palindrome`，不是的話輸出 `It is not a palindrome`

- 當 n == 0，結束程式
- n < 0 時輸出 `invalid`，繼續要求輸入

### 執行結果

```
input n 12321
reverse = 12321
It is a palindrome
input n 1234
reverse = 4321
It is not a palindrome
input n 7
reverse = 7
It is a palindrome
input n -5
invalid
input n 0
```

### 注意

- **不可以把數字轉成字串再反轉**（不可用 `str(n)[::-1]`），必須用整數除法 `//` 和餘數 `%` 一位一位取出
- 反轉後的結果要是**整數**，不是字串

---

## 第二題（50 分）Caesar Cipher（凱撒密碼）

**Caesar cipher** 是把字母表中的每個字母往後位移固定格數的加密法。例如位移 3 時，`a` 變成 `d`、`b` 變成 `e`、`x` 變成 `a`（繞回開頭）。

輸入一個字串 s 和一個整數 k（位移量），輸出加密後的字串。規則：

- 小寫英文字母 `a`–`z` 位移後仍是小寫，超過 `z` 要繞回 `a`
- 大寫英文字母 `A`–`Z` 位移後仍是大寫，超過 `Z` 要繞回 `A`
- **其他字元（空白、標點、數字）原樣保留，不做任何變動**
- k 可以是負數（往前位移），也可以大於 26

### 執行結果

```
input s Hello, World!
input k 3
Khoor, Zruog!
```

```
input s abcXYZ
input k 3
defABC
```

```
input s abc
input k -1
zab
```

```
input s abc
input k 29
def
```

### 提示

- 用 `ord()` 把字元轉成整數、`chr()` 把整數轉回字元
- 判斷是不是小寫字母可以直接比大小：`if 'a' <= ch <= 'z':`
- 繞回開頭用 `%` 26
- k 先做 `k = k % 26`，負數和超過 26 的情況就一起解決了
