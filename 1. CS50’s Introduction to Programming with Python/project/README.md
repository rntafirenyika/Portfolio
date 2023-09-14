# FUEL COST CALCULATOR FOR A REMOVALS BUSINESS
#### **Video Demo:**  <https://youtu.be/jzBL4FH5JQk>
#### **Description:** Calculator for getting total fuel cost for a vehicle on a job.
<br />
This project is a fuel cost calculator for a business that does removal services for its clients. The model is based on a business that dispatches its vehicles from a depot, collects goods from the origin and delivers to the destination. Depending on the quantity of goods to be transported, more than just a single trip may be necessary to complete a single job. At the core of this project are google maps APIs which requires an API key which can be obtained from the [Google Cloud console.](https://console.cloud.google.com/apis/credentials)
<br />
<br />

#### **Google Maps APIs**
The following google maps APIs are used in this project:

    Distance Matrix API - Used to calculate distance travelled and duration.
    Geocoding API - Reverse geocoding is used in this project to convert the geographic coordinates into a human-readable address.
<br />
<br />

#### **USING THE PROGRAM**
#### **Step 1**
Obtaining user input for the origin, destination, and the number trips for the job. The project requires the input of the locations in the form of coordinates which are easily obtainable from google maps by right clicking on a location. Coordinates ensures great accuracy and eliminate errors that may be encountered when dealing with addresses like addresses with similar street names but different suburbs. These inputs are used to calculate the driving distance and time travelled starting from the depot to the origin, then from the origin to the destination and lastly from the destination back to the depot. If more than one trip is required, then the extra distance is factored in. If the inputs are invalid, the program will re-prompt until a valid input is entered.

#### **Step 2**
Obtaining user input for the fuel type used by the vehicle and the average fuel consumption of the vehicle. In South Africa, the fuel price depends on whether the town is located along/near the coastal line or not and for this project, the coastal prices are used since the depot is in Cape Town. The program can however be easily modified to use inland prices when required. The fuel type input is required to get the fuel prices from the Shell Website and if the program for whatever reason cannot obtain the price from the website, it will prompt the user to input a fuel price manually. If the manually entered fuel price is too low or too high, the program will prompt the user again. From here the total fuel cost can then be calculated using the fuel price, total distance travelled and the average fuel consumption of the vehicle.If the inputs are invalid, the program will re-prompt until a valid input is entered.

#### **Final step**
The inputs and calculations above are then displayed to the user in the form of a table. After displaying the results, the program prompts the user if they want to generate a pdf version of the results and if the user is happy with the results, the pdf version is then generated and the program exits. If the user does not want the pdf then the program will exit without generating one.
<br />
<br />

#### **Documentation & resources**
- [Shell South Africa](https://www.shell.co.za/motorists/shell-fuels/petrol-price.html)
- [Distance Matrix API](https://developers.google.com/maps/documentation/distancematrix)
- [Geocoding API](https://developers.google.com/maps/documentation/geocoding)
