# Way Too Long Words  
## 📚 Description  
Sometimes, words like **localization** or **internationalization** are so long that repeating them multiple times becomes *tiresome*. To simplify, we can **abbreviate** such words using a specific rule.

A word is considered **too long** if its length is **strictly more than 10 characters**.

The abbreviation rule is:  
- Keep the **first** and **last** letters.  
- Replace the letters **in between** with the **count of those letters** in decimal form.

### 🔤 Examples:  
**localization** → `l10n`  
**internationalization** → `i18n`  

Words that are **not too long** remain **unchanged**.  

---

## 📥 Input  
- The first line contains an integer `n` (1 ≤ n ≤ 100) — the number of words.  
- Each of the next `n` lines contains one word.  
- All words consist of **lowercase Latin letters** and have lengths from **1 to 100** characters.  

---

## 📤 Output  
- Print `n` lines.  
- Each line should contain the **abbreviated word** if the word is too long, or the **original word** if it is not.  

---

## ✅ Example  

### **Input**  
```
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
```

### **Output**  
```
word
l10n
i18n
p43s
```

---

## 💡 Explanation  

**word** → 4 characters → not too long → stays the same.  
**localization** → first: `l`, last: `n`, 10 letters in between → `l10n`  
**internationalization** → first: `i`, last: `n`, 18 letters in between → `i18n`  
**pneumonoultramicroscopicsilicovolcanoconiosis** → 45 characters → `p43s`

---

🔗 **Problem Link:** [Way Too Long Words – Codeforces](https://codeforces.com/problemset/problem/71/A)
