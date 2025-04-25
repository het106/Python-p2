social_grade_labels = {
    -8.0: "Does not apply",
     1.0: "AB Higher and intermediate managerial/administrative/professional occupations",
	 2.0: "C1 Supervisory, clerical and junior managerial/administrative/professional occupations",
	 3.0: "C2 Skilled manual occupations",
	 4.0: "DE Semi-skilled and unskilled manual occupations; unemployed and lowest grade" 
} 

country_of_birth_labels = {
    -8.0: "Does not apply",
     1.0: "United Kingdom",
     2.0: "Other countries"
}

economic_activity_labels = {
    -8.0: "Does not apply",
	 1.0: "Economically active (excluding full-time students): In employment: Employee",
	 2.0: "Economically active (excluding full-time students): In employment: Self-employed",
	 3.0: "Economically active (excluding full-time students): Unemployed: Seeking work or waiting to start a job already obtained",
	 4.0: "Economically active and a full-time student",
	 5.0: "Economically inactive: Retired",
	 6.0: "Economically inactive: Student",
	 7.0: "Economically inactive: Looking after home or family",
	 8.0: "Economically inactive: Long-term sick or disabled",
	 9.0: "Economically inactive: Other"
}

ethinic_groups_labels = {
    -8.0: "Does not apply",
     1.0: "Asian, Asian British or Asian Welsh",
	 2.0: "Black, Black British, Black Welsh, Caribbean or African",
	 3.0: "Mixed or Multiple ethnic groups",
	 4.0: "White",
	 5.0: "Other ethnic group",
}

health_labels = {
    -8.0: "Does not apply",
     1.0: "Very good health",
     2.0: "Good health",
     3.0: "Fair health",
     4.0: "Bad health",
     5.0: "Very bad health"
}

family_labels = {
    -8.0: "Does not apply",
	 1.0: "One-person household",
	 2.0: "Married or civil partnership couple household",
	 3.0: "Cohabiting couple household",
	 4.0: "Lone parent household",
	 5.0: "Multi-person household",
}

hours_labels = {
    -8.0: "Does not apply",
    1.0: "15 hours or less",
    2.0: "16 to 30",
    3.0: "31 to 48",
    4.0: "49 or more"
}

education_labels = {
    -8.0: "Does not apply",
     1.0: "Student",
     2.0: "Not a student",
}

industry_labels = {
    -8.0: "Does not apply",
    1.0: "A Agriculture, forestry and fishing",
	2.0: "C Manufacturing",
	3.0: "B, D, E Energy and water",
	4.0: "F Construction",
	5.0: "G, I Distribution, hotels and restaurants",
	6.0: "H, J Transport and communication",
	7.0: "K, L, M, N Financial, real estate, professional and administrative activities",
	8.0: "O, P, Q Public administration, education and health",
	9.0: "R, S, T, U Other"
}

london_labels = {
    -8.0: "Does not apply",
    "E13000001": "Inner London",
    "E13000002": "Outer London"
}

partner_labels = {
    -8.0: "Does not apply",
     1.0: "Never married and never registered a civil partnership",
     2.0: "Married or in a registered civil partnership",
     3.0: "Separated, but still legally married or still legally in a civil partnership",
     4.0: "Divorced or civil partnership dissolved",
     5.0: "Widowed or surviving civil partnership partner"
}

occupation_labels = {
    -8.0: "Does not apply",
	 1.0: "Managers, directors and senior officials",
	 2.0: "Professional occupations",
	 3.0: "Associate professional and technical occupations",
	 4.0: "Administrative and secretarial occupations",
	 5.0: "Skilled trades occupations",
	 6.0: "Caring, leisure and other service occupations",
	 7.0: "Sales and customer service occupations",
	 8.0: "Process, plant and machine operatives",
	 9.0: "Elementary occupations"
}

region_labels = {
    "E12000001":  "North East",
	"E12000002":  "North West",
	"E12000003":  "Yorkshire and The Humber",
	"E12000004":  "East Midlands",
	"E12000005":  "West Midlands",
	"E12000006":  "East of England",
	"E12000007":  "London",
	"E12000008":  "South East",
	"E12000009":  "South West",
	"W92000004":  "Wales",
	"N99999999":  "Does not apply: Northern Ireland",
	"S99999999":  "Does not apply: Scotland"
}

religion_labels = {
    -8.0: "Does not apply",
	 1.0: "No religion",
	 2.0: "Christian",
	 3.0: "Buddhist",
	 4.0: "Hindu",
	 5.0: "Jewish",
	 6.0: "Muslim",
	 7.0: "Sikh",
	 8.0: "Other religion",
	 9.0: "Not answered"
}

residence_labels = {
    1.0: "Lives in a household",
    2.0: "Lives in a communal establishment"
}

age_labels = {
    -8.0: "Does not apply",
     1.0: "Aged 15 years and under",
     2.0: "Aged 16 to 24 years",
     3.0: "Aged 25 to 34 years",
     4.0: "Aged 35 to 44 years",
     5.0: "Aged 45 to 54 years",
     6.0: "Aged 55 to 64 years",
     7.0: "Aged 65 years and over"
}

sex_labels = {
    -8.0: "Does not apply",
     1.0: "Female",
     2.0: "Male"
}

usual_student_labels = {
    -8.0: "Does not apply",
     1.0: "Is a usual resident",
     2.0: "Is a student living at an alternative address in term time",
     3.0: "Is a non-UK-born short-term resident, staying 3 to 12 months"
}

