# 期中考模擬卷 A

**時間**：兩節課（每題約 50 分鐘）
**範圍**：Ch1、Ch2、Ch3 + 4.1、4.2 String Operations
**限制**：4.3 以後不考，所有 string method（`upper()`、`find()`、`split()`、`replace()`、`format()`…）**一律不可使用**

可用的工具只有：`input()`、`int()`、`float()`、`str()`、`len()`、`ord()`、`chr()`、`range()`、`enumerate()`、`reversed()`、`abs()`、`round()`、`math` 模組、索引、切片、`+`、`*`、`in`、f-string、if/elif/else、while、for、break、continue。

---

## 第一題（50 分）Harshad Number（尼文數）

A **Harshad number** (尼文數) is an integer that is divisible by the sum of its own digits.
一個正整數如果能被「它自己各位數字之和」整除，就稱為尼文數。

例如：
- `18` → 各位數字和 `1 + 8 = 9`，而 `18 % 9 == 0`，所以 18 **是**尼文數
- `11` → 各位數字和 `1 + 1 = 2`，而 `11 % 2 == 1`，所以 11 **不是**尼文數

使用 **while-loop 持續輸入** nonnegative integer n (n >= 0)，找出 **1 到 n 之間所有的尼文數**並列出，最後輸出總共有幾個。

- 當 n == 0，結束程式
- 程式必須驗證 n 是否為 nonnegative integer，若為負數輸出 `invalid` 並繼續要求輸入

### 執行結果

```
input n 20
1 2 3 4 5 6 7 8 9 10 12 18 20
total = 13
input n -3
invalid
input n 0
```

---

## 第二題（50 分）Character Search and Removal

輸入一個字串 s，再輸入一個字元 c，請輸出以下三行：

1. `index:` 後面接 c 在 s 中**所有出現位置的索引**，以空白分隔
2. `count:` 後面接 c 在 s 中出現的**總次數**
3. `removed:` 後面接把 s 中**所有的 c 刪掉**之後剩下的字串

若 c 完全沒有出現在 s 中，`index:` 後面留空、`count:` 為 0、`removed:` 就是原字串。

### 執行結果

```
input s banana
input c a
index: 1 3 5
count: 3
removed: bnn
```

```
input s hello
input c z
index:
count: 0
removed: hello
```

### 注意

- 不可使用任何 string method
- 第三行的答案必須是**組好的一個字串**，不可以邊跑迴圈邊 `print(..., end="")` 湊出畫面
