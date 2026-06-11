try:
    score = float(input("กรุณากรอกคะแนนของคุณ (0-100): "))
    
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
        
    print(f"คะแนนของคุณคือ {score} ได้รับเกรด: {grade}")
        
except ValueError:
    print("กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")