The LSEG Data Library for Python provides a set of ease-of-use interfaces offering your applications a uniform access to the breadth and depth of financial data and services available on the Data Platform.

With this library, the same Python code can be used to retrieve data whatever the access point you choose to connect your application to the Data Platform. It can be either via a direct connection, via Eikon, via LSEG Workspace, via CodeBook or even via a local Real-Time Distribution System.

The library provides several abstraction layers enabling different programming styles and technics suitable for all developers from Financial Coders to Seasoned Developers:

 - Using the __Access layer__ is the easiest way to get LSEG data. The __Access layer__ provides simple interfaces allowing you to rapidly prototype solutions within interactive environments such as Jupyter Notebooks. It has been designed for quick experimentation with our data and for Financial Coders specific needs. 
 - The __Content layer__ is the basement of the Access layer. It provides developers with interfaces suitable for more advanced use cases (synchronous function calls, async/await, event driven). The __Content layer__ refers to logical market data objects like market data prices and quotes, fundamental & reference data, historical data, company research data and so on. 
 - The __Delivery layer__ is a low abstraction layer that defines interfaces used to interact with service agnostic delivery mechanisms of the Data Platform. The __Delivery layer__ is a foundational component of the __Content layer__.
 - The __Session layer__ defines interfaces allowing your application to connect to the Data Platform via different access points (either via a direct connection, via Eikon, via the LSEG Workspace, via CodeBook or even via a local Real-Time Distribution System).

# Some examples...


## ... with the __Access layer__


### Import the LSEG Data Library

```python
import lseg.data as ld
```

### Open a data session

```python
ld.open_session()
```

### Get pricing snapshots and fundamental data

```python
    df = ld.get_data(
        universe=['IBM.N', 'VOD.L'], 
        fields=['BID', 'ASK', 'TR.Revenue']
    )
    print(df)
```

|     | Instrument | BID    | ASK   |
| --- | ---------- | ------ | ----- |
| 0   | IBM.N      | 0.00   | 0.0   |
| 1   | VOD.L      | 120.02 | 120.1 |


### Get Fundamental and pricing history

```python
    df = ld.get_history(
        universe="GOOG.O",
        fields=["BID", "ASK", "TR.Revenue"],
        interval="1Y",
        start="2015-01-01",
        end="2019-10-01",
    )
    print(df)
```

| GOOG.O     | BID     | ASK     | Revenue      |
| ---------- | ------- | ------- | ------------ |
| 2015-12-31 |  759.06 |  758.99 | 74989000000  |
| 2016-12-31 |  772.94 |  772.12 | 90272000000  |
| 2017-12-31 | 1046.46 | 1046.4  | 110855000000 |
| 2018-12-31 | 1037.36 | 1036.98 | <NA>         |
| 2019-12-31 | 1336.94 | 1335.9  | <NA>         |



### Close the session

```python
ld.close_session()
```

## ... with the __Content layer__ dedicated to advanced use cases

### Import the LSEG Data Library

```python
import lseg.data as ld
```

### Open a data session

```python
ld.open_session()
```

### Fundamental And Reference data retrieval

```python
from lseg.data.content import fundamental_and_reference

response = fundamental_and_reference.Definition(
    ["TRI.N", "IBM.N"],
    ["TR.Revenue", "TR.GrossProfit"]
).get_data()

print(response.data.df)
```

|     | instrument | date                | TR.Revenue  | TR.GrossProfit |
| --- | ---------- | ------------------- | ----------- | -------------- |
| 0   | TRI.N      | 2020-12-31T00:00:00 | 5984000000  | 5656000000     |
| 1   | IBM.N      | 2020-12-31T00:00:00 | 73620000000 | 35574000000    |


### Historical data retrieval

```python
from lseg.data.content import historical_pricing

response = historical_pricing.summaries.Definition(
    universe='VOD.L',
    interval=historical_pricing.Intervals.DAILY,
    fields=['BID', 'ASK', 'OPEN_PRC', 'HIGH_1', 'LOW_1', 'TRDPRC_1', 'NUM_MOVES', 'TRNOVR_UNS']
).get_data()

print(response.data.df)
```

|   | BID | ASK | OPEN_PRC | HIGH_1 | LOW_1 | TRDPRC_1 | NUM_MOVES | TRNOVR_UNS |
| --- | --- | --- | -------- | ------ | ----- | -------- | --------- | ---------- |
| 2019-12-12 | 144.32 | 144.34 | 144.42 | 145.66 | 143.46 | 144.18 | 12631.0 | 8498347218.71154 |
| 2019-12-11 | 143.58 | 143.6 | 142.72 | 144.8 | 142.62 | 143.58 | 10395.0 | 8815450412.65353 |
| 2019-12-10 | 142.74 | 142.78 | 143.84 | 143.84 | 141.48 | 142.74 | 10311.0 | 8070285210.45742 |
| ... | ... | ... | ... | ... | ... | ... | ... | ... |
| 2019-11-18 | 152.1 | 152.12 | 154.74 | 155.66 | 152.0 | 152.12 | 14606.0 | 19322988639.34 |
| 2019-11-15 | 154.6 | 154.62 | 160.68 | 160.68 | 154.06 | 154.6326 | 17035.0 | 31993013818.37456 |


