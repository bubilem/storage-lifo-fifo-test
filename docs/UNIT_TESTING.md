# Průvodce Unit testováním v Pythonu (`unittest`)

Tento dokument slouží jako srozumitelný návod pro žáky a studenty, jak funguje automatické testování kódu, jak je testovací třída poskládaná a jak se testy spouští a vyhodnocují.

---

## 1. Co je to Unit test (jednotkový test)?

**Unit test** je krátký kód, který automaticky ověřuje, zda se konkrétní malá část programu (třída, metoda nebo funkce) chová přesně tak, jak očekáváme.

Místo toho, abyste program pokaždé spouštěli ručně a zkoušeli zadávat vstupy do konzole, napíšete testy. Ty proběhnou za zlomek sekundy a řeknou vám: **„Vše funguje“** nebo **„Na řádku X je chyba“**.

### Univerzální vzor AAA (Arrange – Act – Assert)
Každý dobře napsaný test se skládá ze tří kroků:
1. **Arrange (Připrav):** Vytvoříte potřebné objekty a připravíte data.
2. **Act (Proveď):** Zavoláte testovanou metodu (provedete akci).
3. **Assert (Ověř):** Zkontrolujete, zda je výsledek přesně takový, jaký má být.

Příklad z našeho kódu:
```python
def test_stack_lifo_order(self):
    # 1. Arrange (Připrav)
    stack = Stack()
    stack.push(10)
    stack.push(20)

    # 2. Act (Proveď)
    vysledek = stack.pop()

    # 3. Assert (Ověř)
    self.assertEqual(vysledek, 20)
```

---

## 2. Anatomie testovacího souboru (`tests/test_storage.py`)

Podívejme se na základní strukturu souboru s testy:

```python
import unittest                               # 1. Import vestavěné knihovny pro testy
from src.storage import Queue, Stack, Storage # 2. Import kódu ze složky src


class TestStorageHierarchy(unittest.TestCase): # 3. Testovací třída dědící z unittest.TestCase
    
    def test_queue_fifo_order(self):           # 4. Testovací metoda (MUSÍ začínat na 'test_')
        """Ověří princip FIFO."""              # 5. Docstring (popis testu pro výpis)
        queue = Queue()
        queue.enqueue(10)
        self.assertEqual(queue.dequeue(), 10)


if __name__ == "__main__":                # 6. Spouštěcí blok
    unittest.main()
```

### Klíčová pravidla struktury:

#### 1. Dědičnost z `unittest.TestCase`
Všechny vaše testovací třídy **musí dědit** z `unittest.TestCase`. Tím vaše třída získá všechny potřebné schopnosti (kontrolní metody `self.assertEqual`, zachytávání chyb atd.).

#### 2. Pustí se automaticky všechny metody? Magická předpona `test_`
Častá otázka: *„Pustí `unittest` automaticky všechny metody v mé třídě?“*
**Ano, ale POUZE ty, jejichž název začíná na `test_`!**

Funguje to pomocí tzv. *Test Discovery* (automatického vyhledávání testů):
* `unittest` vezme třídu a prozkoumá její metody.
* Metoda `test_stack_lifo_order` $\rightarrow$ začíná na `test_` $\rightarrow$ **automaticky se spustí**.
* Metoda `test_queue_fifo_order` $\rightarrow$ začíná na `test_` $\rightarrow$ **automaticky se spustí**.
* Kdybyste si vytvořili pomocnou metodu např. `def vygeneruj_testovaci_cisla(self):` $\rightarrow$ **nespustí se jako test**, ale můžete ji volat z ostatních testů jako pomocníka.

#### 3. Pozor na pořadí spouštění (Abecední pravidlo!)
Metody se **nespouští shora dolů**, jak jste je v souboru napsali!
Ve výchozím nastavení je `unittest` řadí a spouští **abecedně podle jejich názvu**.
* **Důsledek:** Nikdy nesmíte spoléhat na to, že jeden test proběhne dříve než druhý. Každý test musí být 100% soběstačný a nezávislý.

#### 4. Docstring (dokumentační komentář pod hlavičkou metody)
Text v trojitých uvozovkách `"""Ověří metodu clear()."""` slouží jako srozumitelný lidský popis. Když testy spustíte v podrobném režimu, uvidíte přímo tento text.

---

## 3. Kontrolní metody (Assert metody)

Uvnitř testu nikdy nepoužíváme `print()`. Používáme speciální metody začínající na `self.assert...`, které dokáží porovnat výsledek s očekáváním:

