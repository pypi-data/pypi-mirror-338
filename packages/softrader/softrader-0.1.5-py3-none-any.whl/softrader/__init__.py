from typing import Literal as Lit
import MetaTrader5      as mt5
import alpaca.trading   as ap_trading
import ib_insync        as IBkr


nan = float('nan')
inf = float('inf')


# ========================================================================= #
# ================================ Connect ================================ #
# ========================================================================= #
def connect(PLATAFORM:Lit['METATRADER','ALPACA','IBROKER'], ID=None, SECRET=None, PROVIDER=None):
    if (PLATAFORM == 'METATRADER'):
        mt5.initialize()
        mt5.login(ID, SECRET, PROVIDER)
        return mt5

    if (PLATAFORM == 'ALPACA'):
        ap_client= ap_trading.TradingClient(ID, SECRET)
        return ap_client

    if (PLATAFORM == 'IBROKER'):
        IBkr.util.startLoop()
        ib_client = IBkr.IB()
        ib_client.connect(port=PROVIDER)
        return ib_client
    

def infer_platform(client):
    if           (client is mt5):                     return 'METATRADER'
    if isinstance(client, ap_trading.TradingClient):  return 'ALPACA'
    if isinstance(client, IBkr.IB):                   return 'IBROKER'



# ====================================================================== #
# ================================ Open ================================ #
# ====================================================================== #
def send_open(client, symbol:str, quant:float, limit=nan, tp=nan, sl=nan, 
    tif:Lit['GTC','DAY','IOC','FOK','OPG','DTC','GTD','GTT','ATR']='GTC'
):

    has_limit = (0 < limit < inf)
    has_tp    = (0 < tp    < inf)
    has_sl    = (0 < sl    < inf)


    if (not has_limit):  BOOK = 'MARKET'
    if (    has_limit):  BOOK = 'LIMIT'

    if (quant > 0):  SIDE = 'BUY'
    if (quant < 0):  SIDE = 'SELL'

    if           (client is mt5):                     PLATFORM = 'METATRADER'
    if isinstance(client, ap_trading.TradingClient):  PLATFORM = 'ALPACA'
    if isinstance(client, IBkr.IB):                   PLATFORM = 'IBROKER'


    # ==================================================== #
    # ==================== MetaTrader ==================== #
    # ==================================================== #
    if (PLATFORM == 'METATRADER'):
        req = {}

        if (BOOK == 'MARKET'):  req.update({ 'action':mt5.TRADE_ACTION_DEAL    }) 
        if (BOOK == 'LIMIT'):   req.update({ 'action':mt5.TRADE_ACTION_PENDING }) 

        if [BOOK,SIDE] == ['MARKET','BUY' ]:  req.update({ 'type':mt5.ORDER_TYPE_BUY        }) 
        if [BOOK,SIDE] == ['MARKET','SELL']:  req.update({ 'type':mt5.ORDER_TYPE_SELL       }) 
        if [BOOK,SIDE] == ['LIMIT', 'BUY' ]:  req.update({ 'type':mt5.ORDER_TYPE_BUY_LIMIT  }) 
        if [BOOK,SIDE] == ['LIMIT', 'SELL']:  req.update({ 'type':mt5.ORDER_TYPE_SELL_LIMIT }) 
        
        req.update({ 'symbol':symbol     })
        req.update({ 'volume':abs(quant) })

        if (has_limit):  req.update({ 'price':limit }) 
        if (has_tp):     req.update({ 'tp':tp       }) 
        if (has_sl):     req.update({ 'sl':sl       }) 
        
        if (tif == 'GTC'):  req.update({ 'type_time':mt5.ORDER_TIME_GTC }) 
        if (tif == 'DAY'):  req.update({ 'type_time':mt5.ORDER_TIME_DAY }) 

        return client.send_order(req)


    # ======================================================== #
    # ======================== Alpaca ======================== #
    # ======================================================== #
    if (PLATFORM == 'ALPACA'):
        req = {}

        if (BOOK == 'MARKET'):  req.update({ 'action':ap_trading.OrderType.MARKET }) 
        if (BOOK == 'LIMIT'):   req.update({ 'action':ap_trading.OrderType.LIMIT  }) 

        if (SIDE == 'BUY'):     req.update({ 'type':ap_trading.OrderSide.BUY  }) 
        if (SIDE == 'SELL'):    req.update({ 'type':ap_trading.OrderSide.SELL }) 
        
        req.update({ 'symbol':symbol  })
        req.update({ 'qty':abs(quant) })

        if (has_limit):  req.update({ 'limit_price':limit })
        if (has_tp):     req.update({ 'take_profit':tp    })
        if (has_sl):     req.update({ 'stop_loss':sl      })
        
        if (tif == 'GTC'):  req.update({ 'time_in_force':ap_trading.TimeInForce.GTC }) 
        if (tif == 'DAY'):  req.update({ 'time_in_force':ap_trading.TimeInForce.DAY }) 
        if (tif == 'IOC'):  req.update({ 'time_in_force':ap_trading.TimeInForce.IOC }) 
        if (tif == 'FOK'):  req.update({ 'time_in_force':ap_trading.TimeInForce.FOK }) 
        if (tif == 'OPG'):  req.update({ 'time_in_force':ap_trading.TimeInForce.OPG }) 
        if (tif == 'CLS'):  req.update({ 'time_in_force':ap_trading.TimeInForce.CLS }) 

        return client.submit_order(ap_trading.OrderRequest(**req))


    # ========================================================== #
    # ======================== IBRokers ======================== #
    # ========================================================== #
    if (PLATFORM == 'IBROKER'):

        order = IBkr.Order()
        con   = IBkr.Contract()


        if (BOOK == 'MARKET'):  order.orderType = 'MKT'
        if (BOOK == 'LIMIT'):   order.orderType = 'LMT'

        if (SIDE == 'BUY'):     order.action = 'BUY'
        if (SIDE == 'SELL'):    order.action = 'SELL'
        
        con.symbol          = symbol
        order.totalQuantity = abs(quant)

        if (has_limit):  order.lmtPrice = limit
        if (has_tp):     pass
        if (has_sl):     pass
        
        if (tif == 'GTC'):  order.tif = 'GTC'
        if (tif == 'DAY'):  order.tif = 'DAY'
        if (tif == 'IOC'):  order.tif = 'IOC'
        if (tif == 'FOK'):  order.tif = 'FOK'
        if (tif == 'OPG'):  order.tif = 'OPG'
        if (tif == 'DTC'):  order.tif = 'DTC'
        if (tif == 'GTD'):  order.tif = 'GTD'
        if (tif == 'GTT'):  order.tif = 'GTT'
        if (tif == 'ATR'):  order.tif = 'ATR'

        for CON in ['STK','FUND','BOND','CASH','FUT','OPT','CRYPTO','BAG','CMDTY','IND','CFD','FOP','WAR','NEWS','EVENT']: 
            con.secType = CON
            if client.qualifyContracts(con):
                return client.placeOrder(con, order)


