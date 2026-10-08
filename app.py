import streamlit as st
from datetime import date, timedelta
import random
import string

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CINEMAX - Movie Ticket Booking",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #080b16 0%, #10162b 45%, #080b16 100%);
    color: white;
}

.main-title {
    font-size: 52px;
    font-weight: 900;
    text-align: center;
    margin-bottom: 5px;
    background: linear-gradient(90deg, #ff4b4b, #ffb347, #ff4b4b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #b9bfd0;
    font-size: 18px;
    margin-bottom: 30px;
}

.hero-box {
    padding: 35px;
    border-radius: 24px;
    background: linear-gradient(135deg, #171d35, #101426);
    border: 1px solid #303752;
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
    margin-bottom: 25px;
}

.movie-card {
    background: #151a2d;
    border: 1px solid #303752;
    border-radius: 18px;
    padding: 14px;
    margin-bottom: 20px;
    height: 100%;
    transition: 0.3s;
}

.movie-card:hover {
    border-color: #ff4b4b;
    transform: translateY(-3px);
}

.movie-title {
    font-size: 21px;
    font-weight: 800;
    margin-top: 10px;
}

.movie-info {
    color: #aeb5c8;
    font-size: 14px;
    margin-top: 5px;
}

.rating {
    color: #ffd166;
    font-weight: bold;
}

.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 20px;
    background: #ff4b4b;
    color: white;
    font-size: 12px;
    font-weight: bold;
}

.section-title {
    font-size: 30px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 18px;
}

.summary-box {
    background: #151a2d;
    border: 1px solid #303752;
    border-radius: 18px;
    padding: 22px;
}

.ticket {
    background: linear-gradient(135deg, #191f38, #101426);
    border: 2px dashed #ff4b4b;
    border-radius: 22px;
    padding: 28px;
    margin-top: 20px;
}

.ticket-title {
    font-size: 30px;
    font-weight: 900;
    color: #ff6262;
}

.big-price {
    font-size: 34px;
    font-weight: 900;
    color: #ffd166;
}

.small-muted {
    color: #9fa6ba;
}

div[data-testid="stButton"] button {
    border-radius: 10px;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# MOVIE DATA
# ============================================================

movies = [
    {
        "title": "Neon Pursuit",
        "genre": "Action",
        "language": "English",
        "rating": 4.8,
        "duration": "2h 18m",
        "price": 180,
        "badge": "🔥 TRENDING",
        "description": "A high-speed action thriller through a futuristic city.",
        "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=900"
    },
    {
        "title": "Starlight Horizon",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 4.7,
        "duration": "2h 25m",
        "price": 220,
        "badge": "⭐ TOP RATED",
        "description": "A breathtaking journey beyond the limits of space.",
        "image": "https://images.unsplash.com/photo-1446776877081-d282a0f896e2?w=900"
    },
    {
        "title": "Crimson Signal",
        "genre": "Thriller",
        "language": "English",
        "rating": 4.6,
        "duration": "2h 05m",
        "price": 190,
        "badge": "🔥 HOT",
        "description": "A detective races against time to uncover a secret.",
        "image": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=900"
    },
    {
        "title": "Laughing Avenue",
        "genre": "Comedy",
        "language": "English",
        "rating": 4.4,
        "duration": "1h 55m",
        "price": 150,
        "badge": "😂 COMEDY HIT",
        "description": "A hilarious journey filled with unexpected adventures.",
        "image": "https://images.unsplash.com/photo-1585647347384-2593bc35786b?w=900"
    },
    {
        "title": "The Hidden Valley",
        "genre": "Adventure",
        "language": "English",
        "rating": 4.5,
        "duration": "2h 12m",
        "price": 170,
        "badge": "🌄 ADVENTURE",
        "description": "A group of explorers discover a mysterious hidden world.",
        "image": "https://images.unsplash.com/photo-1500534623283-312aade485b7?w=900"
    },
    {
        "title": "Pixel Pals",
        "genre": "Animation",
        "language": "English",
        "rating": 4.9,
        "duration": "1h 42m",
        "price": 140,
        "badge": "👨‍👩‍👧 FAMILY",
        "description": "A colorful animated adventure for the whole family.",
        "image": "https://images.unsplash.com/photo-1535016120720-40c646be5580?w=900"
    },
    {
        "title": "Letters at Dawn",
        "genre": "Drama",
        "language": "English",
        "rating": 4.3,
        "duration": "2h 01m",
        "price": 160,
        "badge": "💫 EMOTIONAL",
        "description": "An emotional story about dreams, friendship and hope.",
        "image": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=900"
    },
    {
        "title": "Echoes of Midnight",
        "genre": "Mystery",
        "language": "English",
        "rating": 4.6,
        "duration": "2h 08m",
        "price": 190,
        "badge": "🕵️ MYSTERY",
        "description": "A mysterious case takes a shocking turn after midnight.",
        "image": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=900"
    },
    {
        "title": "Quantum Run",
        "genre": "Sci-Fi",
        "language": "English",
        "rating": 4.8,
        "duration": "2h 20m",
        "price": 230,
        "badge": "🚀 BLOCKBUSTER",
        "description": "A thrilling race through time and alternate realities.",
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=900"
    },
    {
        "title": "Family Express",
        "genre": "Family",
        "language": "English",
        "rating": 4.2,
        "duration": "1h 50m",
        "price": 130,
        "badge": "❤️ FAMILY",
        "description": "A cheerful family trip becomes an unforgettable adventure.",
        "image": "https://images.unsplash.com/photo-1511895426328-dc8714191300?w=900"
    },
    {
        "title": "Ocean Beyond",
        "genre": "Adventure",
        "language": "English",
        "rating": 4.5,
        "duration": "2h 15m",
        "price": 175,
        "badge": "🌊 NEW",
        "description": "A deep-sea adventure reveals something extraordinary.",
        "image": "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=900"
    },
    {
        "title": "The Last Lantern",
        "genre": "Drama",
        "language": "English",
        "rating": 4.7,
        "duration": "2h 10m",
        "price": 165,
        "badge": "🏆 AWARD WINNER",
        "description": "A powerful story of courage, family and new beginnings.",
        "image": "https://images.unsplash.com/photo-1519608487953-e999c86e7455?w=900"
    }
]

# ============================================================
# SESSION STATE
# ============================================================

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

if "selected_seats" not in st.session_state:
    st.session_state.selected_seats = []

if "booking_complete" not in st.session_state:
    st.session_state.booking_complete = False

if "booking_id" not in st.session_state:
    st.session_state.booking_id = None

if "booked_seats" not in st.session_state:
    st.session_state.booked_seats = {}

# ============================================================
# FUNCTIONS
# ============================================================

def generate_booking_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=6))
    return f"CMX-{letters}-{numbers}"


def get_booked_seats(movie, show_date, screen, show_time):
    key = f"{movie}-{show_date}-{screen}-{show_time}"

    if key not in st.session_state.booked_seats:
        rng = random.Random(sum(ord(c) for c in key))

        all_seats = [
            f"{row}{number}"
            for row in ["A", "B", "C", "D", "E", "F"]
            for number in range(1, 9)
        ]

        st.session_state.booked_seats[key] = set(
            rng.sample(all_seats, 8)
        )

    return st.session_state.booked_seats[key]


def reset_booking():
    st.session_state.selected_movie = None
    st.session_state.selected_seats = []
    st.session_state.booking_complete = False
    st.session_state.booking_id = None


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🎬 CINEMAX")

    st.caption("Your premium movie booking experience")

    st.divider()

    menu = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🎟️ Book Tickets",
            "❤️ Favorites"
        ]
    )

    st.divider()

    st.markdown("### 🎯 Quick Stats")
    st.metric("Movies", len(movies))
    st.metric("Screens", "6")
    st.metric("Show Times", "18+")

    st.divider()

    st.info(
        "💡 Demo project\n\n"
        "Bookings are stored only during the current Streamlit session."
    )

# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🎬 CINEMAX</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your perfect movie experience in just a few clicks.</div>',
    unsafe_allow_html=True
)

# ============================================================
# HOME
# ============================================================

if menu == "🏠 Home":

    st.markdown("""
    <div class="hero-box">
        <h1>🍿 Lights. Camera. Your Seat.</h1>
        <p style="color:#b9bfd0;font-size:18px;">
        Discover the latest movies, choose your favourite seats,
        and book your cinema experience instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("🎬 Movies", "12+")

    with col2:
        st.metric("💺 Seats", "48 / Screen")

    with col3:
        st.metric("⭐ Ratings", "4.5+")

    with col4:
        st.metric("🎟️ Booking", "Instant")

    st.markdown(
        '<div class="section-title">🔥 Now Showing</div>',
        unsafe_allow_html=True
    )

    search = st.text_input(
        "🔎 Search movies",
        placeholder="Search by movie name or genre..."
    )

    col1, col2 = st.columns(2)

    with col1:
        genres = ["All"] + sorted(list(set(movie["genre"] for movie in movies)))

        selected_genre = st.selectbox(
            "🎭 Genre",
            genres
        )

    with col2:
        sort_option = st.selectbox(
            "↕️ Sort By",
            [
                "Recommended",
                "Rating: High to Low",
                "Price: Low to High",
                "Price: High to Low"
            ]
        )

    filtered_movies = movies.copy()

    if search:
        filtered_movies = [
            movie for movie in filtered_movies
            if search.lower() in movie["title"].lower()
            or search.lower() in movie["genre"].lower()
        ]

    if selected_genre != "All":
        filtered_movies = [
            movie for movie in filtered_movies
            if movie["genre"] == selected_genre
        ]

    if sort_option == "Rating: High to Low":
        filtered_movies.sort(
            key=lambda x: x["rating"],
            reverse=True
        )

    elif sort_option == "Price: Low to High":
        filtered_movies.sort(
            key=lambda x: x["price"]
        )

    elif sort_option == "Price: High to Low":
        filtered_movies.sort(
            key=lambda x: x["price"],
            reverse=True
        )

    if not filtered_movies:
        st.warning("😕 No movies found.")
    else:

        for start in range(0, len(filtered_movies), 3):

            cols = st.columns(3)

            for index, movie in enumerate(
                filtered_movies[start:start + 3]
            ):

                with cols[index]:

                    st.image(
                        movie["image"],
                        use_container_width=True
                    )

                    st.markdown(
                        f"**{movie['title']}**"
                    )

                    st.caption(
                        f"🎭 {movie['genre']}  •  "
                        f"🕐 {movie['duration']}  •  "
                        f"🌐 {movie['language']}"
                    )

                    st.markdown(
                        f"⭐ **{movie['rating']} / 5**   "
                        f"•   ₹{movie['price']} onwards"
                    )

                    st.markdown(
                        f"🔥 **{movie['badge']}**"
                    )

                    fav_text = (
                        "💔 Remove Favorite"
                        if movie["title"] in st.session_state.favorites
                        else "❤️ Add Favorite"
                    )

                    fcol1, fcol2 = st.columns(2)

                    with fcol1:
                        if st.button(
                            fav_text,
                            key=f"fav_{movie['title']}"
                        ):

                            if movie["title"] in st.session_state.favorites:
                                st.session_state.favorites.remove(
                                    movie["title"]
                                )
                            else:
                                st.session_state.favorites.append(
                                    movie["title"]
                                )

                            st.rerun()

                    with fcol2:
                        if st.button(
                            "🎟️ Book Now",
                            key=f"book_{movie['title']}"
                        ):
                            st.session_state.selected_movie = movie["title"]
                            st.session_state.selected_seats = []
                            st.session_state.booking_complete = False
                            st.rerun()

                    with st.expander("ℹ️ Movie Details"):
                        st.write(movie["description"])

# ============================================================
# FAVORITES
# ============================================================

elif menu == "❤️ Favorites":

    st.markdown(
        '<div class="section-title">❤️ My Favorite Movies</div>',
        unsafe_allow_html=True
    )

    favorite_movies = [
        movie for movie in movies
        if movie["title"] in st.session_state.favorites
    ]

    if not favorite_movies:
        st.info(
            "You haven't added any movies to your favorites yet."
        )

    else:

        for movie in favorite_movies:

            col1, col2, col3 = st.columns([1, 2, 1])

            with col1:
                st.image(
                    movie["image"],
                    use_container_width=True
                )

            with col2:
                st.markdown(
                    f"### 🎬 {movie['title']}"
                )

                st.write(
                    f"🎭 {movie['genre']}  |  "
                    f"⭐ {movie['rating']}  |  "
                    f"🕐 {movie['duration']}"
                )

                st.write(movie["description"])

            with col3:

                if st.button(
                    "🎟️ Book",
                    key=f"favorite_book_{movie['title']}"
                ):
                    st.session_state.selected_movie = movie["title"]
                    st.session_state.selected_seats = []
                    st.rerun()

                if st.button(
                    "💔 Remove",
                    key=f"favorite_remove_{movie['title']}"
                ):
                    st.session_state.favorites.remove(
                        movie["title"]
                    )
                    st.rerun()

            st.divider()

# ============================================================
# BOOKING PAGE
# ============================================================

elif menu == "🎟️ Book Tickets":

    st.markdown(
        '<div class="section-title">🎟️ Book Your Movie Tickets</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # MOVIE SELECTION
    # --------------------------------------------------------

    movie_names = [movie["title"] for movie in movies]

    default_index = 0

    if st.session_state.selected_movie in movie_names:
        default_index = movie_names.index(
            st.session_state.selected_movie
        )

    selected_movie_name = st.selectbox(
        "🎬 Select Movie",
        movie_names,
        index=default_index
    )

    st.session_state.selected_movie = selected_movie_name

    movie = next(
        movie for movie in movies
        if movie["title"] == selected_movie_name
    )

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            movie["image"],
            use_container_width=True
        )

    with col2:

        st.markdown(
            f"## 🎬 {movie['title']}"
        )

        st.markdown(
            f"⭐ **{movie['rating']} / 5**"
        )

        st.write(
            f"🎭 {movie['genre']}  •  "
            f"🕐 {movie['duration']}  •  "
            f"🌐 {movie['language']}"
        )

        st.write(movie["description"])

        st.success(
            f"Starting from ₹{movie['price']}"
        )

    st.divider()

    # --------------------------------------------------------
    # SHOW DETAILS
    # --------------------------------------------------------

    st.markdown("### 📅 Show Details")

    col1, col2, col3 = st.columns(3)

    available_dates = [
        date.today() + timedelta(days=i)
        for i in range(7)
    ]

    with col1:

        show_date = st.date_input(
            "📅 Select Date",
            min_value=date.today(),
            max_value=date.today() + timedelta(days=6),
            value=date.today()
        )

    with col2:

        screen = st.selectbox(
            "🏢 Select Screen",
            [
                "Screen 1 - IMAX",
                "Screen 2 - PVR",
                "Screen 3 - Dolby Atmos",
                "Screen 4 - 4DX",
                "Screen 5 - Premium",
                "Screen 6 - Family"
            ]
        )

    with col3:

        show_time = st.selectbox(
            "🕐 Show Time",
            [
                "10:00 AM",
                "12:30 PM",
                "03:30 PM",
                "06:30 PM",
                "09:30 PM"
            ]
        )

    # --------------------------------------------------------
    # TICKET CATEGORY
    # --------------------------------------------------------

    st.markdown("### 🎟️ Ticket Category")

    col1, col2, col3 = st.columns(3)

    with col1:
        regular_price = movie["price"]

        regular = st.button(
            f"🟢 Regular\n₹{regular_price}",
            use_container_width=True
        )

    with col2:
        premium_price = movie["price"] + 70

        premium = st.button(
            f"🔵 Premium\n₹{premium_price}",
            use_container_width=True
        )

    with col3:
        recliner_price = movie["price"] + 170

        recliner = st.button(
            f"🟣 Recliner\n₹{recliner_price}",
            use_container_width=True
        )

    if "ticket_category" not in st.session_state:
        st.session_state.ticket_category = "Regular"

    if regular:
        st.session_state.ticket_category = "Regular"
        st.session_state.selected_seats = []

    if premium:
        st.session_state.ticket_category = "Premium"
        st.session_state.selected_seats = []

    if recliner:
        st.session_state.ticket_category = "Recliner"
        st.session_state.selected_seats = []

    category = st.session_state.ticket_category

    if category == "Regular":
        ticket_price = regular_price
        allowed_rows = ["A", "B", "C"]

    elif category == "Premium":
        ticket_price = premium_price
        allowed_rows = ["D", "E"]

    else:
        ticket_price = recliner_price
        allowed_rows = ["F"]

    st.info(
        f"🎟️ Selected Category: **{category}**  |  "
        f"💰 ₹{ticket_price} per ticket"
    )

    # --------------------------------------------------------
    # TICKET COUNTS
    # --------------------------------------------------------

    st.markdown("### 👥 Passenger Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        adults = st.number_input(
            "👨 Adult",
            min_value=0,
            max_value=8,
            value=1
        )

    with col2:
        students = st.number_input(
            "🎓 Student",
            min_value=0,
            max_value=8,
            value=0
        )

    with col3:
        children = st.number_input(
            "🧒 Child",
            min_value=0,
            max_value=8,
            value=0
        )

    total_tickets = adults + students + children

    st.write(
        f"🎫 **Total Tickets Required: {total_tickets}**"
    )

    # --------------------------------------------------------
    # SEAT MAP
    # --------------------------------------------------------

    st.markdown("### 💺 Choose Your Seats")

    st.caption(
        "🟩 Available   |   🔵 Selected   |   🟥 Booked"
    )

    booked = get_booked_seats(
        selected_movie_name,
        show_date,
        screen,
        show_time
    )

    rows = ["A", "B", "C", "D", "E", "F"]

    for row in rows:

        st.markdown(f"**Row {row}**")

        seat_cols = st.columns(8)

        for number in range(1, 9):

            seat = f"{row}{number}"

            with seat_cols[number - 1]:

                is_booked = seat in booked
                is_selected = seat in st.session_state.selected_seats
                allowed = row in allowed_rows

                if is_booked:

                    st.button(
                        f"🟥 {seat}",
                        disabled=True,
                        key=f"seat_{seat}_booked_{show_date}_{show_time}_{screen}"
                    )

                elif not allowed:

                    st.button(
                        f"⬜ {seat}",
                        disabled=True,
                        key=f"seat_{seat}_disabled_{show_date}_{show_time}_{screen}"
                    )

                else:

                    if is_selected:
                        label = f"🔵 {seat}"
                    else:
                        label = f"🟩 {seat}"

                    if st.button(
                        label,
                        key=f"seat_{seat}_{show_date}_{show_time}_{screen}"
                    ):

                        if seat in st.session_state.selected_seats:
                            st.session_state.selected_seats.remove(seat)

                        else:

                            if len(st.session_state.selected_seats) < total_tickets:
                                st.session_state.selected_seats.append(seat)

                            else:
                                st.warning(
                                    "You have already selected enough seats."
                                )

                        st.rerun()

        st.write("")

    selected_seats = st.session_state.selected_seats

    st.info(
        f"💺 Selected Seats: "
        f"{', '.join(selected_seats) if selected_seats else 'None'}"
    )

    if total_tickets > 0 and len(selected_seats) < total_tickets:
        st.warning(
            f"Please select {total_tickets - len(selected_seats)} more seat(s)."
        )

    # --------------------------------------------------------
    # CUSTOMER DETAILS
    # --------------------------------------------------------

    st.markdown("### 👤 Customer Details")

    col1, col2 = st.columns(2)

    with col1:

        customer_name = st.text_input(
            "Full Name",
            placeholder="Enter your name"
        )

        customer_email = st.text_input(
            "Email",
            placeholder="example@email.com"
        )

    with col2:

        customer_phone = st.text_input(
            "Mobile Number",
            placeholder="Enter mobile number"
        )

        payment_method = st.selectbox(
            "💳 Payment Method",
            [
                "UPI",
                "Credit / Debit Card",
                "Cash at Counter"
            ]
        )

    # --------------------------------------------------------
    # COUPON
    # --------------------------------------------------------

    st.markdown("### 🎁 Apply Coupon")

    coupon = st.text_input(
        "Coupon Code",
        placeholder="Try MOVIE10, CINEMA50 or WEEKEND20"
    ).upper().strip()

    discount = 0

    base_ticket_total = (
        adults * ticket_price
        + students * ticket_price * 0.85
        + children * ticket_price * 0.75
    )

    if coupon == "MOVIE10":
        discount = base_ticket_total * 0.10
        st.success("🎉 MOVIE10 applied — 10% discount!")

    elif coupon == "CINEMA50":
        discount = min(50, base_ticket_total)
        st.success("🎉 CINEMA50 applied — ₹50 discount!")

    elif coupon == "WEEKEND20":
        discount = base_ticket_total * 0.20
        st.success("🎉 WEEKEND20 applied — 20% discount!")

    elif coupon:
        st.error("❌ Invalid coupon code.")

    # --------------------------------------------------------
    # BILL CALCULATION
    # --------------------------------------------------------

    discounted_total = base_ticket_total - discount

    convenience_fee = total_tickets * 30

    taxable_amount = discounted_total + convenience_fee

    gst = taxable_amount * 0.18

    grand_total = taxable_amount + gst

    # --------------------------------------------------------
    # BOOKING SUMMARY
    # --------------------------------------------------------

    st.markdown("### 🧾 Booking Summary")

    col1, col2 = st.columns([1.4, 1])

    with col1:

        st.markdown(
            '<div class="summary-box">',
            unsafe_allow_html=True
        )

        st.markdown(f"### 🎬 {movie['title']}")

        st.write(f"📅 Date: **{show_date.strftime('%d %B %Y')}**")
        st.write(f"🕐 Time: **{show_time}**")
        st.write(f"🏢 Screen: **{screen}**")
        st.write(f"🎟️ Category: **{category}**")

        st.write(
            f"💺 Seats: **{', '.join(selected_seats) if selected_seats else 'Not selected'}**"
        )

        st.markdown("---")

        st.write(
            f"🎫 Adult Tickets: ₹{adults * ticket_price:,.2f}"
        )

        st.write(
            f"🎓 Student Tickets: ₹{students * ticket_price * 0.85:,.2f}"
        )

        st.write(
            f"🧒 Child Tickets: ₹{children * ticket_price * 0.75:,.2f}"
        )

        st.write(
            f"🎁 Discount: -₹{discount:,.2f}"
        )

        st.write(
            f"🧾 Convenience Fee: ₹{convenience_fee:,.2f}"
        )

        st.write(
            f"GST (18%): ₹{gst:,.2f}"
        )

        st.markdown("---")

        st.markdown(
            f'<div class="big-price">₹{grand_total:,.2f}</div>',
            unsafe_allow_html=True
        )

        st.caption("Final payable amount")

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    with col2:

        st.markdown("### 🔐 Secure Booking")

        st.success("✓ Seat availability checked")
        st.success("✓ Instant confirmation")
        st.success("✓ Digital ticket")
        st.success("✓ Booking ID generated")

        st.info(
            "Your booking details will appear here after confirmation."
        )

    # --------------------------------------------------------
    # CONFIRM BOOKING
    # --------------------------------------------------------

    st.markdown("")

    can_book = (
        total_tickets > 0
        and len(selected_seats) == total_tickets
        and customer_name.strip() != ""
        and customer_email.strip() != ""
        and customer_phone.strip() != ""
    )

    if st.button(
        "🎟️ CONFIRM & PAY",
        type="primary",
        use_container_width=True,
        disabled=not can_book
    ):

        st.session_state.booking_id = generate_booking_id()

        st.session_state.booking_complete = True

        # Mark seats as booked for current session
        booking_key = f"{selected_movie_name}-{show_date}-{screen}-{show_time}"

        if booking_key not in st.session_state.booked_seats:
            st.session_state.booked_seats[booking_key] = set()

        st.session_state.booked_seats[booking_key].update(
            selected_seats
        )

        st.rerun()

    if not can_book:
        st.caption(
            "Complete customer details and select the required number of seats to continue."
        )

    # --------------------------------------------------------
    # DIGITAL TICKET
    # --------------------------------------------------------

    if st.session_state.booking_complete:

        st.markdown("---")

        st.markdown(
            '<div class="ticket">',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="ticket-title">🎉 BOOKING CONFIRMED!</div>',
            unsafe_allow_html=True
        )

        st.success(
            "Your movie tickets have been booked successfully."
        )

        tcol1, tcol2 = st.columns(2)

        with tcol1:

            st.markdown("### 🎬 Movie")
            st.write(movie["title"])

            st.markdown("### 📅 Date")
            st.write(show_date.strftime("%d %B %Y"))

            st.markdown("### 🕐 Show")
            st.write(show_time)

            st.markdown("### 🏢 Screen")
            st.write(screen)

        with tcol2:

            st.markdown("### 💺 Seats")
            st.write(", ".join(selected_seats))

            st.markdown("### 🎟️ Category")
            st.write(category)

            st.markdown("### 💳 Payment")
            st.write(payment_method)

            st.markdown("### 🆔 Booking ID")
            st.code(st.session_state.booking_id)

        st.divider()

        st.markdown(
            f'<div class="big-price">₹{grand_total:,.2f}</div>',
            unsafe_allow_html=True
        )

        st.caption(
            f"Booked for {customer_name} • {customer_email}"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

        # Downloadable ticket
        ticket_text = f"""
========================================
             CINEMAX
        DIGITAL MOVIE TICKET
========================================

Booking ID : {st.session_state.booking_id}

Movie      : {movie['title']}
Genre      : {movie['genre']}
Date       : {show_date.strftime('%d %B %Y')}
Time       : {show_time}
Screen     : {screen}

Category   : {category}
Seats      : {', '.join(selected_seats)}

Customer   : {customer_name}
Email      : {customer_email}
Mobile     : {customer_phone}

----------------------------------------
Adult      : {adults}
Student    : {students}
Child      : {children}

Ticket     : ₹{base_ticket_total:,.2f}
Discount   : -₹{discount:,.2f}
Convenience: ₹{convenience_fee:,.2f}
GST        : ₹{gst:,.2f}

TOTAL      : ₹{grand_total:,.2f}

Payment    : {payment_method}

========================================
       THANK YOU FOR CHOOSING CINEMAX
========================================
"""

        st.download_button(
            "📥 Download Digital Ticket",
            ticket_text,
            file_name=f"{st.session_state.booking_id}.txt",
            mime="text/plain",
            use_container_width=True
        )

        if st.button(
            "🔄 Make Another Booking",
            use_container_width=True
        ):
            reset_booking()
            st.rerun()

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center;color:#777f95;padding:20px;">
        🎬 <b>CINEMAX</b> • Movie Ticket Booking System<br>
        <small>Built with Python + Streamlit</small>
    </div>
    """,
    unsafe_allow_html=True
)