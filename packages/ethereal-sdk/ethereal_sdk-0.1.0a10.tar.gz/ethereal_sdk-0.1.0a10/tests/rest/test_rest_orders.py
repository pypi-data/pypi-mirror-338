"""Test simple REST API calls for submitting orders"""

import pytest
from typing import List
from ethereal.models.rest import OrderDto, OrderDryRunDto, CancelOrderResultDto


def test_rest_limit_order_submit_cancel(rc, sid):
    """Test submitting and cancelling a limit order."""
    subaccount = [s for s in rc.subaccounts if s.id == sid][0]

    pid = rc.products[0].id
    tick_size = float(rc.products_by_id[pid].tick_size)
    prices = rc.list_market_prices(product_ids=[pid])[0]
    best_bid_price = float(prices.best_bid_price)

    # bid 10% below the best bid price
    bid_price = best_bid_price * 0.90
    bid_price = round(bid_price / tick_size) * tick_size
    order_params = {
        "order_type": "LIMIT",
        "product_id": pid,
        "side": 0,
        "price": bid_price,
        "quantity": 0.001,
        "time_in_force": "GTD",
        "post_only": False,
    }
    order = rc.create_order(**order_params)
    rc.logger.info(f"Limit order: {order}")
    assert isinstance(order, OrderDto)

    # cancel the order
    cancelled_orders = rc.cancel_order(
        sender=rc.chain.address, subaccount=subaccount.name, order_id=order.id
    )
    rc.logger.info(f"Cancelled orders: {cancelled_orders}")
    assert isinstance(cancelled_orders, List)
    assert all(isinstance(o, CancelOrderResultDto) for o in cancelled_orders)


def test_rest_limit_order_submit_cancel_multiple(rc, sid):
    """Test submitting and cancelling multiple limit orders."""
    subaccount = [s for s in rc.subaccounts if s.id == sid][0]

    pid = rc.products[0].id
    tick_size = float(rc.products_by_id[pid].tick_size)
    prices = rc.list_market_prices(product_ids=[pid])[0]
    best_bid_price = float(prices.best_bid_price)

    # bid 10% below the best bid price
    bid_price = best_bid_price * 0.90
    bid_price = round(bid_price / tick_size) * tick_size
    order_params = {
        "order_type": "LIMIT",
        "product_id": pid,
        "side": 0,
        "price": bid_price,
        "quantity": 0.001,
        "time_in_force": "GTD",
        "post_only": False,
    }

    order_ids_to_cancel = []
    for i in range(2):
        order = rc.create_order(**order_params)
        rc.logger.info(f"Limit order: {order}")
        assert isinstance(order, OrderDto)

        # append the order ID to the list of orders to cancel
        order_ids_to_cancel.append(order.id)

    # cancel the orders
    cancelled_orders = rc.cancel_orders(
        sender=rc.chain.address,
        subaccount=subaccount.name,
        order_ids=order_ids_to_cancel,
    )
    rc.logger.info(f"Cancelled orders: {cancelled_orders}")
    assert isinstance(cancelled_orders, List)
    assert all(isinstance(o, CancelOrderResultDto) for o in cancelled_orders)


def test_rest_limit_order_dry(rc, sid):
    """Test dry running a limit order."""
    pid = rc.products[0].id
    tick_size = float(rc.products_by_id[pid].tick_size)
    prices = rc.list_market_prices(product_ids=[pid])[0]
    best_bid_price = float(prices.best_bid_price)

    # bid 10% below the best bid price
    bid_price = best_bid_price * 0.90
    bid_price = round(bid_price / tick_size) * tick_size
    order_params = {
        "order_type": "LIMIT",
        "product_id": pid,
        "side": 0,
        "price": bid_price,
        "quantity": 0.001,
        "time_in_force": "GTD",
        "post_only": False,
        "dry_run": True,
    }
    order = rc.create_order(**order_params)
    rc.logger.info(f"Limit order: {order}")
    assert isinstance(order, OrderDryRunDto)


def test_rest_market_order_dry(rc, sid):
    """Test dry running a market order."""
    pid = rc.products[0].id
    order_params = {
        "order_type": "MARKET",
        "product_id": pid,
        "side": 0,
        "quantity": 0.001,
        "dry_run": True,
    }
    order = rc.create_order(**order_params)
    rc.logger.info(f"Market order: {order}")
    assert isinstance(order, OrderDryRunDto)


def test_rest_market_order_submit(rc, sid):
    """Test submitting a market order."""
    pid = rc.products[0].id
    order_params = {
        "order_type": "MARKET",
        "product_id": pid,
        "side": 0,
        "quantity": 0.001,
    }
    order = rc.create_order(**order_params)
    rc.logger.info(f"Market order: {order}")
    assert isinstance(order, OrderDto)


def test_rest_market_order_submit_read_only(rc_ro, sid):
    """Test submitting a market order from a read-only client fails."""
    pid = rc_ro.products[0].id
    order_params = {
        "order_type": "MARKET",
        "product_id": pid,
        "side": 0,
        "quantity": 0.001,
    }

    with pytest.raises(Exception):
        rc_ro.create_order(**order_params)
