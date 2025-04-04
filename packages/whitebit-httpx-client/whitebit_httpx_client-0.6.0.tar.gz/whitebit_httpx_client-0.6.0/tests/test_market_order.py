from conftest import vcr_c  # noqa
from whitebit_httpx_client import WhiteBITClient  # noqa


@vcr_c.use_cassette("market_order/create_success_buy.yaml")
def test_sync_create_market_order(white_bit_client: WhiteBITClient):
    order_id = "0254d6ab-d427-4c75-8767-64f1ad1599fc"
    response = white_bit_client.create_market_order("TRX_USDT", "buy", "10", order_id)
    assert response["clientOrderId"] == order_id
    assert response["orderId"] == 1262126806853


@vcr_c.use_cassette("market_order/create_success_buy.yaml")
async def test_async_create_market_order(white_bit_client: WhiteBITClient):
    order_id = "0254d6ab-d427-4c75-8767-64f1ad1599fc"
    response = await white_bit_client.async_create_market_order(
        "TRX_USDT", "buy", "10", order_id
    )
    assert response["clientOrderId"] == order_id
    assert response["orderId"] == 1262126806853
