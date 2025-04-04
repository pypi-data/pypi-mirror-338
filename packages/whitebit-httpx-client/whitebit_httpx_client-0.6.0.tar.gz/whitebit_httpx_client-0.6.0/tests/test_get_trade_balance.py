from conftest import vcr_c  # noqa
from whitebit_httpx_client import WhiteBITClient  # noqa


@vcr_c.use_cassette("get_balance/trade.yaml")
def test_sync_get_trade_balance(white_bit_client: WhiteBITClient):
    response = white_bit_client.trade_balance()
    assert response["USDT"]["available"] == "10"
    assert len(response) == 386
    # total count when creating test cassette


@vcr_c.use_cassette("get_balance/trade.yaml")
async def test_async_get_trade_balance(white_bit_client: WhiteBITClient):
    response = await white_bit_client.async_trade_balance()
    assert response["USDT"]["available"] == "10"
    assert len(response) == 386
    # total count when creating test cassette
