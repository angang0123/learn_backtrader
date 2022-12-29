# backtrader library learning notes

Study backtrader. Following official documentation as of 2022.12.29

## Platform Concepts

### Data Feeds

The basis of the work with the platform will be done with **Strategies**. And these will get passed **Data Feeds**.

Almost everything is a Data Feed. **Indicators** and results of **Operations** are also data.

### Parameters

Almost every other class in the platform supports the notion of parameters.
- Parameters along with default values are declared as a class attribute (tuple of tuples or dict-like object)
- Keywords args (**kwargs) are scanned for matching parameters, removing them from **kwargs if found and assigning the value to corresponding parameter
- And parameters can be finally used in instances of the class by accessing the member variable *self.params*

### Lines
    
Almost every other object in the platform is a **Lines** enabled object, meaning it can hold one of more line series. Being a line series an array of values were the values put together in a chart they would form a line.
- E.g. *self.data.lines.close[0]*
- If an **Indicator** is being developed, the *lines* which the indicator has must be declared. Just as with *params*, this takes place as a class attribution **ONLY** as a tuple.
    
#### Accessing *lines* in Data Feeds

- self.data.close[0]
- self.data.lines.close[0]

Both work, but the same doesn't apply to *Indicators*. Because an *Indicator* could have an attribute *close* which holds an intermediate calculation.

In the case of *Data Feeds*, no calculation takes place, because it is only a data source.

#### Lines len

- *len* function applies to
    - Data Feeds
    - Strategies
    - Indicators
    
- *buflen* applies to (when data is **preloaded**)
    - Data Feeds
    
Difference:
- *len* reports how many bars have been processed
- *buflen* reports the total number of bars which have been loaded for the Data Feed

#### Inheritance

TBD


### Indexing 0 and -1

TBD

Slicing for *lines* objects is not supported.

An array with the latest values can still be gotten.

E.g. myslice = self.my_sma.get(ago=0, size=1)

### Lines: DELAYED indexing

TBD

### Lines Coupling

TBD

### Operators, using natural constructs

#### 1. Operators Create Objects

Operators create objects that can be operated upon, assigned or kept as reference for later using during the evaluation phrase of the Strategy's logic.

#### 2. Operators true to nature

Some non-overriden operators/functions

- Operators:
    - and -> And
    - or -> Or
- Logic Control:
    - if -> If
- Functions:
    - any -> Any
    - all -> All
    - cmp -> Cmp
    - max -> Max
    - min -> Min
    - sum -> Sum
    - reduce -> Reduce
    