| Metoda | Co kontroluje | Příklad použití |
| :--- | :--- | :--- |
| **`self.assertEqual(a, b)`** | Zda se `a` rovná `b`. Pokud ne, test selže a vypíše obě hodnoty. | `self.assertEqual(stack.size(), 0)` |
| **`self.assertTrue(x)`** | Zda je výraz `x` pravdivý (`True`). | `self.assertTrue(stack.is_empty())` |
| **`self.assertFalse(x)`** | Zda je výraz `x` nepravdivý (`False`). | `self.assertFalse(stack.is_empty())` |
| **`self.assertIsInstance(obj, Trida)`** | Zda je objekt instancí dané třídy (dědičnost). | `self.assertIsInstance(stack, Storage)` |
| **`self.assertRaises(Vyjimka)`** | Zda kód správně vyhodí očekávanou výjimku/chybu. | *Viz níže* |

### Jak testovat vyvolání výjimky (`assertRaises`)
Často chceme ověřit, že kód správně zahlásí chybu (např. když chceme vybrat prvek z prázdného zásobníku). K tomu slouží blok `with self.assertRaises(...)`:

```python
def test_stack_empty_pop_raises_error(self):
    """Ověří vyvolání výjimky při pop() z prázdného zásobníku."""
    stack = Stack()
    
    # Říkáme: následující řádek MUSÍ vyvolat IndexError.
    # Pokud IndexError nenastane, test SELŽE!
    with self.assertRaises(IndexError):
        stack.pop()
```

---

## 4. Jak testy spouštět a co znamenají parametry příkazu

### Příkaz pro spuštění všech testů:
```bash
python -m unittest discover -s tests -v
```

### Rozpad příkazu na jednotlivé části:
* **`python`**: Spouští interpret jazyka Python.
* **`-m unittest`**: Přepínač `-m` znamená **module** (modul). Spustí vestavěný testovací modul Pythonu.
* **`discover`**: Automaticky prohledá složku a najde všechny soubory a třídy s testy.
* **`-s tests`**: Parametr `-s` (*start directory*) říká: *„Hledej testy uvnitř složky `tests`.“*
* **`-v`** (nebo `--verbose`): Zapíná **podrobný výpis**.
  * **Bez `-v`**: Python vypíše pouze tečky za každý úspěšný test:
    ```text
    .......
    ----------------------------------------------------------------------
    Ran 7 tests in 0.001s
    OK
    ```
  * **S `-v`**: Python vypíše název každého testu i s jeho popisem (docstringem):
    ```text
    test_common_method_clear (test_storage.TestStorageHierarchy.test_common_method_clear)
    Ověří metodu clear(). ... ok
    test_queue_fifo_order (test_storage.TestStorageHierarchy.test_queue_fifo_order)
    Ověří princip FIFO (First In, First Out). ... ok
    ```

### Jak spustit pouze jeden konkrétní test?
Nemusíte spouštět vždy všechny testy naráz:
```bash
# 1. Spuštění celého souboru s testy:
python tests/test_storage.py -v

# 2. Nebo spuštění pouze jedné vybrané metody:
python -m unittest tests.test_storage.TestStorageHierarchy.test_stack_lifo_order -v
```

---

## 5. Jak číst výsledky testů

Když testy doběhnou, mohou nastat 3 stavy:

### 1. `ok` (Vše v pořádku)
Všechny podmínky `assert` byly splněny, kód dělá přesně to, co má.

### 2. `FAIL` (Logická chyba)
Kód sice běží bez pádu, ale vrátil špatnou hodnotu.
```text
FAIL: test_stack_lifo_order (test_storage.TestStorageHierarchy)
AssertionError: 10 != 30
```
$\rightarrow$ *Vysvětlení:* Očekávali jsme hodnotu `30` (vrchol zásobníku), ale metoda vrátila `10`. Máme chybu v logice LIFO!

### 3. `ERROR` (Pád programu / Výjimka)
V kódu nastala neočekávaná chyba dříve, než mohl proběhnout samotný assert (např. překlep v názvu proměnné `NameError`, dělení nulou `ZeroDivisionError`, nebo metoda ještě není implementovaná).

---

## 6. Pro pokročilé: `setUp()` a `tearDown()`

Pokud v každém testu musíte zakládat stejný objekt znovu a znovu:
```python
def setUp(self):
    """Tato metoda se automaticky spustí PŘED KAŽDÝM jednotlivým testem."""
    self.stack = Stack()
    self.queue = Queue()

def tearDown(self):
    """Tato metoda se automaticky spustí PO KAŽDÉM jednotlivém testu (např. úklid souborů)."""
    pass
```
Díky tomu mají testy vždy čistý a nezávislý stav a neovlivňují se navzájem.

---

## 7. Nejčastější chyby začátečníků

1. **Chybějící `test_` v názvu:** Metoda `def zasobnik_funguje(self):` se vůbec nespustí! Vždy pište `def test_zasobnik_funguje(self):`.
2. **Použití obyčejného `assert a == b`:** Funguje, ale při chybě nevypíše, jaké hodnoty se neshodovaly. Vždy používejte `self.assertEqual(a, b)`.
3. **Závislost testů na sobě:** Test B by nikdy neměl spoléhat na to, co udělal Test A. Každý test musí být schopen běžet samostatně v libovolném pořadí.
