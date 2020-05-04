from common.schema.booking import booking_schema
from common.utils import is_validate
from model.booking import BookingData


class TestBooking:

    def test_get_booking(self, client):
        client.get_booking(1)

    def test_create_new_booking(self, client):
        """
        1. Add new booking
        2. Check data and status
        3. Validate schema
        """
        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        booking_info = res.json()
        assert booking_info.get('booking') == data
        assert is_validate(booking_info, booking_schema), \
            'Check booking schema'
