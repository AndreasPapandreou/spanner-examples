TESTBOARD_ID = "200023001347343438323536"
testboard = Testboard(TESTBOARD_ID)

# Our device's 1st Analog Output Pin will be connected to the Testboard's A0, making it our Input Pin 1
INPUT_PIN_1 = "A0"
# Our device's 2nd Analog Output Pin will be connected to the Testboard's A4, making it our Input Pin 2
INPUT_PIN_2 = "A4"

def validate_analog_input_greater():
    # Check PIN state
    # analogRead will give us a value between 0 to 4095, corresponding to a 0-3V3 range.
    value = testboard.analogRead(INPUT_PIN_1)

    # Let's say we want to to make sure the voltage is greater than 1.5V. Given the mapping of 0-3.3V to a value of 0-4096, that means the value we have should be higher than aproximately 1861. For the sake of simplicity and because of possible fluctuations in the values, we'll test with 1800, which is aprox. 1.45V.
    # NOTICE: We could also have used analogReadVoltage() as we do in the next example.
    spanner.assertGreaterThan(1800, value);
    # See also assertGreatherThanOrEqual(), or assertEquals()

def validate_analog_input_less():
    # Check PIN state
    # In this example, we use analogReadVoltage() which gives us a Voltage value directly, without having to care about the ADC converter. However, keep in mind that this value could be slightly less accurate, and given that it's a float it's not the best fit for checking Equality. Still, it's good enough for most purposes.
    value = testboard.analogReadVoltage(INPUT_PIN_2)

    spanner.assertLessThan(2.0, value);
    # See also assertLessThanOrEqual()

if __name__ == "__main__":

    validate_analog_input_greater()

    time.sleep(2)

    validate_analog_input_less()
