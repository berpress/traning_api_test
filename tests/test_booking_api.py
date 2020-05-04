from common.schema.booking import post_booking_schema, get_booking_schema
from common.utils import is_validate
from model.booking import BookingData


class TestBooking:

    def test_get_booking(self, client, create_booking):
        """
           1. Add new booking
           2. Get created booking by id
           3. Check data and status
           4. Validate schema
        """
        id_booking = create_booking.get('bookingid')
        res = client.get_booking(id_booking)
        assert res.json() == create_booking.get('booking')
        assert is_validate(res.json(), get_booking_schema), \
            'Check booking schema'

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
        assert is_validate(booking_info, post_booking_schema), \
            'Check booking schema'
