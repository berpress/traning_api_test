from model.booking import BookingData


class TestBooking:

    def test_get_booking(self, client):
        client.get_booking(1)

    def test_create_new_booking(self, client):
        """
        1. Add new booking
        2. Check data and status
        """
        data = BookingData().random()
        res = client.create_booking(data)
        assert res.status_code == 200
        assert res.json().get('booking') == data
