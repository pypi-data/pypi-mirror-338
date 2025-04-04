# About

⭐ Portal:     https://bit.ly/finance_analytics  
📊 Blog:       https://slashpage.com/jh-analytics  

📈 Softrader:  https://pypi.org/project/softrader

🐍 Python:     https://github.com/jhvissotto/Project_Finance_Api_Python  
🐍 Pypi:       https://pypi.org/project/jh-finance-api  

🟦 TScript:    https://github.com/jhvissotto/Project_Finance_Api_TScript  
🟦 NPM:        https://www.npmjs.com/package/finance-analytics-api  

🔌 Server:     https://bit.ly/jh_finance_api  
🔌 Swagger:    https://bit.ly/jh_finance_api_swagger  



# Library

```py
!pip install softrader
```

```py
from softrader import nan
import softrader as st
```


# Connect

```py
client_ib  = st.connect('IBROKER',    ID=None,   SECRET=None,       PROVIDER=4002)
client_ap  = st.connect('ALPACA',     ID='abcd', SECRET='xxyyzzww')
client_mt5 = st.connect('METATRADER', ID=123456, SECRET='password', PROVIDER='brokername')
```


# Open Position
Send order to any broker with no more configurations

```py
try: 
    res = st.send_open(client_ib, symbol='MSFT', quant=10, limit=nan, tp=nan, sl=nan, tif='GTC')
    print(res)

except Exception as err:
    print(err)
```