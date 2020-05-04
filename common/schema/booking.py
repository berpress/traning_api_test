from schema import Schema

booking_schema = Schema({"bookingid": int, "booking": {
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