### Real-time streaming data retrieval

```python
from lseg.data.content import pricing

pricing_stream = ld.content.pricing.Definition(
    universe=['EUR=', 'GBP=', 'JPY=', 'CAD='],
    fields=['DSPLY_NAME', 'BID', 'ASK']
).get_stream()

pricing_stream.on_refresh(lambda pricing_stream, instrument_name, fields:
                          print(f"Refresh received for {instrument_name}: {fields}"))

pricing_stream.on_update(lambda pricing_stream, instrument_name, fields:
                         print(f"Update received for {instrument_name}: {fields}"))

pricing_stream.open()
```

Output:

    Refresh received for EUR= : {'DSPLY_NAME': 'BARCLAYS     LON', 'BID': 1.1635, 'ASK': 1.1639}
    Refresh received for GBP= : {'DSPLY_NAME': 'NEDBANK LTD  JHB', 'BID': 1.3803, 'ASK': 1.3807}
    Refresh received for CAD= : {'DSPLY_NAME': 'DANSKE BANK  COP', 'BID': 1.2351, 'ASK': 1.2352}
    Refresh received for JPY= : {'DSPLY_NAME': 'ASANPACIFIBK MOW', 'BID': 113.81, 'ASK': 113.83}
    Update received for JPY= : {'DSPLY_NAME': 'NEDBANK LTD  JHB', 'BID': 113.81, 'ASK': 113.83}
    Update received for CAD= : {'DSPLY_NAME': 'DANSKE BANK  COP', 'BID': 1.2351, 'ASK': 1.2352}
    Update received for JPY= : {'DSPLY_NAME': 'ASANPACIFIBK MOW', 'BID': 113.81, 'ASK': 113.83}
    Update received for EUR= : {'DSPLY_NAME': 'BARCLAYS     LON', 'BID': 1.1635, 'ASK': 1.1639}
    Update received for CAD= : {'DSPLY_NAME': 'DANSKE BANK  COP', 'BID': 1.2351, 'ASK': 1.2352}

### Search

```python
from lseg.data.content import search

response = search.Definition("IBM").get_data()

print(response.data.df)
```

|     | RIC      | BusinessEntity | PermID      | DocumentTitle                                     | PI        |
| --- | -------- | -------------- | ----------- | ------------------------------------------------- | --------- |
| 0   | <NA>     | ORGANISATION   | <NA>        | International Business Machines Corp, Public C... | 37036     |
| 1   | IBM      | QUOTExEQUITY   | 55839165994 | International Business Machines Corp, Ordinary... | 1097326   |
| 2   | <NA>     | ORGANISATION   | <NA>        | Tiers Corporate Bond Backed Certificates Trust... | 18062670  |
| 3   | <NA>     | ORGANISATION   | <NA>        | SG Stuttgart Vaihingen BM-Campus 1 UG haftungs... | 27968389  |
| 4   | 0#IBMF:  | QUOTExEQUITY   | 21481052421 | Eurex International Business Machines Equity F... | 48924732  |
| 5   | 0#IBMDF: | QUOTExEQUITY   | 21612423771 | Euronext Amsterdam IBM Dividend Future Chain C... | 259118763 |
| 6   | IBMFc1   | QUOTExEQUITY   | 21481052892 | Eurex International Business Machines Equity F... | 49450681  |
| 7   | IBMFc2   | QUOTExEQUITY   | 21481053949 | Eurex International Business Machines Equity F... | 50092347  |
| 8   | IBMDFc1  | QUOTExEQUITY   | 21613372305 | Euronext Amsterdam IBM Single Stock Dividend F... | 260213021 |
| 9   | IBMFc3   | QUOTExEQUITY   | 21481053950 | Eurex International Business Machines Equity F... | 50092348  |


### Close the session

```python
ld.close_session()
```

# Learn more

 To learn more about the LSEG Data Library for Python simply log into the LSEG Developer Community. By 
 [registering](https://developers.refinitiv.com/iam/register) and 
 [logging in](https://developers.refinitiv.com/content/devportal/en_us/initCookie.html) to the LSEG 
 Developer Community portal you will have free access to a number of 
 learning materials such as
 [Quick Start guides](https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/quick-start),
 [Tutorials](https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/tutorials), 
 [Documentation](https://developers.lseg.com/en/api-catalog/lseg-data-platform/lseg-data-library-for-python/documentation) 
 and much more.

# Help and Support

If you have any questions regarding the API usage, please post them on 
the [Refinitiv Data Q&A Forum](https://community.developers.refinitiv.com/spaces/321/index.html). 
The LSEG Developer Community will be very pleased to help you. 

