def classify(weight, height):
    BMI = weight / height ** 2
    classification = ''
    if(BMI < 17):
        classification = classification + 'underweight'
    elif(BMI >= 17 and BMI < 18.5):
        classification = classification + 'mild_underweight'
    elif(BMI >= 18.5 and BMI < 25.0):
        classification = classification + 'normal'
    elif(BMI >= 25.0 and BMI < 30.0):
        classification = classification + 'overweight'
    else:
        classification = classification + 'obese'
    return classification

print(classify(75, 1.75))
print(classify(78, 1.65))
print(classify(50, 1.65))
print(classify(90, 1.65))