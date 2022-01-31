def BMI(weight, height):
    """ calculates the BMI where 
        weight is in kg and height in metres"""
    return weight / height**2


def bmi_evaluate(bmi_value):
    if bmi_value < 15:
        result = "Very severely underweight"
    elif bmi_value < 16:
        result = "Severely underweight"
    elif bmi_value < 18.5:
        result = "Underweight"
    elif bmi_value < 25:
        result = "Normal (healthy weight)"
    elif bmi_value < 30:
        result = "Overweight"
    elif bmi_value < 35:
        result = "Obese Class I (Moderately obese)"
    elif bmi_value < 40:
        result = "Obese Class II (Severely obese)"
    else:
        result = "Obese Class III (Very severely obese)"
    return result