occupation_order = ["Does not apply", "Managers, directors and senior officials", "Professional occupations", "Associate professional and technical occupations", "Administrative and secretarial occupations", "Skilled trades occupations", "Caring, leisure and other service occupations", "Sales and customer service occupations", "Process, plant and machine operatives", "Elementary occupations"]
social_grade_order = ["Does not apply", "AB Higher and intermediate managerial/administrative/professional occupations", "C1 Supervisory, clerical and junior managerial/administrative/professional occupations", "C2 Skilled manual occupations", "DE Semi-skilled and unskilled manual occupations; unemployed and lowest grade" ]
country_of_birth_order = ["Does not apply", "United Kingdom", "Other countries"]
economic_activity_order = ["Does not apply", "Economically active (excluding full-time students): In employment: Employee", "Economically active (excluding full-time students): In employment: Self-employed", "Economically active (excluding full-time students): Unemployed: Seeking work or waiting to start a job already obtained", "Economically active and a full-time student", "Economically inactive: Retired", "Economically inactive: Student", "Economically inactive: Looking after home or family", "Economically inactive: Long-term sick or disabled", "Economically inactive: Other"]
ethinic_groups_order = ["Does not apply", "Asian, Asian British or Asian Welsh", "Black, Black British, Black Welsh, Caribbean or African", "Mixed or"]
sex_order = ["Does not apply", "Female", "Male"]
health_order = ["Does not apply", "Very good health", "Good health", "Fair health", "Bad health", "Very bad health"]
family_order = ["Does not apply", "One-person household", "Married or civil partnership couple household", "Cohabiting couple household", "Lone parent household", "Multi-person household"]
hours_order = ["Does not apply", "15 hours or less", "16 to 30", "31 to 48", "49 or more"]
education_order = ["Does not apply", "Student", "Not a student"]
region_order = ["North East", "North West", "Yorkshire and The Humber", "East Midlands", "West Midlands", "East of England", "London", "South East", "South West", "Wales", "Does not apply: Northern Ireland", "Does not apply: Scotland"]
usual_student_order = ["Does not apply", "Is a usual resident", "Is a student living at an alternative address in term time", "Is a non-UK-born short-term resident, staying 3 to 12 months"]
partner_order = ["Does not apply", "Never married and never registered a civil partnership", "Married or in a registered civil partnership", "Separated, but still legally married or still legally in a civil partnership", "Divorced or civil partnership dissolved", "Widowed or surviving civil partnership partner"]
london_order = ["Does not apply", "Inner London", "Outer London"]
industry_order = ["Does not apply", "A Agriculture, forestry and fishing", "C Manufacturing", "B, D, E Energy and water", "F Construction", "G, I Distribution, hotels and restaurants", "H, J Transport and communication", "K, L, M, N Financial, real estate, professional and administrative activities", "O, P, Q Public administration, education and health", "R, S, T, U Other"]
religion_order = ["Does not apply", "No religion", "Christian", "Buddhist", "Hindu", "Jewish", "Muslim", "Sikh", "Other religion", "Not answered"]
residence_order = ["Does not apply", "Lives in a household", "Lives in a communal establishment"]
age_order = ["Does not apply", "Aged 15 years and under", "Aged 16 to 24 years", "Aged 25 to 34 years", "Aged 35 to 44 years", "Aged 45 to 54 years", "Aged 55 to 64 years", "Aged 65 years and over"]

label_map = {
    "approx_social_grade": social_grade_labels,
    "country_of_birth_3a": country_of_birth_labels,
    "economic_activity_status_10m": economic_activity_labels,
    "ethnic_group_tb_6a": ethinic_groups_labels,
    "health_in_general": health_labels,
    "hh_families_type_6a": family_labels,
    "hours_per_week_worked": hours_labels,
    "in_full_time_education": education_labels,
    "industry_10a": industry_labels,
    "iol22cd": london_labels,
    "legal_partnership_status_6a": partner_labels,
    "occupation_10a": occupation_labels,
    "region": region_labels,
    "religion_tb": religion_labels,
    "residence_type": residence_labels,
    "resident_age_7d": age_labels,
    "sex": sex_labels,
    "usual_short_student": usual_student_labels
}

order_map = {
    "approx_social_grade": social_grade_order,
    "country_of_birth_3a": country_of_birth_order,
    "economic_activity_status_10m": economic_activity_order,
    "ethnic_group_tb_6a": ethinic_groups_order,
    "health_in_general": health_order,
    "hh_families_type_6a": family_order,
    "hours_per_week_worked": hours_order,
    "in_full_time_education": education_order,
    "industry_10a": industry_order,
    "iol22cd": london_order,
    "legal_partnership_status_6a": partner_order,
    "occupation_10a": occupation_order,
    "region": region_order,
    "religion_tb": religion_order,
    "residence_type": residence_order,
    "resident_age_7d": age_order,
    "sex": sex_order,
    "usual_short_student": usual_student_order
}

name_map = {
    "approx_social_grade": "Social Grade",
    "country_of_birth_3a": "Country of Birth",
    "economic_activity_status_10m": "Economic Activity Status",
    "ethnic_group_tb_6a": "Ethnic Group",
    "health_in_general": "Health",
    "hh_families_type_6a": "Family",
    "hours_per_week_worked": "Hours Worked",
    "in_full_time_education": "Education",
    "iol22cd": "London",
    "legal_partnership_status_6a": "Partner",
    "region": "Region",
    "occupation_10a": "Occupation",
    "religion_tb": "Religion",
    "residence_type": "Residence",
    "resident_age_7d": "Age",
    "sex": "Sex",
    "usual_short_student": "Usual Student",
    "hours_per_week_worked": "Hours worked",
    "industry_10a": "Industry"          
}
