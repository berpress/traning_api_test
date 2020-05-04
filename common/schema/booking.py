from schema import Schema

post_booking_schema = Schema({"bookingid": int, "booking": {
    "firstname": str,
    "lastname": str,
    "totalprice": int,
    "depositpaid": bool,
    "bookingdates": {
        "checkin": str,
        "checkout": str,
    },
    "additionalneeds": str
}})


get_booking_schema = Schema({
    "firstname": str,
    "lastname": str,
    "totalprice": int,
    "depositpaid": bool,
    "bookingdates": {
        "checkin": str,
        "checkout": str,
    },
    "additionalneeds": str
})
