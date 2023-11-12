# WeatherStation class which stores observations about the weather.
class WeatherStation:
    # Constructor which takes the name of the station as its argument.
    def __init__(self, name: str):
        if name == "":
            raise ValueError("Station cannot be an empty string.")
        self.__name = name
        self.__observations = []

    # Returns the total number of observations added.        
    def number_of_observations(self):
        return len(self.__observations)

    # Returns the name of the station and the total number of observations added.
    def __str__(self):
        num_obs = self.number_of_observations()
        if num_obs == 0:
            return ""
        return f"{self.__name}, {num_obs} observations"

    # Adds an observation as the last entry in a list.        
    def add_observation(self, observation: str):
        if observation == "":
            raise ValueError("Observation cannot be an empty string")
        self.__observations.append(observation)

    # Returns the latest observation added to the list.        
    def latest_observation(self):
         if self.number_of_observations() == 0:
             return ""
         return self.__observations[-1]