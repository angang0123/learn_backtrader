# backtrader library learning notes

Study backtrader. Following official documentation as of 2022.12.29

## Platform Concepts

### Data Feeds

The basis of the work with the platform will be done with **Strategies**. And these will get passed **Data Feeds**.

- Almost everything is a Data Feed. **Indicators** and results of **Operations** are also data.

- Almost every other class in the platform supports the notion of parameters.
    - Parameters along with default values are declared as a class attribute (tuple of tuples or dict-like object)
    - Keywords args (**kwargs) are scanned for matching parameters, removing them from **kwargs if found and assigning the value to corresponding parameter
    - And parameters can be finally used in instances of the class by accessing the member variable *self.params*
    
- Almost every other object in the platform is a **Lines** enabled object, meaning it can hold one of more line series. Being a line series an array of values were the values put together in a chart they would form a line.
    - E.g. *self.data.lines.close[0]*
    - If an **Indicator** is being developed, the *lines* which the indicator has must be declared. Just as with *params*, this takes place as a class attribution **ONLY** as a tuple.
    


    
