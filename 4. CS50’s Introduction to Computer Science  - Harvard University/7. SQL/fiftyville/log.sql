-- Keep a log of any SQL queries you execute as you solve the mystery.

/*Selecting and reading initial crime scene report*/
SELECT description FROM crime_scene_reports
WHERE street = 'Humphrey Street'
AND year = 2021
AND month = 7
AND day = 28
AND description LIKE ('%CS50%');

/*Reading reports from the 3 people interviewed*/
SELECT * FROM interviews
WHERE transcript LIKE ('%bakery%')
AND year = 2021
AND month = 7
AND day = 28;

/*Checking vehicles that left within the timeframe specified by one of the interviewees*/
SELECT * FROM bakery_security_logs
WHERE year = 2021
AND month = 7
AND day = 28
AND hour = 10
AND minute BETWEEN 15 AND 20;

/*Checking ATM transactions at Leggett Street before the theft*/
SELECT account_number FROM atm_transactions
WHERE atm_location = 'Leggett Street'
AND transaction_type = 'withdraw'
AND year = 2021
AND month = 7
AND day = 28;

/*Checking phone records just after the theft with duration of less than a minute*/
SELECT * FROM phone_calls
WHERE duration < 60
AND year = 2021
AND month = 7
AND day = 28;

/*Getting owners details of vehicles that left the bakery around the specified time*/
SELECT name, phone_number, passport_number FROM people
JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
WHERE people.license_plate IN (SELECT license_plate FROM bakery_security_logs
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND hour = 10
    AND minute BETWEEN 15 AND 20)
GROUP BY name;

/*Getting personal details of people that transacted at Leggett Street ATM*/
SELECT name, phone_number, passport_number FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE person_id IN (
    SELECT person_id FROM bank_accounts
    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
    WHERE bank_accounts.account_number IN (
        SELECT account_number FROM atm_transactions
        WHERE atm_location = 'Leggett Street'
        AND transaction_type = 'withdraw'
        AND year = 2021
        AND month = 7
        AND day = 28))
GROUP BY name;

/*Getting personal details of people that called for less than a minute on the day of theft*/
SELECT name, passport_number FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE caller IN (SELECT caller FROM phone_calls
    WHERE duration < 60
    AND year = 2021
    AND month = 7
    AND day = 28
    GROUP BY caller)
GROUP BY name;

/*Identifying the thief/person who used the ATM on Leggett Street, whose vehicle left the bakkery and called for less than a minute on the day of theft*/
SELECT name, passport_number FROM people
WHERE passport_number IN (SELECT passport_number FROM people
    JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
    WHERE people.license_plate IN (SELECT license_plate FROM bakery_security_logs
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND hour = 10
        AND minute BETWEEN 15 AND 20)
    GROUP BY passport_number)
AND passport_number IN (SELECT passport_number FROM people
    JOIN bank_accounts ON bank_accounts.person_id = people.id
    WHERE person_id IN (
        SELECT person_id FROM bank_accounts
        JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
        WHERE bank_accounts.account_number IN (
            SELECT account_number FROM atm_transactions
            WHERE atm_location = 'Leggett Street'
            AND transaction_type = 'withdraw'
            AND year = 2021
            AND month = 7
            AND day = 28))
    GROUP BY passport_number)
AND passport_number IN (SELECT passport_number FROM people
    JOIN phone_calls ON phone_calls.caller = people.phone_number
    WHERE caller IN (SELECT caller FROM phone_calls
        WHERE duration < 60
        AND year = 2021
        AND month = 7
        AND day = 28
        GROUP BY caller)
    GROUP BY passport_number);

/*Identifying the city the thief escaped to*/
SELECT city FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
WHERE flights.id IN (SELECT id FROM flights
    JOIN passengers ON passengers.flight_id = flights.id
    WHERE flight_id IN (SELECT flight_id FROM passengers
        JOIN people ON passengers.passport_number = people.passport_number
        WHERE people.passport_number IN (SELECT passport_number FROM people
            WHERE passport_number IN (SELECT passport_number FROM people
                JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
                WHERE people.license_plate IN (SELECT license_plate FROM bakery_security_logs
                    WHERE year = 2021
                    AND month = 7
                    AND day = 28
                    AND hour = 10
                    AND minute BETWEEN 15 AND 20)
                GROUP BY passport_number)
            AND passport_number IN (SELECT passport_number FROM people
                JOIN bank_accounts ON bank_accounts.person_id = people.id
                WHERE person_id IN (
                    SELECT person_id FROM bank_accounts
                    JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
                    WHERE bank_accounts.account_number IN (
                        SELECT account_number FROM atm_transactions
                        WHERE atm_location = 'Leggett Street'
                        AND transaction_type = 'withdraw'
                        AND year = 2021
                        AND month = 7
                        AND day = 28))
                GROUP BY passport_number)
            AND passport_number IN (SELECT passport_number FROM people
                JOIN phone_calls ON phone_calls.caller = people.phone_number
                WHERE caller IN (SELECT caller FROM phone_calls
                    WHERE duration < 60
                    AND year = 2021
                    AND month = 7
                    AND day = 28
                    GROUP BY caller)
                GROUP BY passport_number))));

/*Identifying the accomplice by the phone call that the thief made*/
SELECT name, passport_number FROM people
JOIN phone_calls ON phone_calls.receiver = people.phone_number
WHERE receiver IN (SELECT receiver FROM phone_calls
    WHERE duration < 60
    AND year = 2021
    AND month = 7
    AND day = 28
    AND caller IN (SELECT phone_number FROM people
        WHERE passport_number IN (SELECT passport_number FROM people
            JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
            WHERE people.license_plate IN (SELECT license_plate FROM bakery_security_logs
                WHERE year = 2021
                AND month = 7
                AND day = 28
                AND hour = 10
                AND minute BETWEEN 15 AND 20)
            GROUP BY passport_number)
        AND passport_number IN (SELECT passport_number FROM people
            JOIN bank_accounts ON bank_accounts.person_id = people.id
            WHERE person_id IN (
                SELECT person_id FROM bank_accounts
                JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
                WHERE bank_accounts.account_number IN (
                    SELECT account_number FROM atm_transactions
                    WHERE atm_location = 'Leggett Street'
                    AND transaction_type = 'withdraw'
                    AND year = 2021
                    AND month = 7
                    AND day = 28))
            GROUP BY passport_number)
        AND passport_number IN (SELECT passport_number FROM people
            JOIN phone_calls ON phone_calls.caller = people.phone_number
            WHERE caller IN (SELECT caller FROM phone_calls
                WHERE duration < 60
                AND year = 2021
                AND month = 7
                AND day = 28
                GROUP BY caller)
            GROUP BY passport_number))
    GROUP BY receiver)
GROUP BY name;