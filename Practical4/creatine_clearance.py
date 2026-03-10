# get inputs
age = int(input("Please input your ages："))
weight = float(input("Please input your weight（kg）："))
gender = input("Please input your gender（male/female）：").strip().lower()
cr = float(input("Please input your creatine concentration, Cr, in（µmol/l）："))

# check error
error = False

# check age
if age >= 100:
    print("error：ages shoube be less than 100")
    error = True

# check weight
if weight <= 20 or weight >= 80:
    print("error：weight should be within 20 to 80(kg)")
    error = True

# check creatine concentration, Cr
if cr <= 0 or cr >= 100:
    print("error:creatine concentration, Cr, should be within 0 to 100(µmol/l)")
    error = True

# check gender
if gender not in ["male", "female"]:
    print("error gender should be male or female")
    error = True


if error:
    print("Please input again")
else:
    #calculation
    Crcl = (140 - age) * weight / (72 * cr)
    if gender == "female":
        Crcl *= 0.85
    print(f"（CrCl）=：{Crcl:.2f} ml/min")
