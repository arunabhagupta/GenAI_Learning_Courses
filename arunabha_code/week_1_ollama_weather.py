import ollama
import traceback

def get_weather_forecast(system_prompt, location):
    try:
        res = ollama.chat(
            model="llama3.2:1b",
            messages=[system_prompt,
                      {"role":"user",
                       "content":f"Please provide the weather forecast for {location}"}
                    ],
            options={
                "temperature": 0,
                "seed": 70,
            }
        )
        # print (res)
        # return res["message"]["content"]
        return res.message.content
    except Exception as e:
        print(f"Error in get_weather_forecast method: {e} \r\n {traceback.format_exc()}")


def stored_weather_information(location):
    try:
        weather_info = [{"status": "success", "report": "It is quite sunny today with a high of 25 degrees Celsius in New York City."},
                        {"status": "success", "report": "It is raining today with a high of 18 degrees Celsius in London."},
                        {"status": "success", "report": "It is snowing today with a high of -5 degrees Celsius in Moscow."},
                        {"status": "success", "report": "It is cloudy today with a high of 22 degrees Celsius in San Francisco."},
                        {"status": "success", "report": "It is windy today with a high of 30 degrees Celsius in Dubai."}]
        
        if location:
            location = location.lower().replace(" ", "")
            for city in weather_info:
                if location in city["report"].lower().replace(" ",""):
                    return city["report"]
                else:
                    return False

    except Exception as e:
        print(f"Error in stored_weather_information method: {e} \r\n {traceback.format_exc()}")


def weather_handler(location):
    try:
        res_stored_weather = stored_weather_information(location)
        if res_stored_weather:
            return res_stored_weather
        else:
            system_prompt={"role": "system", "content": "You are a helpful assistant that provides weather forecasts. Keep it very consise and to the point. Do not provide any additional information or explanations. Just provide today's weather forecast for the requested location."}
            res_weather_forecast = get_weather_forecast(system_prompt, location)
            return res_weather_forecast

    except Exception as e:
        print(f"Error in weather_handler method: {e} \r\n {traceback.format_exc()}")


if __name__ == "__main__":
    location = "Bangalore"
    weather_report = weather_handler(location)
    print(f"Weather report for {location}: {weather_report}")