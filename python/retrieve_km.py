from weconnect import weconnect
#from weconnect import Vehicle

# Vervang dit door jouw eigen e-mail en wachtwoord van MijnVolkswagen
username = 'jouw-email@example.com'
password = 'jouw-wachtwoord'

# Login en initialiseer verbinding
connection = weconnect.WeConnect(
    username,
    password,
    updateAfterLogin=True,
    loginOnInit=True
)

# Doorloop voertuigen in jouw account
for vin, vehicle in connection.vehicles.items():
    print(f"Voertuig: {vehicle.title}")
    try:
        odometer = vehicle.domains['VehicleStatus']['odometerStatus'].odometer
        print(f"Kilometerstand: {odometer.value} {odometer.unit}")
    except KeyError:
        print("Kilometerstand niet beschikbaar")
