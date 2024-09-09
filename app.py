from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Sample data for buses, seats, and offers
buses = [
    {"id": 1, "name": "Luxury Bus A", "source": "Mumbai", "destination": "Pune", "price": 500, "departure": "10:00 AM", "arrival": "4:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.5},
    {"id": 2, "name": "Standard Bus B", "source": "Mumbai", "destination": "Pune", "price": 300, "departure": "1:00 PM", "arrival": "7:00 PM", "amenities": "Charging Points, AC", "rating": 4.0},
    {"id": 3, "name": "Luxury Bus C", "source": "Delhi", "destination": "Jaipur", "price": 600, "departure": "9:00 AM", "arrival": "3:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.8},
    {"id": 4, "name": "Comfort Bus D", "source": "Delhi", "destination": "Jaipur", "price": 350, "departure": "2:00 PM", "arrival": "8:00 PM", "amenities": "Charging Points, AC", "rating": 4.2},
    {"id": 5, "name": "Luxury Bus E", "source": "Mumbai", "destination": "Bangalore", "price": 700, "departure": "8:00 AM", "arrival": "4:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.6},
    {"id": 6, "name": "Standard Bus F", "source": "Mumbai", "destination": "Bangalore", "price": 400, "departure": "12:00 PM", "arrival": "8:00 PM", "amenities": "Charging Points, AC", "rating": 4.1},
    {"id": 7, "name": "Luxury Bus G", "source": "Chennai", "destination": "Hyderabad", "price": 650, "departure": "7:00 AM", "arrival": "2:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.7},
    {"id": 8, "name": "Comfort Bus H", "source": "Chennai", "destination": "Hyderabad", "price": 380, "departure": "3:00 PM", "arrival": "10:00 PM", "amenities": "Charging Points, AC", "rating": 4.3},
    {"id": 9, "name": "Luxury Bus I", "source": "Kolkata", "destination": "Bhubaneswar", "price": 500, "departure": "6:00 AM", "arrival": "12:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.4},
    {"id": 10, "name": "Standard Bus J", "source": "Kolkata", "destination": "Bhubaneswar", "price": 300, "departure": "11:00 AM", "arrival": "5:00 PM", "amenities": "Charging Points, AC", "rating": 4.0},
    {"id": 11, "name": "Luxury Bus K", "source": "Mumbai", "destination": "Goa", "price": 800, "departure": "9:00 AM", "arrival": "5:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.8},
    {"id": 12, "name": "Standard Bus L", "source": "Mumbai", "destination": "Goa", "price": 450, "departure": "1:00 PM", "arrival": "9:00 PM", "amenities": "Charging Points, AC", "rating": 4.2},
    {"id": 13, "name": "Luxury Bus M", "source": "Delhi", "destination": "Amritsar", "price": 550, "departure": "10:00 AM", "arrival": "6:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.7},
    {"id": 14, "name": "Comfort Bus N", "source": "Delhi", "destination": "Amritsar", "price": 320, "departure": "4:00 PM", "arrival": "10:00 PM", "amenities": "Charging Points, AC", "rating": 4.3},
    {"id": 15, "name": "Luxury Bus O", "source": "Bangalore", "destination": "Coimbatore", "price": 700, "departure": "8:00 AM", "arrival": "3:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.5},
    {"id": 16, "name": "Standard Bus P", "source": "Bangalore", "destination": "Coimbatore", "price": 400, "departure": "1:00 PM", "arrival": "8:00 PM", "amenities": "Charging Points, AC", "rating": 4.1},
    {"id": 17, "name": "Luxury Bus Q", "source": "Hyderabad", "destination": "Chennai", "price": 650, "departure": "7:00 AM", "arrival": "2:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.7},
    {"id": 18, "name": "Comfort Bus R", "source": "Hyderabad", "destination": "Chennai", "price": 380, "departure": "3:00 PM", "arrival": "10:00 PM", "amenities": "Charging Points, AC", "rating": 4.3},
    {"id": 19, "name": "Luxury Bus S", "source": "Pune", "destination": "Ahmedabad", "price": 600, "departure": "8:00 AM", "arrival": "3:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.6},
    {"id": 20, "name": "Standard Bus T", "source": "Pune", "destination": "Ahmedabad", "price": 350, "departure": "1:00 PM", "arrival": "8:00 PM", "amenities": "Charging Points, AC", "rating": 4.2},
    {"id": 21, "name": "Luxury Bus U", "source": "Jaipur", "destination": "Agra", "price": 500, "departure": "6:00 AM", "arrival": "12:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.4},
    {"id": 22, "name": "Comfort Bus V", "source": "Jaipur", "destination": "Agra", "price": 300, "departure": "11:00 AM", "arrival": "5:00 PM", "amenities": "Charging Points, AC", "rating": 4.0},
    {"id": 23, "name": "Luxury Bus W", "source": "Delhi", "destination": "Chandigarh", "price": 550, "departure": "10:00 AM", "arrival": "4:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.7},
    {"id": 24, "name": "Comfort Bus X", "source": "Delhi", "destination": "Chandigarh", "price": 320, "departure": "4:00 PM", "arrival": "8:00 PM", "amenities": "Charging Points, AC", "rating": 4.3},
    {"id": 25, "name": "Luxury Bus Y", "source": "Kolkata", "destination": "Patna", "price": 550, "departure": "9:00 AM", "arrival": "3:00 PM", "amenities": "Wi-Fi, Reclining Seats, Snacks", "rating": 4.5},
    {"id": 26, "name": "Standard Bus Z", "source": "Kolkata", "destination": "Patna", "price": 300, "departure": "1:00 PM", "arrival": "7:00 PM", "amenities": "Charging Points, AC", "rating": 4.1}
]


offers = [
    {"code": "SUMMER10", "description": "10% off on summer bookings"},
    {"code": "FESTIVE20", "description": "20% off on festive season bookings"},
]

selected_bus = None
selected_seats = []
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = "vsrikanthoffl@gmail.com"
app.config['MAIL_PASSWORD'] = "ownh pfnj keea ekza"
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/confirm-booking', methods=['POST'])
def confirm_booking():
    to_email = request.form.get('email')  # Get recipient's email address from form data
    bus = selected_bus  # Assuming selected_bus is defined in your app
    seats = selected_seats  # Assuming selected_seats is defined in your app

    msg = Message("Booking Confirmation",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=[to_email])
    msg.body = f"""
    Dear Customer,

    Your booking has been confirmed!

    Bus: {bus['name']}
    Seats: {', '.join(seats)}

    Thank you for booking with us!

    Best regards,
    Your Bus Booking Team
    """
    try:
        mail.send(msg)
        return render_template('confirmation.html', bus=bus, seats=seats)
    except Exception as e:
        return str(e)  # Handle exceptions and errors appropriately

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST'])
def search_buses():
    source = request.form.get('source')
    destination = request.form.get('destination')
    date = request.form.get('date')

    available_buses = [bus for bus in buses if bus['source'].lower() == source.lower() and bus['destination'].lower() == destination.lower()]
    return render_template('select_bus.html', buses=available_buses)

@app.route('/select-bus/<int:bus_id>')
def select_bus(bus_id):
    global selected_bus
    selected_bus = next((bus for bus in buses if bus['id'] == bus_id), None)
    if not selected_bus:
        return redirect(url_for('home'))
    return render_template('seat_selection.html', bus=selected_bus)

@app.route('/select-seats', methods=['POST'])
def select_seats():
    global selected_seats
    selected_seats = request.form.getlist('seats')
    seat_names = {key: value for key, value in request.form.items() if key.startswith('seat_names')}
    return render_template('payment.html', bus=selected_bus, seats=selected_seats, offers=offers, seat_names=seat_names)

@app.route('/apply-offer', methods=['POST'])
def apply_offer():
    data = request.get_json()
    offer_code = data.get('offer_code')
    applied_offer = next((offer for offer in offers if offer['code'].upper() == offer_code.upper()), None)
    return jsonify({"offer": applied_offer})

if __name__ == '__main__':
    app.run(debug=True)