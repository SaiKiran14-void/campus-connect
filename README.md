
Campus Connect is a full stack Student Event and Clubs Management Platform.
It has two types of users — Students and Admins. The frontend is built in React and the backend is Django REST Framework with a MySQL database. Authentication is handled using JWT tokens.
Students can:
Register and login, view Events, Clubs, Workshops and Announcements, register for events and workshops, join clubs and see all their activities in a personal dashboard.
Admins can:
Login with a secret code, manage the dashboard which shows real time stats, create and delete events, clubs, workshops and announcements and see how many students registered for each one.
Tech Stack:
React for the UI, Django REST Framework for the APIs, MySQL for the database, JWT for authentication and it is deployed on Railway.
How it works:
The React app is built and served directly through Django — so one server runs everything. React sends JSON requests to Django APIs, Django validates the data using serializers, fetches or saves to MySQL through the ORM and sends back a JSON response. React then displays it.
