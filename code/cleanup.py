import pandas as pd

def make_valid_array(max_valid) :
    return [-8] + list(range(1, (max_valid + 1)))

valid_social_grades = make_valid_array(4)
valid_birth_coutry = make_valid_array(2)
valid_econ_activity = make_valid_array(9)
valid_ethnic_group = make_valid_array(5)
valid_health = make_valid_array(5)
valid_family_type = make_valid_array(5)
valid_hours_worked = make_valid_array(4)
valid_in_education = make_valid_array(2)
valid_industry = make_valid_array(9)
valid_iol = ["-8", "E13000001", "E13000002"]
valid_partner_status = make_valid_array(5)
valid_occupation = make_valid_array(9)
valid_region = ["E12000001", "E12000002", "E12000003", "E12000004", "E12000005", "E12000006", "E12000007", "E12000008", "E12000009", "W92000004", "N99999999", "S99999999"]
valid_religion = make_valid_array(9)
valid_residence = [1, 2]
valid_age = make_valid_array(7)
valid_sex = make_valid_array(2)
valid_usual_short_student = make_valid_array(3)

df = pd.read_csv("../data/publicmicrodatateachingsample.csv")

mask = -df["approx_social_grade"].isin(valid_social_grades)

print(df[mask])