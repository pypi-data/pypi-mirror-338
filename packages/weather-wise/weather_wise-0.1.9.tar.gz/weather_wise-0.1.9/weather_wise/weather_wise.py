"""Provides weather data based on zipcode."""

from pathlib import Path
import requests
from requests.exceptions import HTTPError, Timeout, RequestException
import json
from typing import Union


class WeatherWise:
    """Obtain local weather information based on zipcode.

    Args:
        zipcode (str): The location's zipcode for weather information.
    """

    def __init__(self, zipcode: str) -> None:
        """Instantiate a Weather Class instance."""
        self.zipcode = zipcode
        self.data = self._load_json_data()
        self.latitude, self.longitude = self._get_latitude_longitude()
        self.forecast_url = self._get_weather_forecast_url()
        self.weather_details = self._get_weather_data()

    def _load_json_data(self) -> dict:
        """Load the JSON data set of zipcodes, latitudes and longitudes.

        Returns:
            dict: Data set of zipcodes, latitudes, and longitudes.
        """
        weather_wise_directory = Path(__file__).resolve().parent
        json_path = weather_wise_directory / "data" / "2024_Gaz_zcta_national.json"

        with json_path.open("r") as json_file:
            gazetteer_data = json.load(json_file)

        return gazetteer_data

    def _get_latitude_longitude(self) -> tuple:
        """Get latitude and longitude based on the zipcode provided.

        Raises:
            ValueError: If the zipcode is invalid.

        Returns:
            tuple: Latitude and longitude coordinates.
        """

        zipcode = self.data.get(self.zipcode)

        if zipcode:
            return zipcode["latitude"], zipcode["longitude"]

        raise ValueError(f"Invalid Zip Code: {self.zipcode}.  Please enter a valid 5 digit zip code.")

    def _get_weather_forecast_url(self) -> str:
        """Get National Weather Forecast Office forecast url.

        Raises:
            ConnectionError: If the API endpoint is unreachable or times out.
            ValueError: If the API response is invalid or doesn't contain the expected data.

        Returns:
            str: URL of the local weather office obtained by the latitude and longitude coordinates.
        """
        url = f"https://api.weather.gov/points/{self.latitude},{self.longitude}"

        try:
            # GET request to the API endpoint.
            weather_station_response = requests.get(url, timeout=10)
            weather_station_response.raise_for_status()

            # Parse the JSON response.
            weather_station_data = weather_station_response.json()

            # Get the forecast URL.
            forecast_url = weather_station_data["properties"]["forecastHourly"]

            return forecast_url

        except HTTPError as http_error:
            raise ConnectionError(f"HTTP Error: {http_error}")
        except Timeout as timeout_eror:
            raise ConnectionError(f"Request Timed Out: {timeout_eror}")
        except RequestException as request_error:
            raise ConnectionError(f"Request Error: {request_error}")
        except ValueError as value_error:
            raise ValueError(f"Invalid API Response: {value_error}")

    def _get_weather_data(self) -> dict:
        """Get current weather forecast data.

        Returns:
            dict: Weather related items.
        """
        weather_data_response = requests.get(self.forecast_url, timeout=10)
        weather_data = weather_data_response.json()
        current_weather = weather_data["properties"]["periods"][0]

        weather_information = {
            "short_forecast": current_weather["shortForecast"],
            "detailed_forecast": current_weather["detailedForecast"],
            "temperature": current_weather["temperature"],
            "temperature_unit": current_weather["temperatureUnit"],
            "probability_of_precipitation": current_weather["probabilityOfPrecipitation"]["value"],
            "relative_humidity": current_weather["relativeHumidity"]["value"],
            "wind_speed": current_weather["windSpeed"],
            "wind_direction": current_weather["windDirection"],
            "icon": current_weather["icon"],
        }

        return weather_information

    def get_short_forecast(self) -> str:
        """Get the current short weather forecast.

        Returns:
            str: Current short weather forecast.
        """
        short_forecast = self.weather_details["short_forecast"]

        return short_forecast

    def get_detailed_forecast(self) -> str:
        """Get the current detailed weather forecast.

        Returns:
            str: Current detailed weather forecast.
        """
        detailed_forecast = self.weather_details["detailed_forecast"]

        return detailed_forecast

    def get_temperature_in_fahrenheit(self, temperature_unit: bool = False) -> Union[int, str]:
        """Get the current temperature in fahrenheit.

        Args:
            temperature_unit (bool): Indicate whether to include the temperature unit.

        Returns:
            int: Union[int, str]: Current temperature in Fahrenheit as an integer or a string with the unit.
        """
        temperature_in_fahrenheit = self.weather_details["temperature"]
        if temperature_unit:
            return f"{temperature_in_fahrenheit}F"

        return temperature_in_fahrenheit

    def get_temperature_in_celsius(self, temperature_unit: bool = False) -> Union[float, str]:
        """Get the current temperature in celsius.

        Args:
            temperature_unit (bool): Indicate whether to include the temperature unit.

        Returns:
            Union[float, str]: Current temperature in Celsius as a float or a string with the unit.
        """
        temperature_in_celsius = (self.weather_details["temperature"] - 32) / 1.8
        if temperature_unit:
            return f"{temperature_in_celsius:.2f}C"

        return round(temperature_in_celsius, 2)

    def get_probability_of_precipitation(self, percentage_unit: bool = False) -> Union[int, str]:
        """Get the current probability of precipitation.

        Args:
            percentage_unit (bool): Indicate whether to include the percentage unit.

        Returns:
            Union[int, str]: Current probability of precipitation as an integer or a string with a percentage sign.
        """
        probability_of_precipitation = self.weather_details["probability_of_precipitation"]

        if probability_of_precipitation is None:
            probability_of_precipitation = 0

        if percentage_unit:
            return f"{probability_of_precipitation}%"

        return probability_of_precipitation

    def get_relative_humidity(self, percentage_unit: bool = False) -> Union[int, str]:
        """Get the current relative humidity.

        Args:
            percentage_unit (bool): Indicate whether to include the percentage unit.

        Returns:
            Union[int, str]: Current relative humidity as an integer or a string with a percentage sign.
        """
        relative_humidity = self.weather_details["relative_humidity"]

        if relative_humidity is None:
            return 0

        if percentage_unit:
            return f"{relative_humidity}%"

        return relative_humidity

    def get_wind_speed(self, wind_unit: bool = True) -> Union[int, str]:
        """Get the current wind speed.

        Args:
            wind_unit (bool): Indicate whether to include the wind unit.

        Returns:
            Union[int, str]: Current wind speed as an string with a percentage sign or a int.
        """
        wind_speed = self.weather_details["wind_speed"]

        if not wind_unit:
            return int(wind_speed.replace(" mph", ""))

        return wind_speed

    def get_wind_direction(self) -> str:
        """Get the current wind direction.

        Returns:
            str: Current wind direction.
        """
        wind_direction = self.weather_details["wind_direction"]

        return wind_direction

    def get_weather_icon_url(self) -> str:
        """Get the current weather icon.

        Returns:
            str: Current weather icon hyperlink.
        """
        weather_icon = self.weather_details["icon"]

        return weather_icon
