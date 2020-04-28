has_high_income = True
has_good_credit = True
has_criminal_record = False

#If applicant has good credit AND high income then they are eligible for loan
if has_good_credit and has_high_income:
    print("Moze dostac pozyczke(condition AND)")

#If applicant has good credit OR high income then they are eligible for loan
if has_good_credit or has_high_income:
    print("Moze dostac pozyczke (condition OR)")

#If applicant has good credit and doesnt have criminal record then they are eligible for loan
if has_good_credit and not has_criminal_record:
    print("Eligible for loan(NOT condition)")
else:
    print("Applicant is not eligible for loan since he has bad credit or criminal record")