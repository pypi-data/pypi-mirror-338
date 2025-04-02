Livescraper Python Library
==========================

The library provides convenient access to the `Livescraper API <https://livescraper.com/api-doc.html>`_ from applications written in the Python language. It allows using `Livescraper’s services <https://livescraper.com/services>`_ from your code.

API Docs
--------

Find the full documentation here:
`API Documentation <https://livescraper.com/api-doc.html>`_

Installation
------------

Python 3+ is required.

To install the package, use the following command:

.. code:: bash

   pip install livescraper

For more details, visit:
`Livescraper on PyPI <https://pypi.org/project/livescraper/>`_

Initialization
--------------

To initialize the scraper with your API key:

.. code:: python

   from livescraper import ApiClient

   scraper = ApiClient(api_key)

Create your API key here:
`Create API Key <https://app.livescraper.com/user-profile>`_

Scrape Google Maps (Places)
===========================

To search for businesses in specific locations:

.. code:: python

   # Search for businesses in specific locations
   results = scraper.google_maps_search(
       queries=["Restaurants in Alakanuk, AK, United States"],
       enrichment="True",
       fields=[
           "query", "google_place_url", "business_name", "business_website", "business_phone", 
           "type", "sub_types", "category", "full_address", "borough", "street", "city", 
           "postal_code", "state", "country", "country_code", "timezone", "latitude", "longitude", 
           "plus_code", "area_service", "review_url", "reviews_id", "total_reviews", "average_rating", 
           "reviews_per_score", "reviews_per_score_1", "reviews_per_score_2", "reviews_per_score_3", 
           "reviews_per_score_4", "reviews_per_score_5", "working_hours", "working_hours_old_format", 
           "popular_time", "about", "posts", "description", "logo_url", "photos_count", "photo_url", 
           "street_view", "price_range", "business_status", "is_verified", "owner_title", "owner_link", 
           "owner_id", "reserving_table_links", "booking_appointment_link", "order_link", "menu_link", 
           "place_id", "google_id", "place_cid", "located_in", "located_google_id", "org_link", 
           "host", "domain_status", "email_1", "email_2", "email_3", "all_emails", "phone_1", 
           "phone_2", "phone_3", "all_phones", "contact_page", "facebook", "twitter", "instagram", 
           "youtube", "linkedin", "website_built_with", "website_title", "website_desc"
       ]
   )

   # Get data of a specific place by ID
   results = scraper.google_maps_search(
       queries=["ChIJrc9T9fpYwokRdvjYRHT8nI4"],
       enrichment="True",
       fields=[
           "query", "google_place_url", "business_name", "business_website", "business_phone", 
           "type", "sub_types", "category", "full_address", "borough", "street", "city", 
           "postal_code", "state", "country", "country_code", "timezone", "latitude", "longitude", 
           "plus_code", "area_service", "review_url", "reviews_id", "total_reviews", "average_rating", 
           "reviews_per_score", "reviews_per_score_1", "reviews_per_score_2", "reviews_per_score_3", 
           "reviews_per_score_4", "reviews_per_score_5", "working_hours", "working_hours_old_format", 
           "popular_time", "about", "posts", "description", "logo_url", "photos_count", "photo_url", 
           "street_view", "price_range", "business_status", "is_verified", "owner_title", "owner_link", 
           "owner_id", "reserving_table_links", "booking_appointment_link", "order_link", "menu_link", 
           "place_id", "google_id", "place_cid", "located_in", "located_google_id", "org_link", 
           "host", "domain_status", "email_1", "email_2", "email_3", "all_emails", "phone_1", 
           "phone_2", "phone_3", "all_phones", "contact_page", "facebook", "twitter", "instagram", 
           "youtube", "linkedin", "website_built_with", "website_title", "website_desc"
       ]
   )

   # Search with many queries (batching)
   results = scraper.google_maps_search(
       queries=[
           "restaurants california usa",
           "pub brooklyn usa"
       ],
       enrichment="True",
       fields=[
           "query", "google_place_url", "business_name", "business_website", "business_phone", 
           "type", "sub_types", "category", "full_address", "borough", "street", "city", 
           "postal_code", "state", "country", "country_code", "timezone", "latitude", "longitude", 
           "plus_code", "area_service", "review_url", "reviews_id", "total_reviews", "average_rating", 
           "reviews_per_score", "reviews_per_score_1", "reviews_per_score_2", "reviews_per_score_3", 
           "reviews_per_score_4", "reviews_per_score_5", "working_hours", "working_hours_old_format", 
           "popular_time", "about", "posts", "description", "logo_url", "photos_count", "photo_url", 
           "street_view", "price_range", "business_status", "is_verified", "owner_title", "owner_link", 
           "owner_id", "reserving_table_links", "booking_appointment_link", "order_link", "menu_link", 
           "place_id", "google_id", "place_cid", "located_in", "located_google_id", "org_link", 
           "host", "domain_status", "email_1", "email_2", "email_3", "all_emails", "phone_1", 
           "phone_2", "phone_3", "all_phones", "contact_page", "facebook", "twitter", "instagram", 
           "youtube", "linkedin", "website_built_with", "website_title", "website_desc"
       ]
   )

