from conftest import vcr_c  # noqa
from whitebit_httpx_client import WhiteBITClient  # noqa


@vcr_c.use_cassette("move_founds/move_founds_to_spot.yaml")
def test_sync_move_founds_to_spot(white_bit_client: WhiteBITClient):
    white_bit_client.move_founds("main", "spot", "USDT", "5")


@vcr_c.use_cassette("move_founds/move_founds_to_spot.yaml")
async def test_async_move_founds_to_spot(white_bit_client: WhiteBITClient):
    await white_bit_client.async_move_founds("main", "spot", "USDT", "5")


@vcr_c.use_cassette("move_founds/move_founds_to_main.yaml")
def test_sync_move_founds_from_spot(white_bit_client: WhiteBITClient):
    white_bit_client.move_founds("spot", "main", "USDT", "5")


@vcr_c.use_cassette("move_founds/move_founds_to_main.yaml")
async def test_async_move_founds_from_spot(white_bit_client: WhiteBITClient):
    await white_bit_client.async_move_founds("spot", "main", "USDT", "5")
