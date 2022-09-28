from re import T


country = input("What country do you live in? ")

if country.upper() == "CANADA":
    province = input("What province/state do you live in? ")
    if province.upper() in('ALBERTA', 'NUNAVUT', 'YUKON'):
        tax = 0.05
    elif province.upper() == "ONTARIO":
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print("Your Tax Rate Would Be: " + str(tax))

# Boolean True Evaluation

uk_citizen = ("UNITED KINGDOM", "UK", "ENGLAND", "WALES", "NORTHERN IRELAND", "SCOTLAND")

if country.upper() in uk_citizen:
    uk = True
else:
    uk = False

# If uk evaluates to true, execute print statement, no need to explicitly type if uk = True:
if uk:
    print("Cheerio!")