Scrape Google Maps Reviews
==========================

To get reviews of a specific place:

.. code:: python

   # Get reviews of the specific place by ID
   results = scraper.google_review_search(
       'ChIJrc9T9fpYwokRdvjYRHT8nI4',
       fields=[
           "query", "business_name", "google_id", "place_id", "place_cid", "google_place_url",
           "review_url", "reviews_per_score", "total_reviews", "average_rating", "review_id",
           "author_link", "author_title", "author_id", "author_image", "review_text",
           "review_img_url", "review_img_urls", "owner_answer", "owner_answer_timestamp",
           "owner_answer_timestamp_datetime_utc", "review_link", "review_rating",
           "review_timestamp", "review_datetime_utc", "review_likes", "reviews_id"
       ]
   )

   # Get reviews for places found by search query
   results = scraper.google_review_search(
       'real estate agents in Los Angeles, CA',
       fields=[
           "query", "business_name", "google_id", "place_id", "place_cid", "google_place_url",
           "review_url", "reviews_per_score", "total_reviews", "average_rating", "review_id",
           "author_link", "author_title", "author_id", "author_image", "review_text",
           "review_img_url", "review_img_urls", "owner_answer", "owner_answer_timestamp",
           "owner_answer_timestamp_datetime_utc", "review_link", "review_rating",
           "review_timestamp", "review_datetime_utc", "review_likes", "reviews_id"
       ]
   )

Scrape Emails and Contacts
==========================

To get emails and contacts from a URL:

.. code:: python

   # Get emails and contacts from a specific URL
   results = scraper.google_email_search(
       queries=["livescraper.com"]
   )


Responses examples
==================

Google Maps (Places) response example:

.. code:: python

    [
        {
            "name": "The Rustic Table",
            "full_address": "45 Elm Street, Greenfield, MA 01301",
            "borough": "Downtown Greenfield",
            "street": "45 Elm Street",
            "city": "Greenfield",
            "postal_code": "01301",
            "country_code": "US",
            "country": "United States of America",
            "us_state": "Massachusetts",
            "state": "Massachusetts",
            "plus_code": null,
            "latitude": 42.587042,
            "longitude": -72.601493,
            "time_zone": "America/New_York",
            "popular_times": null,
            "site": "http://www.therustictable.com/",
            "phone": "+1 413-555-1234",
            "type": "Farm-to-table restaurant",
            "category": "restaurants",
            "subtypes": "Farm-to-table restaurant, Bistro, Organic restaurant, Vegan restaurant, Restaurant, Wine bar",
            "posts": null,
            "rating": 4.7,
            "reviews": 540,
            "reviews_data": null,
            "photos_count": 320,
            "google_id": "0x89df123456789abc:0xa1b2c3d4e5f6g7h8",
            "place_id": "ChIJ1234abcd5678efgh90ijkl",
            "reviews_link": "https://search.google.com/local/reviews?placeid=ChIJ1234abcd5678efgh90ijkl&q=restaurants+greenfield+usa&authuser=0&hl=en&gl=US",
            "reviews_id": "-1234567890123456789",
            "photo": "https://example.com/photos/restaurant.jpg",
            "street_view": "https://example.com/streetview/restaurant.jpg",
            "working_hours_old_format": "Monday: Closed | Tuesday: 5–10PM | Wednesday: 5–10PM | Thursday: 5–10PM | Friday: 5–11PM | Saturday: 12–3PM, 5–11PM | Sunday: 12–3PM, 5–9PM",
            "working_hours": {
                "Monday": "Closed",
                "Tuesday": "5–10PM",
                "Wednesday": "5–10PM",
                "Thursday": "5–10PM",
                "Friday": "5–11PM",
                "Saturday": "12–3PM, 5–11PM",
                "Sunday": "12–3PM, 5–9PM"
            },
            "business_status": "OPERATIONAL",
            "about": {
                "Service options": {
                    "Dine-in": true,
                    "Delivery": true,
                    "Takeout": true
                },
                "Health & safety": {
                    "Mask required": false,
                    "Staff required to disinfect surfaces between visits": true
                },
                "Highlights": {
                    "Farm-to-table ingredients": true,
                    "Great cocktails": true,
                    "Live music": true
                },
                "Popular for": {
                    "Lunch": true,
                    "Dinner": true,
                    "Special occasions": true
                },
                "Accessibility": {
                    "Wheelchair accessible entrance": true,
                    "Wheelchair accessible restroom": true,
                    "Wheelchair accessible seating": true
                },
                "Offerings": {
                    "Local beers": true,
                    "Seasonal dishes": true,
                    "Vegetarian options": true,
                    "Vegan options": true,
                    "Organic dishes": true,
                    "Wine": true
                },
                "Dining options": {
                    "Dessert": true,
                    "Outdoor seating": true
                },
                "Amenities": {
                    "Free parking": true,
                    "Wi-Fi": true
                },
                "Atmosphere": {
                    "Cozy": true,
                    "Casual": true,
                    "Family-friendly": true
                },
                "Crowd": {
                    "Groups": true,
                    "Couples": true
                },
                "Planning": {
                    "Dinner reservations recommended": true,
                    "Accepts reservations": true
                },
                "Payments": {
                    "Credit cards": true,
                    "Contactless payments": true
                }
            },
            "range": "$$",
            "reviews_per_score": {
                "1": 5,
                "2": 7,
                "3": 30,
                "4": 120,
                "5": 378
            },
            "reserving_table_link": "https://example.com/reserve",
            "booking_appointment_link": "https://example.com/book",
            "owner_id": "123456789012345678901",
            "verified": true,
            "owner_title": "The Rustic Table",
            "owner_link": "https://www.google.com/maps/contrib/123456789012345678901",
            "location_link": "https://www.google.com/maps/place/The+Rustic+Table/@42.587042,-72.601493,14z/data=!4m8!1m2!2m1!1sRustic+Table!3m4!1s0x89df123456789abc:0xa1b2c3d4e5f6g7h8!8m2!3d42.587042!4d-72.601493"
        }
    ]

