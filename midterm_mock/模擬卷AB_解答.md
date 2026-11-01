# 模擬卷 A / B 參考解答

> 四份都已實際執行驗證過，輸出與題目的執行結果完全相符。
> **先自己寫完再看。**

---

## 卷 A 第一題 — Harshad Number

```python
while True:
    n = int(input("input n "))
    if n == 0:
        break
    elif n < 0:
        print("invalid")
    else:
        count = 0
        k = 1
        while k <= n:
            m = k                  # 另存一份，不要破壞 k
            s = 0
            while m > 0:
                s += m % 10        # 取出個位數
                m //= 10           # 砍掉個位數
            if k % s == 0:
                print(k, end=" ")
                count += 1
            k += 1
        print()                    # 補換行
        print(f"total = {count}")
```

### 三層結構
1. 最外層：輸入迴圈（0 結束、負數 invalid）
2. 中層：`k` 從 1 掃到 n
3. 內層：把 `k` 的各位數字加起來

### 常見錯誤
- **拿 `k` 本身去除**：`while k > 0: k //= 10` 會把 `k` 砍成 0，外層迴圈直接失控。一定要另存 `m = k`。
- **`s` 歸零的位置**：`s = 0` 必須在中層迴圈**裡面**，每個 k 都要重算。放在外面會一路累加。
- **忘了 `print()` 換行**：`total = 13` 會黏在最後一個數字後面。

---

## 卷 A 第二題 — Character Search and Removal

```python
s = input("input s ")
c = input("input c ")

pos = ""
count = 0
rest = ""

i = 0
while i < len(s):
    if s[i] == c:
        pos += str(i) + " "
        count += 1
    else:
        rest += s[i]
    i += 1

print("index:", pos)
print("count:", count)
print("removed:", rest)
```

用 `for i, ch in enumerate(s):` 也可以，更簡潔：

```python
for i, ch in enumerate(s):
    if ch == c:
        pos += str(i) + " "
        count += 1
    else:
        rest += ch
```

### 常見錯誤
- **`pos` 和 `rest` 用覆寫而不是累加**（`pos = str(i)`），畫面看起來可能還對，但變數裡只剩最後一個值。這一題明文要求組成字串，一定要用 `+=`。
- **索引要用 `enumerate()` 或 `range(len(s))`**；寫成 `for ch in s:` 就拿不到 index。
- **`str(i)`**：`pos` 是字串，不能直接 `+= i`（int 不能加到 str），會 TypeError。
- c 沒出現時三行都還是要印，不要用 if 包起來整段跳過。

---

## 卷 B 第一題 — Reverse and Palindrome

```python
while True:
    n = int(input("input n "))
    if n == 0:
        break
    elif n < 0:
        print("invalid")
    else:
        m = n
        rev = 0
        while m > 0:
            rev = rev * 10 + m % 10     # 關鍵這行
            m //= 10
        print(f"reverse = {rev}")
        if rev == n:
            print("It is a palindrome")
        else:
            print("It is not a palindrome")
```

### `rev = rev * 10 + m % 10` 在做什麼

以 n = 123 為例：

| m | `m % 10` | rev 變化 |
|---|---|---|
| 123 | 3 | 0*10+3 = **3** |
| 12 | 2 | 3*10+2 = **32** |
| 1 | 1 | 32*10+1 = **321** |
| 0 | — | 迴圈結束 |

舊的 rev 往左推一位（`*10`），空出來的個位填新取出的數字。

### 常見錯誤
- **直接改 `n`**：比對 `rev == n` 時 n 已經被砍成 0，永遠判成不是回文。必須 `m = n`。
- **`rev` 忘了在 else 裡歸零**：下一輪會接著上一輪的值繼續累。
- **用字串偷吃步**：`str(n)[::-1]` 這題明文禁止。

---

## 卷 B 第二題 — Caesar Cipher

```python
s = input("input s ")
k = int(input("input k "))
k = k % 26                  # 先正規化，負數和 >26 一起解決

out = ""
i = 0
while i < len(s):
    ch = s[i]
    if 'a' <= ch <= 'z':
        out += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    elif 'A' <= ch <= 'Z':
        out += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
    else:
        out += ch           # 其他字元原樣保留
    i += 1
print(out)
```

### 那串運算拆解

以 `ch = 'y'`、`k = 3` 為例：

| 步驟 | 運算 | 結果 | 意義 |
|---|---|---|---|
| 1 | `ord('y') - ord('a')` | 24 | 轉成 0–25 的位置 |
| 2 | `24 + 3` | 27 | 位移 |
| 3 | `27 % 26` | 1 | 繞回開頭 |
| 4 | `1 + ord('a')` | 98 | 轉回 UTF-8 碼 |
| 5 | `chr(98)` | `'b'` | 轉回字元 |

**第 1 步的 `- ord('a')` 是整題的關鍵**：不先轉成 0–25，`% 26` 就會算在錯誤的基準上。

### 常見錯誤
- **漏了 `- ord('a')`**：直接 `chr((ord(ch) + k) % 26)` 會得到奇怪的控制字元。
- **大小寫共用同一個基準**：大寫必須用 `ord('A')`，不能用 `ord('a')`。
- **沒處理負數 k**：Python 的 `%` 對負數會回傳正值（`-1 % 26` 是 25），所以開頭做 `k = k % 26` 就安全了。若少了這行，k = -1 時 `(0 - 1) % 26 = 25`，其實也還是對的 —— 但 k 很大時（如 100）不先正規化容易在其他寫法中出錯，養成習慣比較好。
- **`out` 用覆寫**：同樣要 `+=`。

---

## 交卷前檢查清單

- [ ] 迴圈裡要修改的值，有沒有**另存一份**（`m = n`）？
- [ ] 累加用的變數（`total`、`count`、`out`、`rev`）有沒有在**正確的位置歸零**？
- [ ] 組字串用的是 `+=` 而不是 `=`？
- [ ] 輸入 **0**、**負數**、**空字串**、**目標不存在** 各測一次
- [ ] `end=" "` 之後有沒有補 `print()` 換行？
- [ ] 題目要求的訊息文字（`total = `、`It is a palindrome`）有沒有**一字不差**？