# ======================================================================= #
# ================================ Close ================================ #
# ======================================================================= #
def ib_set_qualified_exchange(ib_client:IBkr.IB, con:IBkr.Contract, EXCHANGES=['SMART','PAXOS']):

    if not con.exchange: 
        for X in EXCHANGES: 
            con.exchange = X
            if ib_client.qualifyContracts(con): 
                return con
            
    return con


def close_all_market_positions(client:IBkr.IB, cancel_orders=True, on_error:Lit['append','pass','raise']='append'):

    # ================ Helpers ================ #
    def _handler(pipe, Lambda, on_error):
        try: 
            pipe.append(Lambda())
        except Exception as E:
            if on_error == 'append':    pipe.append(E)
            if on_error == 'pass':      pass
            if on_error == 'raise':     raise E


    # ================ Main ================ #
    PLATFORM = infer_platform(client)


    # ================ MetaTrader ================ #
    if (PLATFORM == 'METATRADER'):
        
        orders     = mt5.orders_get()
        positions  = mt5.positions_get()
        res_cancel = []
        res_close  = []

        for P in positions: 

            if cancel_orders:
                for O in orders: 
                    if (O.symbol == P.symbol):
                        _handler(res_cancel, lambda:mt5.order_send({ 'action':mt5.TRADE_ACTION_REMOVE, 'order':O.ticket }), on_error)

            req = {
                'action':       mt5.TRADE_ACTION_DEAL, 
                'position':     P.ticket,
                'symbol':       P.symbol,
                'volume':       P.volume,
                'type_time':    mt5.ORDER_TIME_GTC,
                'type_filling': mt5.ORDER_FILLING_IOC,
            }

            if (P.type == mt5.POSITION_TYPE_BUY):   req.append({ 'type':mt5.ORDER_TYPE_SELL })
            if (P.type == mt5.POSITION_TYPE_SELL):  req.append({ 'type':mt5.ORDER_TYPE_BUY  })

            _handler(res_close, lambda:mt5.order_send(req), on_error) 

        return res_close, res_cancel


    # ================ Alpaca ================ #
    if (PLATFORM == 'ALPACA'):
        return client.close_all_positions(cancel_orders)


    # ================ IBroker ================ #
    if (PLATFORM == 'IBROKER'):
        
        trades     = client.openTrades()
        positions  = client.positions()
        res_cancel = []
        res_close  = []

        for P in positions:

            con   = ib_set_qualified_exchange(client, P.contract)
            order = IBkr.Order()

            if cancel_orders: 
                for T in trades: 
                    if (T.contract.symbol == P.contract.symbol):
                        _handler(res_cancel, lambda:client.cancelOrder(T.order), on_error)

            if (P.position > 0):  order.action = 'SELL'
            if (P.position < 0):  order.action = 'BUY'
            
            _handler(res_close, lambda:client.placeOrder(con, order), on_error)

        return res_close, res_cancel