Google Maps Reviews response example:

.. code:: python

    [
        {
            "name": "Urban Feast",
            "address": "123 Main St, Springfield, IL 62701",
            "type": "Contemporary restaurant",
            "postal_code": "62701",
            "latitude": 39.7817213,
            "longitude": -89.6501481,
            "phone": "+1 217-555-1234",
            "rating": 4.8,
            "reviews": 432,
            "site": "http://www.urbanfeast.com/",
            "photos_count": 250,
            "google_id": "0x89abcdef12345678:0xabcdef1234567890",
            "reviews_link": "https://www.google.com/search?q=Urban+Feast,+123+Main+St,+Springfield,+IL+62701&ludocid=1234567890987654321#lrd=0x89abcdef12345678:0xabcdef1234567890,1",
            "reviews_data": [
                {
                    "google_id": "0x89abcdef12345678:0xabcdef1234567890",
                    "autor_link": "https://www.google.com/maps/contrib/11234567890123456789?hl=en-US",
                    "autor_name": "Jane Doe",
                    "autor_id": "11234567890123456789",
                    "review_text": "Amazing food and great atmosphere! Highly recommend the chef's special.",
                    "review_link": "https://www.google.com/maps/reviews/data=!4m5!14m4!1m3!1m2!1s11234567890123456789!2s0x0:0xabcdef1234567890?hl=en-US",
                    "review_rating": 5,
                    "review_timestamp": 1680304800,
                    "review_datetime_utc": "03/31/2023 12:00:00",
                    "review_likes": 10
                }
            ]
        }
    ]

Emails & Contacts Scraper response example:

.. code:: python

    [
        {
            "query": "livescraper.com",
            "domain": "livescraper.com",
            "emails": [
                {
                    "value": "support@livescraper.com",
                    "sources": [
                        {
                            "ref": "https://livescraper.com/",
                            "extracted_on": "2023-01-01T10:00:00.000Z",
                            "updated_on": "2023-03-01T12:00:00.000Z"
                        }
                    ]
                }
            ],
            "phones": [
                {
                    "value": "12812368208",
                    "sources": [
                        {
                            "ref": "https://livescraper.com/",
                            "extracted_on": "2023-01-01T10:00:00.000Z",
                            "updated_on": "2023-03-01T12:00:00.000Z"
                        }
                    ]
                }
            ],
            "socials": {
                "facebook": "https://www.facebook.com/livescraper/",
                "github": "https://github.com/livescraper",
                "linkedin": "https://www.linkedin.com/company/livescraper/",
                "twitter": "https://twitter.com/livescraper",
                "youtube": "https://www.youtube.com/channel/UCDYOuXSEenLpt5tKNq-0l9Q"
            },
            "site_data": {
                "description": "Scrape Google Maps Places, Business Reviews, and more using Livescraper API.",
                "title": "Livescraper - Web Scraping Simplified"
            }
        }
    ]
