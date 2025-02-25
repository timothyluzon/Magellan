import requests

url = "https://api.entur.io/journey-planner/v3/graphql"

headers = "headers: {'ET-Client-Name': 'timothyluzon-my_personal_timetable', 'Content-Type': 'application/json'}"

body = """
{
    stopPlace(id: "NSR:StopPlace:28504") {
        name
        id
        estimatedCalls(numberOfDepartures: 5, whiteListedModes: [bus]) {
            expectedDepartureTime
            aimedDepartureTime
            destinationDisplay {
                frontText
            }
            serviceJourney {
                line {
                    publicCode
                    transportMode
                }
            }
        }
    }
}
"""

response = requests.post(url=url, json={"query": body}) 
print("response status code: ", response.status_code) 
if response.status_code == 200: 
    print("response : ", response.json()) 