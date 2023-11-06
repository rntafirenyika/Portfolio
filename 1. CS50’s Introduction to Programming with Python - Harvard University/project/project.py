import re
from datetime import datetime
import pandas as pd
import googlemaps
from tabulate import tabulate
from fpdf import FPDF
import os



def main():
    #Global varibles
    global origin
    global fuelType


    #Google Maps Credentials
    #Set API key using Terminal with 'export API_key='
    api_key = os.environ.get("API_key")
    #Make sure ENCRYPTION_KEY is set
    if not os.environ.get("API_key"):
        raise RuntimeError("API_key not set")
    gmaps = googlemaps.Client(key=api_key)



    #Defining Locations
    depot = "-33.92713978511783, 18.531791421141854"
    origin = get_coordinates("origin")
    destination = get_coordinates("destination")
    originAddress = gmaps.reverse_geocode((f"{origin}"))[2]["formatted_address"]
    destinationAddress = gmaps.reverse_geocode((f"{destination}"))[2]["formatted_address"]

    #Calculating Distance
    num_of_trips = get_numberOfTrips()
    distance1 = (gmaps.distance_matrix(depot, origin, mode='driving')["rows"][0]["elements"][0]["distance"]["value"])/1000
    distance2 = (gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["distance"]["value"])/1000
    distance3 = (gmaps.distance_matrix(destination, depot, mode='driving')["rows"][0]["elements"][0]["distance"]["value"])/1000
    totalDistance = distance1 + (distance2 * (num_of_trips + (num_of_trips - 1))) + distance3

    #Calculating Duration
    duration1 = (gmaps.distance_matrix(depot, origin, mode='driving')["rows"][0]["elements"][0]["duration"]["value"])/3600
    duration2 = (gmaps.distance_matrix(origin, destination, mode='driving')["rows"][0]["elements"][0]["duration"]["value"])/3600
    duration3 = (gmaps.distance_matrix(destination, depot, mode='driving')["rows"][0]["elements"][0]["duration"]["value"])/3600
    totalDuration = duration1 + (duration2 * num_of_trips) + duration3

    #Fuel Consumption and Cost
    fuelConsumption = get_fuelConsumption()
    fuelPriceSite = "https://www.shell.co.za/motorists/shell-fuels/petrol-price.html"
    fuelPrice = get_fuelPrice(fuelPriceSite)
    TotalFuelCost = (totalDistance / fuelConsumption) * fuelPrice

    #table data
    table = [["Origin Address",f"{originAddress}"],
            ["Destination Address",f"{destinationAddress}"],
            ["Total Fuel Cost",f"R{TotalFuelCost:.2f}"],
            ["Fuel type",f"{fuelType.title()}"],
            ["Fuel Cost per litre",f"R{fuelPrice:.2f}/litre"],
            ["Fuel Consumption",f"{fuelConsumption} km/litre"],
            ["Total Distance Travelled",f"{totalDistance:.1f} km"],
            ["Number of Trips",f"{num_of_trips}"],
            ["Total Duration excl loading/offloading",f"{totalDuration:.2f} Hours ({totalDuration*60:.2f} minutes)"]]

    #Displaying calculations before generating pdf
    print(tabulate(table, tablefmt="grid"))

    #Generating PDF
    generate_pdf(table)


def get_numberOfTrips():
    while True:
        try:
            numTrips = int(input("Number of Trips: "))
            if numTrips > 0:
                return numTrips
            else:
                raise ValueError
        except (ValueError, TypeError):
            pass


def get_fueltype():
    while True:
        try:
            ftype = input("Petrol(P) or Diesel(D)?: ").lower()
            if ftype == "petrol" or ftype == "diesel" or ftype == "d" or ftype == "p":
                return ftype
            else:
                raise ValueError
        except ValueError:
            print("Invalid fuel type, please try again.")
            pass


def get_fuelConsumption():
    while True:
        try:
            consumption = float(input("Please enter your vehicle's fuel consumption in kms/litre: "))
            if 1 < consumption <= 33:
                return consumption
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")
            pass


def get_coordinates(od):
    while True:
        try:
            coordinates = input(f"Please enter the {od} in the format -33.9237271896802, 18.426254547674734: ")
            matches = re.search(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", coordinates)
            if matches:
                return coordinates
            else:
                raise ValueError
        except ValueError:
            print("Invalid coordinates")
            pass


def get_fuelPrice(fps):
    while True:
        global fuelType
        fuelType = get_fueltype()
        try:
            fdata = pd.read_html(f"{fps}")
            df = pd.DataFrame(fdata[1])
            #df.to_csv('my_dataframe.csv', index=False)
            if fuelType in ["diesel", "d"]:
                data = df["COASTAL FUEL PRICES (Zone 1A).3"].values[21]
                return(float(data)/100)
            elif fuelType in ["petrol", "p"]:
                data = df["COASTAL FUEL PRICES (Zone 1A)"].values[20]
                return(float(data)/100)
            else:
                pass
        except OSError:
            try:
                mfp = float(input("Error: Could not get the fuel price, please enter the fuel price you want to use: "))
                if 15 < mfp <= 30:
                    return mfp
            except ValueError:
                print("Invalid input.")
                pass


def generate_pdf(data):
    while True:
        try:
            dt = datetime.now()
            question = input("Do you want to generate the pdf cost estimate (y/n): ").lower()
            if question == "y" or question == "yes":
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Times", "B", 30)
                pdf.cell(0, 20, "Job Fuel Estimate", border=1, align="C", new_x="LEFT", new_y="NEXT")
                pdf.set_font("Times", "B", 12)
                pdf.cell(0, 40, f"Estimate {dt} ", border=0, align="R", new_x="LEFT", new_y="NEXT")
                pdf.set_font("Times", size=10)
                line_height = pdf.font_size * 2.5
                col_width = pdf.epw / 3  # distribute content evenly
                for row in data:
                    for datum in row:
                        pdf.multi_cell(col_width, line_height, datum, border=1,
                                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
                    pdf.ln(line_height)
                return pdf.output('cost_estimate.pdf')
            elif question == "n" or question == "no":
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input")
            pass





if __name__ == "__main__":
    main()