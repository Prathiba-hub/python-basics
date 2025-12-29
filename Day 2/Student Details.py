name = input();
age = int(input());
cgpa = float(input());
grade = input();

cgpa_truncated = int(cgpa * 100) / 100

print("Name:",name);
print("Age:",age);
print("CGPA:",cgpa_truncated);
print("Grade:",grade);
